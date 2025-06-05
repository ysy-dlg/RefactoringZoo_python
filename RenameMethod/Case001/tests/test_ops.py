from core.math_ops import squared_norm

def test_squared_norm():
    result = squared_norm(3, 4)
    assert result == 25
