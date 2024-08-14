def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for row in other_words:
        rowl = row.lower()
        if root_word in rowl:
            same_words.append(row)
        elif rowl in root_word:
            same_words.append(row)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
