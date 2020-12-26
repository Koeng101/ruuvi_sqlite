
1. Remember to add peewee and ruuvitag-sensor packages to the root user of the rpi
2. Run `python3 models.py` once to initialize the database 
3. Open `sudo crontab -e` and add the line `@reboot python3 /home/pi/ruuvi_sqlite/app.py`  
4. Reboot the pi
