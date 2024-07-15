# SOUND
> SOUND sets frequency and duration of sounds from the internal PC speaker if the computer has one or the sound card in QB64.

## SYNTAX
`SOUND frequency# , duration# [, volume# ][, panning# ][, waveform& ]`

## DESCRIPTION
* frequency# is any literal or variable value from 37 to 32767, but 0 is allowed for delays. Just like QuickBASIC 4.5 frequencies on or above 20000 produces silence.
	* Just like QuickBASIC 4.5 frequencies on or above 20000 produces silence.
* Just like QuickBASIC 4.5 frequencies on or above 20000 produces silence.
* duration# is any literal or variable number of [TIMER](TIMER.md) ticks with a duration of 1/18th second. 18 = one second.
* Optional parameter volume# should be between 0.0 (muted) to 1.0 (full volume).
* Optional parameter panning# should be between -1.0 (hard left) to 1.0 (hard right). 0.0 being center.
* Optional parameter waveform& can be one of the following: 1 for square waveform 2 for sawtooth waveform 3 for triangle waveform (default) 4 for sine waveform 5 for white noise
	* 1 for square waveform
	* 2 for sawtooth waveform
	* 3 for triangle waveform (default)
	* 4 for sine waveform
	* 5 for white noise
* 1 for square waveform
* 2 for sawtooth waveform
* 3 for triangle waveform (default)
* 4 for sine waveform
* 5 for white noise
* More waveform types may be introduced in the future.
* [PLAY](PLAY.md) can be used for musical sounds.


## EXAMPLES

```vb
The Seven Music Octaves 

        Note     Frequency      Note     Frequency      Note      Frequency
      1* D#1 ...... 39           G3 ....... 196          A#5 ...... 932
         E1 ....... 41           G#3 ...... 208          B5 ....... 988
         F1 ....... 44           A3 ....... 220       6* C6 ....... 1047
         F#1 ...... 46           A#3 ...... 233          C#6 ...... 1109
         G1 ....... 49           B3 ....... 247          D6 ....... 1175
         G#1 ...... 51        4* C4 ....... 262          D#6 ...... 1245
         A1 ....... 55           C#4 ...... 277          E6 ....... 1318
         A#1 ...... 58           D4 ....... 294          F6 ....... 1397
         B1 ....... 62           D#4 ...... 311          F#6 ...... 1480
      2* C2 ....... 65           E4 ....... 330          G6 ....... 1568
         C#2 ...... 69           F4 ....... 349          G# ....... 1661
         D2 ....... 73           F#4 ...... 370          A6 ....... 1760
         D#2 ...... 78           G4 ....... 392          A#6 ...... 1865
         E2 ....... 82           G#4 ...... 415          B6 ....... 1976
         F2 ....... 87           A4 ....... 440       7* C7 ....... 2093
         F#2 ...... 92           A# ....... 466          C#7 ...... 2217
         G2 ....... 98           B4 ....... 494          D7 ....... 2349
         G#2 ...... 104       5* C5 ....... 523          D#7 ...... 2489
         A2 ....... 110          C#5 ...... 554          E7 ....... 2637
         A#2 ...... 117          D5 ....... 587          F7 ....... 2794
         B2 ....... 123          D#5 ...... 622          F#7 ...... 2960
      3* C3 ....... 131          E5 ....... 659          G7 ....... 3136
         C#3 ...... 139          F5 ....... 698          G#7 ...... 3322
         D3 ....... 147          F#5 ...... 740          A7 ....... 3520
         D#3 ...... 156          G5 ....... 784          A#7 ...... 3729
         E3 ....... 165          G#5 ...... 831          B7 ....... 3951
         F3 ....... 175          A5 ....... 880       8* C8 ....... 4186
         F#3 ...... 185
                                # denotes sharp
```

* [PLAY](PLAY.md) , [BEEP](BEEP.md)
* [_SNDOPEN](_SNDOPEN.md)
* [_SNDRAW](_SNDRAW.md)

```vb
The Seven Music Octaves 

        Note     Frequency      Note     Frequency      Note      Frequency
      1* D#1 ...... 39           G3 ....... 196          A#5 ...... 932
         E1 ....... 41           G#3 ...... 208          B5 ....... 988
         F1 ....... 44           A3 ....... 220       6* C6 ....... 1047
         F#1 ...... 46           A#3 ...... 233          C#6 ...... 1109
         G1 ....... 49           B3 ....... 247          D6 ....... 1175
         G#1 ...... 51        4* C4 ....... 262          D#6 ...... 1245
         A1 ....... 55           C#4 ...... 277          E6 ....... 1318
         A#1 ...... 58           D4 ....... 294          F6 ....... 1397
         B1 ....... 62           D#4 ...... 311          F#6 ...... 1480
      2* C2 ....... 65           E4 ....... 330          G6 ....... 1568
         C#2 ...... 69           F4 ....... 349          G# ....... 1661
         D2 ....... 73           F#4 ...... 370          A6 ....... 1760
         D#2 ...... 78           G4 ....... 392          A#6 ...... 1865
         E2 ....... 82           G#4 ...... 415          B6 ....... 1976
         F2 ....... 87           A4 ....... 440       7* C7 ....... 2093
         F#2 ...... 92           A# ....... 466          C#7 ...... 2217
         G2 ....... 98           B4 ....... 494          D7 ....... 2349
         G#2 ...... 104       5* C5 ....... 523          D#7 ...... 2489
         A2 ....... 110          C#5 ...... 554          E7 ....... 2637
         A#2 ...... 117          D5 ....... 587          F7 ....... 2794
         B2 ....... 123          D#5 ...... 622          F#7 ...... 2960
      3* C3 ....... 131          E5 ....... 659          G7 ....... 3136
         C#3 ...... 139          F5 ....... 698          G#7 ...... 3322
         D3 ....... 147          F#5 ...... 740          A7 ....... 3520
         D#3 ...... 156          G5 ....... 784          A#7 ...... 3729
         E3 ....... 165          G#5 ...... 831          B7 ....... 3951
         F3 ....... 175          A5 ....... 880       8* C8 ....... 4186
         F#3 ...... 185
                                # denotes sharp
```



# SEE ALSO
* [PLAY](PLAY.md) , [BEEP](BEEP.md)
* [_SNDOPEN](_SNDOPEN.md)
* [_SNDRAW](_SNDRAW.md)

