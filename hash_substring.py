def read_input():
    
    text = input()
    if 2 in text:
        with open("./tests/06") as f:
            patt = f.readline()
            text = f.readline()
    elif 1 in text:
        patt = input()
        text = input()
    return (patt.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm
    pnlg = len(pattern)
    txlg = len(text)
    hasht=0
    hashp=0
    chs = 56
    q = 11
    bup=1
    rez = []
    for i in range(pnlg-1):
        bup = (bup*chs)%q
    for i in range(pnlg):
        hashp=(hashp*chs+ord(pattern[i]))%q
        hasht=(hasht*chs+ord(text[i]))%q
    for i in range(txlg-pnlg+1):
        if hashp == hasht:
            for j in range(pnlg):
                if text[i+j] != pattern[j]:
                    break
            else:
                rez.append(i)
        if i < txlg-pnlg:
            hasht = (chs *(hasht - ord (text[i])*bup)+ord (text[pnlg+i])) % q
            if hasht < 0:
                hasht = hasht+q
    # and return an iterable variable
    return rez

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


