from .MonoObject import MonoObject

class FacturaItem(MonoObject):

    def __init__(self):
        self.item_id = None
        self.invoice_id = None
        self.product_id = None
        self.product_code = None
        self.product_name = None
        self.quantity = None
        self.price = None
        self.discount = None
        self.numero_imei = None
        self.numero_serie = None
        self.unidad_medida = None
        self.codigo_producto_sin = None
        self.codigo_actividad = None
        self.subtotal = None
        self.total = None
        self.data = {
            'custom_fields': {}
        }

    def set_custom_field(self, field: str, value):
        if 'custom_fields' not in self.data:
            self.data['custom_fields'] = {}

        self.data['custom_fields'][field] = value

    def calculate_totals(self) -> float:
        self.subtotal = (self.quantity if isinstance(self.quantity, (int, float, complex)) else 0) *\
                        (self.price if isinstance(self.price, (int, float, complex)) else 0)
        self.total = self.subtotal - (self.discount if isinstance(self.discount, (int, float, complex)) else 0)
