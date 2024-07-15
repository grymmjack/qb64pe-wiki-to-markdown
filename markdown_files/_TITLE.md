# _TITLE
> The _TITLE statement provides the program name in the title bar of the program window.

## SYNTAX
`_TITLE text$`

## PARAMETERS
* text$ can be any literal or variable [STRING](STRING.md) or ASCII character value.


## DESCRIPTION
* The title can be changed anywhere in a program procedure.
* The title bar will say "Untitled" if a title is not set.
* Change the title of the $[CONSOLE](CONSOLE.md) windows created using [_CONSOLETITLE](_CONSOLETITLE.md)
* Note: A delay may be required before the title can be set. See [_SCREENEXISTS](_SCREENEXISTS.md) .


## EXAMPLES
> Example 1: How to create the window title bar.

```vb
_TITLE "My New Program"
```

> Example 2: How to find the currently running program module name and current path using a Windows API Library.

```vb
_TITLE "My New Program"
```


```vb
_TITLE "My New Program"
```

* [_TITLE](_TITLE.md)$
* [_ICON](_ICON.md)
* [_DELAY](_DELAY.md)
* ASCII
* [_CONSOLETITLE](_CONSOLETITLE.md)
* [_SCREENEXISTS](_SCREENEXISTS.md)

```vb
_TITLE "My New Program"
```



# SEE ALSO
* [_TITLE](_TITLE.md)$
* [_ICON](_ICON.md)
* [_DELAY](_DELAY.md)
* ASCII
* [_CONSOLETITLE](_CONSOLETITLE.md)
* [_SCREENEXISTS](_SCREENEXISTS.md)

