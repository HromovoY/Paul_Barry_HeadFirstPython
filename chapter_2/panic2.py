phrase = "Don't panic"
split_phrase_on_letters = list(phrase)
print(phrase)
print(split_phrase_on_letters)

new_pharse = ''.join(split_phrase_on_letters[1:3])
new_phrase = new_phrase + ''.join(split_phrase_on_letters[5], split_phrase_on_letters[4],
split_phrase_on_letters[-4], split_phrase_on_letters[-5])
print(new_phrase)
