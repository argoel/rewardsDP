import numpy as np
import matplotlib.pyplot as plt

#calculates the value matrix
def valueF(f,k,d,g,l):
  r = k*d
  V = np.zeros((k+1,f+1))

  for i in range(k):
    V[i,f]=0

  V[k,f] = r + V[0,f] 

  for j in reversed(range(f)):
    for i in range(k):
      left = g*V[i+1,j+1]
      right = (1-l)*d + (1-l)*g*V[i,j+1] + l*g*V[i+1,j+1]
      V[i,j] = max(left,right)
    V[k,j] = r + V[0,j]

  return V

def indicatorF(f,k,d,g,l):
  V = valueF(f,k,d,g,l)
  I = np.zeros((k,f))
  for i in range(k):
    for j in range(f):
      if (V[i,j]==g*V[i+1,j+1]):
        I[i,j]=1
  return I

def revenueF(f,k,d,g,l):
  r = k*d
  V = valueF(f,k,d,g,l)
  I = indicatorF(f,k,d,g,l)
  rev = np.zeros((k+1,f+1))      
  for i in range(k+1):
    rev[i,f] = 0
  for j in reversed(range(f)):
    for i in range(k):
      left = l*(1+rev[i+1,j+1])
      right = (1-l)*(1+rev[i+1,j+1]) if I[i,j]==1 else (1-l)*(0+rev[i,j+1])
      rev[i,j] = left+right
    rev[k,j] = -r + rev[0,j]
  return rev


def findRforAllK(f,d,g,l):
  R = np.zeros(f+1)
  for k in range(f+1):
    R[k] = revenueF(f,k,d,g,l)[0,0]
  return R

def plotR(f,d,g,l):
  R = findRforAllK(f,d,g,l)
  K = range(f+1)
  plt.plot(K,R)
  plt.show() 

def main():
  f = 20
  k = 10
  d = 0.1
  g = 0.9
  l = 1.0/3

if __name__ == "__main__":
    main()
