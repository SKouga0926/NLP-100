def reverse_string(string):
    size_of_string = len(string)
    reversed_string = ""    

    for i in range(size_of_string):
        reversed_string = reversed_string + string[size_of_string - 1 - i]

    return reversed_string

string = "stressed"
reversed_string = reverse_string(string)
print(reversed_string)