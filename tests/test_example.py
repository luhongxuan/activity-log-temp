def check_sign(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def test_check_sign():
    assert check_sign(10) == "positive"