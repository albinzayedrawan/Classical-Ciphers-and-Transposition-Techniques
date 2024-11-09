# Function to perform Caesar Cipher encryption/decryption
def caesar_cipher(text, shift):
    result = ''  # Initialize an empty string to store the result
    # Iterate through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Convert character to lowercase, apply the shift, and wrap around using modulo 26
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            result += shifted_char  # Append the shifted character to the result
        else:
            result += char  # If not a letter, keep the character as it is
    return result

# Get input from the user for the text to encrypt
plaintext = input('Enter the text to encrypt: ')
# Get the shift key from the user (must be between 0 and 25)
shift_key = int(input('Enter the shift key (a number between 0 and 25): '))

# Encrypt the plaintext using the caesar_cipher function
encrypted_text = caesar_cipher(plaintext, shift_key)
print('Encrypted text:', encrypted_text)

# Get input from the user for the text to decrypt
ciphertext = input('Enter the text to decrypt: ')
# Get the shift key from the user for decryption (must be between 0 and 25)
dec_shift_key = int(input('Enter the shift key (a number between 0 and 25): '))

# Decrypt the ciphertext using the negative of the shift key
decrypted_text = caesar_cipher(ciphertext, -dec_shift_key)
print('Decrypted text:', decrypted_text)