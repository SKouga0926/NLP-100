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

def bi_gram_word(string):

    word_list = split_into_words(string)
    
    size_word_list = len(word_list)
    bi_gram_list = []

    for i in range(size_word_list - 1):

        bi_gram_list.append([word_list[i], word_list[i + 1]])
        
    return bi_gram_list

def bi_gram_char(string):

    size_string = len(string)
    bi_gram_list = []

    for i in range(size_string - 1):
        bi_gram_list.append([string[i], string[i + 1]])

    return bi_gram_list

string = "I am an NLPer"
word_list = split_into_words(string)
print(word_list)

bi_gram_list = bi_gram_word(string)
print(bi_gram_list)

bi_gram_list = bi_gram_char(string)
print(bi_gram_list)