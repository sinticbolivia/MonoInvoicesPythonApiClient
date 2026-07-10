import requests
import json
from .MonoInvoice import MonoInvoiceClient
from .Evento import Evento


class ServicioOperaciones(MonoInvoiceClient):

    def __init__(self):
        pass

    def crear_puntoventa(self):
        pass

    def borrar_puntoventa(self):
        pass

    def lista_eventos(self, page: int = 1, limit: int = 25) -> list:
        endpoint = '{0}/invoices/siat/v2/eventos?page={1}&limit={2}'.format(self._base_url, page, limit)
        res = requests.get(endpoint, headers=self._get_headers())

        return res.json()

    def crear_evento(self, evento: Evento):
        endpoint = '{0}/invoices/siat/v2/eventos'.format(self._base_url)
        res = requests.post(endpoint, json=evento.to_dict(), headers=self._get_headers())

        return res.json()

    def cerrar_evento(self, id: int):
        endpoint = '{0}/invoices/siat/v2/eventos/{1}/cerrar'.format(self._base_url, id)
        res = requests.get(endpoint, headers=self._get_headers())

        return res.json()
