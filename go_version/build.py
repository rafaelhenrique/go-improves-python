from pybindgen import retval, param, Module
import sys

mod = Module('gosum')
mod.add_include('"sum_numbers.h"')
mod.add_function(
    'SumSlicePy',
    retval('int'),
    [param('PyObject *', 'slice', transfer_ownership=True)],
)
mod.generate(sys.stdout)
