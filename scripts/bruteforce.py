import json
import sys
from common import split2len, text_to_bytes, bytes_to_text

def knapsack_brute_force(knapsack, x, solution):
    
    if x == 0:
        return [True, solution]
    
    if len(knapsack) == 0:
        if x == 0:
            return [True, solution]
        else:
            print 'c'
            return [False, []]
    
    if len(knapsack) == 1:
        if knapsack[0] == x:
            solution.append(x)
            return [True, solution]
        else:
            return [False, []]
    
    
    curr_elem = knapsack[0]
    
    if curr_elem > x:
        return knapsack_brute_force(knapsack[1:], x, solution)
    
    else:
        # try with taking the first element
        result = knapsack_brute_force(knapsack[1:], x - curr_elem, solution)
        if result[0]:
            solution.append(curr_elem)
            return [True, solution]
        else:
            # try with not taking the first element
            return knapsack_brute_force(knapsack[1:], x, solution)
        
def knapsack_brute_force_bits(knapsack, x):
    sol = knapsack_brute_force(knapsack, x, [])[1]
    res = []
    # dont ask my why in reversed order :D
    for elem in reversed(knapsack):
        if elem in sol:
            res.append(1)
        else:
            res.append(0)
    return res

def decodificar_brute_force(chunks, mochi_c):
    bits = []
    for chunk in chunks:
        bits += list(knapsack_brute_force_bits(mochi_c, chunk))[::-1]
    return bytes_to_text(''.join(map(str, bits)))

if __name__ == "__main__":

    assert len(sys.argv) == 3

    clave = sys.argv[1]
    mensaje_crp = sys.argv[2]

    with open(clave, 'r') as f:
        mochila = list(json.load(f)['Mochila'])

    with open(mensaje_crp, 'r') as g:
        codificado = list(json.load(g)['Encrypted'])

    s = decodificar_brute_force(codificado, mochila)

    with open(mensaje_crp + 'dcrp_brute', 'wb') as f:
        f.write(s)