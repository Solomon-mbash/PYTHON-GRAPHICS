# alphabet list containing all lowercase English letters (duplicates removed)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# ASCII art logo for the Caesar Cipher program
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
 \______||__| | _|      |__|  |__| |_______|| _| `._____|            
""")

# print the logo
print(logo)

# get the direction of the cipher from the user
direction = input("Type 'encode' to 'encrypt' and type 'decode' to 'decrypt'...\n")

# get the text to be encrypted or decrypted from the user
text = input("Type your message? \n").lower()

# get the shift amount from the user
shift = int(input("Type your shift no: \n"))

# function to encrypt the text
def encrypt(plain_txt, shift_amount):
    # initialize an empty string to store the encrypted text
    ciphert_txt = ""
    
    # iterate over each character in the text
    for letter in plain_txt:
        # check if the character is in the alphabet
        if letter in alphabet:
            # get the position of the character in the alphabet
            position = alphabet.index(letter)
            
            # calculate the new position of the character after shifting
            new_position = (position + shift_amount) % 26
            
            # get the character at the new position
            new_letter = alphabet[new_position]
            
            # add the new character to the encrypted text
            ciphert_txt += new_letter
        else:
            # if the character is not in the alphabet, add it to the encrypted text as is
            ciphert_txt += letter
    
    # print the encrypted text
    print(ciphert_txt)
    
    # return the encrypted text
    return ciphert_txt

# function to decrypt the text
def decrypt(cipher_txt, shift_amount):
    # initialize an empty string to store the decrypted text
    decrypt_text = ""
    
    # iterate over each character in the text
    for letter in cipher_txt:
        # check if the character is in the alphabet
        if letter in alphabet:
            # get the position of the character in the alphabet
            position = alphabet.index(letter)
            
            # calculate the new position of the character after shifting
            new_position = (position - shift_amount) % 26
            
            # get the character at the new position
            new_letter = alphabet[new_position]
            
            # add the new character to the decrypted text
            decrypt_text += new_letter
        else:
            # if the character is not in the alphabet, add it to the decrypted text as is
            decrypt_text += letter
    
    # print the decrypted text
    print(decrypt_text)
    
    # return the decrypted text
    return decrypt_text

# check the direction of the cipher
if direction == "encode":
    # if the direction is 'encode', call the encrypt function
    encrypt(plain_txt=text, shift_amount=shift)
elif direction == "decode":
    # if the direction is 'decode', call the decrypt function
    decrypt(cipher_txt=text, shift_amount=shift)
else:
    # if the direction is neither 'encode' nor 'decode', print an error message
    print("OOOOh my Gosh!!!!!!!!!!!!!!!!")