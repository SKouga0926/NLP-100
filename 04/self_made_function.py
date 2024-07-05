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

            
        else :
            right_ptr += 1

    return word_list

string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = split_into_words(string)

size_word_list = len(word_list)
key = []

for i in range(size_word_list):

    if (i == 0):
        key.append(word_list[i][0]) 

    elif (i == 4):
        key.append(word_list[i][0]) 
    
    elif (i == 5):
        key.append(word_list[i][0]) 

    elif (i == 6):
        key.append(word_list[i][0]) 

    elif (i == 7):
        key.append(word_list[i][0]) 
    
    elif (i == 8):
        key.append(word_list[i][0]) 

    elif (i == 14):
        key.append(word_list[i][0]) 

    elif (i == 15):
        key.append(word_list[i][0]) 
    
    elif (i == 18):
        key.append(word_list[i][0]) 

    else :
        key.append(word_list[i][0:2])


dict = {}
for i in range(len(key)):
    dict[key[i]] = i

print(dict)

