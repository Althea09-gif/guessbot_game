import pytest  # I use pytest to check if my functions work properly
from unittest.mock import MagicMock  # I use this to fake a socket connection
from game_utils import generate_random, get_difficulty, provide_feedback, is_valid_guess  # I import the functions I want to test

# I’m testing if generate_random() gives numbers between 1 and 10 for easy mode
def test_generate_random_easy():
    for _ in range(20):
        num = generate_random(1)
        assert 1 <= num <= 10  # I check if the number is inside the correct range

# I test if the function returns numbers between 1 and 50 for medium mode
def test_generate_random_medium():
    for _ in range(20):
        num = generate_random(2)
        assert 1 <= num <= 50

# I test if it gives numbers between 1 and 100 for hard mode
def test_generate_random_hard():
    for _ in range(20):
        num = generate_random(3)
        assert 1 <= num <= 100

# I test if it raises an error when an invalid difficulty is passed
def test_generate_random_invalid():
    with pytest.raises(ValueError):  # I expect this part to raise a ValueError
        generate_random(99)

# I test get_difficulty() with valid input directly (mocked)
def test_get_difficulty_valid_input():
    mock_conn = MagicMock()  # I create a fake connection object
    mock_conn.recv.side_effect = [b"2"]  # I pretend that the user sent "2"
    result = get_difficulty(mock_conn)
    assert result == 2  # I expect it to return 2

# I test if get_difficulty() can handle wrong inputs before getting the correct one
def test_get_difficulty_invalid_then_valid():
    mock_conn = MagicMock()
    mock_conn.recv.side_effect = [b"abc", b"4", b"1"]  # I simulate wrong inputs before a valid "1"
    result = get_difficulty(mock_conn)
    assert result == 1

# I test the feedback based on guess vs target value
def test_provide_feedback():
    assert provide_feedback(30, 50) == "Too low!"   # If guess is lower, it should say "Too low!"
    assert provide_feedback(70, 50) == "Too high!"  # If guess is higher, it should say "Too high!"
    assert provide_feedback(50, 50) == "Correct!"   # If guess is equal, it should say "Correct!"

# I test if is_valid_guess() correctly detects valid and invalid guesses
def test_is_valid_guess():
    assert is_valid_guess("123")         # This should be valid
    assert not is_valid_guess("abc")     # This should be invalid
    assert not is_valid_guess("12a3")    # Also invalid because it has a letter
