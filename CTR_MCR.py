'''
CTR/CMR MANTAINANCE MODELS

This is a very simple program for the CTR
"Criticidad Total por Riesgo"
and MCR
"Matriz de Criticidad por Riesgo"
mantainance models
'''

# Equipment definition as objects

class Equipo(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code
        print('Se ha creado equipo: ' + self.name + ', código: ' + self.code)
    
    def factor_de_frecuencia(self,value):
        self.value = value

######### Main program #########

Equipos = []

print('Modelos CTR/CMR')