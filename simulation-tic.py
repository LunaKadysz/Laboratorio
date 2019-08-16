
from sympy import Rational , Wild
from sympy.abc import x

a = Rational(1,9)
print(a)


p = Wild("p")
q = Wild("q")
r = Wild("r")
e = (2*x)**2
e.match(p*q**r)
en = (p*q**r).xreplace(e.match(p*q**r))
print(en)
