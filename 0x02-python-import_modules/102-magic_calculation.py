#!/usr/bin/pythonn3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
<<<<<<< HEAD
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            return c
        else:
            return (sub(a, b))
=======
        s = add(a, b)
        for i in range(4, 6):
            s = add(s, i)
        return s
    else: 
        return (sub(a, b))
>>>>>>> 69738590ab838226c95d9b94c6bd8e59a97eb41a
