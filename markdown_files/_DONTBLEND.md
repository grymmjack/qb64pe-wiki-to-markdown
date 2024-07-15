# _DONTBLEND
> The _DONTBLEND statement turns off 32 bit alpha blending for the current image or screen mode where _BLEND is default.

## SYNTAX
`_DONTBLEND [ imageHandle& ]`

## PARAMETERS
* If imageHandle& is omitted, it is assumed to be the current _DESTination write page.


## DESCRIPTION
* If imageHandle& is not valid, an Invalid handle error will occur.
* [_DONTBLEND](_DONTBLEND.md) is faster than the default [_BLEND](_BLEND.md) . You may want to disable it , unless you really need to use it in 32 bit.
* 32 bit screen surface backgrounds (black) have zero [_ALPHA](_ALPHA.md) so that they are transparent when placed over other surfaces.
* Use [CLS](CLS.md) to make a new surface background [_ALPHA](_ALPHA.md) 255 or opaque.
* Both [_SOURCE](_SOURCE.md) and [_DEST](_DEST.md) must have [_BLEND](_BLEND.md) enabled, or else colors will [NOT](NOT.md) blend.


## EXAMPLES
> Example 1: Use _DONTBLEND when you want the 32 bit screen surface to be opaque so that it covers up other backgrounds. CLS works too.

```vb
SCREEN _NEWIMAGE(1280, 720, 32)
'CLS
_DONTBLEND '<<< comment out to see the difference

LINE (100, 100)-(500, 500), _RGB32(255, 255, 0), BF

b& = SaveBackground&

PRINT "This is just test junk"
PRINT
PRINT "Hit any key and the text should disappear, leaving us our pretty yellow box."
SLEEP
RestoreBackground b&

END

FUNCTION SaveBackground&
   SaveBackground& = _COPYIMAGE(0)
END FUNCTION

SUB RestoreBackground (Image AS LONG)
   _PUTIMAGE , Image, 0
END SUB
```

> Example 2: Turning off blending to create transparency.

```vb
SCREEN _NEWIMAGE(1280, 720, 32)
'CLS
_DONTBLEND '<<< comment out to see the difference

LINE (100, 100)-(500, 500), _RGB32(255, 255, 0), BF

b& = SaveBackground&

PRINT "This is just test junk"
PRINT
PRINT "Hit any key and the text should disappear, leaving us our pretty yellow box."
SLEEP
RestoreBackground b&

END

FUNCTION SaveBackground&
   SaveBackground& = _COPYIMAGE(0)
END FUNCTION

SUB RestoreBackground (Image AS LONG)
   _PUTIMAGE , Image, 0
END SUB
```

> Explanation: To make the alpha image, turn alpha blending off. Otherwise PSET blends the pixel to instead of making the sprite transparent.

```vb
SCREEN _NEWIMAGE(1280, 720, 32)
'CLS
_DONTBLEND '<<< comment out to see the difference

LINE (100, 100)-(500, 500), _RGB32(255, 255, 0), BF

b& = SaveBackground&

PRINT "This is just test junk"
PRINT
PRINT "Hit any key and the text should disappear, leaving us our pretty yellow box."
SLEEP
RestoreBackground b&

END

FUNCTION SaveBackground&
   SaveBackground& = _COPYIMAGE(0)
END FUNCTION

SUB RestoreBackground (Image AS LONG)
   _PUTIMAGE , Image, 0
END SUB
```


```vb
SCREEN _NEWIMAGE(1280, 720, 32)
'CLS
_DONTBLEND '<<< comment out to see the difference

LINE (100, 100)-(500, 500), _RGB32(255, 255, 0), BF

b& = SaveBackground&

PRINT "This is just test junk"
PRINT
PRINT "Hit any key and the text should disappear, leaving us our pretty yellow box."
SLEEP
RestoreBackground b&

END

FUNCTION SaveBackground&
   SaveBackground& = _COPYIMAGE(0)
END FUNCTION

SUB RestoreBackground (Image AS LONG)
   _PUTIMAGE , Image, 0
END SUB
```

* [_BLEND](_BLEND.md)
* [_BLEND](_BLEND.md) (function)
* Images

```vb
SCREEN _NEWIMAGE(1280, 720, 32)
'CLS
_DONTBLEND '<<< comment out to see the difference

LINE (100, 100)-(500, 500), _RGB32(255, 255, 0), BF

b& = SaveBackground&

PRINT "This is just test junk"
PRINT
PRINT "Hit any key and the text should disappear, leaving us our pretty yellow box."
SLEEP
RestoreBackground b&

END

FUNCTION SaveBackground&
   SaveBackground& = _COPYIMAGE(0)
END FUNCTION

SUB RestoreBackground (Image AS LONG)
   _PUTIMAGE , Image, 0
END SUB
```



# SEE ALSO
* [_BLEND](_BLEND.md)
* [_BLEND](_BLEND.md) (function)
* Images

