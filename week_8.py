# DSC 510
# Week 8
# Programming Assignment Week 8
# Author Allie Dunkel
# 2/3/2023

# Change#: 1 Change(s) Made: I Calculated the total words, and output the number of occurrences of each word in the
# gettysburg file.
# Date of Change: 2/3/2023

import string


def add_word(word, dictionary):
    # Add each word to the dictionary with a frequency of 1
    if word in dictionary.keys():
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1


def process_line(line, dictionary):
    # split the string into a list of words
    word_list = line.split()
    word_list = [ele for ele in word_list if ele != "--"]
    # for loop to remove punctuation
    for word in word_list:
        word = word.lower()
        word = word.strip(string.punctuation)
        add_word(word, dictionary)


def pretty_print(dictionary):
    # sorting my list
    sort_words = sorted(dictionary.items(), key=lambda i: i[1], reverse=True)
    length_dictionary = len(sort_words)
    print("Length of Dictionary: " + str(length_dictionary))
    print('Word\t \t Count')
    print('----------------------------')
    for key, value in sort_words:
        print(f'{key : <14} {value}')


def main():
    # creating the empty dictionary
    dictionary = {}
    # open the file
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, dictionary)
    pretty_print(dictionary)
    # print(dictionary)


if __name__ == '__main__':
    main()
