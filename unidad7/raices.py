def raiz_cuadrada(a):
  return a**(1/2)

def raiz(a, n):
  return a**(1/n)

def cuadratica(a,b,c):
  r1 = ((-b+raiz_cuadrada(b**2-(4*a*c)))/(2*a))
  r2 = ((-b-raiz_cuadrada(b**2-(4*a*c)))/(2*a))
  return r1, r2