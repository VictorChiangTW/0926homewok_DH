import time


p = int('009fdb8b8a004544f0045f1737d0ba2e0b274cdf1a9f588218fb435316a16e374171fd19d8d8f37c39bf863fd60e3e300680a3030c6e4c3757d08f70e6aa871033', 16)
g = 2

a = input("enter a in hexadecimal: ")
a = int(a, 16)

b = input("enter b in hexadecimal: ") 
b = int(b, 16)

start_timeA = time.time()
A = pow(g, a, p)
end_timeA = time.time()
TA = str(float(end_timeA - start_timeA) * 1000.0) + 'ms'
print('A: ', A)


start_timeB = time.time()
B = pow(g, b, p)
end_timeB = time.time()
TB = str(float(end_timeB - start_timeB) * 1000.0) + 'ms'
print('B: ', B)

print("TA: " + TA)
print("TB: " + TB)

start_timeKA = time.time()
KA = pow(B, a, p)
end_timeKA = time.time()
TKA = str(float(end_timeKA - start_timeKA) * 1000.0) + 'ms'



start_timeKB = time.time()
KB = pow(A, b, p)
end_timeKB = time.time()
TKB = str(float(end_timeKB - start_timeKB) * 1000.0) + 'ms'


print("KA: " + str(KA) + '\n', "KB: " + str(KB))

print("TKA: " + TKA)

print("TKB: " + TKB)