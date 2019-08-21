from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    identical = set()
    for line_a in a.splitlines():
        #print(line_a)
        for line_b in b.splitlines():
            if line_a == line_b:
                identical.add(line_a.strip())
                break
    return list(identical)


def sentences(a, b):
    """Return sentences in both a and b"""
    identical = set()
    for sen_a in sent_tokenize(a):
        for sen_b in sent_tokenize(b):
            if sen_a == sen_b:
                identical.add(sen_a.strip())
                break
    return list(identical)

def sub(a, n):
    strings = []
    for x in range(0, len(a)-n + 1):
        strings.append(a[x:x+n])
    return strings

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    identical = set()
    for sub_a in sub(a, n):
        for sub_b in sub(b, n):
            if sub_a == sub_b:
                identical.add(sub_a)
    return list(identical)

