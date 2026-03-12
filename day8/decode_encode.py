en_de = input("Type 'encode' to encode a message, type 'decode' to decode a message: ")
mess = str(input("Type your message"))
shift = int(input("Type the shift number"))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(mess, shift):
    encoded_mess = ""
    for i in mess:
        if i in alphabet:
            i = alphabet[(alphabet.index(i) + shift) % 26]
            encoded_mess += i
        else:
            encoded_mess += i
    print(encoded_mess)

def decode(mess, shift):
    decoded_mess = ""
    for i in mess:
        if i in alphabet:
            i = alphabet[(alphabet.index(i) - shift) % 26]
            decoded_mess += i
        else:
            decoded_mess += i
    print(decoded_mess)

if en_de == "encode":
    encode(mess, shift)
elif en_de == "decode":
    decode(mess, shift)
else:
    print("Invalid input")