import gdb


VMWARE_MONITOR_OUT = ('Supported monitor commands:\n   help\n   r\n   phys\n   virt\nPlease use "monitor help '
                      '<command>" to get details.\n')


class GeneralGdbp:
    def __init__(self):
        self.init = False
        self.vmware = False

    def init_detect_vmware_or_qemu(self) -> None:
        """
        Detect whether the gdbstub is VMware or QEMU
        :return:
        """

        if not self.init:
            out_cmd = gdb.execute("monitor help", to_string=True)
            if out_cmd == VMWARE_MONITOR_OUT:
                print("[gdbp: init_detect_vmware_or_qemu()] - Detected VMware")
                self.set_vmware()
            else:
                print("[gdbp: init_detect_vmware_or_qemu()] - Not detected VMware. assume QEMU")
            self.init = True

        return

    def set_vmware(self) -> None:
        """
        Use the vmware gdb stub monitor commands
        :return:
        """

        self.vmware = True
        self.init = True
        print("[gdbp: set_vmware()] - IS_VMWARE = True")
        return

    def is_vmware(self) -> bool:
        """
        Use the vmware gdb stub monitor commands
        :return:
        """

        if self.init:
            return self.vmware

    def turn_phys_mode_on(self) -> None:
        """
        Set the gdbstub to work with the physical memory rather with the virtual one
        :return:
        """

        if self.vmware:
            gdb.execute("monitor phys", to_string=True)
        else:
            gdb.execute("maint packet Qqemu.PhyMemMode:1", to_string=True)

        return

    def turn_phys_mode_off(self) -> None:
        """
        Return the gdbstub to work with the virtual memory rather with the physical one
        :return:
        """

        if self.vmware:
            gdb.execute("monitor virt", to_string=True)
        else:
            gdb.execute("maint packet Qqemu.PhyMemMode:0", to_string=True)

        return


def get_symbol_address(symbol) -> int:
    """
    :param str symbol: The symbol's name
    :return int: The symbol's address
    """
    # gdb.lookup_symbol was added in GDB 7.2
    symbol_object = gdb.lookup_symbol(symbol)[0]
    if symbol_object:
        return int(symbol_object.value().address)
    else:
        # Workaround for non-debugging symbols
        value_object = gdb.parse_and_eval('&' + symbol)
        return int(value_object)


def hw_bp(addr: int) -> gdb.Breakpoint:
    """
    Set hardware breakpoint via 'gdb.Breakpoint'
    :param addr: int: address
    :return: instance of 'gdb.Breakpoint' object
    """
    try:
        addr_as_str_hex = hex(addr)
    except (SyntaxError, TypeError) as e:
        print(e)
    else:
        return gdb.Breakpoint(f'*{addr_as_str_hex}', type=gdb.BP_HARDWARE_BREAKPOINT)


def disable_bp(bp_obj: gdb.Breakpoint) -> None:
    """
    Disable breakpoint
    :param bp_obj: gdb.Breakpoint object
    :return:
    """
    if bp_obj.is_valid():
        bp_obj.enabled = False
    return


def delete_bp(bp_obj: gdb.Breakpoint) -> None:
    """
    Delete breakpoint
    :param bp_obj: gdb.Breakpoint object
    :return:
    """
    if bp_obj.is_valid():
        bp_obj.delete()

    return


def extract_segment_selector_details(segment_selector) -> dict:
    index = (segment_selector >> 3) & 0x1FFF  # Extract bits 3-15
    ti = (segment_selector >> 2) & 0x1  # Extract bit 2
    rpl = segment_selector & 0x3  # Extract bits 0-1

    # Return as a dictionary
    return {
        'Index': index,
        'TI': 'LDT' if ti else 'GDT',
        'RPL': rpl
    }


def parse_eflags(eflags) -> dict:
    """
    Disable breakpoint
    :param eflags: int: eflags register value
    :return: dict: dict obj contains the bitfields of eflags register
    """
    flags = {
        'CF': bool((eflags >> 0) & 0x1),
        'PF': bool((eflags >> 2) & 0x1),
        'AF': bool((eflags >> 4) & 0x1),
        'ZF': bool((eflags >> 6) & 0x1),
        'SF': bool((eflags >> 7) & 0x1),
        'TF': bool((eflags >> 8) & 0x1),
        'IF': bool((eflags >> 9) & 0x1),
        'DF': bool((eflags >> 10) & 0x1),
        'OF': bool((eflags >> 11) & 0x1),
        'IOPL': (eflags >> 12) & 0x3,  # 2 bits, returning the raw numeric value
        'NT': bool((eflags >> 14) & 0x1),
        'RF': bool((eflags >> 16) & 0x1),
        'VM': bool((eflags >> 17) & 0x1),
        'AC': bool((eflags >> 18) & 0x1),
        'VIF': bool((eflags >> 19) & 0x1),
        'VIP': bool((eflags >> 20) & 0x1),
        'ID': bool((eflags >> 21) & 0x1),
    }

    return flags
