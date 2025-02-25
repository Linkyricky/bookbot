import sys
from stats import count_words
from stats import count_chars
from stats import sort_chars
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    count_words(file_contents)
    wordcount = count_words(file_contents)
    count_chars(file_contents)
    charscount = count_chars(file_contents)
    #print(f"{wordcount} words found in the document")
    #print (charscount)
    print(sort_chars(charscount))
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print ("---------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print ("---------- Character Count ----------")
    for char in sort_chars(charscount): 
        for key, value in char.items():
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============")

main()