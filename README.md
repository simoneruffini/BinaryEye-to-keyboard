# BinaryEye-to-keyboard

## WARNING
**The tool emulates a keyboard, so it will directly type the scanned code wherever the focus is and on whichever window. So be consius on what you scan and where you type**

## Infos
The intended functionality of this repo is to use [Binary Eye](https://github.com/markusfisch/BinaryEye)  as a barcode
reader which will directly write (as a keyboard) the scanned barcode on a host PC.

The user will run a python script on the machine that will recive the scanned codes. 

The python script implements a simple http server that will listen to POST request which will contain the barcode sent by Bynary Eye.

Once the data is received it will be directly written on the screen by using a virtual keyboard.

**IMPORTANT**: the application will work only if the android device and the
host pc are on the same network (__the same wifi more or less__). If this is
not the case use a VPN or a service like [tailscale](https://tailscale.com/) to
put the devices on the same network.


## HOW TO INSTALL
### On the Host PC (server)
- Install `python3` and `pip`
- Run `pip install pyautogui` this module will emulate the keybaord on the PC that will host the server.
- If you have a firewall installed on your machine open the port `8080` for `TCP` connections. 
  If that port is alredy in use by a service on the host PC change the variable `SERVER_PORT` in the script file to another available port number.
- Get the IP address of the network interface you will use: on windows `ipconfig` on linux `ip addr`.
- Run `python ./binaryeye-to-keyboard.py`
### On the Android Phone 
- Install Binary Eye (google play or f-droid)
- Open Binary Eye on your androind device. 
- Type the three dots on the top right, go to settings and go to the _Forwarding_ section.
    - Tap the configuration box called __Request type__ and select `POST application/x-www-form-urlencoded`
    - Toggle the button `Forward scans`
    - Tap the configuration box called __URL to forward to__. In that box wirte
      the IP address and SERVER_PORT number defined in the previous steps with
      this format: `http://IP_ADDRESS:SERVER_PORT` (e.g. `http://192.168.1.123:8080`) 
      - Prss the `TEST URL` button. You should see on the Host PC python console a message writing `test`.

### HOW TO USE
Once you followed the previous steps you can simply open an excel document
select the cell where you want to put the scanned bar/QR code and scan it with
Binary Eye. You should see it wirtten in the cell.


