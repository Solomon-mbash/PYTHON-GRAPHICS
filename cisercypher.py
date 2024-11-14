alphabet = ["a","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z',"a","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z']
logo = ("""
  ______     ___       _______     _______.     ___      .______      
 /      |   /   \     |   ____|   /       |    /   \     |   _  \     
|  ,----'  /  ^  \    |  |__     |   (----`   /  ^  \    |  |_)  |    
|  |      /  /_\  \   |   __|     \   \      /  /_\  \   |      /     
|  `----./  _____  \  |  |____.----)   |    /  _____  \  |  |\  \----.
 \______/__/     \__\ |_______|_______/    /__/     \__\ | _| `._____|
                                                                      
  ______  __  .______    __    __   _______ .______                   
 /      ||  | |   _  \  |  |  |  | |   ____||   _  \                  
|  ,----'|  | |  |_)  | |  |__|  | |  |__   |  |_)  |                 
|  |     |  | |   ___/  |   __   | |   __|  |      /                  
|  `----.|  | |  |      |  |  |  | |  |____ |  |\  \----.             
 \______||__| | _|      |__|  |__| |_______|| _| `._____|             """)
print(logo)
direction = input("Type 'encode' to 'encrypt' and type 'decode' to 'decrypt'...\n")

text = input("Type your message? \n").lower()

shift = int(input("Type your shift no: \n"))


def encrypt(plain_txt,shift_amount):
    ciphert_txt = ""
    for letter in plain_txt:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_positon = position + shift_amount
            new_letter = alphabet[new_positon]
            ciphert_txt += new_letter
        else:
            ciphert_txt += letter
    print(ciphert_txt)
    return ciphert_txt



def decrypt(cipher_txt, shift_amount):
    decrypt_text = ""
    for letter in cipher_txt:
        if letter in alphabet:

            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            decrypt_text += new_letter
        else:
            decrypt_text += letter
    print(decrypt_text)

    return decrypt_text


if direction == "encode":
    encrypt(plain_txt=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_txt=text, shift_amount=shift)

else:
    print("OOOOh my Gosh!!!!!!!!!!!!!!!!")
