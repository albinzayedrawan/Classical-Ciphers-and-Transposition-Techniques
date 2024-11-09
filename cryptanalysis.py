# Function to decrypt a Caesar Cipher given a shift value
def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""

    # Iterate over each character in the ciphertext
    for char in ciphertext:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Shift the character by the given shift value, wrapping around the alphabet
            # Convert the character to uppercase for consistent handling
            shifted_char = chr(((ord(char.upper()) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += shifted_char
        else:
            # If the character is not an alphabet letter, add it unchanged
            decrypted_text += char

    return decrypted_text

# The given ciphertext to decrypt
ciphertext = "WKLV LV D WHVW"

# Print all possible decryptions using a brute-force approach
print("Brute-force decryption of Caesar Cipher:\n")
for key in range(1, 26):
    # Decrypt the ciphertext with the current key
    decrypted_text = caesar_cipher_decrypt(ciphertext, key)

    # Print the result for the current key
    print(f"Key {key}: {decrypted_text}")