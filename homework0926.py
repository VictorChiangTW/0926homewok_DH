import time


p = int('009fdb8b8a004544f0045f1737d0ba2e0b274cdf1a9f588218fb435316a16e374171fd19d8d8f37c39bf863fd60e3e300680a3030c6e4c3757d08f70e6aa871033', 16)
g = 2

a = input("enter a in hexadecimal: ")
a = int(a, 16)

b = input("enter b in hexadecimal: ") 
b = int(b, 16)


def KandKT(g , k, p):
  start_time = time.time()
  K = pow(g, k, p)
  end_time = time.time()
  TK = str(float(end_time -  start_time) * 1000.0) + 'ms'
  return(K, TK)


A, TA = KandKT(g, a, p)
print('A: ', A)


B, TB = KandKT(g, b, p)
print('B: ', B)

print("TA: " + TA)
print("TB: " + TB)

KA, TKA = KandKT(B, a, p)
KB, TKB = KandKT(A, b, p)

print("KA: " + str(KA) + '\n', "KB: " + str(KB))
print("TKA: " + TKA)
print("TKB: " + TKB)