def count_word(string, word):
    words = string.split()  # Split the input string into a list of individual words based on spaces
    return words.count(word)  # Return the number of occurrences of 'word' in the list

# Example usage:
sentence = "This is an example sentence that contains multiple instances of some repeating words"
target_word = "example"
occurrences = count_word(sentence, target_word)
print("The word", target_word, "appears", occurrences, "time in the string.")