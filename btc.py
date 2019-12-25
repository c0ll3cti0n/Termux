import asyncio
import logging
import re
import time
import os
import sys
import random

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

forecast_channel = 'Free_Bitcoin_Claim_Bot'
forecast_group = '@Free_Bitcoin_Claim_Bot'

def print_msg_time(message):
	print('[' + Fore.MAGENTA + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	print(Fore.BLUE + ' ________________ ' + Fore.RESET)
	print(Fore.MAGENTA +  'Edited version ' + Fore.RESET)
	print(Fore.BLUE + ' ________________\n' + Fore.RESET)
	
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	choice = '🎰 Bonus' 
	if not os.path.exists("session"):
		os.mkdir("session")
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	print_msg_time(Fore.MAGENTA + f'Welcome : ({me.first_name}) to ' + forecast_channel + Fore.RESET)
	# Start command /balance
	i = 1
	while i <= 10000:
		await client.send_message(forecast_group, choice)
		print_msg_time(Fore.MAGENTA + 'waiting to get next bonus'+ Fore.RESET)
		time.sleep(1800) 
		i += 1
	
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())

	
   
