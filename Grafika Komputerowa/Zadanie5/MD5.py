import hashlib

def md5checksum(fname):

    md5 = hashlib.md5()

    f = open(fname, "rb")

    while chunk := f.read(4096):
        md5.update(chunk)

    return md5.hexdigest()

def cezar(result):
    tablica = []
    for i in range(8):
        tablica.append(ord(result[i]))
        if(tablica[i] == 57):
            tablica[i] = 48
        elif(tablica[i] >= 48 and tablica[i]<= 56):
            tablica[i] += 1
        elif(tablica[i] >= 115 and tablica[i] <= 122):
            tablica[i] -= 18
        else:
            tablica[i] += 8
        tablica[i] = chr(tablica[i])
    tekst = ''.join(tablica)
    return tekst;

def main():

    result = md5checksum("C:\\Users\\Alicja\\Desktop\\Studia\\zdjecie.png") # tu wpisujemy sciezke dostepu 
    result2 = result[8:16]
    result3 = cezar(result2)
    print(result3)

if __name__ == '__main__':
    main()
