import pytest

from str.string_calculte import stringcalcult

@pytest.mark.parametrize("number,expected",[("0",0),("1",1),("2",2)])
def test_calculte_string(number,expected):
    assert stringcalcult(number) == expected
