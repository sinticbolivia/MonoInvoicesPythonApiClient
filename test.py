from .ServicioSincronizacion import ServicioSincronizacion
from .Config import Config
from . import Utils

def test_cuis():
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

def check_expired_token(jwt:str):
	if Utils.token_expired(jwt):
		print('TOKEN EXPIRED')
	else:
		print('TOKEN NOT EXPIRED')
	

if __name__ == '__main__':
	jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJodHRwczpcL1wvZGVtb3NpYXQuMWJ5dGViby5uZXQiLCJhdWQiOiJodHRwczpcL1wvZGVtb3NpYXQuMWJ5dGViby5uZXQiLCJleHAiOjE3OTMwMzg2MDgsImlhdCI6MTc5Mjk1MjIwOCwibmJmIjoxNzkyOTUyMjA4LCJ1c2VyIjp7InVzZXJfaWQiOjY3LCJ1c2VybmFtZSI6InNpZ2U5IiwidGltZSI6MTc5Mjk1MjIwOH0sInRpbWUiOjE3OTI5NTIyMDh9.j17Ur5oe8IstQtfe2SiISq5zatHlaG-HuEAN2qcPk6Ahj2bEGR4I5bXZTrnN3n1IO1EmEuoTuJ2A8wbQvxu4GA'
	check_expired_token(jwt)
