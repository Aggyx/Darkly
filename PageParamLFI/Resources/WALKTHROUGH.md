As we have seen in previous excersises, the page that is shown depends on the `page` query parameter. for example, the sign in page can be found at `http://192.168.56.104/?page=signin`. when you change `page` to something random, it alerts `Wtf?`. however, when you try to do an LFI attack it seems to change the error message. for example, `page=../../etc/passwd` shows: `Wrong.`. add a couple of `../` and the message shifts to `Almost.`. Finally, after a couple of `../` more, the flag is shown.

Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0  
