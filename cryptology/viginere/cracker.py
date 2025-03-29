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

with open("encryptedText.txt", "r") as f:
    ciphertext = f.read().strip()

for shift in range(26):
    print(f"Shift {shift}:\n", caesar_shift(ciphertext[:500], shift))

def index_of_coincidence(text):
    N = len(text)
    freqs = Counter(text)
    return sum(f*(f-1) for f in freqs.values()) / (N * (N-1))

key = "yourderivedkey"
plaintext = vigenere_decrypt(ciphertext, key)
print(plaintext)

with open("encryptedText.txt", "r") as f:
    ciphertext = f.read().strip()

print("IoC:", index_of_coincidence(ciphertext))
