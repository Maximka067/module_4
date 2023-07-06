def naoborot(a):
    a = a.strip()
    return a[::-1 ] == a

if __name__ == "__main__":
    print(naoborot("ollo"))