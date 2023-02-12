# DSC 510
# Week 9
# Programming Assignment Week 9
# Author Allie Dunkel
# 2/10/2023

# Change#: 1
# Change(s) Made: Made the output that appeared on the screen last week appear in a new file
# Date of Change: 2/10/2023


import string


def add_word(word, dictionary):
    # Add each word to the dictionary with a frequency of 1
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1


def process_line(line, dictionary):
    # split the string into a list of words
    line = line.strip()
    word_list = line.split()
    # for loop to remove punctuation
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip(string.punctuation)
            add_word(word, dictionary)


def process_file(dictionary, user_filename):
    with open(user_filename, 'a') as user_filename:
        user_filename.write(f"{'Word' : <13}{'Count' : >13}" + '\n')
        user_filename.write('-' * 26 + '\n')
        for key, val in sorted(dictionary.items(), key=lambda i: i[1], reverse=True):
            user_filename.write(f"{key : <13}{val : >13}" + '\n')


def main():
    # creating the empty dictionary
    dictionary = {}
    with open('gettysburg.txt', 'r') as f:
        for line in f:
            process_line(line, dictionary)

    user_filename = input('Enter the file name: ')
    with open(user_filename, 'w') as wf:
        wf.write('Length of dictionary: ' + str(len(dictionary)) + '\n')
    process_file(dictionary, user_filename)


if __name__ == '__main__':
    main()
