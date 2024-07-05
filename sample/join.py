def combined_char(origin, name):
    origin_combined = name.join(origin)
    return origin_combined

v = ["Hello", "Python"]
v_combined = "".join(v)
print(v_combined)

v = ["Hello", "Python", "Kouga"]
v_combined = "->".join(v)
print(v_combined)

print(combined_char(v, "---"))