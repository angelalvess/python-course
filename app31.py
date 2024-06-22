phrase = 'one small step,         one giant leap for mankind'
list_words = phrase.split()
old_list_phrase = phrase.split(', ')

new_list_phrase = []
for i, frase in enumerate(old_list_phrase):
    new_list_phrase.append(old_list_phrase[i].strip())

print(new_list_phrase)
print(old_list_phrase)

phrases = '-'.join(new_list_phrase)

print(phrases)
