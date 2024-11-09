# Classical Ciphers and Transposition Techniques

## Caesar Cipher:
- The program should allow the user to input the plaintext and the shift key.
- It should encrypt the plaintext using the shift key and output the ciphertext.
- The program should also be able to reverse the process (decrypt) using the ciphertext and the same shift key.

## Cryptanalysis:
- Ciphertext: WKLV LV D WHVW.
- Python script will attempt to decrypt the message by trying all possible keys (brute force attack).
- Ciphertext will be shifted through all 25 possible shift values (since there are 26 letters in the alphabet).
- It will output each possible decrypted message and the user can identify the correct plaintext based on legibility.

## Vigenère Cipher:
- The program should allow the user to input the plaintext and a keyword.
- It should encrypt the plaintext using the repeating sequence of the keyword and output the ciphertext.
- The program should also allow decryption using the same keyword.
