# _WRITEFILE
> The _WRITEFILE statement writes a string into a new file, overwriting an existing file of the same name. It does OPEN , PUT and CLOSE the file in one run. It's the counterpart to the _READFILE$ function.

## SYNTAX
`_WRITEFILE fileSpec$ , contents$`

## PARAMETERS
* fileSpec$ is the name of the file to write as literal or variable [STRING](STRING.md) , if required inclusive a full or relative path. To avoid errors you should use [_DIREXISTS](_DIREXISTS.md) before using this statement to make sure a desired path exists.
	* To avoid errors you should use [_DIREXISTS](_DIREXISTS.md) before using this statement to make sure a desired path exists.
* To avoid errors you should use [_DIREXISTS](_DIREXISTS.md) before using this statement to make sure a desired path exists.
* contents$ is the literal or variable [STRING](STRING.md) which its contents shall be written into the file.


## DESCRIPTION
* Sometimes you may be in need to quickly dump a huge amount of data into a file without much fuss, e.g. the results of the pack/unpack functions _DEFLATE$ and _INFLATE$ or when copying a file in conjunction with the _READFILE$ function.
* In earlier versions of QB64(PE) you had to implement that saving process manually all the time or create a reusable custom [FUNCTION](FUNCTION.md) for it.
* Now [_WRITEFILE](_WRITEFILE.md) will simplify this, it's mainly for convenience to wrap the following code sequence into one handy statement:


## EXAMPLES

```vb
fh = FREEFILE
OPEN fileSpec$ FOR OUTPUT AS #fh: CLOSE #fh
OPEN fileSpec$ FOR BINARY AS #fh
PUT #fh, , contents$
CLOSE #fh
```

* Featured in our "Keyword of the Day" series
* _READFILE$ , [BLOAD](BLOAD.md) , [BSAVE](BSAVE.md)
* _DEFLATE$ , _INFLATE$

```vb
fh = FREEFILE
OPEN fileSpec$ FOR OUTPUT AS #fh: CLOSE #fh
OPEN fileSpec$ FOR BINARY AS #fh
PUT #fh, , contents$
CLOSE #fh
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* _READFILE$ , [BLOAD](BLOAD.md) , [BSAVE](BSAVE.md)
* _DEFLATE$ , _INFLATE$

