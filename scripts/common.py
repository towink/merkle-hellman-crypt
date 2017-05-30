def split2len(s, n=16):
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))


def text_to_bytes(text, n=0):
    largo = len(text)
    if n > 0:
        text = text + ' ' * (n - (largo % n))
    text = text.decode('utf8')
    text_e = ''.join(['{0:016b}'.format(ord(c)) for c in text])
    return text_e

def bytes_to_text(binary):
    return ''.join([unichr(int(ch,2)) for ch in split2len(binary)])
