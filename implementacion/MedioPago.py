from abc import ABCMeta, abstractmethod

class MedioDePago(metaclass=ABCMeta):
    '''Clase abstracta de medio de pago.'''
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass

class Efectivo(MedioDePago):
    '''Clase que representa el pago en efectivo.'''

    def __str__(self):
        return "Efectivo"

class TarjetaCredito(MedioDePago):
    '''Clase que representa el pago por tarjeta de credito.'''
    
    def __str__(self):
        return "tarjeta de Credito"

class Cheque(MedioDePago):
    '''Clase que representa el pago por medio de cheque.'''

    def __str__(self):
        return "Cheque"