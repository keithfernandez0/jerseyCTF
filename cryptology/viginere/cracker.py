from collections import Counter
import string

def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]
    
    for c, k in zip(ciphertext, key):
        decrypted.append(chr(((ord(c) - ord(k)) % 26) + ord('a')))
    
    return "".join(decrypted)

def caesar_shift(text, shift):
    shifted_alphabet = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    table = str.maketrans(shifted_alphabet, string.ascii_lowercase)
    return text.translate(table)

def letter_frequencies(text):
    freqs = {char: text.count(char) for char in string.ascii_lowercase}
    return sorted(freqs.items(), key=lambda x: x[1], reverse=True)

def index_of_coincidence(text):
    N = len(text)
    freqs = Counter(text)
    return sum(f*(f-1) for f in freqs.values()) / (N * (N-1))

def guess_shift(text):
    # Guess Caesar shift based on frequency analysis (e.g., using 'e' as the most common letter)
    freq = letter_frequencies(text)
    most_common_char = freq[0][0]  # Most frequent letter
    shift = (ord(most_common_char) - ord('e')) % 26  # Assume 'e' is the most frequent letter
    return shift

def derive_key(ciphertext, key_length):
    # Split ciphertext into key_length number of substrings
    substrings = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        substrings[i % key_length] += char
    
    # Now guess the key using Caesar cipher frequency analysis for each substring
    key = ''
    for i, substring in enumerate(substrings):
        shift = guess_shift(substring)
        key += chr(shift + ord('a'))
    
    return key

# Read ciphertext
with open("encryptedText.txt", "r") as f:
    ciphertext = f.read().strip()

# Use derived key length (43 from previous analysis)
key_length = 43
key = derive_key(ciphertext, key_length)
print(f"Derived Key: {key}")

# Decrypt the ciphertext with the derived key
plaintext = vigenere_decrypt(ciphertext, key)
print("Decrypted Text:\n", plaintext)

# Calculate and print the IoC
print("IoC:", index_of_coincidence(ciphertext))
