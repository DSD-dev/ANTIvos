import sys, os, pyfiglet
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore
import config

attack_number_phone = Distribution_Service()

def start(phone):
	attack_number_phone.phone(phone)

	while True:
	    try:
	        attack_number_phone.random_service()
	    except Exception as ex:
	    	print(ex)

os.system('clear')

print(Fore.RED + pyfiglet.figlet_format("ANTIvos"))
print('(===============)')
print(Fore.YELLOW + 'update!')
print(Fore.GREEN + 'made by Veos')
print('Telegram: https://t.me/HackProgramsFromVeos')
print(Fore.RED + '(===============)')
print(Fore.BLUE + '+79999999999')
phone = input('Номер}> ')
print('(===============)')

try:
	attack_number_phone.phone(phone)
except:
	print(Fore.RED + 'Неверный формат ввода.\nВведите номер в формате +7/+3')
	sys.exit()
	


for i in range(750):
	th = Thread(target=start, args=(phone,))
	th.start()