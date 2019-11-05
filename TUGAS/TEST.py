import numpy as np
import XOR_1 as NN1
import XOR_2 as NN2
import XOR_3 as NN3
import XOR_4 as NN4

x1 = input("masukan x1: ")
x2 = input("masukan x2: ")

if x1=='1' and x2=='1':
    hasil = NN1.maju()
    print(hasil)
    print(0)

elif x1=='1' and x2=='0':
    hasil = NN2.maju()
    print(hasil)
    print(1)

elif x1=='0' and x2=='1':
    hasil = NN3.maju()
    print(hasil)
    print(1)

elif x1=='0' and x2=='0':
    hasil = NN4.maju()
    print(hasil)
    print(0)

else:
    print("gatau")
