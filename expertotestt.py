from pyDatalog import pyDatalog
import math
from Backpropagation import *
from Fuzzy import *

pyDatalog.create_terms('Velocidad, V, Accidentalidad, Velocidad_limite')

def experto(acc_):

    print(acc_)

    Accidentalidad=round(acc_)
    #conocimiento para decision
    +Velocidad(0,"100")
    +Velocidad(1,"90")
    +Velocidad(2,"80")
    +Velocidad(3,"70")
    +Velocidad(4,"60")
    +Velocidad(5,"50")
    +Velocidad(6,"40")
    +Velocidad(7,"30")
    +Velocidad(8,"20")
    +Velocidad(9,"10")

    V(Accidentalidad,Velocidad_limite) <= Velocidad(Accidentalidad, Velocidad_limite)
    print(V(Accidentalidad,Velocidad_limite))



def main():
    #[clima,riesgo,mes],[accidentalidad]
    while(True):
        display=[
            [[0,0.15,0.01],[0.0]],
            [[1,0.88,0.01],[0.9]],
            [[1,0.15,0.01],[0.8]],
            [[0,0.15,0.12],[0.6]],
            [[0,0.88,0.01],[0.8]],
            [[0,0.50,0.01],[0.6]],
            [[0.50,0.50,0.01],[0.5]],
            [[1,0.15,0.12],[0.8]],
            [[1,0.80,0.12],[0.9]],
            [[0.50,0.50,0.07],[0.5]],
            [[0.50,0.80,0.07],[0.8]],
            [[0.40,0.70,0.05],[0.6]],
            [[0.50,0.16,0.06],[0.7]]
            ]

        red = RedNeuronal(3,3,1)
        red.Entrenamiento(display)
        red.Resultado(display)

        dia = input("ingrese dia [0(lunes)-6(domingo)]: ")
        estado_carretera = input("ingrese estado carretera [0(buena) - 100(mala)]: ")
        mes = input("ingrese mes [1-12]: ")
        clima = input("ingrese nivel de lluvia [0(sol) - 100(lluvia)]: ")
        riesgo = calcular_Riesgo(int(dia),int(estado_carretera))
        riesgo = riesgo/100
        print((str(float(clima)/100)+ " " + str(riesgo) + " " +str(float(mes)/100)))
        n = [
            [[(float(clima)/100),(riesgo),(float(mes)/100)],[0.0]]
        ]
        accidentalidad = red.Resultado(n)
        accidentalidad = float(accidentalidad[0])*10
        print((accidentalidad))
        experto(round(accidentalidad))
main()
