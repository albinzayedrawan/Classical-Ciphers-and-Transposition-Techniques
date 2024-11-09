# Vigenere Cipher Encryption Function
def vigenere_encrypt(plaintext, keyword):
    # Convert the keyword and plaintext to lowercase
    keyword = keyword.lower()
    plaintext = plaintext.lower()
    result = ""

    # Loop through each character in the plaintext
    for i in range(len(plaintext)):
        char = plaintext[i]

        # Calculate the shift value based on the keyword
        shift = ord(keyword[i % len(keyword)]) - ord('a')

        if char.isalpha():
            # Shift the character and wrap around using modulo 26
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted_char
        else:
            # If character is not a letter, add it unchanged
            result += char

    return result

# Vigenere Cipher Decryption Function
def vigenere_decrypt(ciphertext, keyword):
    # Convert the keyword and ciphertext to lowercase
    keyword = keyword.lower()
    ciphertext = ciphertext.lower()
    result = ""

    # Loop through each character in the ciphertext
    for i in range(len(ciphertext)):
        char = ciphertext[i]

        # Calculate the shift value based on the keyword
        shift = ord(keyword[i % len(keyword)]) - ord('a')

        if char.isalpha():
            # Reverse the shift to decrypt and wrap around using modulo 26
            shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result += shifted_char
        else:
            # If character is not a letter, add it unchanged
            result += char

    return result

# Main Program Execution
if __name__ == "__main__":
    # Print program introduction
    print("Vigenere Cipher Program")

    # Get the plaintext and keyword from the user
    plaintext = input("Enter the plaintext: ").lower()
    keyword = input("Enter the keyword: ").lower()

    # Encrypt the plaintext using Vigenere Cipher
    encrypted_text = vigenere_encrypt(plaintext, keyword)
    print("Encrypted text:", encrypted_text)

    # Decrypt the encrypted text using Vigenere Cipher
    decrypted_text = vigenere_decrypt(encrypted_text, keyword)
    print("Decrypted text:", decrypted_text)