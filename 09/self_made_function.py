import random

def shuffle_word(word):
    first_char = word[0]
    last_char = word[-1]
    middle_char = list(word[1:-1])
    random.shuffle(middle_char)
    shuffled_word = ''.join([first_char] + middle_char + [last_char])
    return shuffled_word

string = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

word_list = string.replace(".", "").split(" ")

shuffle_word_list = []

for word in word_list:
    if len(word) <= 4:
        pass
    else:
        shuffled_words = shuffle_word(word)
        shuffle_word_list.append(shuffled_words)
        

shuffled_string = ' '.join(shuffle_word_list)
print("シャッフル後:", shuffled_string)