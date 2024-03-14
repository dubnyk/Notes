import gmpy2

e =
p =
q = 
n = p * q

c = []

phi = (p - 1) * (q - 1)

d = gmpy2.invert(e, phi)
print(d)

for i in c:
  m = pow(i, d, n)
  print(char(m))

print("")
