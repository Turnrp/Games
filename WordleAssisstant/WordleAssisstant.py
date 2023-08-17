from os import system, name
from random import choice as c

def find_word_with_most_unique_letters(word_list):
    max_unique_letters = 0
    word_with_most_unique_letters = ""

    for word in word_list:
        unique_letters = set(word)
        num_unique_letters = len(unique_letters)

        if num_unique_letters > max_unique_letters:
            max_unique_letters = num_unique_letters
            word_with_most_unique_letters = word

    return word_with_most_unique_letters

def filter_words_by_length(word_list, length):
    filtered_words = [word for word in word_list if len(word) == length]
    return filtered_words

def filter_words_without_letter_at_index(word_list, letter, index):
    filtered_words = [word for word in word_list if len(word) <= index or word[index] != letter]
    return filtered_words

def filter_words_without_letter(word_list, letter):
    filtered_words = [word for word in word_list if not letter in word]
    return filtered_words

def filter_words_with_letter(word_list, letter):
    filtered_words = [word for word in word_list if letter in word]
    return filtered_words

def filter_words_by_index(word_list, character, index):
    words_with_character_at_index = [word for word in word_list if word[index] == character]
    return words_with_character_at_index

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
 
# Using words.txt get all the words
with open("words.txt", "r") as f:
    words = f.read().splitlines()

while 1:
    # Clear terminal and use the words to start filtering all words
    clear()
    allWords = words

    # Recommend a starting word base on best starter wordles
    bestWord = c(['later', 'alter', 'alert', 'irate', 'arose', 'stare', 'raise', 'arise', 'renal', 'learn', 'snare', 'saner', 'steal', 'slate', 'stale', 'least', 'trace', 'react', 'crate', 'cater'])
    print("The word you should start with is: " + bestWord)
    choice = input('To see all other words press "y" (WARNING IT MAY BE A LOT) or press "r" for a random one: ')
    if choice == "y":
        allWords.remove(bestWord)
        print("Try these words: ", allWords)
    elif choice == "r":
        allWords.remove(bestWord)
        while 1:
            randomWord = c(allWords)
            if input("Try this word: " + randomWord + "\nIf that worked press y: ") == "y":
                break
            else:
                allWords.remove(randomWord)

    while 1:
        # Get the last word inputted
        while 1:
            word = input("What is the last word inputted: ")
            if len(word) == 5 and word in words:
                if not word in allWords:
                    choice = input("Are you sure you wanna use " + word + " its eliminated already? y/n\n")
                    if choice == "y":
                        break
                    else:
                        continue
                break
        letters = {}
        green_positions = []

        # Get what words are grey, green, or yellow
        for i in range(5):
            while True:
                choice = input(f"For spot {i}, if it's grey: x, yellow: y, green: g\n").lower()
                if choice in ["x", "y", "g"]:
                    letters[i] = choice
                    if choice == "g":
                        green_positions.append(word[i])
                    break
        
        # Make duplicates yellow if one is grey and the other is green
        for index, letter_status in letters.items():
            letter = word[index]
            if letter_status == "x" and letter in green_positions:
                letters[index] = "y"
        
        # Filter all words out from all the information
        for index, letter_status in letters.items():
            letter = word[index]
            if letter_status == "x":
                allWords = filter_words_without_letter(allWords, letter)
            elif letter_status == "y":
                allWords = filter_words_without_letter_at_index(allWords, letter, index)
                allWords = filter_words_with_letter(allWords, letter)
            elif letter_status == "g":
                allWords = filter_words_by_index(allWords, letter, index)

        # Now with the information recommend a letter or get a random one after all th filtering
        print("The word you should use is: " + find_word_with_most_unique_letters(allWords))
        choice = input('To see all other words press "y" (WARNING IT MAY BE A LOT)\nor press "r" for a random one: ')
        if choice == "y":
            print("Try these words: ", allWords)
        elif choice == "r":
            while 1:
                if input("Try this word: " + c(allWords) + "\nIf that worked press y: ") == "y":
                    break
        
        # If there is one word left or the player cancels restart
        if len(allWords) == 1 or input("Cancel? y/n\n") == "y":
            break