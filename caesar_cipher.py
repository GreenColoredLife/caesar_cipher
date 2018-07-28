filename = 'message.txt'


def crypt(key, msg, mode):
    msg = msg.upper().strip()
    words = msg.split()
    msg = ""
    for word in words:
        new_word = ""
        for letter in word:
            if letter == "." or letter == ",":
                continue
            if mode == "d":
                letter = chr((((ord(letter)-65) - key) % 26) + 65)
            if mode == "e":
                letter = chr((((ord(letter)-65) + key) % 26) + 65)
            new_word += letter
        word = new_word
        msg += word + " "
    return msg


key = int(input("Insert key: "))
mode = input("Decrypt(d) or Encrypt(e)?: ")
try:
    with open(filename) as f:
        msg = f.read()
except FileNotFoundError:
    print("Please create a new file called 'message.txt' with your message")
else:
    new_msg = crypt(key, msg, mode)
    new_file = ""
    if mode == 'd':
        new_file = "decrypted_message.txt"
    if mode == 'e':
        new_file = "encrypted_message.txt"
    with open(new_file, 'w') as f:
        f.write(new_msg)
