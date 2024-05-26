PROGRAM_NAME := test_program
CFLAGS = -g -Wall -no-pie -fno-stack-protector $(PROGRAM_NAME).lds

all: $(PROGRAM_NAME)_32 $(PROGRAM_NAME)_64

$(PROGRAM_NAME)_32: $(PROGRAM_NAME).c
	gcc $(CFLAGS) -m32 -o $@ $?

$(PROGRAM_NAME)_64: $(PROGRAM_NAME).c
	gcc $(CFLAGS) -m64 -o $@ $?

clean:
	$(RM) $(PROGRAM_NAME)_32 $(PROGRAM_NAME)_64
