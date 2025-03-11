import pytest

from fib_r import fib

def test_fib():
	assert fib( 0) ==    0
	assert fib( 1) ==    1
	assert fib( 2) ==    1
	assert fib( 3) ==    2
	assert fib( 4) ==    3
	assert fib( 5) ==    5
	assert fib( 6) ==    8
	assert fib( 7) ==   13
	assert fib( 8) ==   21
	assert fib( 9) ==   34
	assert fib(10) ==   55

	assert fib(11) ==   89
	assert fib(12) ==  144
	assert fib(13) ==  233
	assert fib(14) ==  377
	assert fib(15) ==  610
	assert fib(16) ==  987
	assert fib(17) == 1597
	assert fib(18) == 2584
	assert fib(19) == 4181
	assert fib(20) == 6765

#def test_fib_46():
#	assert fib(46) == 
#
#def test_fib_47():
#	assert fib(47) == 
