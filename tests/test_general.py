import gdbp
from common import TEST_VARIABLE_NAME, TEST_VARIABLE_ADDRESS


def test_get_symbol_address():
    assert gdbp.get_symbol_address(TEST_VARIABLE_NAME) == TEST_VARIABLE_ADDRESS
