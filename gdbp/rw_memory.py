import gdb
import struct


def read_bytes(address: int, length: int) -> bytes:
    """
    :param int address: Address to read from
    :param int length: Number of bytes to read
    :return bytes: The first ``length`` bytes starting at ``address``
    """
    # gdb.Inferior.read_memory was added in GDB 7.2
    return bytes(gdb.selected_inferior().read_memory(address, length))


def read8(address: int, big=False) -> int:
    """
    :param address: Address of unsigned uint8
    :param big : byte order big-endian. default = False.
    :return int: Value of uint8
    """
    if not big:
        return struct.unpack('<B', read_bytes(address, 1))[0]
    else:
        return struct.unpack('>B', read_bytes(address, 1))[0]


def read16(address: int, big=False) -> int:
    """
    :param int address: Address of unsigned uint16, little endian
    :param big : byte order big-endian. default = False.
    :return int: Value of uint16
    """
    if not big:
        return struct.unpack('<H', read_bytes(address, 2))[0]
    else:
        return struct.unpack('>H', read_bytes(address, 2))[0]


def read32(address: int, big=False) -> int:
    """
    :param int address: Address of unsigned uint32, little endian
    :param big : byte order big-endian. default = False.
    :return int: Value of integer
    """
    if not big:
        return struct.unpack('<L', read_bytes(address, 4))[0]
    else:
        return struct.unpack('>L', read_bytes(address, 4))[0]


def read64(address: int, big=False) -> int:
    """
    :param int address: Address of unsigned uint64, little endian
    :param big : byte order big-endian. default = False.
    :return int: Value of integer
    """
    if not big:
        return struct.unpack('<Q', read_bytes(address, 8))[0]
    else:
        return struct.unpack('>Q', read_bytes(address, 8))[0]


def write8(address: int, value: int) -> None:
    """
    :param int address: Address of unsigned uint8
    :param value: value of unsigned uint8
    :return
    """
    gdb.selected_inferior().write_memory(address, struct.pack("<B", value), 1)
    return


def write16(address: int, value: int) -> None:
    """
    :param int address: Address of unsigned uint16, little endian
    :param value: value of unsigned uint16
    :return
    """
    gdb.selected_inferior().write_memory(address, struct.pack("<H", value), 2)
    return


def write32(address: int, value: int) -> None:
    """
    :param int address: Address of unsigned uint32, little endian
    :param value: value of unsigned uint32
    :return
    """
    gdb.selected_inferior().write_memory(address, struct.pack("<L", value), 4)
    return


def write64(address: int, value: int) -> None:
    """
    :param int address: Address of unsigned uint64, little endian
    :param value: value of unsigned uint64
    :return
    """
    gdb.selected_inferior().write_memory(address, struct.pack("<Q", value), 8)
    return
