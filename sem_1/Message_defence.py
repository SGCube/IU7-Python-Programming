spliters = '., :;/\\-+="!?()[]{}|&^~`'
spliters += "'"

s = input('Введите строку: ')
words = []
word = ''

for x in s:
    if spliters.find(x) >= 0:
        if word != '':
            word = word.lower()
            found = False
            for y in words:
                if y == word:
                    found = True
            if not found:
                words.append(word)
                word = ''
    else:
        word += x

if word != '':
    word = word.lower()
    found = False
    for y in words:
        if y == word:
            found = True
    if not found:
        words.append(word)

for i in range(len(words)):
    for j in range(len(words)):
        if len(words[i]) > len(words[j]):
            words[i], words[j] = words[j], words[i]

print('\nСлова строки в порядке убывания длины строки:')
for x in words:
    print(x)
