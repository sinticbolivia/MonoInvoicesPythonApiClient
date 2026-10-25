from .ServicioSincronizacion import ServicioSincronizacion
from .Config import Config

config = Config('')
config.server = 'https://demosiat.1bytebo.net'
config.username = 'valkiria2_400'
config.password = 'valkiria2_400'

service = ServicioSincronizacion()
service.set_config(config)
service.login()
res = service.cuis()
print(res)
res = service.cufd()
print(res)
