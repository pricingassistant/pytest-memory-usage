# -*- coding: utf-8 -*-

import pytest
import _pytest.config
import os
import sys
import psutil
import gc


def pytest_addoption(parser):
    group = parser.getgroup('memory-usage')
    group.addoption(
        '--memory-usage',
        action='store_true',
        default=False,
        help='Report memory usage'
    )

    parser.addini('memory_usage', 'Report memory usage', type='bool', default=False)


configuration = None
writer = None


def pytest_configure(config):
    global configuration
    configuration = config
    global writer
    writer = _pytest.config.create_terminal_writer(config, sys.stdout)


class MemoryState(object):
    def __init__(self):
        self.clear()

    def clear(self):
        self.before_setup = {}
        self.before_call = {}
        self.after_setup = {}
        self.after_call = {}
        self.processes = {}
        self.memory = {} # per-process memory usage


_TWO_20 = float(2 ** 20)


def get_memory(process, include_children=True):
    """Inspired by the memory_profiler module's implementation"""
    try:
        mem = process.memory_info()[0] / _TWO_20
        if include_children:
            for p in process.children(recursive=True):
                mem += p.memory_info()[0] / _TWO_20
        return mem
    except psutil.AccessDenied:
        return None

def get_processes():
    processes = {proc.name(): proc for proc in psutil.process_iter()}
    return processes


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup(item):
    if configuration.getoption('memory_usage') or configuration.getini('memory_usage'):
        state.clear()
        state.processes = get_processes()
        gc.disable()
        for name, process in state.processes.iteritems():
            state.before_setup[name] = get_memory(process)
        yield
        for name, process in state.processes.iteritems():
            state.after_setup[name] = get_memory(process)
        gc.enable()
    else:
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    if configuration.getoption('memory_usage') or configuration.getini('memory_usage'):
        gc.disable()
        for name, process in state.processes.iteritems():
            state.before_call[name] = get_memory(process)
        yield
        for name, process in state.processes.iteritems():
            state.after_call[name] = get_memory(process)
        gc.enable()
    else:
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    if configuration.getoption('memory_usage') or configuration.getini('memory_usage'):
        outcome = yield
        report = outcome.get_result()
        memory_usage = 0
        for name in state.processes:
            state.memory[name] = 0
            if (name in state.before_setup and name in state.after_setup):
                memory = state.after_setup[name] - state.before_setup[name]
                if memory > 0:
                    state.memory[name] += memory

            if (name in state.before_call and name in state.after_call):
                memory = state.after_call[name] - state.before_call[name]
                if memory > 0:
                    state.memory[name] += memory

            memory_usage += state.memory[name]

        report.__dict__.update(dict(memory_usage=memory_usage, memory_details=state.memory))

    else:
        yield


@pytest.hookimpl(trylast=True)
def pytest_runtest_logreport(report):
    if configuration.getoption('memory_usage') or configuration.getini('memory_usage'):
        if report.when == 'call' and report.passed:
            if hasattr(report, 'memory_usage'):
                writer.write('Total: {memory_usage:.0f}MB'.format(memory_usage=report.memory_usage))
                if report.memory_usage < 0:
                    writer.write(' (gc.collect() probably called explicitly)')

            if hasattr(report, 'memory_details'):
                for name, memory_usage in report.memory_details.iteritems():
                    writer.write('  {name}: {memory_usage:.0f}MB'.format(name=name, memory_usage=memory_usage))
                    if memory_usage < 0:
                        writer.write(' (gc.collect() probably called explicitly)')


state = MemoryState()
