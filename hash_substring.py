import numpy as np
    # Aleksandrs Kurjans 6.gr 221RDB420

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use 1 (input from keyboard) and 2 (input from file) to choose which input type will follow
    source = input()
    if source[0] == '1':
        return (input().rstrip(), input().rstrip())
    elif source[0] == '2':
        with open("tests/06", 'r') as f:
            return (f.readline().rstrip(), f.readline().rstrip())
    else:
        return None
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin-Karp algorithm 
    d = 10
    q = 997
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


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


