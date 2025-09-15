# Darkly
Web Security Iso Challenge

This project consist in a .iso file that when built it deploys an WebServer.

Our objective for the mandatory part is to find 14 different breaches.

# Repo Structure
```
$> ls -al
[..]
drwxr-xr-x 2 root root 4096 Dec 3 XX:XX {Breach name}
[..]
$> ls -alR {Breach name}
{Breach name}:
total 16
drwxr-xr-x 3 root root 4096 Dec 3 15:22 .
drwxr-xr-x 6 root root 4096 Dec 3 15:20 ..
-rw-r--r-- 1 root root 5 Dec 3 15:22 flag
drwxr-xr-x 2 root root 4096 Dec 3 15:22 Resources
{Breach name}/Resources:
total 8
drwxr-xr-x 2 root root 4096 Dec 3 15:22 .
drwxr-xr-x 3 root root 4096 Dec 3 15:22 ..
-rw-r--r-- 1 root root 0 Dec 3 15:22 whatever.whatever
$> cat {Breach name}/flag | cat -e
XXXXXXXXXXXXXXXXXXXXXXXXXXXX$
$>
```