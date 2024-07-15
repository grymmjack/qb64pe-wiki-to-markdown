# _SNDRAW
> The _SNDRAW statement plays sound wave sample frequencies created by a program.

## SYNTAX
`_SNDRAW leftSample [, rightSample ][, pipeHandle& ]`

## PARAMETERS
* The leftSample and rightSample value(s) can be any [SINGLE](SINGLE.md) or [DOUBLE](DOUBLE.md) literal or variable frequency value from -1.0 to 1.0.
* The pipeHandle& parameter refers to the sound pipe opened using [_SNDOPENRAW](_SNDOPENRAW.md) .


## DESCRIPTION
* Specifying pipeHandle& allows sound to be played through two or more channels at the same time ( version 1.000 and up ).
* If only leftSample value is used, the sound will come out of both speakers.
* Using [_SNDRAW](_SNDRAW.md) will pause any currently playing music.
* [_SNDRAW](_SNDRAW.md) is designed for continuous play. It will not produce any sound until a significant number of samples have been queued. No sound is played if only a few samples are queued.
* Ensure that [_SNDRAWLEN](_SNDRAWLEN.md) is comfortably above 0 (until you've actually finished playing sound). If you are getting occasional unintended random clicks, this generally means that [_SNDRAWLEN](_SNDRAWLEN.md) has dropped to 0.
* [_SNDRAW](_SNDRAW.md) is not intended to queue up many minutes worth of sound. It will probably work but will chew up a lot of memory (and if it gets swapped to disk, your sound could be interrupted abruptly).
* [_SNDRATE](_SNDRATE.md) determines how many samples are played per second, but timing is done by the sound card, not your program.
* Do not attempt to use _TIMER or [_DELAY](_DELAY.md) or [_LIMIT](_LIMIT.md) to control the timing of [_SNDRAW](_SNDRAW.md). You may use them for delays or to limit your program's CPU usage, but how much to queue should only be based on the [_SNDRAWLEN](_SNDRAWLEN.md) .


## EXAMPLES
> Example 1: Sound using a sine wave with _SNDRAW Amplitude * SIN(8 * ATN(1) * Duration * (Frequency / _SNDRATE))

```vb
FREQ = 400                             'any frequency desired from 36 to 10,000
Pi2 = 8 * ATN(1)                       '2 * pi
Amplitude = .3                         'amplitude of the signal from -1.0 to 1.0
SampleRate = _SNDRATE                  'sets the sample rate
FRate = FREQ / SampleRate'
FOR Duration = 0 TO 5 * SampleRate     'play 5 seconds
       _SNDRAW Amplitude * SIN(Pi2 * Duration * FRate)            'sine wave
      '_SNDRAW Amplitude * SGN(SIN(Pi2 * Duration * FRate))       'square wave
NEXT
_SNDRAWDONE
DO: LOOP WHILE _SNDRAWLEN
END
```

> Example 2: A simple ringing bell tone that tapers off.

```vb
FREQ = 400                             'any frequency desired from 36 to 10,000
Pi2 = 8 * ATN(1)                       '2 * pi
Amplitude = .3                         'amplitude of the signal from -1.0 to 1.0
SampleRate = _SNDRATE                  'sets the sample rate
FRate = FREQ / SampleRate'
FOR Duration = 0 TO 5 * SampleRate     'play 5 seconds
       _SNDRAW Amplitude * SIN(Pi2 * Duration * FRate)            'sine wave
      '_SNDRAW Amplitude * SGN(SIN(Pi2 * Duration * FRate))       'square wave
NEXT
_SNDRAWDONE
DO: LOOP WHILE _SNDRAWLEN
END
```

> Example 3: Routine uses _SNDRAW to display and play 12 notes from octaves 1 through 9.

```vb
FREQ = 400                             'any frequency desired from 36 to 10,000
Pi2 = 8 * ATN(1)                       '2 * pi
Amplitude = .3                         'amplitude of the signal from -1.0 to 1.0
SampleRate = _SNDRATE                  'sets the sample rate
FRate = FREQ / SampleRate'
FOR Duration = 0 TO 5 * SampleRate     'play 5 seconds
       _SNDRAW Amplitude * SIN(Pi2 * Duration * FRate)            'sine wave
      '_SNDRAW Amplitude * SGN(SIN(Pi2 * Duration * FRate))       'square wave
NEXT
_SNDRAWDONE
DO: LOOP WHILE _SNDRAWLEN
END
```


```vb
FREQ = 400                             'any frequency desired from 36 to 10,000
Pi2 = 8 * ATN(1)                       '2 * pi
Amplitude = .3                         'amplitude of the signal from -1.0 to 1.0
SampleRate = _SNDRATE                  'sets the sample rate
FRate = FREQ / SampleRate'
FOR Duration = 0 TO 5 * SampleRate     'play 5 seconds
       _SNDRAW Amplitude * SIN(Pi2 * Duration * FRate)            'sine wave
      '_SNDRAW Amplitude * SGN(SIN(Pi2 * Duration * FRate))       'square wave
NEXT
_SNDRAWDONE
DO: LOOP WHILE _SNDRAWLEN
END
```

* [_SNDRATE](_SNDRATE.md) , [_SNDRAWLEN](_SNDRAWLEN.md)
* [_SNDOPENRAW](_SNDOPENRAW.md) , [_SNDRAWDONE](_SNDRAWDONE.md)
* [_SNDOPEN](_SNDOPEN.md)
* [PLAY](PLAY.md) , [BEEP](BEEP.md)
* DTMF Phone Demo

```vb
FREQ = 400                             'any frequency desired from 36 to 10,000
Pi2 = 8 * ATN(1)                       '2 * pi
Amplitude = .3                         'amplitude of the signal from -1.0 to 1.0
SampleRate = _SNDRATE                  'sets the sample rate
FRate = FREQ / SampleRate'
FOR Duration = 0 TO 5 * SampleRate     'play 5 seconds
       _SNDRAW Amplitude * SIN(Pi2 * Duration * FRate)            'sine wave
      '_SNDRAW Amplitude * SGN(SIN(Pi2 * Duration * FRate))       'square wave
NEXT
_SNDRAWDONE
DO: LOOP WHILE _SNDRAWLEN
END
```



# SEE ALSO
* [_SNDRATE](_SNDRATE.md) , [_SNDRAWLEN](_SNDRAWLEN.md)
* [_SNDOPENRAW](_SNDOPENRAW.md) , [_SNDRAWDONE](_SNDRAWDONE.md)
* [_SNDOPEN](_SNDOPEN.md)
* [PLAY](PLAY.md) , [BEEP](BEEP.md)
* DTMF Phone Demo

