import requests
import json
from .MonoInvoice import MonoInvoiceClient
from .Factura import Factura


class ServicioFacturacion(MonoInvoiceClient):

    def __init__(self):
        super().__init__()

    def crear_factura(self, factura: Factura):
        endpoint = '{0}/invoices'.format(self._base_url)
        # factura_json = factura.to_json()
        # print('FACTURA JSON', factura_json)
        res = requests.post(endpoint, json=factura.to_dict(), headers=self._get_headers())

        return res.json()

    def anular_factura(self, id: int, motivo: int):
        endpoint = '{0}/invoices/{1}/void'.format(self._base_url, id)
        data = {
            'invoice_id': id,
            'motivo_id': motivo
        }
        res = requests.post(endpoint, json=data, headers=self._get_headers())

        return res.json()

    def revertir(self, id: int):
        endpoint = '{0}/invoices/siat/v2/invoices/{1}/revert-void'.format(
            self._base_url,
            id
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def validar_nit(self, nit: int):
        endpoint = '{0}/invoices/siat/v2/validate-nit?nit={1}'.format(
            self._base_url,
            nit
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def get_pdf(self, id: int, tpl: str = 'oficio'):
        endpoint = '{0}/invoices/{1}/pdf?tpl={2}'.format(self._base_url, id, tpl)
        res = requests.get(endpoint, headers=self._get_headers())

        return res.json()

    def get_facturas(self, pagina: int = 1):
        endpoint = '{0}/invoices/siat/v2/invoices?page={1}'.format(self._base_url, pagina)
        res = requests.get(endpoint, headers=self._get_headers())

        return res.json()
