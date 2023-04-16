import numpy as np

def read_input():
    source= input()
    if source[0] == 'I':
        return (input().rstrip(), input().rstrip())
    elif source[0] == 'F':
        with open("tests/06", 'r') as f:
            return (f.readline().rstrip(), f.readline().rstrip())
    else:
        return

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    d = 10
    q = 968
    pattern_l = len(pattern)
    text_l = len(text)
    m = 0
    n = 0
    h = 1
    occurrences = []
    for i in range(pattern_l-1):
        h = (h * d) % q
    for i in range(pattern_l):
       m = (d*m + ord(pattern[i])) % q
       n = (d*n + ord(text[i])) % q
    for i in range(text_l - pattern_l + 1):
        if m == n and text[i:i+pattern_l] == pattern:
          occurrences.append(i)
        if i < text_l - pattern_l:
          n = (d*(n - ord(text[i])*h) + ord(text[i+pattern_l])) % q

        if n < 0:
            n += q
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

