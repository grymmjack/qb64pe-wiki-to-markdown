# _INFLATE$
> The _INFLATE$ function decompresses a string compressed by the _DEFLATE$ function.

## SYNTAX
`result$ = _INFLATE$ ( stringToDecompress$[, originalSize&] )`

## DESCRIPTION
* result$ will contain the original version of stringToDecompress$ .
* Optional parameter originalSize& can be used if the original size of the uncompressed data is known beforehand, which makes the decompression routine run more efficiently. If unspecified, decompression still works as expected, but may use more steps and need to allocate more memory internally.
	* If unspecified, decompression still works as expected, but may use more steps and need to allocate more memory internally.
* If unspecified, decompression still works as expected, but may use more steps and need to allocate more memory internally.


## EXAMPLES
> Example 1: Compressing a long string of text.

```vb
a$ = "The quick brown fox jumps over the lazy dog. "
PRINT "Original string (a$): "; a$
FOR i = 1 TO 15
   a$ = a$ + a$
NEXT

PRINT "After concatenating it into itself several times, LEN(a$) ="; LEN(a$)

b$ = _DEFLATE$(a$)
PRINT "After using _DEFLATE$ to compress it, LEN ="; LEN(b$)
PRINT USING "(compressed size is #.###% of the original)"; ((LEN(b$) * 100) / LEN(a$))
c$ = _INFLATE$(b$)
PRINT "After using _INFLATE$ to decompress it, LEN ="; LEN(c$)
```


```vb
a$ = "The quick brown fox jumps over the lazy dog. "
PRINT "Original string (a$): "; a$
FOR i = 1 TO 15
   a$ = a$ + a$
NEXT

PRINT "After concatenating it into itself several times, LEN(a$) ="; LEN(a$)

b$ = _DEFLATE$(a$)
PRINT "After using _DEFLATE$ to compress it, LEN ="; LEN(b$)
PRINT USING "(compressed size is #.###% of the original)"; ((LEN(b$) * 100) / LEN(a$))
c$ = _INFLATE$(b$)
PRINT "After using _INFLATE$ to decompress it, LEN ="; LEN(c$)
```

* _DEFLATE$

```vb
a$ = "The quick brown fox jumps over the lazy dog. "
PRINT "Original string (a$): "; a$
FOR i = 1 TO 15
   a$ = a$ + a$
NEXT

PRINT "After concatenating it into itself several times, LEN(a$) ="; LEN(a$)

b$ = _DEFLATE$(a$)
PRINT "After using _DEFLATE$ to compress it, LEN ="; LEN(b$)
PRINT USING "(compressed size is #.###% of the original)"; ((LEN(b$) * 100) / LEN(a$))
c$ = _INFLATE$(b$)
PRINT "After using _INFLATE$ to decompress it, LEN ="; LEN(c$)
```



# SEE ALSO
* _DEFLATE$

