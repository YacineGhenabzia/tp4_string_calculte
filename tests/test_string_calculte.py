import pytest

from str.string_calculte import stringcalcult

@pytest.mark.parametrize("number,expected",[("0",0),("1",1),("2",2)])
def test_calculte_string_0_return_0(number,expected):
    assert stringcalcult(number) == expected
