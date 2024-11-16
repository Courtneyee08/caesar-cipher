# add your code here
alphabet = " abcdefghijklmnopqrstuvwxyz"

sentence = str(input("Enter the sentence you wish to decipher: "))
sentence = sentence.lower()
shift = 5
secret_sent = ""
 
for char in sentence:
  if char == " ":
    secret_sent += " " 
  elif char in alphabet:
    index = alphabet.find(char)
    index = (index + shift) % 26
    char = alphabet[index]
    secret_sent += char

print(secret_sent)