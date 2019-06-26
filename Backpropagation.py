import random
import math




class RedNeuronal:


    def __init__(self, ne, ni, ns):
        self.NeuronasEntrada = ne+1
        self.NeuronasSalida = ns
        self.NeuronasEscondidas = ni

        self.n=0.16

        self.x = [1.0]*self.NeuronasEntrada
        self.h = [1.0]*self.NeuronasEscondidas
        self.o = [1.0]*self.NeuronasSalida

        self.W1 = []
        for x in range(self.NeuronasEntrada):
            self.W1.append([0.0]*self.NeuronasEscondidas)

        self.W2 = []
        for x in range(self.NeuronasEscondidas):
            self.W2.append([0.0]*self.NeuronasSalida)

        for i in range(self.NeuronasEntrada):
            for j in range(self.NeuronasEscondidas):
                self.W1[i][j] = random.uniform(-0.1,0.1)
        for i in range(self.NeuronasEscondidas):
            for j in range(self.NeuronasSalida):
                self.W2[i][j] = random.uniform(-0.1,0.1)

    def siguiente(self, x1):

        #paso 1
        for i in range(self.NeuronasEntrada-1):
            self.x[i] = x1[i]

        #paso 2

        for j in range(self.NeuronasEscondidas):
            sum = 0.0
            for i in range(self.NeuronasEntrada):
                sum = sum + self.x[i] * self.W1[i][j]
            self.h[j] = self.sigmoid(sum)

        #paso 3

        for i in range(self.NeuronasSalida):
            sum = 0.0
            for j in range(self.NeuronasEscondidas):
                sum = sum + self.h[j] * self.W2[j][i]
            self.o[i] = self.sigmoid(sum)



    def Backpropagation(self, salida):

        deltaW2 = [0.0] * self.NeuronasSalida
        for i in range(self.NeuronasSalida):
            error = salida[i]-self.o[i]
            deltaW2[i] = self.DerivadaFA(self.o[i]) * error

        deltaW1 = [0.0] * self.NeuronasEscondidas
        for j in range(self.NeuronasEscondidas):
            error = 0.0
            for k in range(self.NeuronasSalida):
                error = error + deltaW2[k]*self.W2[j][k]
            deltaW1[j] = self.DerivadaFA(self.h[j]) * error

        # Actualizar los pesos de la capa de salida
        for j in range(self.NeuronasEscondidas):
            for k in range(self.NeuronasSalida):
                change = deltaW2[k]*self.h[j]
                self.W2[j][k] = self.W2[j][k] + self.n*change

       # Actualizar los pesos de la capa de entrada
        for i in range(self.NeuronasEntrada):
            for j in range(self.NeuronasEscondidas):
                change = deltaW1[j]*self.x[i]
                self.W1[i][j] = self.W1[i][j] + self.n*change

        return error

    def DerivadaFA(self,y):
        return (1.0 - y**2)


    def Resultado(self, input):
        for p in input:
            self.siguiente(p[0])
            temp,temp1=[],[]
            for x in self.o:
                temp.append(format(x,".2f"))
                temp1.append(int(round(x)))
            #print (p[0], "->",p[1],"->",temp)
        return temp

    def Entrenamiento(self, input):
        for i in range(5000):
            error = 0.0
            for p in input:
                inputs = p[0]
                outputs = p[1]
                self.siguiente(inputs)
                error = error + self.Backpropagation(outputs)



    def sigmoid(self, z):
        ##z = -z
        ##return 1/(1+np.exp(z))
        return math.tanh(z)





        #dw2 = np.multiply(-(y - self.o), self.sigmoidPrima(self.hw2))
        #djdw2 = np.dot(self.xiw1.T, dw2
        #dw1 = np.dot(dw2, self.W2.T)*self.sigmoidPrima(self.xiw1)
        #djdw1 = np.dot(x.T, dw1)
