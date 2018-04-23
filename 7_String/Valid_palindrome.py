# coding=<unicode>

word = "13 list\\u0026\\u0026 t sil)) 3%% 1"

word_new = ''.join(ch if ch.isalnum() else '' for ch in word)
letter = list(word_new)
result = True

print(letter)

for i in range(len(letter)//2):
  if letter[i] != letter[(len(letter)-1-i)]:
    result = False

print(result)