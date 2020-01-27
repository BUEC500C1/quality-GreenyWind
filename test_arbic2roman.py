import pytest
from arbic2roman import a2r

def test_invalid_input():
	assert a2r("*") == "invalid input: not a number"

def test_not_integer():
	assert a2r(1.1) == "invalid input: not an integer"

def test_not_positive():
	assert a2r(0) == "invalid input: not a positive integer"
	assert a2r(-1) == "invalid input: not a positive integer"

def test_too_large():
	assert a2r(4000) == "invalid input: integer out of range [1, 3999]"

def test_normal_input():
	assert a2r(3) == "III"
	assert a2r(4) == "IV"
	assert a2r(8) == "VIII"
	assert a2r(9) == "IX"
	assert a2r(20) == "XX"
	assert a2r(40) == "XL"
	assert a2r(80) == "LXXX"
	assert a2r(90) == "XC"
	assert a2r(300) == "CCC"
	assert a2r(400) == "CD"
	assert a2r(800) == "DCCC"
	assert a2r(900) == "CM"
	assert a2r(1999) == "MCMXCIX"
	assert a2r(549) == "DXLIX"