from collections import defaultdict
from matplotlib import pyplot as plt
import re
import PyPDF2
from bs4 import BeautifulSoup


def textPreprocessing(file):
    fileText = ""
    textList = []
    finalTextList = []
    supported_formats = [".txt", ".pdf", ".html"]
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
    if file[-4:] or file[-5:] in supported_formats:
        # proceed to opening txt file
        if file[-4:] == ".txt":
            try:
                with open(file, "r") as inFile:
                    # read the entire text into a string
                    fileText = inFile.read()
            except IOError:
                message = f"Sorry, the file {file} cannot be opened. Please check it exists in your directory."

                return message

        # try to open PDF file
        elif file[-4:] == ".pdf":
            try:
                with open(file, "rb") as pdfFile:
                    # create pdfReader object
                    pdfReader = PyPDF2.PdfFileReader(pdfFile)

                    # get total number of pages
                    totalPages = pdfReader.numPages

                    # extract text from all pdf pages
                    for page in range(totalPages):
                        # create page page object
                        pdfPage = pdfReader.getPage(page)

                        # append extracted text to fileText string
                        fileText = fileText + " " + pdfPage.extractText()

            except IOError:
                message = f"Sorry, the file {file} cannot be opened. Please check it exists in your directory."

                return message

        # parsing html: https://www.geeksforgeeks.org/how-to-parse-local-html-file-in-python/
        # try to open HTML file
        elif file[-5:] == ".html":
            try:
                # opening the html file
                with open(file, "r") as htmlFile:

                    # read the html file
                    htmlContents = htmlFile.read()

                    # create BeautifulSoup object with specific parser
                    parserObj = BeautifulSoup(htmlContents, 'html.parser')

                    # extract text from html
                    fileText = parserObj.get_text()

            except IOError:
                message = f"Sorry, the file {file} cannot be opened. Please check it exists in your directory."

                return message

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

        finalTextList.sort()

        return finalTextList
    else:
        return "format not supported"




def count_words(sorted_text_list):
    # create dictionary with first entry
    text_count = defaultdict(int)  # {sorted_text_list[0]: 1}

    # offset by one so that loop does not go out of bound
    # for index in range(len(sorted_text_list) - 1):
    #     currentWord = sorted_text_list[index]
    #     neighbor = sorted_text_list[index + 1]
    #     if currentWord == neighbor:
    #         text_count[currentWord] += 1
    #     else:
    #         text_count[neighbor] = 1

    # idea for defaultdict comes from:
    # https://www.humaneer.org/blog/how-to-plot-a-histogram-using-python-matplotlib/
    for word in sorted_text_list:
        text_count[word] += 1

    return dict(text_count)


def generate_histogram(text_count_dict):
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
    plt.xticks(rotation=45)

    # display the plot
    plt.show()


def word_counter(file):
    preprocessing = textPreprocessing(file)

    # checking to see preprocessing properly opened file
    # error occurred if textPreprocessing() returns a string
    if type(preprocessing) == type('str'):
        print(preprocessing)

    # preprocessing successful if a sorted list is returned
    else:
        count_dict = count_words(preprocessing)

        generate_histogram(count_dict)


if __name__ == '__main__':
    # result = textPreprocessing("test1.txt")
    #
    # print(result)
    #
    # count_results = count_words(result)
    #
    # print(count_results)
    #
    # generate_histogram(count_results)

    word_counter("testPDF2pages.pdf")
