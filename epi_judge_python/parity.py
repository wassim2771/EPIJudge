from test_framework import generic_test



def parityAux(x: int) -> int:
    result = 0
    while x:
        result ^= 1 
        x &= x-1
    return result

cache = []
for i in range(0xFFFF):
    cache += [parityAux(i)]

def parity(x: int) -> int:
    shift_size = 16
    trim_mask = 0xFFFF
    return (cache[x >> (3 * shift_size)]) ^ (cache[(x >> (2* shift_size))&trim_mask]) ^ (cache[(x >> shift_size)&trim_mask]) ^ (cache[x & trim_mask])

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
