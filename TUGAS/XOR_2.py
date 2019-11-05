import numpy as np
def maju():

    #inisialisasi bobot awal
    Vij = [0.2, 0.3, -0.1, 0.3, 0.1, -0.1]
    bi = [-0.3, 0.3, 0.3]
    Wij = [0.5, -0.3, -0.4]
    bi_2 = -0.1
    hitung = 0

    try:
        while True:
            #feedforward menghitung keluaran hidden layer
            Z_net1 = float(bi[0]) + (float(x1[1])*float(Vij[0])) + (float(x2[1])*float(Vij[3]))
            Z_net2 = float(bi[1]) + (float(x1[1])*float(Vij[1])) + (float(x2[1])*float(Vij[4]))
            Z_net3 = float(bi[2]) + (float(x1[1])*float(Vij[2])) + (float(x2[1])*float(Vij[5]))
            #print(Z_in1, Z_in2, Z_in3)
            Z1 = 1/(1+(np.exp(-Z_net1)))
            Z2 = 1/(1+(np.exp(-Z_net2)))
            Z3 = 1/(1+(np.exp(-Z_net3)))
            #print(Z1, Z2, Z3)

            Y_net = bi_2 + (Z1*(Wij[0])) + (Z2*(Wij[1])) + (Z3*(Wij[2]))
            #print(Y_net)
            Y = 1/(1+(np.exp(-Y_net)))
            #print(Y)

            if Y > 0.995:
                #print("sesuai target")
                #print(Y)
                return Y
                break
            else :
                #Z_net1
                hitung += 1
                print(hitung)

            #fase propagasi mundur
            S1 = (Target[1]-Y)*(Y)*(1-Y)
            #print(S1)
            delta_W1 = alpha*S1*Z1
            delta_W2 = alpha*S1*Z2
            delta_W3 = alpha*S1*Z3
            delta_W0 = alpha*S1
            #print(delta_W1, delta_W2, delta_W3, delta_W0)

            #hitung faktor S di hidden layer
            S_net1 = S1*Wij[0]
            S_net2 = S1*Wij[1]
            S_net3 = S1*Wij[2]
            #print(S_net1, S_net2, S_net3)
            S1_H = S_net1*Z1*(1-Z1)
            S2_H = S_net2*Z2*(1-Z2)
            S3_H = S_net3*Z2*(1-Z3)
            #print(S1_H, S2_H, S3_H)

            delta_b1 = alpha*S1_H*x1[0]
            delta_b2 = alpha*S2_H*x1[0]
            delta_b3 = alpha*S3_H*x1[0]

            delta_V1 = alpha*S1_H*x1[0]
            delta_V2 = alpha*S2_H*x1[0]
            delta_V3 = alpha*S3_H*x1[0]
            delta_V4 = alpha*S1_H*x1[0]
            delta_V5 = alpha*S2_H*x1[0]
            delta_V6 = alpha*S3_H*x1[0]
            #print (delta_b1, delta_b2, delta_b3)

            #update bobot
            V1_baru = Vij[0] + delta_V1
            V2_baru = Vij[1] + delta_V2
            V3_baru = Vij[2] + delta_V3
            V4_baru = Vij[3] + delta_V4
            V5_baru = Vij[4] + delta_V5
            V6_baru = Vij[5] + delta_V6

            b1_baru = bi[0] + delta_b1
            b2_baru = bi[1] + delta_b2
            b3_baru = bi[2] + delta_b3

            W1_baru = Wij[0] + delta_W1
            W2_baru = Wij[1] + delta_W2
            W3_baru = Wij[2] + delta_W3

            W0_baru = bi_2 + delta_W0

            #print (W0_baru, W1_baru, W2_baru, W3_baru)

            Vij = [V1_baru, V2_baru, V3_baru, V4_baru, V5_baru, V6_baru]
            bi = [b1_baru, b2_baru, b3_baru]
            Wij = [W1_baru, W2_baru, W3_baru]
            bi_2 = W0_baru

            #return Y
    except KeyboardInterrupt:
        print("finish")

x1 = [1,1,0,0]
x2 = [1,0,1,0]
alpha = 0.2
Target = [0,1,1,0]
#maju()
