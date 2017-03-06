from django.test import TestCase

# Create your tests here.


def deco(fun):
    def _deco(*args, **kwargs):
        print 'before'
        ret = fun(*args, **kwargs)
        print 'after'
        return ret
    return _deco

@deco
def test(a,b,c):
    print a,b,c

test(1,2,3)