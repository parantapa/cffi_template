from pathlib import Path
from cffi import FFI

CUR_DIR = Path(__file__).parent

CDEF = """
float pi_approx(int n);
"""

SOURCE = """
#include "pi.h"
"""

MODULE_NAME = "cffi_test._pi"

ffibuilder = FFI()
ffibuilder.cdef(CDEF)
ffibuilder.set_source(MODULE_NAME, SOURCE,
        sources=[str(CUR_DIR / "pi.c")],
        libraries=["m"],
        include_dirs=[str(CUR_DIR)]
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
