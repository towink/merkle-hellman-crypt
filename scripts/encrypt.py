import json
import sys
from common import split2len, text_to_bytes, bytes_to_text

def codificar(mochila_camuflada, text):
    largo_mochila = len(mochila_camuflada)

    texto_codificado = text_to_bytes(text, largo_mochila)
    a_codifcar = split2len(texto_codificado, largo_mochila)
    return [sum([b for (a, b) in zip(k, mochila_camuflada) if a == '1']) for k in a_codifcar]

if __name__ == "__main__":

    assert len(sys.argv) == 3

    clave = sys.argv[1]
    mensaje = sys.argv[2]

    with open(clave, 'r') as f:
        mochila = list(json.load(f)['Mochila'])

    with open(mensaje, 'r') as g:
        texto = g.read()

    mensaje_encriptado = codificar(mochila, texto)
    res = {'Encrypted': mensaje_encriptado}
    mensaje_encriptado_b = ''.join([bin(x)[2:] for x in mensaje_encriptado])
    with open(mensaje +'.crp', 'wb') as g:
        json.dump(res,g)