def get_max_legth(words: tuple) -> str:
    max_length = words[0]

    for i in words:
        if len(i) > len(max_length):
            max_length = i
    
    return max_length

words = ("apple", "banana", "strawberry", "kiwi")
print(get_max_legth(words=words))