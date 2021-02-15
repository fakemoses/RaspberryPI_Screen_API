This uncomplete project serves as a medium for me to improve my skills and refreshes some skills of my python language. The software for the hardware is still under development as I still can't solve some of the issues but it still works fine, just not as how I wanted it to run.

## Requirements
- Raspberry PI (Any versions & I am using PI Zero)
- A TFT screen with GPIO Connector (I am using IlI9431 driver based screen)
- Raspberry Pi OS with desktop (I have multiple issues with the lite version so I would not recommend it for this one)

## Setup the RaspberryPI

The screen must be connected to the PI itself and the following connection is used:

```
BL   -----------pin 12 (GPIO 18)
SCK  -----------pin 23 (GPIO 11)
MISO -----------pin 21 (GPIO 9)
MOSI -----------pin 19 (GPIO 10)
CS   -----------pin 24 (GPIO 8)
RST  -----------pin 22 (GPIO 25)
D/C  -----------pin 18 (GPIO 24)
VIN  -----------pin 17 (3.3v)
GND  -----------pin 20 (GND)
```

Please search in google for your GPIO Pin layout as they may differ depending on your Raspberry PI

Enable the SPI and disable the Overscan (RPI Zero does not have overscan) in the advanced options:

```
sudo raspi-config
```

To load the screen module every time the RPI loads:

```
sudo nano /etc/modules
```

type the following and save the file (Make sure to run with sudo!):

```
spi-bcm2835
fbtft_device
```

Run the following command and paste the options:

```
sudo nano /etc/modprobe.d/fbtft.conf
```

```
options fbtft_device name=fb_ili9341 gpios=reset:25,dc:24,led:18 speed=16000000 bgr=1 rotate=90
```

after you are done with this, reboot the RPI and run the main.py.

## Enabling the RPI to load the script every time it boots

There are many methods to execute the script on start but I am opting for crontab.

```
crontab -e
```

inside the crontab, paste the following and change **your-dir** to the directory where you put the main.py
```
@reboot python /your-dir/RaspberryPI_Screen_API/main.py
```
reboot the system. It should run after 10s or so. 

