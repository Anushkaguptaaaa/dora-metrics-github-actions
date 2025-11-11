import app

def test_main_function():
    """Test the main function returns expected string"""
    result = app.main()
    assert result == "Hello DevOps This is a sample CI pipeline test"
    print("✓ Test passed: main function works correctly")

def test_addition():
    """A simple mathematical test"""
    assert 1 + 1 == 2
    print("✓ Test passed: basic addition works")