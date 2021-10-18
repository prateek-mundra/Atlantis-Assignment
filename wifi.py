import subprocess
import os
os.system('cmd /c "netsh wlan show networks"')
#find  available networks
networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
available_netwoks = networks.decode('ascii')
print("Below is the available networks")
print(available_netwoks)

#Function to connect the wifi based on the available networks
def connectWifi(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
    with open(name+".xml", 'w') as file:
        file.write(config)
    os.system(command)
  
   
def connect(name, SSID):
    command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    os.system(command)
  
  

name = input("Your Choice? ")
password = input("Password: ")
  
# establish new connection
connectWifi(name, name, password)
print("Connected!")
# connect to the wifi network
connect(name, name)
print("If wifi {} is not connected please use the correct password to connect".format(name))