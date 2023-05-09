def split_tuple():
    word = input('>>> ')
    result = tuple(value for value in set(word) if word.count(value) < 2)
    print(result)
    
split_tuple()
