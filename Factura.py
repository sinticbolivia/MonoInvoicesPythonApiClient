from .FacturaItem import FacturaItem
from .MonoObject import MonoObject


class Factura(MonoObject):

    def __init__(self):
        self.codigo_documento_sector = 1
        self.codigo_metodo_pago = 1
        self.codigo_moneda = 1
        self.codigo_sucursal = 0
        self.punto_venta = 0
        self.complemento = None
        self.customer_id = None
        self.customer = None
        self.customer_email = None
        self.nit_ruc_nif = None
        self.tipo_documento_identidad = 1
        self.discount = 0
        self.monto_giftcard = 0
        self.subtotal = 0
        self.total = 0
        self.total_tax = 0
        self.tipo_cambio = 1
        self.numero_tarjeta = None
        self.invoice_date_time = None
        self.items = []
        self.data = {
            'custom_fields': {}
        }

    def add_item(self, item: FacturaItem):
        item.calculate_totals()
        self.items.append(item)

    def set_custom_field(self, field: str, value):
        if 'custom_fields' not in self.data:
            self.data['custom_fields'] = {}

        self.data['custom_fields'][field] = value

    def calcular_total(self) -> float:
        self.subtotal = 0
        self.total = 0
        for item in self.items:
            self.subtotal = self.subtotal + item.calculate_totals()
        self.total = self.subtotal - (self.discount if isinstance(self.discount, (int, float, complex)) else 0)

        return self.total

    def validar(self):
        if len(self.items) <= 0:
            raise Exception('La factura no tiene items')

        return True

    def bind(self, data: dict, skip_fields=[]):
        super().bind(data, skip_fields)
        print('INVOICEDATA ITEMS: ', len(data.get('items', [])))
        for item_data in data.get('items', []):
            item = FacturaItem()
            item.bind(item_data)
            self.add_item(item)

        print('INVOICE ITEMS: ', len(self.items))

    def to_dict(self) -> dict:
        data = {}
        for key, val in self.__dict__.items():
            if key == 'items':
                continue
            data[key] = val

        data['items'] = [item.to_dict() for item in self.items]

        return data
