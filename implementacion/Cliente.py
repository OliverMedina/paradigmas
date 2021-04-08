from abc import ABCMeta, abstractmethod

class Cliente(metaclass=ABCMeta):
    '''Clase abstracta de clientes'''
    def __init__(self, nombre='S/N', apellido='S/A', ruc='***'):
        self.__nombre = nombre
        self.__apellido = apellido
        # Definimos el atributo monto a pagar.
        self.monto_a_pagar = 0

        self.medio_de_pago = None

    def __str__(self):
        '''Genera la cadena apellido, nombre.............monto a pagar'''
        # Antes de imprimir los datos debemos calcular el monto a pagar.
        self._monto_a_pagar()
        # Creamos la cadena con el formato "apellido, nombre"
        self.__ape_nom = 'Cliente: ' + self.__apellido + ', ' + self.__nombre + '\nMonto a pagar:'
        # Generamos un formato de impresion para el monto a pagar.
        return '{:-<040} {:2n}'.format(self.__ape_nom, self.monto_a_pagar)

    @abstractmethod
    def _monto_a_pagar(self):
        '''Metodo abstracto para el calculo del
           monto a pagar segun el tipo de cliente'''
        pass



class ClienteConvencional(Cliente):
    '''Clase que representa a los clientes que no reciben
        algun tipo de variante sobre el precio total.'''
    def __init__(self, precio_total, medio_de_pago, **kwargs):
        super().__init__(**kwargs)
        self.precio_total = precio_total
        self.medio_de_pago = medio_de_pago

    def _monto_a_pagar(self):
        '''Implementacion del metodo abstracto para el
           calculo del monto a pagar para los clientes convencionales.'''
        self.monto_a_pagar = self.precio_total 


class ClienteEspecial(Cliente, metaclass=ABCMeta):
    '''Clase abstracta que representa a los clientes que reciben
       algun tipo de variante en su precio total.'''

    pass

class ClienteFiel(ClienteEspecial):
    '''Clase que representa a los clientes que reciben un
        descuento especial.'''
    
    def __init__(self, precio_total, medio_de_pago, **kwargs):
        super().__init__(**kwargs)
        self.precio_total = precio_total
        self.medio_de_pago = medio_de_pago
        self.__descuento = 0.9

    def _monto_a_pagar(self):
        '''Implementacion del metodo abstracto para el
           calculo del monto a pagar para los clientes fieles.'''
        self.monto_a_pagar = self.precio_total * self.__descuento

class ClienteVIP(ClienteEspecial):
    '''Clase que representa a los clientes que reciben un
        descuento especial.'''

    def __init__(self, precio_total, medio_de_pago, **kwargs):
        super().__init__(**kwargs)
        self.precio_total = precio_total
        self.medio_de_pago = medio_de_pago
        self.__aumento = 1.05

    def _monto_a_pagar(self):
        '''Implementacion del metodo abstracto para el
           calculo del monto a pagar para los clientes vip.'''
        self.monto_a_pagar = self.precio_total * self.__aumento
