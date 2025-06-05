from core.math_ops import square_sum

def test_square_sum():
    result = square_sum(3, 4)
    assert result == 25
