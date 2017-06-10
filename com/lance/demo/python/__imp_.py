# from __func_ import cal
import __func_
import __class_
print __func_.cal(1, 2)

# dir
print dir(__func_)

# globals
print globals()

# locals
print locals()

# reload
reload(__func_)

t = __class_.demoClass("lance")
t.demo()

print t.__doc__

print t.__class__

print t.__module__