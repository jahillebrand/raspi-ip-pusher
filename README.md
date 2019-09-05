# raspi-ip-pusher
## Simple python script to send the user a Pushbullet notification with the host device's IP address

To set up this script:
1. Clone the repo to your machine
2. Put the get\_ip\_addr.py file in a safe location on your machine
3. Edit the get\_ip\_addr.py file and insert your Pushbullet [Access Token](https://www.pushbullet.com/#settings) on line 18 for the `<pushbullet auth here>` string
3. type `crontab -e` and pick an editor (if you've never used it before)
4. Go to the end of the file, and type `@reboot python /path/to/the/get_ip_addr.py &`
5. Save the file

## Note
When this script runs, it will first pause for roughly 45 seconds to allow the system to fully boot and let network manager connect to a network. Only then will the program find the machine's IP address and push it to your account. Additionally, if the program fails to retrieve an IP, it will wait 5 seconds, then try again. This process will repeat indefinitely. 


