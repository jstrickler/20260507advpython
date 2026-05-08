#!/usr/bin/env python
from pytest import fixture

# from other_file import *

@fixture
def common_fixture():  # user-defined fixture
    return ['alpha', 'beta', 'gamma']


# predefined hook (all hooks start with 'pytest_')
def pytest_runtest_setup(item):
    if "test_config" in str(item):
        print(f"Hello from setup, {item}", end=" ")
