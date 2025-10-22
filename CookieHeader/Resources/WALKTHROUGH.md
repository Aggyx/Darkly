"I_am_admin" Cookie
===================

There is a cookie called `I_am_admin` with a value that seems to be an MD5 hash (`68934a3e9455fa72420237eb05902327`).
If you have seen a sufficient amount of hashes, that is probably the first thing you thought of. It's 32 characters long (16 bytes) and there are only hexadecimal characters.

Let's see on crackstation if we can crack this hash.

Exactly, the value in clear text is `false`. So obviously, if we set I_am_admin to true, it should lead us to somewhere.
`true` in MD5 is: `b326b5062b2f0e69046810717534cb09`. Let's set this cookie and reset the page.

Bingo, we get the following alert:

```
Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

