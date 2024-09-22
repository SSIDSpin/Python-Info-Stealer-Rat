# Python-Info-Stealer-Rat

## Disclaimer
**Usage of Python-Info-Stealer-Rat for hacking or attacking infrastructures without prior mutual consent can be considered illegal activity. It is the final user's responsibility to obey all applicable local, state, and federal laws. Authors assume no liability and are not responsible for any misuse or damage caused by this program.**

**Note:** Considering some of you struggled setting up  my last project Im going to try to keep it all inside the Main.py file.

## What Does It Do?
This is a malicious tool, aimed to look like a HWID Spoofer. The program finds the saved chrome details of the user and decrypts them. It also find out if; Exodus, Electrum, Metamask, Coinbase is installed on the system. It also gets the Minecraft SSID and player UUID. Once done so they are submitted to the Webhook selected by the owner. Furthermore it also opens up a FTP protocol on the users computer so you can directly access files you want to view.

## What It Obtains
- OS Data
- Crypto Wallets
- Minecraft SSID
- Discord Account Grabber
- Roblox Account Grabber
- Chrome Saved Passwords <br>
**Extras:** 
- FTP Connection
- Desktop Screenshot

## How To Run

1. **Download Python**: [Download Python](https://www.python.org/downloads/release/python-31012/)
2. **Install Requirements**:
    - Open Command Prompt in the project folder and run `pip install -r requirements.txt`.
3. **Create Your Webhook**:
    - Generate your Webhook URL/Token.
4. **Set Up Webhook**:
    - Place The Webhook Inside "" On Line 17
5. **Test It**:
    - Run The File And Watch What Happends.

**Note:** I Would recommend changing the logo to something that suits what you plan to use this for, 
          to do the big ascii text similar to what i did visit [patorjk.com](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Spin)

## How To Compile

1. **Run The build_exe.py** 
    - Open CMD in the folder where the project is.
    - Run py build_exe.py
    - And wait for it to fully complete.
2. **Open The Dist Folder**
    - Thats where your exe will be
3. **Changing Name**
    - To change the name of the exe, open the build_exe.py and change line 10.
4. **Changing Icon**
    - To change the icon of the exe, just replace the file named Icon.ico with what you desire. (Make sure its named Icon.ico)

## Dummy Log Images<br>

![Logs](https://i.imgur.com/STJnGu1.png)

**Note:** None Of The Data Shown In The Log Is Correct And Has Been Ran On A RDP Server
