# -*- coding: utf-8 -*-
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
estado_carretera = ctrl.Antecedent(np.arange(0, 101, 1), 'estado_carretera')
dia = ctrl.Antecedent(np.arange(0, 7, 1), 'dia')
riesgo = ctrl.Consequent(np.arange(0, 101, 1), 'riesgo')

names=['bajo','medio','alto']
carreteras=['buena','regular','mala']
dias=['semana','fin de semana']

# Auto-membership function population is possible with .automf(3, 5, or 7)
estado_carretera.automf(names=carreteras)
dia.automf(names=dias)
riesgo.automf(names=names)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API

estado_carretera['buena'] = fuzz.trapmf(estado_carretera.universe, [0, 0, 15, 30])
estado_carretera['regular'] = fuzz.trapmf(estado_carretera.universe, [25, 35, 60, 70])
estado_carretera['mala'] = fuzz.trapmf(estado_carretera.universe, [60, 75, 100, 100])

dia['semana'] = fuzz.trapmf(dia.universe, [0, 0, 0, 7])
dia['fin de semana'] = fuzz.trapmf(dia.universe, [4, 5.5, 7, 7])

riesgo['bajo'] = fuzz.trapmf(riesgo.universe, [0, 0, 15, 35])
riesgo['medio'] = fuzz.trapmf(riesgo.universe, [25, 40, 60, 75])
riesgo['alto'] = fuzz.trapmf(riesgo.universe, [70, 85, 100, 100])

rule1 = ctrl.Rule(dia['semana'] & estado_carretera['buena'],  riesgo['bajo'])
rule2 = ctrl.Rule(dia['semana'] & estado_carretera['regular'],  riesgo['medio'])
rule3 = ctrl.Rule(dia['semana'] & estado_carretera['mala'],  riesgo['alto'])
rule4 = ctrl.Rule(dia['fin de semana'] & estado_carretera['buena'], riesgo['medio'])
rule4 = ctrl.Rule(dia['fin de semana'] & estado_carretera['regular'],  riesgo['alto'])
rule5 = ctrl.Rule(dia['fin de semana'] & estado_carretera['mala'], riesgo['alto'])


#nivel_riesgo.compute()
#print("Riesgo, " + str(nivel_riesgo.output['riesgo']))
#acc= nivel_riesgo.output['riesgo']

def calcular_Riesgo(l,c):
    riesgo_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    nivel_riesgo = ctrl.ControlSystemSimulation(riesgo_ctrl)
    nivel_riesgo.input['dia'] = l
    nivel_riesgo.input['estado_carretera'] = c
    nivel_riesgo.compute()
    print("Riesgo, " + str(nivel_riesgo.output['riesgo']))
    return nivel_riesgo.output['riesgo']
    #riesgo.view(sim=nivel_riesgo)
