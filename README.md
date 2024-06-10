
```
 ██████╗ ██╗   ██╗██████╗ ███╗   ██╗      ███╗   ███╗ ██████╗ ███╗   ██╗ ██╗████████╗ ██████╗ ██████╗  ██╗███╗   ██╗ ██████╗ 
██╔═══██╗██║   ██║██╔══██╗████╗  ██║      ████╗ ████║██╔═████╗████╗  ██║███║╚══██╔══╝██╔═████╗██╔══██╗███║████╗  ██║██╔════╝ 
██║   ██║██║   ██║██████╔╝██╔██╗ ██║█████╗██╔████╔██║██║██╔██║██╔██╗ ██║╚██║   ██║   ██║██╔██║██████╔╝╚██║██╔██╗ ██║██║  ███╗
██║   ██║╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║╚════╝██║╚██╔╝██║████╔╝██║██║╚██╗██║ ██║   ██║   ████╔╝██║██╔══██╗ ██║██║╚██╗██║██║   ██║
╚██████╔╝ ╚████╔╝ ██║     ██║ ╚████║      ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║ ██║   ██║   ╚██████╔╝██║  ██║ ██║██║ ╚████║╚██████╔╝
 ╚═════╝   ╚═══╝  ╚═╝     ╚═╝  ╚═══╝      ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝
made with ♥ by @h1lmy                                                                                                               
```
OpenVPN Monitoring System and notif to telegram.

## Instalation
Tested on Ubuntu 22.04
```
sudo apt install python3-pip python3-venv
python3 -m pip install pyTelegramBotAPI
git clone https://github.com/mxzyy/openvpn-monitoring.git
```

## Config (Do before running!!!)
```
mkdir /etc/openvpn/scripts
cp -R /openvpn-monitoring/app.py /etc/openvpn/scripts/client-connections.py
ln -s /etc/openvpn/scripts/client-connections.py /etc/openvpn/scripts/client-connect.py
ln -s /etc/openvpn/scripts/client-connections.py /etc/openvpn/scripts/client-disconnect.py
echo '' > /var/log/openvpn/client-connections.log
echo '{}' > /etc/openvpn/scripts/active.json
```

## Add this into openvpn server.conf
```
nano /etc/openvpn/server/server.conf

script-security 3
client-connect /etc/openvpn/scripts/client-connect.py
client-disconnect /etc/openvpn/scripts/client-disconnect.py
```


## Testing
Just connect using client.ovpn
