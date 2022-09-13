#include <arm_neon.h>

uint32x4_t double_elements(uint32x4_t input)
{
    return (vaddq_u32(input, input));
}
