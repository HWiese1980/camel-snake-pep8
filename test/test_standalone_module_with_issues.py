
from __future__ import print_function, division, absolute_import

#
# Test collisions due to Rope renaming.
#

def camelFunction(camelArg1, camelArg2, camelArg3, camelArg4, camelArg5):
    """Warning given on this is correct: it causes an error if camelArg4 is converted
    to existing variable `camel_arg4`."""
    class snake_class(object):
        camelArg5 = camelArg3
    snake_class.camelArg1 = camelArg1
    snake_class.camelArg3 = snake_class.camelArg1
    snake_class.camelArg3 = camelArg2
    snake_class.camelArg5 = camelArg5
    camelArg4 = 999
    return 333

a_a = 44
def fF(aA, a, bB, b, cC, c, dD=3, d=a_a): # Test short names and rename to global.
    """Warning is not correct on `aA` in this function, since it does not actually
    cause an error (`a_a` exists only in module scope, but scoping isn't taken into
    account).  The resulting code is correct, but `aA` is not converted when the
    warning is heeded."""
    pass

#
# Test collision when the two suggested strings collide.
#

myVar = 5
myVAR = 44



class _snake_name(object):
    """This is a class that uses `snake_name` as its name to test when `snake_name`
    will be modified by Rope with docs set to change or not."""
    d = {"snake_name": "snake_name"}
#
# Test multiple assignment.
#


#
# Test multiple assignment.
#

xX, yY, zZ = 1, 2, 3 # xX is not modified, Rope bug in is_assigned_in_a_tuple_assignment or is_assigned_here?

yY = 100 # This change does not cause a problem since Rope also gets above yY.

#
# Test some special case short names.
#

# Names that are all caps and underscores are left unchanged (might be consts).
def _G(_, X, xX, yY, ZZ, _Y, _rR_=__name__):
    pass

