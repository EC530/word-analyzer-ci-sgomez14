from word_counter import word_counter


def test_short_txt() -> None:
    """Testing txt file with short content"""

    countingResult = word_counter("test1.txt")

    expectedResult = {"hello": 1, "lamb": 2, "little": 2, "mary": 1}

    assert countingResult == expectedResult

def test_empty_file_txt() -> None:
    """Testing txt file that is empty"""

    countingResult = word_counter("emptyText.txt")

    expectedResult = {}

    assert countingResult == expectedResult

def test_file_with_only_nltk_txt() -> None:
    """Testing txt file that only has nltk words"""

    countingResult = word_counter("all_nltk_text.txt")

    expectedResult = {}

    assert countingResult == expectedResult
