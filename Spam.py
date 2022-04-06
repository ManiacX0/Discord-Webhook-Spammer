import random
from discord_webhook import DiscordWebhook
from colorama import Fore, init
import socket
import ctypes
from threading import Thread
from datetime import datetime


ctypes.windll.kernel32.SetConsoleTitleW("Discord Webhook Spammer | By ManiacX0")
init(autoreset=True)
now = datetime.now()
ts = datetime.timestamp(now)
name = socket.gethostname()
print("Welcome " + Fore.CYAN + f"{name} !\n")


url = input("Paste the webhook url > ")

amount = input("\nMessage > ")
threads = int(input("\nHow many threads ? > "))
print("\n> Starting threads...\n")

proxys = open("proxies.txt", "r")
proxys = proxys.readlines()
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36',
          'X-RateLimit-Limit': '100000',
          'X-RateLimit-Remaining': '100000',
          'X-RateLimit-Reset': '1000',
          'X-RateLimit-Reset-After': '10',
          'X-RateLimit-Bucket': 'abcd1234',
          'X-RateLimit-Scope': 'shared'
          }

def Spamming(url, proxys):
    error = 0
    while True:
        for proxy in proxys:
            PROX = {'https': proxy}
            webhook = DiscordWebhook(url=f"{url}",content=f"{amount}", proxies=PROX, headers=header)
            try:
                response = webhook.execute()
                print(response)
                if response.status_code == 200:
                    print("Message sent !")
                elif response.status_code == 429:
                    print(Fore.LIGHTRED_EX + "Retry...")
            except:
                error = error + 1

for i in range(threads):
    t = Thread(target=Spamming, args=(url, proxys))
    t.start()
    t.join(0.3)