import requests

from .MonoInvoice import MonoInvoiceClient


class ServicioSincronizacion(MonoInvoiceClient):

    def __init__(self):
        super().__init__()

    def cuis(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/cuis?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def cufd(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/cufd?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def unidades_medida(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-unidades-medida?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def tipos_documentos_identidad(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-documentos-identidad?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def motivos_anulacion(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-motivos-anulacion?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def actividades(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/actividades?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def lista_productos(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/lista-productos-servicios?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def leyendas(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/lista-leyendas-factura?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def monedas(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-tipos-moneda?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def metodos_pago(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-metodos-pago?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def tipos_documentos_sector(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-tipos-documentos-sector?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def actividades_document_sector(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/lista-actividades?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def tipos_habitacion(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/lista-tipos-habitacion?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def tipos_punto_venta(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-tipos-punto-venta?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

    def tipos_facturas(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-tipos-facturas?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

    def tipos_emision(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-tipos-emision?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

    def tipos_eventos(self, sucursal: int = 0, puntoventa: int = 0):
        endpoint = '{0}/invoices/siat/v2/sync-eventos?sucursal_id={1}&puntoventa_id={2}'.format(
            self._base_url,
            sucursal,
            puntoventa
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

    def puntosventa(self, sucursal: int = 0):
        endpoint = '{0}/invoices/siat/v2/puntos-venta?sucursal_id={1}'.format(
            self._base_url,
            sucursal,
        )
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

    def user_documentos_sector(self):
        endpoint = '{0}/invoices/users/sectors'.format(self._base_url)
        headers = self._get_headers()
        res = requests.get(endpoint, headers=headers)
        json_obj = res.json()

        return json_obj

