# _READFILE$
> The _READFILE$ function returns the complete contents of a file in a single string, but without the usual overhead. It does OPEN , GET and CLOSE the file in one run.

## SYNTAX
`contents$ = _READFILE$ ( fileSpec$ )`

## PARAMETERS
* contents$ is the entire file contents returned as [STRING](STRING.md) . May return an empty string, if the specified file was empty, or if the program was continued from a file related [ERROR](ERROR.md) .
* fileSpec$ is the name of the file to read as literal or variable [STRING](STRING.md) , if required inclusive a full or relative path. To avoid errors you should use [_FILEEXISTS](_FILEEXISTS.md) before calling this function to make sure the file exists.
	* To avoid errors you should use [_FILEEXISTS](_FILEEXISTS.md) before calling this function to make sure the file exists.
* To avoid errors you should use [_FILEEXISTS](_FILEEXISTS.md) before calling this function to make sure the file exists.


## DESCRIPTION
* Sometimes it's required or at least useful to have the whole contents of a file in a single string for further processing, e.g. to pass it to hashing or compression functions which expect strings.
* In earlier versions of QB64(PE) you had to implement that loading process manually all the time or create a reusable custom [FUNCTION](FUNCTION.md) for it.
* Now _READFILE$ will simplify this, it's mainly a convenience function to wrap the following code sequence into one handy function:


## EXAMPLES

```vb
fh = FREEFILE
OPEN fileSpec$ FOR BINARY AS #fh
contents$ = SPACE$(LOF(fh))
GET #fh, , contents$
CLOSE #fh
```

* Featured in our "Keyword of the Day" series
* [_WRITEFILE](_WRITEFILE.md) , [BLOAD](BLOAD.md) , [BSAVE](BSAVE.md)
* _DEFLATE$ , _INFLATE$
* [_ADLER32](_ADLER32.md) , [_CRC32](_CRC32.md) , _MD5$

```vb
fh = FREEFILE
OPEN fileSpec$ FOR BINARY AS #fh
contents$ = SPACE$(LOF(fh))
GET #fh, , contents$
CLOSE #fh
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* [_WRITEFILE](_WRITEFILE.md) , [BLOAD](BLOAD.md) , [BSAVE](BSAVE.md)
* _DEFLATE$ , _INFLATE$
* [_ADLER32](_ADLER32.md) , [_CRC32](_CRC32.md) , _MD5$

