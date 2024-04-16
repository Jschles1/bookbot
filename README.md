# Bookbot

Bookbot is a Python application designed to analyze text files, specifically books, to provide insights into the content. It reads a text file, counts the number of words, and calculates the frequency of each letter in the text.

## Features

Word Count: Bookbot counts the total number of words in the text file.
Letter Frequency: It calculates how many times each letter appears in the text.

## How to Use

1. Place your text file in the books directory. Note: The .gitignore file is configured to exclude this directory from version control.
2. Update the book_path variable in main.py to the path of your text file. For example:

```
book_path = "books/yourbook.txt"
```

3. Run the script:

```
python main.py
```

## Output

Bookbot will print the total word count and a list of letters with their corresponding frequencies in the text. The output ends with a "--- End report ---" line for clarity.

## Requirements

- Python 3.x