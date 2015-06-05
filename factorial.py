"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""

from nose.tools import assert_equal


def factorial_recursive(n):
    n = int(n)
    if n == 1:
        output = 1
        return output
    else:
        output = n * factorial_recursive(n - 1)
        return output


def test_factorial():
    assert_equal(factorial_recursive(1), 1)
    assert_equal(factorial_recursive(2), 2)
    assert_equal(factorial_recursive(3), 6)


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))
