# Шифр Виженера код

def index_k(letters, word, key):   # Находит индексты в letterts, под которыми находятся буквы из key
    index_key = []
    for i in range(len(word) - len(key)):
        key += key[i]

    for j in range(len(word)):
        for k in range(len(letters)):
            if key[j] in letters[k]:
                index_key.append(k)
    return index_key
   
word = list(input("Исходный текст:"))
key = list(input("Ключ:"))
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
index_key = index_k(letters, word, key)
cipher = []

for i in range(len(word)):
    new_letters = []
    new_letters = letters[index_key[i] : len(letters) + 1] + letters[0 : index_key[i]]   # Сдвиг в letters равен числу из index_key 
    c_ind = letters.index(word[i])   # получаем индекс в letters, под которым находится буква из word
    cipher.append(new_letters[c_ind])
print(*cipher, sep="")
