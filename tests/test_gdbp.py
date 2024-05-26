import gdb
import gdbp


def test_general_purpose_registers():
    general_purpose_registers_out = gdb.execute("i r ", to_string=True)
    print(general_purpose_registers_out)

    # get rax, eax, ax, ah, al
    rax = gdbp.get_rax()
    eax = gdbp.get_eax()
    ax = gdbp.get_ax()
    ah = gdbp.get_ah()
    al = gdbp.get_al()
    print("test_general_purpose_registers:")
    print(f"rax: {hex(rax)}, eax: {hex(eax)}, ax: {hex(ax)}, ah: {hex(ah)}, ah: {hex(al)}")

    # get rbx, ebx, bx, bl
    rbx = gdbp.get_rbx()
    ebx = gdbp.get_ebx()
    bx = gdbp.get_bx()
    bl = gdbp.get_bl()
    print(f"rbx: {hex(rbx)}, ebx: {hex(ebx)}, bx: {hex(bx)}, bl: {hex(bl)}")

    # get rcx, ecx, cx, cl
    rcx = gdbp.get_rcx()
    ecx = gdbp.get_ecx()
    cx = gdbp.get_cx()
    cl = gdbp.get_cl()
    print(f"rcx: {hex(rcx)}, ecx: {hex(ecx)}, cx: {hex(cx)}, cl: {hex(cl)}")

    # get rdx, edx, dx, dl
    rdx = gdbp.get_rdx()
    edx = gdbp.get_edx()
    dx = gdbp.get_dx()
    dl = gdbp.get_dl()
    print(f"rdx: {hex(rdx)}, edx: {hex(edx)}, dx: {hex(dx)}, dl: {hex(dl)}")

    # get rsi, esi, si, sil
    rsi = gdbp.get_rsi()
    esi = gdbp.get_esi()
    si = gdbp.get_si()
    sil = gdbp.get_sil()
    print(f"rsi: {hex(rsi)}, esi: {hex(esi)}, si: {hex(si)}, sil: {hex(sil)}")

    # get rdi, edi, di, dil
    rdi = gdbp.get_rdi()
    edi = gdbp.get_edi()
    di = gdbp.get_di()
    dil = gdbp.get_dil()
    print(f"rdi: {hex(rdi)}, edi: {hex(edi)}, di: {hex(di)}, dil: {hex(dil)}")

    # get rbp, ebp, bp, bpl
    rbp = gdbp.get_rbp()
    ebp = gdbp.get_ebp()
    bp = gdbp.get_bp()
    bpl = gdbp.get_bpl()
    print(f"rbp: {hex(rbp)}, ebp: {hex(ebp)}, bp: {hex(bp)}, bpl: {hex(bpl)}")

    # get rsp, esp, sp, spl
    rsp = gdbp.get_rsp()
    esp = gdbp.get_esp()
    sp = gdbp.get_sp()
    spl = gdbp.get_spl()
    print(f"rsp: {hex(rsp)}, esp: {hex(esp)}, sp: {hex(sp)}, spl: {hex(spl)}")

    # get r8, r8d, r8w, r8b
    r8 = gdbp.get_r8()
    r8d = gdbp.get_r8d()
    r8w = gdbp.get_r8w()
    r8b = gdbp.get_r8b()
    print(f"r8: {hex(r8)}, r8d: {hex(r8d)}, r8w: {hex(r8w)}, r8b: {hex(r8b)}")

    # get r9, r9d, r9w, r9b
    r9 = gdbp.get_r9()
    r9d = gdbp.get_r9d()
    r9w = gdbp.get_r9w()
    r9b = gdbp.get_r9b()
    print(f"r9: {hex(r9)}, r9d: {hex(r9d)}, r9w: {hex(r9w)}, r9b: {hex(r9b)}")

    # get r10, r10d, r10w, r10b
    r10 = gdbp.get_r10()
    r10d = gdbp.get_r10d()
    r10w = gdbp.get_r10w()
    r10b = gdbp.get_r10b()
    print(f"r10: {hex(r10)}, r10d: {hex(r10d)}, r10w: {hex(r10w)}, r10b: {hex(r10b)}")

    # get r11, r11d, r11w, r11b
    r11 = gdbp.get_r11()
    r11d = gdbp.get_r11d()
    r11w = gdbp.get_r11w()
    r11b = gdbp.get_r11b()
    print(f"r11: {hex(r11)}, r11d: {hex(r11d)}, r11w: {hex(r11w)}, r11b: {hex(r11b)}")

    # get r12, r12d, r12w, r12b
    r12 = gdbp.get_r12()
    r12d = gdbp.get_r12d()
    r12w = gdbp.get_r12w()
    r12b = gdbp.get_r12b()
    print(f"r12: {hex(r12)}, r12d: {hex(r12d)}, r12w: {hex(r12w)}, r12b: {hex(r12b)}")

    # get r13, r13d, r13w, r13b
    r13 = gdbp.get_r13()
    r13d = gdbp.get_r13d()
    r13w = gdbp.get_r13w()
    r13b = gdbp.get_r13b()
    print(f"r13: {hex(r13)}, r13d: {hex(r13d)}, r13w: {hex(r13w)}, r13b: {hex(r13b)}")

    # get r14, r14d, r14w, r14b
    r14 = gdbp.get_r14()
    r14d = gdbp.get_r14d()
    r14w = gdbp.get_r14w()
    r14b = gdbp.get_r14b()
    print(f"r14: {hex(r14)}, r14d: {hex(r14d)}, r14w: {hex(r14w)}, r14b: {hex(r14b)}")

    # get r15, r15d, r15w, r15b
    r15 = gdbp.get_r15()
    r15d = gdbp.get_r15d()
    r15w = gdbp.get_r15w()
    r15b = gdbp.get_r15b()
    print(f"r15: {hex(r15)}, r15d: {hex(r15d)}, r15w: {hex(r15w)}, r15b: {hex(r15b)}")

    rip = gdbp.get_rip()
    eip = gdbp.get_eip()
    ip = gdbp.get_ip()

    print(f"rip: {hex(rip)}, eip: {hex(eip)}, ip: {hex(ip)}")

    eflags = gdbp.get_eflags()
    print(f"eflags: {hex(eflags)}\n")


def test_segment_registers():
    segment_registers_out = gdb.execute("i r cs ss ds es fs gs", to_string=True)
    print(segment_registers_out)

    cs = gdbp.get_cs()
    ss = gdbp.get_ss()
    ds = gdbp.get_ds()
    es = gdbp.get_es()
    fs = gdbp.get_fs()
    gs = gdbp.get_gs()

    print("test_segment_registers:")
    print(f"cs: {hex(cs)}")
    print(f"ss: {hex(ss)}")
    print(f"ds: {hex(ds)}")
    print(f"es: {hex(es)}")
    print(f"fs: {hex(fs)}")
    print(f"gs: {hex(gs)}\n")


def test_control_registers():
    cr0_out = gdb.execute("monitor r cr0", to_string=True)
    cr2_out = gdb.execute("monitor r cr2", to_string=True)
    cr3_out = gdb.execute("monitor r cr3", to_string=True)
    cr4_out = gdb.execute("monitor r cr4", to_string=True)

    print(cr0_out.strip())
    print(cr2_out.strip())
    print(cr3_out.strip())
    print(cr4_out)

    cr0 = gdbp.get_cr0()
    cr2 = gdbp.get_cr2()
    cr3 = gdbp.get_cr3()
    cr4 = gdbp.get_cr4()

    print("test_control_registers:")
    print(f"cr0: {hex(cr0)}")
    print(f"cr2: {hex(cr2)}")
    print(f"cr3: {hex(cr3)}")
    print(f"cr4: {hex(cr4)}\n")


def test_other_registers():
    gdtr_out = gdb.execute("monitor r gdtr", to_string=True)
    idtr_out = gdb.execute("monitor r idtr", to_string=True)
    ldtr_out = gdb.execute("monitor r ldtr", to_string=True)

    print(gdtr_out.strip())
    print(idtr_out.strip())
    print(ldtr_out)

    gdtr_base, gdtr_limit = gdbp.get_gdtr()
    idtr_base, idtr_limit = gdbp.get_idtr()
    ldtr_info = gdbp.get_ldtr()

    print("test_other_registers:")
    print(f"gdtr base={hex(gdtr_base)} limit={hex(gdtr_limit)}")
    print(f"idtr base={hex(idtr_base)} limit={hex(idtr_limit)}")
    print(f"ldtr sel {hex(ldtr_info['sel'])} base {hex(ldtr_info['base'])} limit {hex(ldtr_info['limit'])} "
          f"type {hex(ldtr_info['type'])} s {hex(ldtr_info['s'])} dpl {hex(ldtr_info['dpl'])} "
          f"p {hex(ldtr_info['p'])}\n")


def test_write_read_registers():
    try:
        print("test_write_read_registers():")
        # 64-bit registers
        gdbp.set_rax(0x123456789ABCDEF0)
        assert gdbp.get_rax() == 0x123456789ABCDEF0

        gdbp.set_rbx(0x123456789ABCDEF0)
        assert gdbp.get_rbx() == 0x123456789ABCDEF0

        gdbp.set_rcx(0x123456789ABCDEF0)
        assert gdbp.get_rcx() == 0x123456789ABCDEF0

        gdbp.set_rdx(0x123456789ABCDEF0)
        assert gdbp.get_rdx() == 0x123456789ABCDEF0

        gdbp.set_rsi(0x123456789ABCDEF0)
        assert gdbp.get_rsi() == 0x123456789ABCDEF0

        gdbp.set_rdi(0x123456789ABCDEF0)
        assert gdbp.get_rdi() == 0x123456789ABCDEF0

        gdbp.set_rbp(0x123456789ABCDEF0)
        assert gdbp.get_rbp() == 0x123456789ABCDEF0

        gdbp.set_rsp(0x123456789ABCDEF0)
        assert gdbp.get_rsp() == 0x123456789ABCDEF0

        gdbp.set_r8(0x123456789ABCDEF0)
        assert gdbp.get_r8() == 0x123456789ABCDEF0

        gdbp.set_r9(0x123456789ABCDEF0)
        assert gdbp.get_r9() == 0x123456789ABCDEF0

        gdbp.set_r10(0x123456789ABCDEF0)
        assert gdbp.get_r10() == 0x123456789ABCDEF0

        gdbp.set_r11(0x123456789ABCDEF0)
        assert gdbp.get_r11() == 0x123456789ABCDEF0

        gdbp.set_r12(0x123456789ABCDEF0)
        assert gdbp.get_r12() == 0x123456789ABCDEF0

        gdbp.set_r13(0x123456789ABCDEF0)
        assert gdbp.get_r13() == 0x123456789ABCDEF0

        gdbp.set_r14(0x123456789ABCDEF0)
        assert gdbp.get_r14() == 0x123456789ABCDEF0

        gdbp.set_r15(0x123456789ABCDEF0)
        assert gdbp.get_r15() == 0x123456789ABCDEF0

        # Lower 32 bits
        gdbp.set_eax(0x89ABCDEF)
        assert gdbp.get_eax() == 0x89ABCDEF

        gdbp.set_ebx(0x89ABCDEF)
        assert gdbp.get_ebx() == 0x89ABCDEF

        gdbp.set_ecx(0x89ABCDEF)
        assert gdbp.get_ecx() == 0x89ABCDEF

        gdbp.set_edx(0x89ABCDEF)
        assert gdbp.get_edx() == 0x89ABCDEF

        gdbp.set_esi(0x89ABCDEF)
        assert gdbp.get_esi() == 0x89ABCDEF

        gdbp.set_edi(0x89ABCDEF)
        assert gdbp.get_edi() == 0x89ABCDEF

        gdbp.set_ebp(0x89ABCDEF)
        assert gdbp.get_ebp() == 0x89ABCDEF

        gdbp.set_esp(0x89ABCDEF)
        assert gdbp.get_esp() == 0x89ABCDEF

        gdbp.set_r8d(0x89ABCDEF)
        assert gdbp.get_r8d() == 0x89ABCDEF

        gdbp.set_r9d(0x89ABCDEF)
        assert gdbp.get_r9d() == 0x89ABCDEF

        gdbp.set_r10d(0x89ABCDEF)
        assert gdbp.get_r10d() == 0x89ABCDEF

        gdbp.set_r11d(0x89ABCDEF)
        assert gdbp.get_r11d() == 0x89ABCDEF

        gdbp.set_r12d(0x89ABCDEF)
        assert gdbp.get_r12d() == 0x89ABCDEF

        gdbp.set_r13d(0x89ABCDEF)
        assert gdbp.get_r13d() == 0x89ABCDEF

        gdbp.set_r14d(0x89ABCDEF)
        assert gdbp.get_r14d() == 0x89ABCDEF

        gdbp.set_r15d(0x89ABCDEF)
        assert gdbp.get_r15d() == 0x89ABCDEF

        # Lower 16 bits
        gdbp.set_ax(0xCDEF)
        assert gdbp.get_ax() == 0xCDEF

        gdbp.set_bx(0xCDEF)
        assert gdbp.get_bx() == 0xCDEF

        gdbp.set_cx(0xCDEF)
        assert gdbp.get_cx() == 0xCDEF

        gdbp.set_dx(0xCDEF)
        assert gdbp.get_dx() == 0xCDEF

        gdbp.set_si(0xCDEF)
        assert gdbp.get_si() == 0xCDEF

        gdbp.set_di(0xCDEF)
        assert gdbp.get_di() == 0xCDEF

        gdbp.set_bp(0xCDEF)
        assert gdbp.get_bp() == 0xCDEF

        gdbp.set_sp(0xCDEF)
        assert gdbp.get_sp() == 0xCDEF

        gdbp.set_r8w(0xCDEF)
        assert gdbp.get_r8w() == 0xCDEF

        gdbp.set_r9w(0xCDEF)
        assert gdbp.get_r9w() == 0xCDEF

        gdbp.set_r10w(0xCDEF)
        assert gdbp.get_r10w() == 0xCDEF

        gdbp.set_r11w(0xCDEF)
        assert gdbp.get_r11w() == 0xCDEF

        gdbp.set_r12w(0xCDEF)
        assert gdbp.get_r12w() == 0xCDEF

        gdbp.set_r13w(0xCDEF)
        assert gdbp.get_r13w() == 0xCDEF

        gdbp.set_r14w(0xCDEF)
        assert gdbp.get_r14w() == 0xCDEF

        gdbp.set_r15w(0xCDEF)
        assert gdbp.get_r15w() == 0xCDEF

        # Lower 8 bits
        gdbp.set_al(0xEF)
        assert gdbp.get_al() == 0xEF

        gdbp.set_bl(0xEF)
        assert gdbp.get_bl() == 0xEF

        gdbp.set_cl(0xEF)
        assert gdbp.get_cl() == 0xEF

        gdbp.set_dl(0xEF)
        assert gdbp.get_dl() == 0xEF

        gdbp.set_sil(0xEF)
        assert gdbp.get_sil() == 0xEF

        gdbp.set_dil(0xEF)
        assert gdbp.get_dil() == 0xEF

        gdbp.set_bpl(0xEF)
        assert gdbp.get_bpl() == 0xEF

        gdbp.set_spl(0xEF)
        assert gdbp.get_spl() == 0xEF

        gdbp.set_r8b(0xEF)
        assert gdbp.get_r8b() == 0xEF

        gdbp.set_r9b(0xEF)
        assert gdbp.get_r9b() == 0xEF

        gdbp.set_r10b(0xEF)
        assert gdbp.get_r10b() == 0xEF

        gdbp.set_r11b(0xEF)
        assert gdbp.get_r11b() == 0xEF

        gdbp.set_r12b(0xEF)
        assert gdbp.get_r12b() == 0xEF

        gdbp.set_r13b(0xEF)
        assert gdbp.get_r13b() == 0xEF

        gdbp.set_r14b(0xEF)
        assert gdbp.get_r14b() == 0xEF

        gdbp.set_r15b(0xEF)
        assert gdbp.get_r15b() == 0xEF

        gdbp.set_cs(0x90)
        assert gdbp.get_cs() == 0x90

        gdbp.set_ss(0x90)
        assert gdbp.get_ss() == 0x90

        gdbp.set_es(0x90)
        assert gdbp.get_es() == 0x90

        gdbp.set_ds(0x90)
        assert gdbp.get_ds() == 0x90

        gdbp.set_fs(0x90)
        assert gdbp.get_fs() == 0x90

        gdbp.set_gs(0x90)
        assert gdbp.get_gs() == 0x90

        print("All register functions executed successfully and passed the assertions.")

    except Exception as e:
        print(f"Error during testing registers: {e}")


gdbp.init_rw_memory()
test_general_purpose_registers()
test_segment_registers()
test_control_registers()
test_other_registers()
test_write_read_registers()
