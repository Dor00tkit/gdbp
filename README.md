# gdbp
This repo is based on:
https://github.com/ramikg/gdbp

A wrapper for GDB's Python API, helping you write GDB Python scripts efficiently and intuitively.

## Features
* Detecting QEMU\VMware gdbstub
* Read\Write to memory (also added support physical memory)
* Read\Write - to registers (also added support reading of CR0, CR2 CR3, CR4 - QEMU and VMware. GDTR, IDTR and LDTR -  VMware only)

## Installation
```sh
git clone https://github.com/Dor00tkit/gdbp.git
cd gdbp
python setup.py install
```

## Supported platforms
- GDB 7.2+
- Python 3.0+
- Any GDB-supported architecture
