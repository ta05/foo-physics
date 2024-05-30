from foo.foo import volume

def test_volume():
    """Test volume function"""
    expected = {
        0: 0.0,
        10: 4188.790204786391,
        198: 32515031.57531224,
        7.11: 1505.5577247239269,
    }
    for k in expected:
        actual = volume(k)
        assert actual == expected[k], f"Incorrect, the volume of a sphere of radius {k} is {expected[k]} not {actual}"
