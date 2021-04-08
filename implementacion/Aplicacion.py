from Cliente import *

class Aplicacion():
    '''Clase destinada a la ejecucion de la aplicacion segun la especificacion dada.'''
    # Definimos una lista de clientes.
    lista_clientes = []

    @staticmethod
    def cargar_lista_clientes():
        '''Crea instancias de clientes y los agrega en la lista.'''
        # Creamos los clientes.
        cli1 = ClienteConvencional(50000, nombre='Oscar', apellido='Mendez', ruc='123-2')
        cli2 = ClienteFiel(120000, nombre='Julio', apellido='Irrazabal', ruc='369-5')
        cli3 = ClienteConvencional(30000)
        cli4 = ClienteVIP(115000, nombre='Victor', apellido='Rios', ruc='745-1')
        cli5 = ClienteFiel(200000, nombre='Pedro', apellido='Perez', ruc='3545-2')
        # Agregamos en la lista los clientes que pasaron esta semana.
        Aplicacion.lista_clientes.append(cli1)
        Aplicacion.lista_clientes.append(cli2)
        Aplicacion.lista_clientes.append(cli3)
        Aplicacion.lista_clientes.append(cli4)
        Aplicacion.lista_clientes.append(cli5)

    @staticmethod
    def generar_listado_clientes():
        '''Recorre la lista de empleados y los imprime con formato.'''
        # Imprimimos un encabezado para el listado
        print('Lista de Clientes'.center(65, '*'))
        # Iteramos sobre la lista para imprimir los montos a pagar.
        nro_linea = 0
        for cliente in Aplicacion.lista_clientes:
            nro_linea+=1
            print('{:2}- {}'.format(nro_linea, cliente))


    @staticmethod
    def main():
        '''Punto de inicio del programa'''
        Aplicacion.cargar_lista_clientes()
        Aplicacion.generar_listado_clientes()

if __name__ == '__main__':
     Aplicacion.main()