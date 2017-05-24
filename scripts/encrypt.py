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


def codificar(mochila_camuflada, text):
    largo_mochila = len(mochila_camuflada)
    assert largo_mochila % 16 == 0

    texto_codificado = text_to_bytes(text, largo_mochila // 16)
    a_codifcar = split2len(texto_codificado, largo_mochila)
    return [sum([b for (a, b) in zip(k, mochila_camuflada) if a == '1']) for k in a_codifcar]

if __name__ == "__main__":

    assert len(sys.argv) == 3

    clave = sys.argv[1]
    mensaje = sys.argv[2]

    with open(clave, 'r') as f:
        mochila = list(json.load(f)['Mochila'])
    
    # print mochila
    with open(mensaje, 'r') as g:
        texto = g.read()

    mensaje_encriptado = codificar(mochila, texto)
    # print mensaje_encriptado
    # print len(mensaje_encriptado)
    # print '\n\n'
    res = {'Encrypted': mensaje_encriptado}
    mensaje_encriptado_b = ''.join([bin(x)[2:] for x in mensaje_encriptado])
    print mensaje_encriptado_b
    with open(mensaje +'.crp', 'wb') as g:
        json.dump(res,g)