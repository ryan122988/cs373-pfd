#!/usr/bin/env python



# -------------
# pfd_compute
# -------------



# -------------
# pfd_print
# -------------

def pfd_print (w, output)
    """
    prints out the integers passed into it
    from the output array on a single line
    with a space between each and terminated
    with a newline character
    """
    x = len(output)
    x -= 1
    i = 0
    while i < x
        w.write(str(output[i]) + " ")
        i += 1
    w.write(str(output[x] + "\n")



# -------------
# collatz_solve
# -------------

def pfd_solve (r, w) :
    """
    r is a reader and it is passed 
    to the function pfd_compute
    w is a writer which is passed along
    with the output array to pfd_print
    
    """
    output = pfd_compute(r)
    pfd_print(w, output)
