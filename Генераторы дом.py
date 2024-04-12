def all_variants(text):
    for count in range(1, len(text) + 1):
        for i in range(len(text) + 1 - count):
            print(count, i, i + count)
            yield (text[i: i + count])


for substr in all_variants('abc'):
    print(substr)
