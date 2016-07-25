# chickendoor
Raspberry Pi Chicken Door

##Sunwiat##
http://www.risacher.org/sunwait/

Sunwait is a small C program for calculating sunrise and sunset, as well as civil, nautical, and astronomical twilights. It has features that make it useful for home automation tasks.

##CRONTAB##
0 04 * * * /bin/sunwait sun up 00:15; python /home/pi/Projects/chickendoor/open_door.py >> /tmp/door.log 2>&1
0 16 * * * /bin/sunwait sun down 00:15; python /home/pi/Projects/chickendoor/close_door.py >> /tmp/door.log 2>&1
