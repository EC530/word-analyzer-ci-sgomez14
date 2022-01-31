from collections import defaultdict
from matplotlib import pyplot as plt
import re
# import PyPDF2
# import fitz
from bs4 import BeautifulSoup


# returns file type as string else it returns "invalidFileName"
def getFileFormat(file):

    print("Determining file type.")

    # checking if the argument passed is a string
    if isinstance(file, str):

        # tokenize the file string into file name and type
        fileName = file.split(".")

        # split returns list with only one element if delimiter not present in string
        if len(fileName) > 1:

            print(f"User passed \"{file}\" as file name.")

            # extract the file type
            fileType = fileName[1]

            print(f"The file extension is: {fileType}")
            return fileType

        else:
            print(f"\"{file}\" is not a valid file name")
            return "invalidFileName"


def processTextFile(file):
    """returns contents of txt file in a string and True to indicate file opened successfully,
    else it returns message and False to indicate that file could not be opened"""

    print("\nProcessing txt file.")

    try:
        with open(file, "r") as inFile:
            # read the entire text into a string
            fileText = inFile.read()

            # opening file successful
            openResult = True

            return fileText, openResult

    except IOError:
        message = f"Error:Sorry, the file {file} cannot be opened. Please check it exists in your directory."
        openResult = False
        print(message)

        return message, openResult


def processPDFFile(file):

    print("\nProcessing PDF file.")

    fileText = ""

    try:
        print("placeholder for pdf parsing")
        # PyPDF2 version: commenting out since testing showed it has text parsing errors
        # with open(file, "rb") as pdfFile:
        #     # create pdfReader object
        #     pdfReader = PyPDF2.PdfFileReader(pdfFile)
        #
        #     # get total number of pages
        #     totalPages = pdfReader.numPages
        #
        #     # extract text from all pdf pages
        #     for page in range(totalPages):
        #         # create page page object
        #         pdfPage = pdfReader.getPage(page)
        #
        #         # append extracted text to fileText string
        #         fileText = fileText + " " + pdfPage.extractText()
        #
        #     # opening file successful
        #     openResult = True
        #
        #     return fileText, openResult

        # fitz version
        # pdfDocObj = fitz.Document(file)
        #
        # for page in pdfDocObj:
        #
        #     fileText = fileText + " " + page.get_text("text")
        #
        # # opening file successful
        # openResult = True
        #
        # return fileText, openResult

    except IOError:
        message = f"Sorry, the file {file} cannot be opened. Please check it exists in your directory."
        openResult = False
        print(message)

        return message, openResult


def processHTMLFile(file):

    # parsing html: https://www.geeksforgeeks.org/how-to-parse-local-html-file-in-python/
    # try to open HTML file
    try:
        # opening the html file
        with open(file, "r") as htmlFile:

            # read the html file
            htmlContents = htmlFile.read()

            # create BeautifulSoup object with specific parser
            parserObj = BeautifulSoup(htmlContents, 'html.parser')

            # extract text from html
            fileText = parserObj.get_text()

            # opening file successful
            openResult = True

            return fileText, openResult

    except IOError:
        message = f"Sorry, the file {file} cannot be opened. Please check it exists in your directory."
        openResult = False
        print(message)

        return message, openResult


# returns the contents of file in string and true to indicate opening was successful
# otherwise returns string with warning message and false to indicate that opening was not successful
def openSupportedFormat(file, filetype):

    if filetype == "txt":

        fileContents, openResult = processTextFile(file)

    elif filetype == "pdf":

        fileContents, openResult = processPDFFile(file)

    elif filetype == "html":

        fileContents, openResult = processHTMLFile(file)

    else:
        fileContents = "File format not supported"
        openResult = False

    return fileContents, openResult


def textPreprocessing(file):
    fileText = ""
    textList = []
    finalTextList = []
    supported_formats = ["txt", "pdf", "html"]
    removeList = ["\n", ".", "?", "!", ";", ":", ";", ","]

    # set of words to filter out
    nltk = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
            "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
            "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
            "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
            "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    # checking if file format supported
    fileType = getFileFormat(file)

    if fileType in supported_formats:

        fileText, openResult = openSupportedFormat(file, fileType)

        if openResult:

            # removing all punctuation using regex:
            # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
            fileText = re.sub(r'[^\w\s]', '', fileText)

            # make lowercase
            fileText = fileText.lower()

            # split string into list
            # possible issue to solve in future is compound words separated with space
            textList = fileText.split()

            # remove before submission
            print(textList)

            # remove all nltk words from text
            for word in textList:
                if word not in nltk:
                    finalTextList.append(word)

            # sort words in ascending order
            finalTextList.sort()

            # preprocessing successful
            preprocessingResult = True

            return finalTextList, preprocessingResult

        else:
            message = fileText
            preprocessingResult = False
            return message, preprocessingResult

    else:
        message = "File format not supported"
        preprocessingResult = False
        return message, preprocessingResult


def count_words(sorted_text_list):
    # create dictionary with defaultdict collection type. (int) to indicate that values will be integers
    text_count = defaultdict(int)

    # idea for defaultdict comes from:
    # https://www.humaneer.org/blog/how-to-plot-a-histogram-using-python-matplotlib/
    for word in sorted_text_list:
        text_count[word] += 1

    return dict(text_count)


def generate_histogram(text_count_dict):

    print("Creating Histogram.")
    words = text_count_dict.keys()
    counts = text_count_dict.values()

    plt.bar(range(len(words)), counts)

    # give title to histogram
    plt.title("Histogram of Word Counts in Text")

    # label y-axis
    plt.ylabel("No. of Occurrences")

    # label each tick
    plt.xticks(range(len(words)), words)

    # rotate labels for better readability
    plt.xticks(rotation=15)

    # having issues with generating larger image for histrogram
    # plt.figure(figsize=(100, 100))

    # display the plot
    plt.show()


def word_counter(file, display_histogram=False) -> dict:
    """if preprocessing is successful then a sorted list is returned,
    otherwise a string message is returned along with a boolean that is false"""

    preprocessingContents, preprocessingResult = textPreprocessing(file)

    if preprocessingResult:

        # pass sorted list to count_words function
        # expecting a dictionary where the words are the keys and the values are the count of that word
        count_dict = count_words(preprocessingContents)

        print(count_dict)

        """User option to display histogram"""
        if display_histogram:
            # pass dictionary to get histogram
            generate_histogram(count_dict)

        return count_dict

    else:
        # prints processing error
        print(preprocessingContents)

        emptyDictionary = {}

        return emptyDictionary


if __name__ == '__main__':

    # Sample call of word_counter()
    word_counter("test1.txt")
