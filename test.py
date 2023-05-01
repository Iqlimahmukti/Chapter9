# first_name = 'Iqlimah Mukti'
# last_name = 'Nugroho'
# full_name = i'{first_name} {last_name}'
# print (full_name)

from datetime import datetime

today = datetime.now()

datetime = today.strftime('%Y-%m-%d-%H-%M-%S')
print (datetime)