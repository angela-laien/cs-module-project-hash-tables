def no_dups(s):
    # Your code here
    seq = {}
    filtered = []

    for word in s.split():
        if word not in seq:
            seq[word] = 1
            filtered.append(word)
    result = " ".join(filtered)
    return result

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))