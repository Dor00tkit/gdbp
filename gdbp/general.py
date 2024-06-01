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
    Parsing the eflags register
    :param eflags: int: eflags register value
    :return: dict: dict obj contains the bitfields of eflags register
    """

    parsed_eflags = {
        'CF': bool((eflags >> 0) & 0x1),  # Carry Flag
        'PF': bool((eflags >> 2) & 0x1),  # Parity Flag
        'AF': bool((eflags >> 4) & 0x1),  # Auxiliary Carry Flag
        'ZF': bool((eflags >> 6) & 0x1),  # Zero Flag
        'SF': bool((eflags >> 7) & 0x1),  # Sign Flag
        'TF': bool((eflags >> 8) & 0x1),  # Trap Flag
        'IF': bool((eflags >> 9) & 0x1),  # Interrupt Enable Flag
        'DF': bool((eflags >> 10) & 0x1),  # Direction Flag
        'OF': bool((eflags >> 11) & 0x1),  # Overflow Flag
        'IOPL': (eflags >> 12) & 0x3,  # I/O Privilege Level (2 bits)
        'NT': bool((eflags >> 14) & 0x1),  # Nested Task Flag
        'RF': bool((eflags >> 16) & 0x1),  # Resume Flag
        'VM': bool((eflags >> 17) & 0x1),  # Virtual-8086 Mode Flag
        'AC': bool((eflags >> 18) & 0x1),  # Alignment Check
        'VIF': bool((eflags >> 19) & 0x1),  # Virtual Interrupt Flag
        'VIP': bool((eflags >> 20) & 0x1),  # Virtual Interrupt Pending
        'ID': bool((eflags >> 21) & 0x1),  # ID Flag
    }

    return parsed_eflags


def parse_cr0(cr0) -> dict:
    """
    Parsing the CR0 register
    :param cr0: int: CR0 register value
    :return: dict: dict object containing the bitfields of the CR0 register
    """

    parsed_cr0 = {
        'PE': bool((cr0 >> 0) & 0x1),  # Protection Enable
        'MP': bool((cr0 >> 1) & 0x1),  # Monitor Coprocessor
        'EM': bool((cr0 >> 2) & 0x1),  # Emulation
        'TS': bool((cr0 >> 3) & 0x1),  # Task Switched
        'ET': bool((cr0 >> 4) & 0x1),  # Extension Type
        'NE': bool((cr0 >> 5) & 0x1),  # Numeric Error
        'WP': bool((cr0 >> 16) & 0x1),  # Write Protect
        'AM': bool((cr0 >> 18) & 0x1),  # Alignment Mask
        'NW': bool((cr0 >> 29) & 0x1),  # Not Write-through
        'CD': bool((cr0 >> 30) & 0x1),  # Cache Disable
        'PG': bool((cr0 >> 31) & 0x1)  # Paging
    }

    return parsed_cr0


def parse_cr4(cr4) -> dict:
    """
    Parsing the CR4 register
    :param cr4: int: CR4 register value
    :return: dict: dict object containing the bitfields of the CR4 register
    """
    parsed_cr4 = {
        'VME': bool((cr4 >> 0) & 0x1),        # Virtual-8086 Mode Extensions
        'PVI': bool((cr4 >> 1) & 0x1),        # Protected-Mode Virtual Interrupts
        'TSD': bool((cr4 >> 2) & 0x1),        # Time Stamp Disable
        'DE': bool((cr4 >> 3) & 0x1),         # Debugging Extensions
        'PSE': bool((cr4 >> 4) & 0x1),        # Page Size Extensions
        'PAE': bool((cr4 >> 5) & 0x1),        # Physical Address Extension
        'MCE': bool((cr4 >> 6) & 0x1),        # Machine-Check Enable
        'PGE': bool((cr4 >> 7) & 0x1),        # Page Global Enable
        'PCE': bool((cr4 >> 8) & 0x1),        # Performance-Monitoring Counter Enable
        'OSFXSR': bool((cr4 >> 9) & 0x1),     # Operating System Support for SAVE and FXRSTOR instructions
        'OSXMMEXCPT': bool((cr4 >> 10) & 0x1),  # Operating System Support for Unmasked SIMD Floating-Point Exceptions
        'UMIP': bool((cr4 >> 11) & 0x1),      # User-Mode Instruction Prevention
        'LA57': bool((cr4 >> 12) & 0x1),      # 57-bit linear addresses
        'VMXE': bool((cr4 >> 13) & 0x1),      # VMX-Enable Bit
        'SMXE': bool((cr4 >> 14) & 0x1),      # SMX-Enable Bit
        'FSGSBASE': bool((cr4 >> 16) & 0x1),  # FSGSBASE-Enable Bit
        'PCIDE': bool((cr4 >> 17) & 0x1),     # PCID-Enable Bit
        'OSXSAVE': bool((cr4 >> 18) & 0x1),   # XSAVE and Processor Extended States-Enable Bit
        'KL': bool((cr4 >> 19) & 0x1),        # Key-Locker-Enable Bit
        'SMEP': bool((cr4 >> 20) & 0x1),      # SMEP-Enable Bit
        'SMAP': bool((cr4 >> 21) & 0x1),      # SMAP-Enable Bit
        'PKE': bool((cr4 >> 22) & 0x1),       # Protection Key Enable
        'CET': bool((cr4 >> 23) & 0x1),       # Control-flow Enforcement Technology
        'PKS': bool((cr4 >> 24) & 0x1),       # Enable protection keys for supervisor-mode pages
        'UNTR': bool((cr4 >> 25) & 0x1),      # User Interrupts Enable Bit
    }

    return parsed_cr4


def parse_ia32_efer(ia32_efer) -> dict:
    """
    Parsing the IA32_EFER register
    :param ia32_efer: int: IA32_EFER register value
    :return: dict: dict object containing the bitfields of the IA32_EFER register
    """
    parsed_ia32_efer = {
        'SCE': bool((ia32_efer >> 0) & 0x1),  # SYSCALL Enable
        # Bits 7:1 are reserved
        'LME': bool((ia32_efer >> 8) & 0x1),  # IA-32e Mode Enable
        # Bit 9 is reserved
        'LMA': bool((ia32_efer >> 10) & 0x1), # IA-32e Mode Active
        'NXE': bool((ia32_efer >> 11) & 0x1), # Execute Disable Bit Enable
        # Bits 63:12 are reserved
    }

    return parsed_ia32_efer
