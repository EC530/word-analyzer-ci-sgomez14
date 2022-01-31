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


def test_file_with_only_numbers_txt() -> None:
    """Testing txt file that only has numbers"""

    countingResult = word_counter("only_nums_text.txt")

    expectedResult = {"10": 2, "28": 2, "1991": 2, "2000": 1}

    assert countingResult == expectedResult

def test_longer_text_txt() -> None:
    """Testing a text file with longer paragraph.
    It comes from the first paragraph of ISO 8859-1 (1987)"""

    countingResult = word_counter("iso_text.txt")

    expectedResult = {"following": 1, "graphical": 1, "noncontrol": 1, "characters": 1, "defined": 1,
                      "iso": 1, "88591": 1, "1987": 1, "descriptions": 1, "words": 1, "arent": 1,
                      "helpful": 1, "theyre": 1, "best": 1, "text": 1, "graphics": 1, "file": 2,
                      "illustrating": 1, "character": 1, "set": 1, "available": 1, "archive": 1}

    assert countingResult == expectedResult


