from word_counter import word_counter

test_files = "test_files/"


# General tests for all supported formats

def test_invalid_filename() -> None:
    """Testing function by passing invalid file name"""

    countingResult = word_counter("invalidFile")

    expectedResult = {}

    assert countingResult == expectedResult


def test_unsupported_format() -> None:
    """Testing function by passing unsupported format"""

    countingResult = word_counter("Mary.docx")

    expectedResult = {}

    assert countingResult == expectedResult


# Txt tests start here

def test_short_txt() -> None:
    """Testing txt file with short content"""

    countingResult = word_counter(test_files + "test1.txt")

    expectedResult = {"hello": 1, "lamb": 2, "little": 2, "mary": 1}

    assert countingResult == expectedResult


def test_empty_file_txt() -> None:
    """Testing txt file that is empty"""

    countingResult = word_counter(test_files + "emptyText.txt")

    expectedResult = {}

    assert countingResult == expectedResult


def test_file_doesnt_exist_txt() -> None:
    """Testing file does not exist"""

    countingResult = word_counter("fileDoesntExist.txt")

    expectedResult = {}

    assert countingResult == expectedResult


def test_file_with_only_nltk_txt() -> None:
    """Testing txt file that only has nltk words"""

    countingResult = word_counter(test_files + "all_nltk_text.txt")

    expectedResult = {}

    assert countingResult == expectedResult


def test_file_with_only_numbers_txt() -> None:
    """Testing txt file that only has numbers"""

    countingResult = word_counter(test_files + "only_nums_text.txt")

    expectedResult = {"10": 2, "28": 2, "1991": 2, "2000": 1}

    assert countingResult == expectedResult


def test_longer_text_txt() -> None:
    """Testing a text file with longer paragraph.
    It comes from https://www.w3.org/TR/PNG/iso_8859-1.txt
    and is about ISO 8859-1 (1987)"""

    countingResult = word_counter(test_files + "iso_text.txt")

    expectedResult = {"following": 1, "graphical": 1, "noncontrol": 1, "characters": 1, "defined": 1,
                      "iso": 1, "88591": 1, "1987": 1, "descriptions": 1, "words": 1, "arent": 1,
                      "helpful": 1, "theyre": 1, "best": 1, "text": 1, "graphics": 1, "file": 2,
                      "illustrating": 1, "character": 1, "set": 1, "available": 1, "archive": 1}

    assert countingResult == expectedResult


# HTML tests start here

def test_simple_html() -> None:
    """This test assess the code with an simple HTML file from Geeks4Geeks"""

    countingResult = word_counter(test_files + "htmlTest.html")

    expectedResult = {"geeksforgeeks": 1, "computer": 1, "science": 1, "portal": 1}

    assert countingResult == expectedResult


def test_empty_file_html() -> None:
    """Testing html file that is empty"""

    countingResult = word_counter(test_files + "emptyHTML.html")

    expectedResult = {}

    assert countingResult == expectedResult


def test_no_content_html() -> None:
    """Testing html file that has valid tag structure but no actual content to render.
    HTML generated by Quackit.com"""

    countingResult = word_counter(test_files + "noContentHTML.html")

    expectedResult = {}

    assert countingResult == expectedResult


def test_file_doesnt_exist_html() -> None:
    """Testing file does not exist"""

    countingResult = word_counter("fileDoesntExist.html")

    expectedResult = {}

    assert countingResult == expectedResult


def test_file_with_only_nltk_html() -> None:
    """Testing html file that only has nltk words.
    HTML generated by Quackit.com"""

    countingResult = word_counter(test_files + "all_nltk_text.html")

    expectedResult = {}

    assert countingResult == expectedResult


def test_file_with_only_numbers_html() -> None:
    """Testing html file that only has numbers.
    HTML generated by Quackit.com"""

    countingResult = word_counter(test_files + "only_nums_text.html")

    expectedResult = {"10": 2, "28": 2, "1991": 2, "2000": 1}

    assert countingResult == expectedResult


def test_longer_text_html() -> None:
    """Testing a text file with longer paragraph.
    It comes from https://www.w3.org/TR/PNG/iso_8859-1.txt
    and is about ISO 8859-1 (1987)"""

    countingResult = word_counter(test_files + "iso_text.html")

    expectedResult = {"following": 1, "graphical": 1, "noncontrol": 1, "characters": 1, "defined": 1,
                      "iso": 1, "88591": 1, "1987": 1, "descriptions": 1, "words": 1, "arent": 1,
                      "helpful": 1, "theyre": 1, "best": 1, "text": 1, "graphics": 1, "file": 2,
                      "illustrating": 1, "character": 1, "set": 1, "available": 1, "archive": 1}

    assert countingResult == expectedResult

