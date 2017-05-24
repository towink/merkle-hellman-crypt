from __future__ import division

import itertools
import json
import sys
from random import randint, seed


def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

def gcd(a, b):
    return xgcd(a, b)[0]

def inverse_mod(r, q):
    assert gcd(r, q) == 1
    res = xgcd(r, q)[1]
    if res < 0:
        res += q
    assert res > 0 and res < q
    return res

def new_mochila(N=10, jump=10):
    diff = [randint(1, jump) for k in range(N)]
    mochila = [diff[0]]
    for i in range(1, len(diff)):
        new_val = sum(mochila) + diff[i]
        mochila.append(new_val)
    return mochila


def select_q(mochila):
    suma = sum(mochila)
    return randint(suma + 1, suma * 10)


def select_r(q):
    try_r = randint(2, q - 1)
    while gcd(try_r, q) != 1:
        try_r = randint(2, q - 1)
    return try_r, inverse_mod(try_r, q)


def mochila_camuflada(mochila, q, r):
    return [(r * x) % q for x in mochila]


if __name__ == "__main__":

    assert len(sys.argv) == 3

    N = int(sys.argv[1])
    jump = int(sys.argv[2])
    mochila = new_mochila(N, jump)
    q = select_q(mochila)
    r, ri = select_r(q)
    mochila_pub = mochila_camuflada(mochila, q, r)

    clave_publica = {'Mochila': mochila_pub}
    clave_privada = {'Mochila' : mochila, 'q': q, 'ri': ri}
    with open('clave.pub', 'wb') as f:
        json.dump(clave_publica, f)

    with open('clave.priv', 'wb') as g:
        json.dump(clave_privada, g)
