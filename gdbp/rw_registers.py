import gdb
import general

MASK_64BIT = 0xFFFFFFFFFFFFFFFF
MASK_32BIT = 0xFFFFFFFF
MASK_16BIT = 0xFFFF
MASK_8BIT = 0xFF

GDBP_OBJ = general.GeneralGdbp()


def splice(string: str, start_token: str, end_token: str):
    start_pos = string.find(start_token)
    end_pos = string.rfind(end_token)

    if start_pos == -1 or end_pos == -1:
        return None

    start_pos += len(start_token)

    if start_pos > end_pos:
        return None

    return string[start_pos:end_pos]


class GdbpInvalidRegister(RuntimeError):
    pass


def read_register(register_name) -> int:
    """
    :param str register_name: A valid register name (according to GDB)
    :return int: The register's (unsigned) value in the selected frame
    """
    # gdb.parse_and_eval & gdb.TYPE_CODE_VOID were added in GDB 7.1
    # gdb.Frame.read_register was added in GDB 7.9, which is higher than the min supported version
    value_object = gdb.parse_and_eval('$' + register_name)
    if value_object.type.code == gdb.TYPE_CODE_VOID:
        raise GdbpInvalidRegister()

    register_size_in_bits = value_object.type.sizeof * 8

    value = int(value_object)
    if value < 0:
        value += 2 ** register_size_in_bits

    return value


def write_register(register_name, value):
    """
    :param str register_name: A valid register name (according to GDB)
    :param int value: Value to write to register
    """
    # Verify that the register is readable
    read_register(register_name)

    # gdb.execute was added in GDB 7.0
    gdb.execute('set ${register_name} = {value}'.format(register_name=register_name, value=value))


def get_curr_frame() -> gdb.Frame:
    """
    :return: Return the selected frame object. see:
    https://sourceware.org/gdb/current/onlinedocs/gdb.html/Selection.html#Selection
    """
    curr_frame = gdb.selected_frame()
    if curr_frame:
        if curr_frame.is_valid():
            return curr_frame
    else:
        return None


def get_rax() -> int:
    f = get_curr_frame()
    if f:
        try:
            rax = f.read_register('rax')
            return int(rax) & MASK_64BIT
        except Exception as e:
            print(f"Error reading rax register: {e}")


def get_eax() -> int:
    f = get_curr_frame()
    if f:
        try:
            eax = f.read_register('eax')
            return int(eax) & MASK_32BIT
        except Exception as e:
            print(f"Error reading eax register: {e}")


def get_ax() -> int:
    f = get_curr_frame()
    if f:
        try:
            ax = f.read_register('ax')
            return int(ax) & MASK_16BIT
        except Exception as e:
            print(f"Error reading ax register: {e}")


def get_ah() -> int:
    f = get_curr_frame()
    if f:
        try:
            ah = f.read_register('ah')
            return int(ah) & MASK_8BIT
        except Exception as e:
            print(f"Error reading ah register: {e}")


def get_al() -> int:
    f = get_curr_frame()
    if f:
        try:
            al = f.read_register('al')
            return int(al) & MASK_8BIT
        except Exception as e:
            print(f"Error reading al register: {e}")


def set_rax(value: int) -> None:
    try:
        gdb.execute(f"set $rax = {value}")
    except Exception as e:
        print(f"Error setting rax register: {e}")


def set_eax(value: int) -> None:
    try:
        gdb.execute(f"set $eax = {value}")
    except Exception as e:
        print(f"Error setting eax register: {e}")


def set_ax(value: int) -> None:
    try:
        gdb.execute(f"set $ax = {value}")
    except Exception as e:
        print(f"Error setting ax register: {e}")


def set_al(value: int) -> None:
    try:
        gdb.execute(f"set $al = {value}")
    except Exception as e:
        print(f"Error setting al register: {e}")


def get_rbx() -> int:
    f = get_curr_frame()
    if f:
        try:
            rbx = f.read_register('rbx')
            return int(rbx) & MASK_64BIT
        except Exception as e:
            print(f"Error reading rbx register: {e}")


def get_ebx() -> int:
    f = get_curr_frame()
    if f:
        try:
            ebx = f.read_register('ebx')
            return int(ebx) & MASK_32BIT
        except Exception as e:
            print(f"Error reading ebx register: {e}")


def get_bx() -> int:
    f = get_curr_frame()
    if f:
        try:
            bx = f.read_register('bx')
            return int(bx) & MASK_16BIT
        except Exception as e:
            print(f"Error reading bx register: {e}")


def get_bl() -> int:
    f = get_curr_frame()
    if f:
        try:
            bl = f.read_register('bl')
            return int(bl) & MASK_8BIT
        except Exception as e:
            print(f"Error reading bl register: {e}")


def set_rbx(value: int) -> None:
    try:
        gdb.execute(f"set $rbx = {value}")
    except Exception as e:
        print(f"Error setting rbx register: {e}")


def set_ebx(value: int) -> None:
    try:
        gdb.execute(f"set $ebx = {value}")
    except Exception as e:
        print(f"Error setting ebx register: {e}")


def set_bx(value: int) -> None:
    try:
        gdb.execute(f"set $bx = {value}")
    except Exception as e:
        print(f"Error setting bx register: {e}")


def set_bl(value: int) -> None:
    try:
        gdb.execute(f"set $bl = {value}")
    except Exception as e:
        print(f"Error setting bl register: {e}")


def get_rcx() -> int:
    f = get_curr_frame()
    if f:
        try:
            rcx = f.read_register('rcx')
            return int(rcx) & MASK_64BIT
        except Exception as e:
            print(f"Error reading rcx register: {e}")


def get_ecx() -> int:
    f = get_curr_frame()
    if f:
        try:
            ecx = f.read_register('ecx')
            return int(ecx) & MASK_32BIT
        except Exception as e:
            print(f"Error reading ecx register: {e}")


def get_cx() -> int:
    f = get_curr_frame()
    if f:
        try:
            cx = f.read_register('cx')
            return int(cx) & MASK_16BIT
        except Exception as e:
            print(f"Error reading cx register: {e}")


def get_cl() -> int:
    f = get_curr_frame()
    if f:
        try:
            cl = f.read_register('cl')
            return int(cl) & MASK_8BIT
        except Exception as e:
            print(f"Error reading cl register: {e}")


def set_rcx(value: int) -> None:
    try:
        gdb.execute(f"set $rcx = {value}")
    except Exception as e:
        print(f"Error setting rcx register: {e}")


def set_ecx(value: int) -> None:
    try:
        gdb.execute(f"set $ecx = {value}")
    except Exception as e:
        print(f"Error setting ecx register: {e}")


def set_cx(value: int) -> None:
    try:
        gdb.execute(f"set $cx = {value}")
    except Exception as e:
        print(f"Error setting cx register: {e}")


def set_cl(value: int) -> None:
    try:
        gdb.execute(f"set $cl = {value}")
    except Exception as e:
        print(f"Error setting cl register: {e}")


def get_rdx() -> int:
    f = get_curr_frame()
    if f:
        try:
            rdx = f.read_register('rdx')
            return int(rdx) & MASK_64BIT
        except Exception as e:
            print(f"Error reading rdx register: {e}")


def get_edx() -> int:
    f = get_curr_frame()
    if f:
        try:
            edx = f.read_register('edx')
            return int(edx) & MASK_32BIT
        except Exception as e:
            print(f"Error reading edx register: {e}")


def get_dx() -> int:
    f = get_curr_frame()
    if f:
        try:
            dx = f.read_register('dx')
            return int(dx) & MASK_16BIT
        except Exception as e:
            print(f"Error reading dx register: {e}")


def get_dl() -> int:
    f = get_curr_frame()
    if f:
        try:
            dl = f.read_register('dl')
            return int(dl) & MASK_8BIT
        except Exception as e:
            print(f"Error reading dl register: {e}")


def set_rdx(value: int) -> None:
    try:
        gdb.execute(f"set $rdx = {value}")
    except Exception as e:
        print(f"Error setting rdx register: {e}")


def set_edx(value: int) -> None:
    try:
        gdb.execute(f"set $edx = {value}")
    except Exception as e:
        print(f"Error setting edx register: {e}")


def set_dx(value: int) -> None:
    try:
        gdb.execute(f"set $dx = {value}")
    except Exception as e:
        print(f"Error setting dx register: {e}")


def set_dl(value: int) -> None:
    try:
        gdb.execute(f"set $dl = {value}")
    except Exception as e:
        print(f"Error setting dl register: {e}")


def get_rsi() -> int:
    f = get_curr_frame()
    if f:
        try:
            rsi = f.read_register('rsi')
            return int(rsi) & MASK_64BIT
        except Exception as e:
            print(f"Error reading rsi register: {e}")


def get_esi() -> int:
    f = get_curr_frame()
    if f:
        try:
            esi = f.read_register('esi')
            return int(esi) & MASK_32BIT
        except Exception as e:
            print(f"Error reading esi register: {e}")


def get_si() -> int:
    f = get_curr_frame()
    if f:
        try:
            si = f.read_register('si')
            return int(si) & MASK_16BIT
        except Exception as e:
            print(f"Error reading si register: {e}")


def get_sil() -> int:
    f = get_curr_frame()
    if f:
        try:
            sil = f.read_register('sil')
            return int(sil) & MASK_8BIT
        except Exception as e:
            print(f"Error reading sil register: {e}")


def set_rsi(value: int) -> None:
    try:
        gdb.execute(f"set $rsi = {value}")
    except Exception as e:
        print(f"Error setting rsi register: {e}")


def set_esi(value: int) -> None:
    try:
        gdb.execute(f"set $esi = {value}")
    except Exception as e:
        print(f"Error setting esi register: {e}")


def set_si(value: int) -> None:
    try:
        gdb.execute(f"set $si = {value}")
    except Exception as e:
        print(f"Error setting si register: {e}")


def set_sil(value: int) -> None:
    try:
        gdb.execute(f"set $sil = {value}")
    except Exception as e:
        print(f"Error setting sil register: {e}")


def get_rdi() -> int:
    f = get_curr_frame()
    if f:
        try:
            rdi = f.read_register('rdi')
            return int(rdi) & MASK_64BIT
        except Exception as e:
            print(f"Error reading rdi register: {e}")


def get_edi() -> int:
    f = get_curr_frame()
    if f:
        try:
            edi = f.read_register('edi')
            return int(edi) & MASK_32BIT
        except Exception as e:
            print(f"Error reading edi register: {e}")


def get_di() -> int:
    f = get_curr_frame()
    if f:
        try:
            di = f.read_register('di')
            return int(di) & MASK_16BIT
        except Exception as e:
            print(f"Error reading di register: {e}")


def get_dil() -> int:
    f = get_curr_frame()
    if f:
        try:
            dil = f.read_register('dil')
            return int(dil) & MASK_8BIT
        except Exception as e:
            print(f"Error reading dil register: {e}")


def set_rdi(value: int) -> None:
    try:
        gdb.execute(f"set $rdi = {value}")
    except Exception as e:
        print(f"Error setting rdi register: {e}")


def set_edi(value: int) -> None:
    try:
        gdb.execute(f"set $edi = {value}")
    except Exception as e:
        print(f"Error setting edi register: {e}")


def set_di(value: int) -> None:
    try:
        gdb.execute(f"set $di = {value}")
    except Exception as e:
        print(f"Error setting di register: {e}")


def set_dil(value: int) -> None:
    try:
        gdb.execute(f"set $dil = {value}")
    except Exception as e:
        print(f"Error setting dil register: {e}")


def get_rbp() -> int:
    f = get_curr_frame()
    if f:
        try:
            rbp = f.read_register('rbp')
            return int(rbp) & MASK_64BIT
        except Exception as e:
            print(f"Error reading rbp register: {e}")


def get_ebp() -> int:
    f = get_curr_frame()
    if f:
        try:
            ebp = f.read_register('ebp')
            return int(ebp) & MASK_32BIT
        except Exception as e:
            print(f"Error reading ebp register: {e}")


def get_bp() -> int:
    f = get_curr_frame()
    if f:
        try:
            bp = f.read_register('bp')
            return int(bp) & MASK_16BIT
        except Exception as e:
            print(f"Error reading bp register: {e}")


def get_bpl() -> int:
    f = get_curr_frame()
    if f:
        try:
            bpl = f.read_register('bpl')
            return int(bpl) & MASK_8BIT
        except Exception as e:
            print(f"Error reading bpl register: {e}")


def set_rbp(value: int) -> None:
    try:
        gdb.execute(f"set $rbp = {value}")
    except Exception as e:
        print(f"Error setting rbp register: {e}")


def set_ebp(value: int) -> None:
    try:
        gdb.execute(f"set $ebp = {value}")
    except Exception as e:
        print(f"Error setting ebp register: {e}")


def set_bp(value: int) -> None:
    try:
        gdb.execute(f"set $bp = {value}")
    except Exception as e:
        print(f"Error setting bp register: {e}")


def set_bpl(value: int) -> None:
    try:
        gdb.execute(f"set $bpl = {value}")
    except Exception as e:
        print(f"Error setting bpl register: {e}")


def get_rsp() -> int:
    f = get_curr_frame()
    if f:
        try:
            rsp = f.read_register('rsp')
            return int(rsp) & MASK_64BIT
        except Exception as e:
            print(f"Error reading rsp register: {e}")


def get_esp() -> int:
    f = get_curr_frame()
    if f:
        try:
            esp = f.read_register('esp')
            return int(esp) & MASK_32BIT
        except Exception as e:
            print(f"Error reading esp register: {e}")


def get_sp() -> int:
    f = get_curr_frame()
    if f:
        try:
            sp = f.read_register('sp')
            return int(sp) & MASK_16BIT
        except Exception as e:
            print(f"Error reading sp register: {e}")


def get_spl() -> int:
    f = get_curr_frame()
    if f:
        try:
            spl = f.read_register('spl')
            return int(spl) & MASK_8BIT
        except Exception as e:
            print(f"Error reading spl register: {e}")


def set_rsp(value: int) -> None:
    try:
        gdb.execute(f"set $rsp = {value}")
    except Exception as e:
        print(f"Error setting rsp register: {e}")


def set_esp(value: int) -> None:
    try:
        gdb.execute(f"set $esp = {value}")
    except Exception as e:
        print(f"Error setting esp register: {e}")


def set_sp(value: int) -> None:
    try:
        gdb.execute(f"set $sp = {value}")
    except Exception as e:
        print(f"Error setting sp register: {e}")


def set_spl(value: int) -> None:
    try:
        gdb.execute(f"set $spl = {value}")
    except Exception as e:
        print(f"Error setting spl register: {e}")


def get_r8() -> int:
    f = get_curr_frame()
    if f:
        try:
            r8 = f.read_register('r8')
            return int(r8) & MASK_64BIT
        except Exception as e:
            print(f"Error reading r8 register: {e}")


def get_r8d() -> int:
    f = get_curr_frame()
    if f:
        try:
            r8d = f.read_register('r8d')
            return int(r8d) & MASK_32BIT
        except Exception as e:
            print(f"Error reading r8d register: {e}")


def get_r8w() -> int:
    f = get_curr_frame()
    if f:
        try:
            r8w = f.read_register('r8w')
            return int(r8w) & MASK_16BIT
        except Exception as e:
            print(f"Error reading r8w register: {e}")


def get_r8b() -> int:
    return get_r8w() & MASK_8BIT


def set_r8(value: int) -> None:
    try:
        gdb.execute(f"set $r8 = {value}")
    except Exception as e:
        print(f"Error setting r8 register: {e}")


def set_r8d(value: int) -> None:
    try:
        gdb.execute(f"set $r8d = {value}")
    except Exception as e:
        print(f"Error setting r8d register: {e}")


def set_r8w(value: int) -> None:
    try:
        gdb.execute(f"set $r8w = {value}")
    except Exception as e:
        print(f"Error setting r8w register: {e}")


def set_r8b(value: int) -> None:
    try:
        gdb.execute(f"set $r8b = {value}")
    except Exception as e:
        print(f"Error setting r8b register: {e}")


def get_r9() -> int:
    f = get_curr_frame()
    if f:
        try:
            r9 = f.read_register('r9')
            return int(r9) & MASK_64BIT
        except Exception as e:
            print(f"Error reading r9 register: {e}")


def get_r9d() -> int:
    f = get_curr_frame()
    if f:
        try:
            r9d = f.read_register('r9d')
            return int(r9d) & MASK_32BIT
        except Exception as e:
            print(f"Error reading r9d register: {e}")


def get_r9w() -> int:
    f = get_curr_frame()
    if f:
        try:
            r9w = f.read_register('r9w')
            return int(r9w) & MASK_16BIT
        except Exception as e:
            print(f"Error reading r9w register: {e}")


def get_r9b() -> int:
    return get_r9w() & MASK_8BIT


def set_r9(value: int) -> None:
    try:
        gdb.execute(f"set $r9 = {value}")
    except Exception as e:
        print(f"Error setting r9 register: {e}")


def set_r9d(value: int) -> None:
    try:
        gdb.execute(f"set $r9d = {value}")
    except Exception as e:
        print(f"Error setting r9d register: {e}")


def set_r9w(value: int) -> None:
    try:
        gdb.execute(f"set $r9w = {value}")
    except Exception as e:
        print(f"Error setting r9w register: {e}")


def set_r9b(value: int) -> None:
    try:
        gdb.execute(f"set $r9b = {value}")
    except Exception as e:
        print(f"Error setting r9b register: {e}")


def get_r10() -> int:
    f = get_curr_frame()
    if f:
        try:
            r10 = f.read_register('r10')
            return int(r10) & MASK_64BIT
        except Exception as e:
            print(f"Error reading r10 register: {e}")


def get_r10d() -> int:
    f = get_curr_frame()
    if f:
        try:
            r10d = f.read_register('r10d')
            return int(r10d) & MASK_32BIT
        except Exception as e:
            print(f"Error reading r10d register: {e}")


def get_r10w() -> int:
    f = get_curr_frame()
    if f:
        try:
            r10w = f.read_register('r10w')
            return int(r10w) & MASK_16BIT
        except Exception as e:
            print(f"Error reading r10w register: {e}")


def get_r10b() -> int:
    return get_r10w() & MASK_8BIT


def set_r10(value: int) -> None:
    try:
        gdb.execute(f"set $r10 = {value}")
    except Exception as e:
        print(f"Error setting r10 register: {e}")


def set_r10d(value: int) -> None:
    try:
        gdb.execute(f"set $r10d = {value}")
    except Exception as e:
        print(f"Error setting r10d register: {e}")


def set_r10w(value: int) -> None:
    try:
        gdb.execute(f"set $r10w = {value}")
    except Exception as e:
        print(f"Error setting r10w register: {e}")


def set_r10b(value: int) -> None:
    try:
        gdb.execute(f"set $r10b = {value}")
    except Exception as e:
        print(f"Error setting r10b register: {e}")


def get_r11() -> int:
    f = get_curr_frame()
    if f:
        try:
            r11 = f.read_register('r11')
            return int(r11) & MASK_64BIT
        except Exception as e:
            print(f"Error reading r11 register: {e}")


def get_r11d() -> int:
    f = get_curr_frame()
    if f:
        try:
            r11d = f.read_register('r11d')
            return int(r11d) & MASK_32BIT
        except Exception as e:
            print(f"Error reading r11d register: {e}")


def get_r11w() -> int:
    f = get_curr_frame()
    if f:
        try:
            r11w = f.read_register('r11w')
            return int(r11w) & MASK_16BIT
        except Exception as e:
            print(f"Error reading r11w register: {e}")


def get_r11b() -> int:
    return get_r11w() & MASK_8BIT


def set_r11(value: int) -> None:
    try:
        gdb.execute(f"set $r11 = {value}")
    except Exception as e:
        print(f"Error setting r11 register: {e}")


def set_r11d(value: int) -> None:
    try:
        gdb.execute(f"set $r11d = {value}")
    except Exception as e:
        print(f"Error setting r11d register: {e}")


def set_r11w(value: int) -> None:
    try:
        gdb.execute(f"set $r11w = {value}")
    except Exception as e:
        print(f"Error setting r11w register: {e}")


def set_r11b(value: int) -> None:
    try:
        gdb.execute(f"set $r11b = {value}")
    except Exception as e:
        print(f"Error setting r11b register: {e}")


def get_r12() -> int:
    f = get_curr_frame()
    if f:
        try:
            r12 = f.read_register('r12')
            return int(r12) & MASK_64BIT
        except Exception as e:
            print(f"Error reading r12 register: {e}")


def get_r12d() -> int:
    f = get_curr_frame()
    if f:
        try:
            r12d = f.read_register('r12d')
            return int(r12d) & MASK_32BIT
        except Exception as e:
            print(f"Error reading r12d register: {e}")


def get_r12w() -> int:
    f = get_curr_frame()
    if f:
        try:
            r12w = f.read_register('r12w')
            return int(r12w) & MASK_16BIT
        except Exception as e:
            print(f"Error reading r12w register: {e}")


def get_r12b() -> int:
    return get_r12w() & MASK_8BIT


def set_r12(value: int) -> None:
    try:
        gdb.execute(f"set $r12 = {value}")
    except Exception as e:
        print(f"Error setting r12 register: {e}")


def set_r12d(value: int) -> None:
    try:
        gdb.execute(f"set $r12d = {value}")
    except Exception as e:
        print(f"Error setting r12d register: {e}")


def set_r12w(value: int) -> None:
    try:
        gdb.execute(f"set $r12w = {value}")
    except Exception as e:
        print(f"Error setting r12w register: {e}")


def set_r12b(value: int) -> None:
    try:
        gdb.execute(f"set $r12b = {value}")
    except Exception as e:
        print(f"Error setting r12b register: {e}")


def get_r13() -> int:
    f = get_curr_frame()
    if f:
        try:
            r13 = f.read_register('r13')
            return int(r13) & MASK_64BIT
        except Exception as e:
            print(f"Error reading r13 register: {e}")


def get_r13d() -> int:
    f = get_curr_frame()
    if f:
        try:
            r13d = f.read_register('r13d')
            return int(r13d) & MASK_32BIT
        except Exception as e:
            print(f"Error reading r13d register: {e}")


def get_r13w() -> int:
    f = get_curr_frame()
    if f:
        try:
            r13w = f.read_register('r13w')
            return int(r13w) & MASK_16BIT
        except Exception as e:
            print(f"Error reading r13w register: {e}")


def get_r13b() -> int:
    return get_r13w() & MASK_8BIT


def set_r13(value: int) -> None:
    try:
        gdb.execute(f"set $r13 = {value}")
    except Exception as e:
        print(f"Error setting r13 register: {e}")


def set_r13d(value: int) -> None:
    try:
        gdb.execute(f"set $r13d = {value}")
    except Exception as e:
        print(f"Error setting r13d register: {e}")


def set_r13w(value: int) -> None:
    try:
        gdb.execute(f"set $r13w = {value}")
    except Exception as e:
        print(f"Error setting r13w register: {e}")


def set_r13b(value: int) -> None:
    try:
        gdb.execute(f"set $r13b = {value}")
    except Exception as e:
        print(f"Error setting r13b register: {e}")


def get_r14() -> int:
    f = get_curr_frame()
    if f:
        try:
            r14 = f.read_register('r14')
            return int(r14) & MASK_64BIT
        except Exception as e:
            print(f"Error reading r14 register: {e}")


def get_r14d() -> int:
    f = get_curr_frame()
    if f:
        try:
            r14d = f.read_register('r14d')
            return int(r14d) & MASK_32BIT
        except Exception as e:
            print(f"Error reading r14d register: {e}")


def get_r14w() -> int:
    f = get_curr_frame()
    if f:
        try:
            r14w = f.read_register('r14w')
            return int(r14w) & MASK_16BIT
        except Exception as e:
            print(f"Error reading r14w register: {e}")


def get_r14b() -> int:
    return get_r14w() & MASK_8BIT


def set_r14(value: int) -> None:
    try:
        gdb.execute(f"set $r14 = {value}")
    except Exception as e:
        print(f"Error setting r14 register: {e}")


def set_r14d(value: int) -> None:
    try:
        gdb.execute(f"set $r14d = {value}")
    except Exception as e:
        print(f"Error setting r14d register: {e}")


def set_r14w(value: int) -> None:
    try:
        gdb.execute(f"set $r14w = {value}")
    except Exception as e:
        print(f"Error setting r14w register: {e}")


def set_r14b(value: int) -> None:
    try:
        gdb.execute(f"set $r14b = {value}")
    except Exception as e:
        print(f"Error setting r14b register: {e}")


def get_r15() -> int:
    f = get_curr_frame()
    if f:
        try:
            r15 = f.read_register('r15')
            return int(r15) & MASK_64BIT
        except Exception as e:
            print(f"Error reading r15 register: {e}")


def get_r15d() -> int:
    f = get_curr_frame()
    if f:
        try:
            r15d = f.read_register('r15d')
            return int(r15d) & MASK_32BIT
        except Exception as e:
            print(f"Error reading r15d register: {e}")


def get_r15w() -> int:
    f = get_curr_frame()
    if f:
        try:
            r15w = f.read_register('r15w')
            return int(r15w) & MASK_16BIT
        except Exception as e:
            print(f"Error reading r15w register: {e}")


def get_r15b() -> int:
    return get_r15w() & MASK_8BIT


def set_r15(value: int) -> None:
    try:
        gdb.execute(f"set $r15 = {value}")
    except Exception as e:
        print(f"Error setting r15 register: {e}")


def set_r15d(value: int) -> None:
    try:
        gdb.execute(f"set $r15d = {value}")
    except Exception as e:
        print(f"Error setting r15d register: {e}")


def set_r15w(value: int) -> None:
    try:
        gdb.execute(f"set $r15w = {value}")
    except Exception as e:
        print(f"Error setting r15w register: {e}")


def set_r15b(value: int) -> None:
    try:
        gdb.execute(f"set $r15b = {value}")
    except Exception as e:
        print(f"Error setting r15b register: {e}")


def get_pc() -> int:
    f = get_curr_frame()
    if f:
        try:
            pc = f.pc()
            return pc
        except Exception as e:
            print(f"Error reading pc register: {e}")


def get_rip() -> int:
    f = get_curr_frame()
    if f:
        try:
            pc = f.pc()
            return pc & MASK_64BIT
        except Exception as e:
            print(f"Error reading rip register: {e}")


def get_eip() -> int:
    f = get_curr_frame()
    if f:
        try:
            pc = f.pc()
            return pc & MASK_32BIT
        except Exception as e:
            print(f"Error reading eip register: {e}")


def get_ip() -> int:
    f = get_curr_frame()
    if f:
        try:
            pc = f.pc()
            return pc & MASK_16BIT
        except Exception as e:
            print(f"Error reading ip register: {e}")


def set_pc(value: int) -> None:
    try:
        gdb.execute(f"set $pc = {value}")
    except Exception as e:
        print(f"Error setting pc register: {e}")


def set_rip(value: int) -> None:
    try:
        value = value & MASK_64BIT
        set_pc(value)
    except Exception as e:
        print(f"Error setting rip register: {e}")


def set_eip(value: int) -> None:
    try:
        value = value & MASK_32BIT
        set_pc(value)
    except Exception as e:
        print(f"Error setting eip register: {e}")


def set_ip(value: int) -> None:
    try:
        value = value & MASK_16BIT
        set_pc(value)
    except Exception as e:
        print(f"Error setting ip register: {e}")


def get_eflags() -> int:
    f = get_curr_frame()
    if f:
        try:
            eflags = f.read_register('eflags')
            return int(eflags) & MASK_64BIT
        except Exception as e:
            print(f"Error reading eflags register: {e}")


def set_eflags(value: int) -> None:
    try:
        gdb.execute(f"set $eflags = {value}")
    except Exception as e:
        print(f"Error setting eflags register: {e}")


def get_cs() -> int:
    f = get_curr_frame()
    if f:
        try:
            cs = f.read_register('cs')
            return int(cs) & MASK_16BIT
        except Exception as e:
            print(f"Error reading cs register: {e}")


def get_ss() -> int:
    f = get_curr_frame()
    if f:
        try:
            ss = f.read_register('ss')
            return int(ss) & MASK_16BIT
        except Exception as e:
            print(f"Error reading ss register: {e}")


def get_ds() -> int:
    f = get_curr_frame()
    if f:
        try:
            ds = f.read_register('ds')
            return int(ds) & MASK_16BIT
        except Exception as e:
            print(f"Error reading ds register: {e}")


def get_es() -> int:
    f = get_curr_frame()
    if f:
        try:
            es = f.read_register('es')
            return int(es) & MASK_16BIT
        except Exception as e:
            print(f"Error reading es register: {e}")


def get_fs() -> int:
    f = get_curr_frame()
    if f:
        try:
            fs = f.read_register('fs')
            return int(fs) & MASK_16BIT
        except Exception as e:
            print(f"Error reading fs register: {e}")


def get_gs() -> int:
    f = get_curr_frame()
    if f:
        try:
            gs = f.read_register('gs')
            return int(gs) & MASK_16BIT
        except Exception as e:
            print(f"Error reading gs register: {e}")


def set_cs(value: int) -> None:
    try:
        gdb.execute(f"set $cs = {value}")
    except Exception as e:
        print(f"Error setting cs register: {e}")


def set_ss(value: int) -> None:
    try:
        gdb.execute(f"set $ss = {value}")
    except Exception as e:
        print(f"Error setting cs register: {e}")


def set_ds(value: int) -> None:
    try:
        gdb.execute(f"set $ds = {value}")
    except Exception as e:
        print(f"Error setting ds register: {e}")


def set_es(value: int) -> None:
    try:
        gdb.execute(f"set $es = {value}")
    except Exception as e:
        print(f"Error setting es register: {e}")


def set_fs(value: int) -> None:
    try:
        gdb.execute(f"set $fs = {value}")
    except Exception as e:
        print(f"Error setting fs register: {e}")


def set_gs(value: int) -> None:
    try:
        gdb.execute(f"set $gs = {value}")
    except Exception as e:
        print(f"Error setting gs register: {e}")


def get_cr0() -> int:
    """
    Get the CR0 of the current logical processor
    :return: int: value of the CR0 register
    """
    global GDBP_OBJ

    if GDBP_OBJ.is_vmware():
        read_cr0 = gdb.execute("monitor r cr0", to_string=True)
        cr0 = int(splice(read_cr0, "cr0=", "\n"), 16)
        return cr0

    else:
        f = get_curr_frame()
        if f:
            try:
                cr0 = f.read_register('cr0')
                return int(cr0) & MASK_64BIT
            except Exception as e:
                print(f"Error reading cr0 register: {e}")


def get_cr2() -> int:
    """
    Get the CR2 of the current logical processor
    :return: int: value of the CR2 register
    """
    global GDBP_OBJ

    if GDBP_OBJ.is_vmware():
        read_cr2 = gdb.execute("monitor r cr2", to_string=True)
        cr2 = int(splice(read_cr2, "cr2=", "\n"), 16)
        return cr2

    else:
        f = get_curr_frame()
        if f:
            try:
                cr2 = f.read_register('cr2')
                return int(cr2) & MASK_64BIT
            except Exception as e:
                print(f"Error reading cr2 register: {e}")


def get_cr3() -> int:
    """
    Get the CR3 of the current logical processor
    :return: int: value of the CR3 register
    """
    global GDBP_OBJ

    if GDBP_OBJ.is_vmware():
        read_cr3 = gdb.execute("monitor r cr3", to_string=True)
        cr3 = int(splice(read_cr3, "cr3=", "\n"), 16)
        return cr3

    else:
        f = get_curr_frame()
        if f:
            try:
                cr3 = f.read_register('cr3')
                return int(cr3) & MASK_64BIT
            except Exception as e:
                print(f"Error reading cr3 register: {e}")


def get_cr4() -> int:
    """
    Get the CR4 of the current logical processor
    :return: int: value of the CR4 register
    """
    global GDBP_OBJ

    if GDBP_OBJ.is_vmware():
        read_cr4 = gdb.execute("monitor r cr4", to_string=True)
        cr4 = int(splice(read_cr4, "cr4=", "\n"), 16)
        return cr4

    else:
        f = get_curr_frame()
        if f:
            try:
                cr4 = f.read_register('cr4')
                return int(cr4) & MASK_64BIT
            except Exception as e:
                print(f"Error reading cr4 register: {e}")


def get_gdtr() -> tuple[int, int]:
    """
    VMware only!
    Get the gdtr of the current logical processor
    :return: tuple[int, int]: value of the gdtr base register and his limit
    """
    global GDBP_OBJ

    if GDBP_OBJ.is_vmware():
        read_gdtr = gdb.execute("monitor r gdtr", to_string=True)
        gdtr_base = int(splice(read_gdtr, "base=", " "), 16)
        gdtr_limit = int(splice(read_gdtr, "limit=", "\n"), 16)
        return gdtr_base, gdtr_limit

    else:
        raise Exception("Not supported in QEMU :(")


def get_idtr() -> tuple[int, int]:
    """
    VMware only!
    Get the idtr of the current logical processor
    :return: tuple[int, int]: value of the idtr base register and his limit
    """
    global GDBP_OBJ

    if GDBP_OBJ.is_vmware():
        read_idtr = gdb.execute("monitor r idtr", to_string=True)
        idtr_base = int(splice(read_idtr, "base=", " "), 16)
        idtr_limit = int(splice(read_idtr, "limit=", "\n"), 16)
        return idtr_base, idtr_limit

    else:
        raise Exception("Not supported in QEMU :(")


def get_ldtr() -> dict:
    """
    VMware only!
    Get the ldtr of the current logical processor
    :return: tuple[int, int]: value of the ldtr base register and his limit
    """
    global GDBP_OBJ
    if GDBP_OBJ.is_vmware():
        ldtr_info = {}

        read_ldtr = gdb.execute("monitor r ldtr", to_string=True)
        try:
            ldtr_sel = int(splice(read_ldtr, "sel ", " base"), 16)
            ldtr_base = int(splice(read_ldtr, "base ", " limit"), 16)
            ldtr_limit = int(splice(read_ldtr, "limit ", " type"), 16)
            ldtr_type = int(splice(read_ldtr, "type ", " s"), 16)
            ldtr_s = int(splice(read_ldtr, "s ", " dpl"), 16)
            ldtr_dpl = int(splice(read_ldtr, "dpl ", " p"), 16)
            ldtr_p = int(splice(read_ldtr, "p ", "\n"), 16)

            ldtr_info["sel"] = ldtr_sel
            ldtr_info["base"] = ldtr_base
            ldtr_info["limit"] = ldtr_limit
            ldtr_info["type"] = ldtr_type
            ldtr_info["s"] = ldtr_s
            ldtr_info["dpl"] = ldtr_dpl
            ldtr_info["p"] = ldtr_p
        except ValueError as e:
            print(f"Error parsing ldtr register: {e}")

        return ldtr_info

    else:
        raise Exception("Not supported in QEMU :(")


def init_rw_memory():
    global GDBP_OBJ
    GDBP_OBJ.init_detect_vmware_or_qemu()
