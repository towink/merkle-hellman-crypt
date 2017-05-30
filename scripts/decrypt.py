import json
import sys
from common import split2len, text_to_bytes, bytes_to_text

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

def decodificar(chunks, mochila_o, q, i_r):
    bits = []
    for chunk in chunks:
        message = (chunk * i_r) % q
        bits += list(unpack(message, mochila_o))[::-1]
    return bytes_to_text(''.join(map(str, bits)))

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

    s = decodificar(codificado, mochila, q, ri)

    with open(mensaje_crp + '.dcrp', 'wb') as f:
        f.write(s)