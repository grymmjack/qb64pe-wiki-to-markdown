# _KEYCLEAR
> _KEYCLEAR clears all keyboard input buffers.

## SYNTAX
`_KEYCLEAR [ buffer& ]`

## PARAMETERS
* buffer& indicates the buffer to be cleared: 1 - Clear the regular keyboard buffer, as used by all input command except the following:  [_KEYHIT](_KEYHIT.md), [_KEYDOWN](_KEYDOWN.md), [INP](INP.md)(&H60.  This is the same as the the emulated BIOS keyboard buffer, so legacy code reading from it via [PEEK](PEEK.md)/[POKE](POKE.md)/[CALL](CALL.md) [ABSOLUTE](ABSOLUTE.md) will also be affected. 2 - Clear the buffer used by [_KEYHIT](_KEYHIT.md). 3 - Clear [INP](INP.md)(&H60) buffer. (see Warning in the the description below)
	* 1 - Clear the regular keyboard buffer, as used by all input command except the following:  [_KEYHIT](_KEYHIT.md), [_KEYDOWN](_KEYDOWN.md), [INP](INP.md)(&H60.  This is the same as the the emulated BIOS keyboard buffer, so legacy code reading from it via [PEEK](PEEK.md)/[POKE](POKE.md)/[CALL](CALL.md) [ABSOLUTE](ABSOLUTE.md) will also be affected.
	* 2 - Clear the buffer used by [_KEYHIT](_KEYHIT.md).
	* 3 - Clear [INP](INP.md)(&H60) buffer. (see Warning in the the description below)
* 1 - Clear the regular keyboard buffer, as used by all input command except the following:  [_KEYHIT](_KEYHIT.md), [_KEYDOWN](_KEYDOWN.md), [INP](INP.md)(&H60.  This is the same as the the emulated BIOS keyboard buffer, so legacy code reading from it via [PEEK](PEEK.md)/[POKE](POKE.md)/[CALL](CALL.md) [ABSOLUTE](ABSOLUTE.md) will also be affected.
* 2 - Clear the buffer used by [_KEYHIT](_KEYHIT.md).
* 3 - Clear [INP](INP.md)(&H60) buffer. (see Warning in the the description below)
* If no parameter is passed, all three buffers are cleared.


## DESCRIPTION
* The [_KEYCLEAR](_KEYCLEAR.md) command clears the specified keyboard input buffer. In effect, it is as if a loop has been used to read from the buffer until it is empty. All keys cleared are lost.
* Warning: The buffer read by [INP](INP.md)(&H60) does not behave as the other buffers do. Whilst reading from the others will eventually empty after reading all data, this buffer will continue to return the last value. For this reason, [_KEYCLEAR](_KEYCLEAR.md) is of little effect, but is included for completeness (an internal flag indicating new data on the port is cleared). However, using [INP](INP.md) for anything is strongly discouraged, and is for backwards compatibility only.
* This command is best used just before getting input, in order to clear stray key presses from commands such as [SLEEP](SLEEP.md), or just random keyboard bashing by the user. The programmer also ought to be aware of key release events in the [_KEYHIT](_KEYHIT.md) buffer; consider the following code:


## EXAMPLES
> Example:

```vb
INPUT "Name: ", name$
_KEYCLEAR
_DELAY 2 'Simulate doing some processing that takes some time.
PRINT _KEYHIT
```


```vb
INPUT "Name: ", name$
_KEYCLEAR
_DELAY 2 'Simulate doing some processing that takes some time.
PRINT _KEYHIT
```

* Featured in our "Keyword of the Day" series
* [SLEEP](SLEEP.md)
* INKEY$ , [_KEYHIT](_KEYHIT.md)

```vb
INPUT "Name: ", name$
_KEYCLEAR
_DELAY 2 'Simulate doing some processing that takes some time.
PRINT _KEYHIT
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* [SLEEP](SLEEP.md)
* INKEY$ , [_KEYHIT](_KEYHIT.md)

