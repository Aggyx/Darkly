User-Agent and Referer Header Challenge
=======================================

At the bottom of the home page, there is a link with the text "© BornToSec", which leads to the following page:
`http://darkly/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`

The hash is not cracked in CrackStation.
The page does not contain any suspicious link or visible content.

After inspecting the HTML source, I found that there are a couple of comments, of which 2 are important, and the rest are just 42 nonsense.

```HTML
<!--
You must come from : "https://www.nsa.gov/".
-->

<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```

The first comment suggests that the page from which we jump to this page should be the NSA's website. For this, we can manipulate the "Referer" header.

https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer

The second comment asks us to use the "ft_bornToSec" browser, which of course does not exists. However, the "User-Agent" header is the header that gives information about the user's browser, operating system and it's version. This is useful for stuff like auto recommending the download file based on the operating system.

https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent

With this sorted out, we can craft a request with these requirements:

```bash
curl \
  -H "User-Agent: ft_bornToSec" \
  -H "Referer: https://www.nsa.gov/" \
  http://darkly/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

The output is not very clear on the command line, but if we save it to an html file and then open it in the broswer, we can clearly see the flag.

Also, this is much more visual using a program like Burp Suite, which let's us modify a request before sending it, and visaulize it in a broswer.


```bash
$ curl -s -H "User-Agent: ft_bornToSec"   -H "Referer: https://www.nsa.gov/"   http://darkly/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f | grep flag

<center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
```
