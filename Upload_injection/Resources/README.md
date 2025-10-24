Upload Image Injection
======================

On the home page, there is a link to `http://darkly/?page=upload`,
which contains file browser button, and an upload button.

The file browser itself does not limit selecting files of extension.
When the file is too large, we get an 413 Entity Too Large error from NGINX (this is configured NGINX, not in the application itself).
The magic number of the file is not checked, we can successfully upload any file content as a `jpg`, so long it respects the `Content-Type`.

The files that get accepted are saved to the `/tmp` directory. This directory is not exposed by nginx, so we won't be able to retrieve the file.
(Which is usually necessary to trigger some sort of action. For example if you upload a php reverse shell, you would have to make the web server retrieve and execute the php file in order to obtain the shell.)

When uploading a reverse shell, nothing happens, the file is uploaded correctly, even though it is not a correct `jpg` file.
The extension of the file is only checked by the browser in order to craft the request (with the correct `Content-Type`), but it is not checked by the server.

If we upload a file called `foobar.php`, but with `image/jpeg` as the `Content-Type`, it returns the flag.

```
curl -s --form 'uploaded=@foobar.php;filename=foobar.php;type=image/jpeg' --form 'Upload=Upload' http://darkly/?page=upload | grep flag
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/foobar.php succesfully uploaded.</pre>
```
