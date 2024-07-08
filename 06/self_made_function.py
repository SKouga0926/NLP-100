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

        if (string[right_ptr] == " " or string[right_ptr] == "," or string[right_ptr] == "."):

            for j in range(left_ptr, right_ptr):
                word = word + string[j]

            word_list.append(word)
            word_size_list_of_word_list.append(len(word))
            word = ""

            while True:
                if (string[right_ptr] == " " or string[right_ptr] == "," or string[right_ptr] == "."):
                    right_ptr += 1
                    if (right_ptr >= size_of_string):
                        break
                else : 
                    left_ptr = right_ptr
                    break

        if (right_ptr == size_of_string - 1):
            for j in range(left_ptr, right_ptr + 1):
                word = word + string[j]

            word_list.append(word)
            word_size_list_of_word_list.append(len(word))
            word = ""
            break


        else :
            right_ptr += 1

    return word_list

def n_gram_word(n, string):

    word_list = split_into_words(string)
    size_word_list = len(word_list)

    temp_list1 = []
    temp_list2 = []

    start_index = 0

    while True:

        for i in range(start_index, start_index + n):
            if (start_index + n - 1 == size_word_list):
                break

            temp_list1.append(word_list[i])

        if (start_index + n - 1 == size_word_list):
            break 

        temp_list2.append(temp_list1)
        temp_list1 = []

        start_index = start_index + 1

    n_gram_word_list = temp_list2

    return n_gram_word_list

def n_gram_char(n, string):

    size_string = len(string)

    temp_char1 = ""
    temp_list1 = []

    start_index = 0

    while True:

        for i in range(start_index, start_index + n):
            if (start_index + n - 1 == size_string):
                break

            temp_char1 += string[i]

        if (start_index + n - 1 == size_string):
            break 

        temp_list1.append(temp_char1)
        temp_char1 = ""

        start_index = start_index + 1

    n_gram_char_list = temp_list1

    return n_gram_char_list

string1 = "paraparaparadise"
string2 = "paragraph"

X = frozenset(n_gram_char(2, string1))
Y = frozenset(n_gram_char(2, string2))

union_set = X | Y
difference_set = X - Y
intersection_set = X & Y

print("union =", union_set)
print("difference = ", difference_set)
print("intersection = ", intersection_set)