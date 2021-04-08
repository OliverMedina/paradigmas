from abc import ABCMeta, abstractmethod

class Comprobante(metaclass=ABCMeta):
    '''Clase abstracta de comprobante.'''

    def __init__(self, cliente):
        self.__cliente = cliente

    def __str__(self):
        return self.__cliente

class Factura(Comprobante):
    '''Clase que representa el comprobante de tipo factura.'''
    def __init__(self, cli, **kwargs):
        super().__init__(**kwargs)
        self.__cli = cli

    def __str__(self):
        self.__monto_pagado = '\nMonto Pagado: '
        self.__medio_de_pago = '\nMedio De Pago: ' 
        return '{} {} {} {} {}'.format(self.__cli, 
                                    self.__monto_pagado,
                                    self.__cli.precio_total,
                                    self.__medio_de_pago,
                                    self.__cli.medio_de_pago) 

