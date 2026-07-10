from .MonoObject import MonoObject


class Evento(MonoObject):

    def __init__(self):
        self.codigo_evento = None
        self.codigo_sucursal = 0
        self.codigo_puntoventa = 0
        self.codigo_recepcion = None
        self.fecha_inicio = None
        self.fecha_fin = None
        self.cufd_evento = None

    def to_dict(self) -> dict:
        data = super().to_dict()
        data['sucursal_id'] = self.codigo_sucursal
        data['puntoventa_id'] = self.codigo_puntoventa
        data['evento_id'] = self.codigo_evento
        data.pop('codigo_sucursal')
        data.pop('codigo_puntoventa')
        data.pop('codigo_evento')

        return data

