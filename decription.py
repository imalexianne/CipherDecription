letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '  

num_letters = len(letters) 

def decrypt(text, key):
    result = ''
    
    for letter in text:
        letter = letter.upper()
#        
        index = letters.find(letter)
            # an entered character is not found in letters
#         
        if index == -1:
            result += letter
        else:
         
             
            new_index = index - key        
            if new_index < 0:
                                   
                    # Example: c==>2 - 3 =-1 ==> 26 + (-1) ==>letters[25] ==>z
                new_index += num_letters
            result += letters[new_index]        
            #letters[-7]
    return result
        
print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('ENCRYPTION MODE ACTIVATED')
print()
key =int(input('Enter the key: '))
text = input('Enter the text to decrypt: ')
Plaintext = decrypt(text, key)
print(f'PLAINTEXT: {Plaintext}')