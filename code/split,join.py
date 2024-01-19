import time

a = "I love you"
b = a.split("v")
print(b)
c = ['aa','bb','cc']
d = "***".join(c)
print(d)


import time

time1 = time.time()
a = ""
for i in range(1000000):
    a +="stx"
time2 = time.time()
print("+连接的运算时间："+str(time2-time1))

time3 = time.time()
li = []
for i in range(1000000):
    li.append("stx")

b = "".join(li)
time4 = time.time()
print("join()连接的运算时间："+str(time4-time3))