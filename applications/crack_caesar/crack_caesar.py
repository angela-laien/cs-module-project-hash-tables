# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
ciphertext = open('applications/crack_caesar/ciphertext.txt').read()
letters = 'ETAOHNRISDLWUGFBMYCPKVQJXZ'

def calculate_freq(txt):
    txt = txt.upper()
    freq = {}

    for l in letters:
        freq[l] = 0
    for l in txt:
        if l in letters:
            freq[l] += 1
    return freq

frequency = calculate_freq(ciphertext)
freq_list = ''.join(sorted(frequency, key=lambda f: frequency[f], reverse=True))
print(freq_list)

def decode(txt):
    plaintext = ''
    for t in txt:
        i = freq_list.find(t)
        if letters[i] == 'Z':
            plaintext += ' '
        else:
            plaintext += letters[i]
    return plaintext

print(decode(ciphertext))