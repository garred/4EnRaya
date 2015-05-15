# # -*- coding: utf-8 -*-

# class MyClass(object):
#     def __init__(self):
#         pass

# def set(var, new_value):
#     var = new_value

# def to_zero(var):
#     var = 0

# a = True
# b = "Cadena"
# c = MyClass()

# print "Antes de modificar:"
# print a
# print b
# print c

# set(a, False)
# set(b, MyClass())
# set(c, object())

# print "\nDespues de modificar:"
# print a
# print b
# print c

# to_zero(a)
# to_zero(b)
# to_zero(c)

# print "\nDespues de modificar 2:"
# print a
# print b
# print c

def devuelve_multiples_valores():
    return 1, 2, 3

a = devuelve_multiples_valores()
print a#,b,c
print a[1]
a[1]=34