from collections import defaultdict
from matplotlib import pyplot as plt


def textPreprocessing(file):
    fileText = ""
    textList = []
    finalTextList = []
    supported_formats = [".txt", ".pdf"]
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
    if file[-4:] not in supported_formats:
        return "format not supported"
    else:
        # proceed to opening file
        if file[-4:] == ".txt":
            with open(file, "r") as inFile:
                # read the entire text into a string
                fileText = inFile.read()

        # remove all punctuation
        for element in removeList:
            fileText.replace(element, "")

        # make lowercase
        fileText = fileText.lower()

        # split string into list
        # possible issue to solve in future is compound words separated with space
        textList = fileText.split()

        # remove all nltk words from text
        for word in textList:
            if word not in nltk:
                finalTextList.append(word)

        finalTextList.sort()

        return finalTextList


def count_words(sorted_text_list):

    # create dictionary with first entry
    text_count = defaultdict(int) #{sorted_text_list[0]: 1}

    # offset by one so that loop does not go out of bound
    # for index in range(len(sorted_text_list) - 1):
    #     currentWord = sorted_text_list[index]
    #     neighbor = sorted_text_list[index + 1]
    #     if currentWord == neighbor:
    #         text_count[currentWord] += 1
    #     else:
    #         text_count[neighbor] = 1

    # idea for defaultdict comes from https://www.humaneer.org/blog/how-to-plot-a-histogram-using-python-matplotlib/
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

    # display the plot
    plt.show()


def word_counter(file):
    preprocessing = textPreprocessing(file)

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

    word_counter("test1.txt")