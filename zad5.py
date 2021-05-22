

def logger():
	while True:
		
		login = input('Введите логин: ')
		if len(login) < 5:
			print('Логин слишком короткий')
		else:	
			break
	while True:
						
		parol1 = input('Введите пароль: ')
		if len(parol1) < 8:	
			print('Слишком короткий пароль:')
		else:
			break	
	while True:
					
		
		parol2 = input('Повторите пароль: ')
		if parol2 != parol1:
			print('пароли не совпадают')
		else:
			break	
	

logger()				


