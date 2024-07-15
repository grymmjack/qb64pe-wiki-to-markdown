# _ALLOWFULLSCREEN
> The _ALLOWFULLSCREEN statement allows setting the behavior of the ALT+ENTER combo.

## SYNTAX
`_ALLOWFULLSCREEN [{_STRETCH|_SQUAREPIXELS|OFF|_ALL}][, {_SMOOTH|OFF|_ALL}]`

## DESCRIPTION
* Calling the statement with no parameters enables all four possible full screen modes (and is the default state when a program is started): both [_STRETCH](_STRETCH.md) ( [_SMOOTH](_SMOOTH.md) and [_OFF](_OFF.md) ) and [_SQUAREPIXELS](_SQUAREPIXELS.md) ( [_SMOOTH](_SMOOTH.md) and [_OFF](_OFF.md) ). Using [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md) [_ALL](_ALL.md) , [_ALL](_ALL.md) has the same effect.
	* Using [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md) [_ALL](_ALL.md) , [_ALL](_ALL.md) has the same effect.
* Using [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md) [_ALL](_ALL.md) , [_ALL](_ALL.md) has the same effect.
* [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md) only affects the behavior of ALT+ENTER. The [_FULLSCREEN](_FULLSCREEN.md) statement is not bound by [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md) 's settings so all modes can be accessed programmatically.
* To limit just the mode but allow both [_SMOOTH](_SMOOTH.md) + [_OFF](_OFF.md) antialiasing modes, pass just the first parameter: Example: [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md) [_SQUAREPIXELS](_SQUAREPIXELS.md)
* To allow multiple modes with [_SMOOTH](_SMOOTH.md) or [_OFF](_OFF.md) as default, pass just the second parameter. Example: [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md) , [_SMOOTH](_SMOOTH.md)
* Any possible permutation of the parameters is allowed.
* With [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md) [_OFF](_OFF.md) you can trap Alt+Enter manually in your program and reassign it. See example 2 below.


## EXAMPLES
> Example 1: Allowing only one fullscreen mode with square pixels and no antialiasing:

```vb
_ALLOWFULLSCREEN _SQUAREPIXELS , OFF
```

> Example 2: Disabling _FULLSCREEN with Alt+ENTER so the combo can be manually trapped:

```vb
_ALLOWFULLSCREEN _SQUAREPIXELS , OFF
```


```vb
_ALLOWFULLSCREEN _SQUAREPIXELS , OFF
```

* [_FULLSCREEN](_FULLSCREEN.md) , [_SMOOTH](_SMOOTH.md) (function)

```vb
_ALLOWFULLSCREEN _SQUAREPIXELS , OFF
```



# SEE ALSO
* [_FULLSCREEN](_FULLSCREEN.md) , [_SMOOTH](_SMOOTH.md) (function)

