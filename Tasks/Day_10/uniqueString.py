def is_unique(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

print(is_unique("abCDE"))
print(is_unique("nonunique"))