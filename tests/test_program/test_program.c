#include <stdint.h>

#define TEST_REGISTER_NAME "edx"
#define TEST_REGISTER_VALUE_TO_SET (41)

static uint64_t __attribute__((section (".test_variable"))) __attribute__((used)) test_variable = 0xF123456789ABCDEF;

void set_test_register_value()
{
	asm volatile ("mov %0, %%" TEST_REGISTER_NAME
		:
		: "n" (TEST_REGISTER_VALUE_TO_SET)
		: TEST_REGISTER_NAME);
}

int main()
{
	set_test_register_value(TEST_REGISTER_VALUE_TO_SET);

after_test_preparations:
 __attribute__((unused));
	return 0;
}
