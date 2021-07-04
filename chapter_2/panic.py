phrase = "Don't panic"
split_phrase_on_letters = list(phrase)
print(phrase)
print(split_phrase_on_letters)
split_phrase_on_letters.remove("D")
split_phrase_on_letters.remove(" ")
split_phrase_on_letters.insert(3, " ")
split_phrase_on_letters.remove("'")
split_phrase_on_letters.insert(4, "a")
for i in range(4):
    split_phrase_on_letters.pop(-1)
new_phrase = ''.join(split_phrase_on_letters)
print(split_phrase_on_letters)
print(new_phrase)
