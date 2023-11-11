# SitAlertPi ⬆️
Here's a little project to help you get up from your standing desk regularly

I have also uploaded a video about this project to YouTube. [Check it out](https://youtube.com/EasyTec100) (german video)

# What is needed?
- RaspberryPi (I use a RaspPi 3b+, but I think it doesn't matter)
- Breadboard or other solutions (maybe you soldering it yourself)
  - Jumper cable (if needed)
- Ultrasonic sensor HC-SR04
- 2 LED's (I use: 1x red and 1x blue)
- resistors (2x 150Ω; 1x 330Ω; 1x 10kΩ)

# connection diagram
First of all, the hardware must be connected.
If you like, you can also use a different PIN assignment, **but don't forget that you need to customize them in both scripts!**
![Connection Diagram](https://github.com/EasyTecRepository/SitAlertPi/blob/main/SitAlertPi_Steckplatine.png)

# Setup
You must edit a few variables in my script.

| Variables                    | Description                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
|SENSOR_TRIGGER                | This is the Pin where you have connected the "trigger"-cable of the sensor                                 |
|SENSOR_ECHO                   | This is the Pin where you have connected the "echo"-cable of the sensor                                    |
|PIN_output_LED_r              | This is the Pin where you have connected the positive (+) red LED                                          |
|PIN_output_LED_b              | This is the Pin where you have connected the positive (+) blue LED                                         |
|def_distance                  | Defines the distance at which the alarm is triggered (if distance is greater than this variable)           |
|duration                      | Defines the duration of the flashing/flickering LEDs                                                       |
|speed                         | Defines the speed of the flashing/flickering LEDs                                                          |
|time_before_stand_up          | Defines the time after which you should be prompted to get up                                              |

Furthermore, you must install Python3 and Python3-pip, if not already done.
```
sudo apt-get update && sudo apt-get install python3 python3-pip
```

Now, we're ready to create this script on the Raspberry Pi.
First, we create a file, no matter in which folder.
The name of your script doesn't matter.
```
nano SitAlertPi.py
```
Afterward, you paste the [script from this repository](https://github.com/EasyTecRepository/SitAlertPi/blob/main/SitAlertPi.py) into your editor.
After you have changed all the above-mentioned variables you can save the script with:
- control+O & control+X (macOS)
- STRG+O & STRG+X (Windows)

Finally, you can run the following command:
```
python3 SitAlertPi.py
```

# automation 

If you want the script to start when your Raspberry Pi starts:
I use autostart ([Based on this Tutorial](https://tutorials-raspberrypi.de/raspberry-pi-autostart-programm-skript/)). Here is how it works:
First, we need to create another script.
In my case, the name is SitAlertPi.
This will be the name of your service.
The name of this script doesn't matter.
```
sudo nano /etc/init.d/SitAlertPi
```
Here you must paste [this script](https://github.com/EasyTecRepository/SitAlertPi/blob/main/SitAlertPi).
Make sure that you have edited the "{YOUR USERNAME}" variable (3 times in the script). This is your username.

Here you must edit a few things.
Please be save, that your path of the Python script is correct.
In my example is the path ```/home/{YOUR USERNAME}/{YOUR FOLDER}/SitAlertPi.py```.
If you're not sure, what the right path is, go into the folder where your Python script is and type in: ```pwd```
This command outputs the complete path in which you are located. Now you only need to append the name of your script and you have the complete path.

After that, we give the script more rights.
```
sudo chmod 755 /etc/init.d/SitAlertPi
```
Note that this path must be the same as the one you specified earlier.

Now you can add this service to autostart.
```
sudo update-rc.d SitAlertPi defaults
```
Here too, use the same name as the service!

If you don't want autostart anymore, run this:
```
sudo update-rc.d -f SitAlertPi remove
```
And when you want to start/stop your script manually, you can do this:
```
sudo /etc/init.d/SitAlertPi start
```
```
sudo /etc/init.d/SitAlertPi stop
```

