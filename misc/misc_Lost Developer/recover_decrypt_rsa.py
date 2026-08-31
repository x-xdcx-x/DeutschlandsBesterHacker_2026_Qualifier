from sympy import factorint, totient

n = 0x009ec9fe56d1616909213bfb6373298eef
e = 65537
c = 0x2655eacc028dfa8924e8223e39fad4b3

# totient = phi-function 
phi = int(totient(n))
d = pow(e, -1, phi)

m = pow(c, d, n)
plaintext = m.to_bytes(16, "big").decode()

print("Plaintext:", plaintext)
