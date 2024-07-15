# _DEFLATE$
> The _DEFLATE$ function compresses a string .

## SYNTAX
`result$ = _DEFLATE$ ( stringToCompress$ )`

## DESCRIPTION
* result$ will contain the compressed version of stringToCompress$ .
* To decompress the resulting string, use _INFLATE$ .


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

* _INFLATE$

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
* _INFLATE$

