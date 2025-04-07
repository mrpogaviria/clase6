from datetime import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo= " "
        self.__peso= " "
        self.__fecha_ingreso= ''
        self.__lista_medicamentos= []
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        if t in ['canino', 'felino']:
            self.__tipo = t
        else:
            print('Ingrese canino o felino')
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 

    
class sistemaV:
    def __init__(self):
        self.__mascotas = {'canino':{},'felino': {}}
    
    def verificarExiste(self,historia):
        return any(historia in self.__mascotas[tipo] for tipo in self.__mascotas)
        
    def verNumeroMascotas(self):
        return sum(len(self.__mascotas[tipo]) for tipo in self.__mascotas)
    
    def ingresarMascota(self,mascota):
        if mascota.verTipo():
            self.__mascotas[mascota.verTipo()][mascota.verHistoria()] = mascota 
   
    def verFechaIngreso(self , historia):
        #busco la mascota y devuelvo el atributo solicitado
        for tipo in self.__mascotas:
            if historia in self.__mascotas[tipo]:
                return self.__mascotas[tipo][historia].verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for tipo in self.__mascotas:
            if historia in self.__mascotas[tipo]:
                return self.__mascotas[tipo][historia].verLista_Medicamentos() 
        return None
    
    def eliminarMedicamento(self, historia, nombre_med):
        for tipo in self.__mascotas:
            if historia in self.__mascotas[tipo]: #verifica si la mascota existe
                mascota = self.__mascotas[tipo][historia]
                for med in mascota.verLista_Medicamentos(): 
                    if med.verNombre() == nombre_med:
                        mascota.verLista_Medicamentos().remove(med)
                        return True 
        return False
  
       
    def eliminarMascota(self, historia):
        for tipo in self.__mascotas:
            if historia in self.__mascotas[tipo]:
                del self.__mascotas [tipo][historia]  #opcion con el pop
                return True  #eliminado con exito
        return False 

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       1- Ingresar una mascota 
                       2- Ver fecha de ingreso 
                       3- Ver número de mascotas en el servicio 
                       4- Ver medicamentos que se están administrando
                       5- Eliminar mascota
                       6- Eliminar medicamento 
                       7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                while True:
                    fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                    try: 
                        datetime.strptime(fecha, "%d/%m/%Y")
                        print('Fecha válida')
                        break
                    except ValueError:
                        print('La fecha debe estar en dd/mm/aaaa')
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                cont = 0
                while cont<nm:
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    if any(med.verNombre() == nombre_medicamentos for med in lista_med):
                        print('Medicamento ya existente')
                        continue
                        
                    else:  
                        dosis =int(input("Ingrese la dosis: "))
                        medicamento = Medicamento()
                        medicamento.asignarNombre(nombre_medicamentos)
                        medicamento.asignarDosis(dosis)
                        lista_med.append(medicamento)
                        cont += 1

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
                print ('Mascota ingresada con éxito')

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con éxito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu == 6: #Eliminar medicamento
            historia = int(input("Número de historia clínica: "))
            nombre_medicamento = input("Ingrese el nombre del medicamento: ").strip().lower()

            if servicio_hospitalario.eliminarMedicamento(historia, nombre_medicamento):
                print(f"Medicamento '{nombre_medicamento}' eliminado correctamente.")
            else:
                print("No se pudo eliminar el medicamento.")
                
        elif menu == 7:
            r = input('¿Quiere salir del sistema?: 1. Si 2. No ')
            if r == '1':
                print("Usted ha salido del sistema de servicio de hospitalización...")
                break
            else:
                continue 
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main() #se cumple cuando 
    # me permite hacer pequeñas pruebas en equipos aislados





            

                

