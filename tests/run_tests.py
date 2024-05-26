import gdb
import pytest


def run_tests_and_quit_gdb():
    gdb.execute('set pagination off')

    exit_code = pytest.main(['--capture=no'])

    gdb.execute('quit {}'.format(exit_code))


if __name__ == '__main__':
    run_tests_and_quit_gdb()
