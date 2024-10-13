def all_variants(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]


a = all_variants("abc")
for i in a:
    print(i)
