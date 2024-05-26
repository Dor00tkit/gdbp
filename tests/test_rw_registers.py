import pytest

import gdbp
from common import TEST_REGISTER_NAME, TEST_REGISTER_ORIGINAL_VALUE, TEST_REGISTER_NEW_VALUE


def test_read_register():
    assert gdbp.read_register(TEST_REGISTER_NAME) == TEST_REGISTER_ORIGINAL_VALUE


def test_read_register_non_existent_name():
    with pytest.raises(gdbp.GdbpInvalidRegister):
        gdbp.read_register('not_a_register')


@pytest.mark.xfail
def test_read_register_existent_non_register_name():
    with pytest.raises(gdbp.GdbpInvalidRegister):
        gdbp.read_register('_')


def test_read_register_larger_than_max_signed_value():
    MAX_SIGNED_VALUE_PLUS_ONE = 2 ** 31
    gdbp.write_register(TEST_REGISTER_NAME, MAX_SIGNED_VALUE_PLUS_ONE)
    assert gdbp.read_register(TEST_REGISTER_NAME) == MAX_SIGNED_VALUE_PLUS_ONE


def test_write_register():
    gdbp.write_register(TEST_REGISTER_NAME, TEST_REGISTER_NEW_VALUE)
    assert gdbp.read_register(TEST_REGISTER_NAME) == TEST_REGISTER_NEW_VALUE
