import re
calculated = {}

def word_count(s):
    # Your code here
    global calculated
    filtered_s = re.sub(r"[^\w\d'\s]", '', s)
    lowered = filtered_s.lower()
    for word in lowered.split():
        if word not in calculated.keys():
            calculated[word] = 1
        else:
            calculated[word] += 1
    s = calculated
    calculated = {}
    return s


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))