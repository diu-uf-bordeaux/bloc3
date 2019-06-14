from datetime import datetime

now = datetime.now()
print('Nous sommes le '+now.strftime('%d/%m/%Y'))
print('Il est '+now.strftime('%H:%M:%S'))