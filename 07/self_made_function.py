def generate_sentence(x, y, z):
    sentence = str(x) + "時の" + str(y) + "は" + str(z)
    return sentence

sentence = generate_sentence(12, "気温", 22.4)
print(sentence)