# KEY LIST
> The KEY n statement is used to assign a "soft key" string or a flag and scan code to a function key or display function soft key assignments.

## SYNTAX
`KEY n% , textString$`

## EXAMPLES
> Example 1: Shows a list of all the string assignments to the function keys F1-F12 (Prints help every time F1 is pressed in the input)

```vb
KEY 1, "Help" 'returns the string "Help" to INPUT variable when F1 is pressed
```

> Example 2: Trapping the Control + key combination. Use the Control Keyboard flag 4 and + key scancode 13.

```vb
KEY 1, "Help" 'returns the string "Help" to INPUT variable when F1 is pressed
```

> Example 3: Differentiating the extended cursor keypad arrows from the predefined Number Pad arrow keys.

```vb
KEY 1, "Help" 'returns the string "Help" to INPUT variable when F1 is pressed
```


```vb
KEY 1, "Help" 'returns the string "Help" to INPUT variable when F1 is pressed
```

> ( Return to Table of Contents )

```vb
KEY 1, "Help" 'returns the string "Help" to INPUT variable when F1 is pressed
```


```vb
KEY 1, "Help" 'returns the string "Help" to INPUT variable when F1 is pressed
```

* [KEY](KEY.md) [LIST](LIST.md) , [ON](ON.md) [KEY](KEY.md)(n)
* [KEY](KEY.md)(n) , INKEY$
* [_KEYHIT](_KEYHIT.md) , [_KEYDOWN](_KEYDOWN.md)
* Keyboard scancodes

```vb
KEY 1, "Help" 'returns the string "Help" to INPUT variable when F1 is pressed
```



# SEE ALSO
* [KEY](KEY.md) [LIST](LIST.md) , [ON](ON.md) [KEY](KEY.md)(n)
* [KEY](KEY.md)(n) , INKEY$
* [_KEYHIT](_KEYHIT.md) , [_KEYDOWN](_KEYDOWN.md)
* Keyboard scancodes

