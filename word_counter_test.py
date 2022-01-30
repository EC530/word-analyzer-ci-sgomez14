from word_counter import word_counter


def test_short_txt() -> None:
    """Testing txt file with short content"""

    countingResult = word_counter("test1.txt")

    expectedResult = {"hello": 1, "lamb": 2, "little": 2, "mary": 1}

    assert countingResult == expectedResult

