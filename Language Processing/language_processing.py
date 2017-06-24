from collections import Counter
import os
import pandas as pd

text = "this is my test text"

def count_words(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch,"")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch,"")
    word_counts = Counter(text.split(" "))
    return word_counts

#print(count_words_fast(text))
#print(count_words(text))

def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

#print(count_words_fast(read_book("./books/English/shakespeare/Romeo and Juliet.txt")))

def word_stats(word_counts):
    """
    Return number of unique words and word frequencies
    """
    no_of_unique_words = len(word_counts)
    counts=word_counts.values()
    return(no_of_unique_words, counts)

#print(word_stats(count_words_fast(read_book("./books/English/shakespeare/Romeo and Juliet.txt"))))

book_dir = "./books"

# Pandas Data frame
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))

title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            input_file = book_dir + "/" + language + "/" + author + "/" + title
            #print(input_file)
            (num_unique_words, counts) = word_stats(count_words_fast(read_book(input_file)))
            #print("Number of unique words = " + str(num_unique_words))

            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique_words
            title_num += 1

print(stats.head())
