string = "abcde"

reversed_string_list = list(reversed(string))
print(type(reversed(string)))
print(type(reversed_string_list))
print(reversed_string_list)

reversed_string = ''.join(reversed_string_list)
print(reversed_string)