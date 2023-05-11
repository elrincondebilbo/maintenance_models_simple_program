'''
CTR/CMR MAITENANCE MODELS

This is a very simple program for the CTR
"Criticidad Total por Riesgo"
and MCR
"Matriz de Criticidad por Riesgo"
maintenance models
'''

# Equipment and inventary definition as objects

class Equipo:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        print('Se ha creado equipo: ' + self.name + ' , código: ' + self.code)
    
    def modelo_CTR(self, FF, IO, FO, CM, SHA):
        self.FF = FF
        self.IO = IO
        self.FO = FO
        self.CM = CM
        self.SHA = SHA

        # Variable cast
        F_F = int(self.FF)
        I_O = int(self.IO)
        F_O = int(self.FO)
        C_M = int(self.CM)
        S_H_A = int(self.SHA)

        CTR = F_F * ( (I_O * F_O) + C_M + S_H_A )
        CTR_info = {'FF':self.FF, 'IO':self.IO, 'FO':self.FO, 'CM':self.CM, 'SHA':self.SHA, 'CTR':str(CTR)}

        print('Valor CTR de' + self.name + ': {}').format(str(CTR))

class Inventario:
    Equipos = []

    def __init__(self, Equipos=[]):
        self.Equipos = Equipos

    def add(self,E):
        self.Equipos.append(E)
    
    def show(self):
        for E in self.Equipos:
            print(E)

######### Main program #########

print('')
print('================================')
print('Modelos CTR/CMR')

while True:
    print('================================')
    print('')
    print('Main Menu: ¿Qué desea hacer?')
    print('''
    [1] Crear un nuevo equipo y sus datos \n
    [2] Ver lista de equipos creados \n
    [3] Modificar equipo \n
    [4] Borrar equipo \n
    [5] Cerrar terminal \n
    ''')
    que_hacer = input('Ingrese opción seleccionada: ')

    if que_hacer == '1':
        print('')
        equipo = input('Ingrese nombre de equipo: ')
        codigo = input('Ingrese código del equipo: ')
        print('')
        e = Equipo(equipo,codigo)

        print('')
        print('Elija un modelo')
        print('''
    [1] CTR \n
    [2] MCR \n
        ''')
        modelo_seleccionado = input('Ingrese opción seleccionada: ')

        # ---------------------------------------------------------------- CTR MODEL ----------------------------------------------------------------

        if modelo_seleccionado == '1':

            while True:
                print('')
                print('================================')
                print('Factor de frecuencia de fallos (FF)')
                print('''
    [4] Frecuente: Mayor de 2 veces al año
    [3] Promedio: 1 y 2 eventos al año
    [2] Bueno: entre 0.5 y 1 evento al año
    [1] Excelente: menos de 0.5 eventos al año
                ''')

                FF = int(input('Ingrese su selección: '))

                print('')
                print('================================')
                print('Impacto operacional (IO)')
                print('[10] Pérdidas de producción superioroes al 75%')
                print('[7] Pérdidas de producción entre el 50% y el 74%')
                print('[5] Pérdidas de producción entre el 25% y el 49%')
                print('[3] Pérdidas de producción entre el 10% y el 24%')
                print('[1] Pérdidas de producción menores al 9%')
                print('')
                
                IO = int(input('Ingrese su selección: '))

                print('')
                print('================================')
                print('Impacto por flexibilidad operacional (FO)')
                print('[4] No se cuenta con unidades de reserva para cubrir la producción, tiepos de reparación y logística muy grandes')
                print('[2] Se cuenta con unidades de reserva que logran curbir de forma parcial el impacto de producción, tiempos de reparación y logística intermedios')
                print('[1] Se cuenta con unidades de reserva en línea, tiempos de reparación y logística pequeños')
                print('')

                FO = int(input('Ingrese su selección: '))

                print('')
                print('================================')
                print('Impacto en Costes de Mantenimiento (CM)')
                print('[2] costes de reparación y mano de obra superiores a $20 000')
                print('[1] costes de reparación y mano de obra inferiores a $20 000')
                print('')

                CM = int(input('Ingrese su selección: '))

                print('')
                print('================================')
                print('Impacto en Seguridad, Higiene y Ambiente (SHA)')
                print('[8] Riesgo alto de pérdida de vida, daños graves a ala salud del personal y/o incidente ambiental mayor (catastrófico) que excedem los límites permitidos')
                print('[6] Riesgo medio de pérdida de vida , daños importantes a al saud, y/o incidente ambiental de difícil reparación')
                print('[3] Roesgp mínimo de pérdda de vida y afección a la salud (recuperable en el corto plazo) y/o incidente ambiental menor (controlable), derrames fáciles de contener y fugas repetitivas')
                print('[1] No existe ningún riesgo de pérdida de vida, ni afección a la salud, ni daño ambientales')
                print('')

                SHA = int(input('Ingrese su selección: '))
                # Add detection to invalid command
                #if FF != ['1','2','3','4']:
                #    print('Comando inválido. Cerrando terminal...')
                #    break
                #else:
                #    Equipo.modelo_CTR()

                e.modelo_CTR(FF,IO,FO,CM,SHA) # Still problems to create the model

                break
                

        elif modelo_seleccionado == '2':
        
        # ---------------------------------------------------------------- MCR MODEL ----------------------------------------------------------------

            print('================================')
            print('En mantenimiento. Cerrando terminal...')
            break

        else:
            print('')
            print('Comando inválido. Cerrando terminal...')
            break


    elif que_hacer == '2':
        print('')
        print('En mantenimiento. Cerrando terminal...')
        break

        # Trabajo con ficheros (base de datos)
        #if len(Inventario.show()) == 0:
        #    print('')
        #    print('No se ha encontrado ningún equipo.')
        #else:
        #    print(Inventario.shw())

    elif que_hacer == '3':
        print('')
        print('En mantenimiento. Cerrando terminal...')
        break

    elif que_hacer == '4':
        print('')
        print('En mantenimiento. Cerrando terminal...')
        break

    elif que_hacer == '5':
        break

    else:
        print('')
        print('Comando inválido. Cerrando terminal...')
        break

print('================================')