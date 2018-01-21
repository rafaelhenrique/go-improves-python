from pybindgen import retval, param, Module
import sys

mod = Module('gosum_module')
mod.add_include('"gosum.h"')
mod.add_function(
    'SumSlicePy',
    retval('int'),
    [param('PyObject *', 'slice', transfer_ownership=True)],
)
mod.generate(sys.stdout)
