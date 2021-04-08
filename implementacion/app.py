from Cliente import *
from MedioPago import *
from Comprobante import *
from os import system

class Aplicacion():
    '''Clase destinada a la ejecucion de la aplicacion segun la especificacion dada.'''

    @staticmethod
    def main():
        '''Crea instancias de clientes y los agrega en la lista.'''
        # Creamos los clientes.
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        ruc = input("Ingrese el ruc: ")
        monto = int(input("Ingrese el monto a pagar: "))
        valido = True
        while(valido):
            opc = int( input("Seleccione el tipo de cliente: "
            "\n1)Cliente Convencional"
            "\n2)Cliente Fiel"
            "\n3)Cliente VIP\n:") )
            validop = True
            while(validop):
                opcp = int( input("Seleccione el medio de pago: "
                "\n1)Efectivo"
                "\n2)Tarjeta de Credito"
                "\n3)Cheque\n:") )
                if( opcp == 1):
                    mdp = Efectivo()
                    validop = False
                elif( opcp == 2):
                    mdp = TarjetaCredito()
                    validop = False
                elif( opcp == 3):
                    mdp = Cheque()
                    validop = False
                else:
                    print("Opcion invalida")

            if( opc == 1):
                cliente = ClienteConvencional(monto, mdp, nombre=nombre, apellido=apellido, ruc=ruc)
                valido = False
            elif( opc == 2):
                cliente = ClienteFiel(monto, mdp, nombre=nombre, apellido=apellido, ruc=ruc)
                valido = False
            elif( opc == 3):
                cliente = ClienteVIP(monto, mdp, nombre=nombre, apellido=apellido, ruc=ruc)
                valido = False
            else:
                print("Opcion invalida")
        factura = Factura(cliente, cliente=cliente)
        system('clear')
        print(factura)
    

if __name__ == '__main__':
     Aplicacion.main()