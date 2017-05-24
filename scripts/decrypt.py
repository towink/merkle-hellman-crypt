import json
import sys

def split2len(s, n=16):
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))


def text_to_bytes(text, n=0):
    '''

    '''
    largo = len(text)
    if n > 0:
        text = text + ' ' * (n - (largo % n))
    text = text.decode('utf8')
    text_e = ''.join(['{0:016b}'.format(ord(c)) for c in text])
    return text_e

def bytes_to_text(binary):
    return ''.join([unichr(int(ch,2)) for ch in split2len(binary)])


def unpack(n,l):
    i = len(l) -1
    for i in range(len(l)-1,-1,-1):
        if n>0:
            if l[i] <= n:
                n -= l[i]
                res = 1
            else:
                res = 0
            i-=1
        else:
            res = 0
        yield res

def decodificar(chunk, mochila_o, q, i_r):
    message = (chunk * i_r) % q
    int_message = list(unpack(message,mochila_o))[::-1]
    return bytes_to_text(''.join(map(str,int_message)))

if __name__ == "__main__":

    assert len(sys.argv) == 3

    clave = sys.argv[1]
    mensaje_crp = sys.argv[2]

    with open(clave, 'r') as f:
        dict_ = json.load(f)
        q = int(dict_['q'])
        mochila = list(dict_['Mochila'])
        ri = int(dict_['ri'])

    with open(mensaje_crp, 'r') as g:
        codificado = list(json.load(g)['Encrypted'])

    s = ''
    for c in codificado:
        s += decodificar(c,mochila, q, ri)
    # print s

    with open('mensae_descencriptado.txt', 'wb') as f:
        f.write(s)