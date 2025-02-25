def count_words(text):
    wordlist = text.split()
    return len(wordlist)

def count_chars(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
        
def helper_function(dictionary):
    return list(dictionary.values())[0]

def sort_chars(count_chars):
    char_list = []
    for key, value in count_chars.items():
        char_list.append({key: value})
    char_list.sort(reverse=True, key=helper_function)
    return char_list
