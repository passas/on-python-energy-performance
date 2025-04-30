#from datetime import datetime
from collections import defaultdict

FROM = '01/04/2025' #%d/%m/%Y

def main():

	users = {}
	drivers = {}
	#rides_by_user = defaultdict(list)
	rides_by_driver = defaultdict(list)

	# Load users
	with open('users.csv', 'r') as file:
		linhas = file.readlines()
		for linha in linhas:
			fields = linha.rstrip().split(';')
			u = {
				'username': fields[0],
				'name': fields[1],
				'gender': fields[2],
				'birth_date': fields[3],
				'account_creation': fields[4],
				'pay_method': fields[5],
				'account_status': fields[6]
			}
			if len(u['username'])>0 and len(u['name'])>0 and len(u['gender']) and len(u['pay_method'])>0 and valid_date(u['birth_date']) and valid_date(u['account_creation']) and valid_accountStatus(u['account_status']):
				#print(u)
				users[u['username']] = u
				#pass

	# Load drivers
	with open('drivers.csv', 'r') as file:
		linhas = file.readlines()
		for linha in linhas:
			fields = linha.rstrip().split(';')
			d = {
				'id': fields[0],
				'name': fields[1],
				'birth_date': fields[2],
				'gender': fields[3],
				'car_class': fields[4],
				'license_plate': fields[5],
				'city': fields[6],
				'account_creation': fields[7],
				'account_status': fields[8]
			}
			if len(d['id'])>0 and len(d['name'])>0 and len(d['gender'])>0 and len(d['license_plate'])>0 and	len(d['city'])>0 and valid_date(d['account_creation']) and valid_accountStatus(d['account_status']):
				#print(d)
				drivers[d['id']] = d
				#pass

	# Load rides
	with open('rides.csv', 'r') as file:
		linhas = file.readlines()
		for linha in linhas:
			fields = linha.rstrip().split(';')
			r = {
				'id': fields[0],
				'date': fields[1],
				'driver': fields[2],
				'user': fields[3],
				'city': fields[4],
				'distance': fields[5], #int
				'score_user': fields[6], #float
				'score_driver': fields[7], #float
				'tip': fields[8], #float
				#'comment': fields[9]
			}
			if len(r['id'])>0 and len(r['driver'])>0 and len(r['user'])>0 and len(r['city'])>0 and valid_date(r['date']) and valid_integer(r['distance']) and valid_float(r['score_user']) and valid_float(r['score_driver']) and valid_float(r['tip']):
				#print(r)
				#rides_by_user[r['user']].append(r)
				rides_by_driver[r['driver']].append(r)
				#pass

	#Q1: User
	#username = 'AAbreu' #1 drivers accesses _min
	#username = 'SalvSantos516' #11 drivers accesses _moda
	#username = 'BeaNogueira1187' #33 driver acesses _max
	#nome = users[username]['name']
	#genero = users[username]['gender']
	#idade = age_FromBirth(users[username]['birth_date'])
	#avaliacao = 0.0
	#total = 0.0
	#n = 0
	#for ride in rides_by_user[username]:
	#	avaliacao += float(ride['score_user'])
	#	tax = getTax(drivers[ride['driver']]['car_class'])
	#	total += tax['tax'] + tax['km'] * float(ride['distance'])
	#	n += 1
	#avaliacao /= n
	#print(f'{nome};{genero};{idade};{avaliacao:.1f};{n};{total:.2f}')

	#Q2: Driver N Top Score
	n = len(drivers) #100 000
	top = []
	for driver, rides in rides_by_driver.items():
		avaliacao = 0.0
		for ride in rides:
			avaliacao += float(ride['score_driver'])
		avaliacao /= len(rides)
		top.append({
			'id': driver,
			'nome': drivers[driver]['name'],
			'avaliacao': avaliacao
		})
	for driver in sorted(top, key=lambda x: x['avaliacao'], reverse=True)[0:n]:
		#print(f"{driver['id']};{driver['nome']};{driver['avaliacao']:.1f}")
		pass

def valid_date(string):
	#try:
	#	datetime.strptime(string, '%d/%m/%Y').date()
	#	#d = datetime.strptime(string, '%d/%m/%Y').date()
	#	#d.strftime('%Y-%m-%d')
	#except ValueError:
	#	return False
	#else:
	#	return True
	try:
		day = int(string[0])*10 + int(string[1])
		month = int(string[3])*10 + int(string[4])
		year = int(string[6])*1000 + int(string[7])*100 + int(string[8])*10 + int(string[9])
	except ValueError:
		return 0
	else:
		if string[2] == '/' and string[5] == '/' and day >= 1 and day <= 31 and month >= 1 and month <= 12:
			if month == 2 and day > 29:
				return 0
			elif month in [4,6,9,11] and day > 30:
				return 0
			return 1
		return 0
	
def valid_accountStatus(string):
	if string.title() == 'Active' or 'Inactive':
		return True
	return False

def valid_carClass(string):
	if string.title() == 'Basic' or 'Green' or 'Premium':
		return True
	return False

def valid_integer(string):
	try:
		int(string)
	except ValueError:
		return False
	else:
		return True

def valid_float(string):
	try:
		float(string)
	except ValueError:
		return False
	else:
		return True

def age_FromBirth(birth_date):
	
	day = int(birth_date[0])*10 + int(birth_date[1])
	month = int(birth_date[3])*10 + int(birth_date[4])
	year = int(birth_date[6])*1000 + int(birth_date[7])*100 + int(birth_date[8])*10 + int(birth_date[9])

	yo = 2025 - year
	if month < 4:
		yo -= 1
	elif month == 4 and day < 1:
		yo -= 1

	return yo

def getTax(car_type):
	tax = 0.0
	km = 0.0
	c = car_type.title()
	if c == 'Basic':
		tax, km = 3.25, .62
	elif c == 'Green':
		tax, km = 4.0, .79
	elif 'Premium':
		tax, km = 5.2, .94
	return {
		'tax': tax,
		'km': km
	}

if __name__ == "__main__":
	main()