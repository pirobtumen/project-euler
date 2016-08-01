"""
	Project Euler - 2
	======================

    'Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.'


	Alberto Sola - 2016
"""

def fibonacci_sum(n):
    a = 1
    b = 2
    c = 0
    fib_sum = 2

    a_even = False
    b_even = True

    c = a + b

    while c < n:
        c_even = (a_even and b_even) or (not a_even and not b_even)
        a_even = b_even
        b_even = c_even

        if c_even:
            fib_sum += c

        a = b
        b = c
        c = a + b

    return fib_sum

if __name__ == '__main__':

    N = 4000000
    #N = 100

    fib_sum = fibonacci_sum(N)

    print("Sum: " + str(fib_sum))
