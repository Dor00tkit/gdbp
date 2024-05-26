import gdb
import pytest

from common import TEST_PROGRAM_MAIN_FUNCTION, TEST_PROGRAM_SOURCE_FILE, TEST_PROGRAM_LABEL_NAME


@pytest.fixture(autouse=True)
def break_on_label_and_start_program():
    gdb.execute('break {}:{}:{}'.format(
        TEST_PROGRAM_SOURCE_FILE, TEST_PROGRAM_MAIN_FUNCTION, TEST_PROGRAM_LABEL_NAME))
    gdb.execute('r')
    yield
    gdb.execute('delete breakpoints')
