# _SNDOPEN
> The _SNDOPEN function loads a sound file into memory and returns a LONG handle value above 0.

## SYNTAX
`soundHandle& = _SNDOPEN ( fileName$ [, capabilities$ ])`

## DESCRIPTION
* Returns a [LONG](LONG.md) soundHandle& value to the sound file in memory. A value of zero means the sound could not be loaded.
* The literal or variable [STRING](STRING.md) sound fileName$ can be WAV, AIFF, AIFC, FLAC, OGG, MP3, MID, IT, XM, S3M, [MOD](MOD.md), RAD (v1 & v2), AHX, HVL & QOA file types. MID support is enabled via the $MIDISOUNDFONT metacommand.
	* MID support is enabled via the $MIDISOUNDFONT metacommand.
* MID support is enabled via the $MIDISOUNDFONT metacommand.
* The literal or variable [STRING](STRING.md) capabilities$ is optional but can be one of the following. Anything else is ignored. Multiple capability strings can be specified separated by a comma. STREAM : This will "stream" the sound into memory rather than fully decoding it. MEMORY : This will treat fileName$ as a memory buffer containing the sound file instead of a file name.
	* STREAM : This will "stream" the sound into memory rather than fully decoding it.
	* MEMORY : This will treat fileName$ as a memory buffer containing the sound file instead of a file name.
* STREAM : This will "stream" the sound into memory rather than fully decoding it.
* MEMORY : This will treat fileName$ as a memory buffer containing the sound file instead of a file name.
* Short sounds should not be loaded using STREAM . Use STREAM when you want to play long sounds as background music and want to avoid loading delays.
* [_MEMSOUND](_MEMSOUND.md) will not work for sounds loaded using STREAM or MEMORY .
* Always check the handle value returned is greater than zero before attempting to play the sound.
* The handle can be used by most of the _SND sound playing functions and statements in QB64 except [_SNDPLAYFILE](_SNDPLAYFILE.md) which plays a sound file directly from the disk and does not use a handle value.
* Handles can be closed with [_SNDCLOSE](_SNDCLOSE.md) when the sound is no longer necessary.
* If a WAV sound file won't play, try it using the Windows Play WAV sounds library to check it or convert the sound file to FLAC, OGG or MP3.


## EXAMPLES
> Snippet 1: Loading a sound file to use in the program later. Only load it once and use the handle any time you want.

```vb
h& = _SNDOPEN("dog.wav")
IF h& <= 0 THEN BEEP ELSE _SNDPLAY h&      'check for valid handle before using!
```

> Snippet 2: Playing a sound from 2 different speakers based on program results.

```vb
h& = _SNDOPEN("dog.wav")
IF h& <= 0 THEN BEEP ELSE _SNDPLAY h&      'check for valid handle before using!
```

> Snippet 3: Loading a sound file from memory and then playing it.

```vb
h& = _SNDOPEN("dog.wav")
IF h& <= 0 THEN BEEP ELSE _SNDPLAY h&      'check for valid handle before using!
```


```vb
h& = _SNDOPEN("dog.wav")
IF h& <= 0 THEN BEEP ELSE _SNDPLAY h&      'check for valid handle before using!
```

* [_SNDCLOSE](_SNDCLOSE.md) , [_SNDPLAY](_SNDPLAY.md) , [_SNDSTOP](_SNDSTOP.md)
* [_SNDPAUSE](_SNDPAUSE.md) , [_SNDLOOP](_SNDLOOP.md) , [_SNDLIMIT](_SNDLIMIT.md)
* [_SNDSETPOS](_SNDSETPOS.md) , [_SNDGETPOS](_SNDGETPOS.md)
* [_SNDPLAYING](_SNDPLAYING.md) , [_SNDPAUSED](_SNDPAUSED.md)
* [_SNDCOPY](_SNDCOPY.md) , [_SNDPLAYCOPY](_SNDPLAYCOPY.md)
* [_SNDBAL](_SNDBAL.md) , [_SNDLEN](_SNDLEN.md) , [_SNDVOL](_SNDVOL.md)
* [_SNDPLAYFILE](_SNDPLAYFILE.md)
* [_SNDRAW](_SNDRAW.md) , [_SNDRATE](_SNDRATE.md) , [_SNDRAWLEN](_SNDRAWLEN.md)

```vb
h& = _SNDOPEN("dog.wav")
IF h& <= 0 THEN BEEP ELSE _SNDPLAY h&      'check for valid handle before using!
```



# SEE ALSO
* [_SNDCLOSE](_SNDCLOSE.md) , [_SNDPLAY](_SNDPLAY.md) , [_SNDSTOP](_SNDSTOP.md)
* [_SNDPAUSE](_SNDPAUSE.md) , [_SNDLOOP](_SNDLOOP.md) , [_SNDLIMIT](_SNDLIMIT.md)
* [_SNDSETPOS](_SNDSETPOS.md) , [_SNDGETPOS](_SNDGETPOS.md)
* [_SNDPLAYING](_SNDPLAYING.md) , [_SNDPAUSED](_SNDPAUSED.md)
* [_SNDCOPY](_SNDCOPY.md) , [_SNDPLAYCOPY](_SNDPLAYCOPY.md)
* [_SNDBAL](_SNDBAL.md) , [_SNDLEN](_SNDLEN.md) , [_SNDVOL](_SNDVOL.md)
* [_SNDPLAYFILE](_SNDPLAYFILE.md)
* [_SNDRAW](_SNDRAW.md) , [_SNDRATE](_SNDRATE.md) , [_SNDRAWLEN](_SNDRAWLEN.md)

