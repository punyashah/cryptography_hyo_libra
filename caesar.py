alphabet = 'abcdefghijklmnopqrstuvwxyz'


for counter in range(len(alphabet)):
    decrypt = ""
    for letter in word:
        index = alphabet.find(letter)
        index = (index - counter) %len(alphabet)
        decrypt += alphabet[index]

    print(decrypt)
