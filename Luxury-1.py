import os, sys
os.system("git pull")
os.system('xdg-open https://chat.whatsapp.com/+46726413604')
try:
    __import__("SIYAM ").menu()
except Exception as e:
    exit(str(e))
