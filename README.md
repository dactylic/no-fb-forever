# What is this?

A script for closing Facebook at given intervals. 

## Use

The main function takes arguments for length of time to run the script, the unit of time to measure length in, and the interval at which to check for Facebook. Interval is always in seconds.

For example, you can call the script like this:

```
fuckfacebook(length=2, unit=h, interval=5)
```

This would make the script run for 2 hours (length is 2, unit is h for "hour"), checking every 5 seconds. Or you could do it like this:

```
fuckfacebook(length=30, unit=m, interval=60)
```

This would make the script run for 30 minutes, checking the window title every minute.


### Side Note
The script checks your current window title for "Facebook", so if you are on a window that is titled "Facebook is set to die tomorrow" it will also close that window at the scheduled interval. 
