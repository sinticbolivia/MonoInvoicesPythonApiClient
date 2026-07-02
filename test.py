from .ServicioSincronizacion import ServicioSincronizacion

service = ServicioSincronizacion()
service.set_server('https://demosiat.1bytebo.net')
service.login('valkiria2_400', 'valkiria2_400')
res = service.cuis()
print(res)
res = service.cufd()
print(res)