def split_into_words(string):

    size_of_string = len(string)

    word_list = []
    word = ""

    left_ptr = 0
    right_ptr = 0

    word_size_list_of_word_list = []

    for i in range(size_of_string):

        if (right_ptr >= size_of_string):
            break

        if (string[right_ptr] == " " or string[right_ptr] == ","):

            for j in range(left_ptr, right_ptr):
                word = word + string[j]

            word_list.append(word)
            word_size_list_of_word_list.append(len(word))
            word = ""

            while True:
                if (string[right_ptr] == " " or string[right_ptr] == ","):
                    right_ptr += 1
                else : 
                    left_ptr = right_ptr
                    break

            
        else :
            right_ptr += 1

    return word_list

def get_words_lengths(word_list):

    length_word_list = len(word_list)
    length_word = []

    for i in range(length_word_list):
        length_word.append(len(word_list[i]))

    return length_word
  


string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word_list = split_into_words(string)

length_word = get_words_lengths(word_list)

print(word_list)
print(length_word)