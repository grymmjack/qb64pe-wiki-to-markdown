


\_SNDRAW - QB64 Phoenix Edition Wiki








# \_SNDRAW



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDRAW statement plays sound wave sample frequencies created by a program.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_SNDRAW *leftSample*[, *rightSample*][, *pipeHandle&*]
  




## Parameters


* The *leftSample* and *rightSample* value(s) can be any [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") literal or variable frequency value from -1.0 to 1.0.
* The *pipeHandle&* parameter refers to the sound pipe opened using [\_SNDOPENRAW](/qb64wiki/index.php/SNDOPENRAW "SNDOPENRAW").


  




## Description


* Specifying *pipeHandle&* allows sound to be played through two or more channels at the same time (**version 1.000 and up**).
* If only *leftSample* value is used, the sound will come out of both speakers.
* Using \_SNDRAW will pause any currently playing music.
* \_SNDRAW is designed for continuous play. It will not produce any sound until a significant number of samples have been queued. No sound is played if only a few samples are queued.
* Ensure that [\_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN") is comfortably above 0 (until you've actually finished playing sound). If you are getting occasional unintended random clicks, this generally means that [\_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN") has dropped to 0.
* \_SNDRAW is not intended to queue up many minutes worth of sound. It will probably work but will chew up a lot of memory (and if it gets swapped to disk, your sound could be interrupted abruptly).
* [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE") determines how many samples are played per second, but timing is done by the sound card, not your program.
* **Do not attempt to use [\_TIMER](/qb64wiki/index.php/TIMER "TIMER") or [\_DELAY](/qb64wiki/index.php/DELAY "DELAY") or [\_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") to control the timing of \_SNDRAW. You may use them for delays or to limit your program's CPU usage, but how much to queue should only be based on the [\_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN").**


  




## Examples


*Example 1:* Sound using a sine wave with \_SNDRAW Amplitude \* SIN(8 \* ATN(1) \* Duration \* (Frequency / \_SNDRATE))





| ``` FREQ = 400                             'any frequency desired from 36 to 10,000 Pi2 = 8 * [ATN](/qb64wiki/index.php/ATN "ATN")(1)                       '2 * pi Amplitude = .3                         'amplitude of the signal from -1.0 to 1.0 SampleRate = [_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE")                  'sets the sample rate FRate = FREQ / SampleRate' [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") Duration = 0 [TO](/qb64wiki/index.php/TO "TO") 5 * SampleRate     'play 5 seconds         _SNDRAW Amplitude * [SIN](/qb64wiki/index.php/SIN "SIN")(Pi2 * Duration * FRate)            'sine wave        '_SNDRAW Amplitude * [SGN](/qb64wiki/index.php/SGN "SGN")([SIN](/qb64wiki/index.php/SIN "SIN")(Pi2 * Duration * FRate))       'square wave [NEXT](/qb64wiki/index.php/NEXT "NEXT") [_SNDRAWDONE](/qb64wiki/index.php/SNDRAWDONE "SNDRAWDONE") [DO](/qb64wiki/index.php/DO "DO"): LOOP [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN") [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by DarthWho
*Explanation:* The loop Duration is determined by the number of seconds times the [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE") number of samples per second. Square waves can use the same formula with Amplitude \* [SGN](/qb64wiki/index.php/SGN "SGN")(SIN(8 \* ATN(1) \* Duration \* (Frequency/\_SNDRATE))).
  

*Example 2:* A simple ringing bell tone that tapers off.





| ``` t = 0 tmp$ = "Sample = ##.#####   Time = ##.#####" LOCATE 1, 60: PRINT "Rate:"; [_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE") DO   'queue some sound   DO WHILE [_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN") < 0.2             'you may wish to adjust this     sample = [SIN](/qb64wiki/index.php/SIN "SIN")(t * 440 * [ATN](/qb64wiki/index.php/ATN "ATN")(1) * 8)  '440Hz sine wave (t * 440 * 2π)     sample = sample * [EXP](/qb64wiki/index.php/EXP "EXP")(-t * 3)       'fade out eliminates clicks after sound     _SNDRAW sample     t = t + 1 / [_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE")                'sound card sample frequency determines time   LOOP    'do other stuff, but it may interrupt sound   LOCATE 1, 1: PRINT USING tmp$; sample; t LOOP WHILE t < 3.0                      'play for 3 seconds  [_SNDRAWDONE](/qb64wiki/index.php/SNDRAWDONE "SNDRAWDONE") DO WHILE [_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN") > 0                 'Finish any left over queued sound! LOOP [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Artelius
  

*Example 3:* Routine uses \_SNDRAW to display and play 12 notes from octaves 1 through 9.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") rate& rate& = [_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE") DO   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Enter the octave 1 to 8 (0 quits!):";   oct% = [VAL](/qb64wiki/index.php/VAL "VAL")([INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1)): [PRINT](/qb64wiki/index.php/PRINT "PRINT") oct%   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") oct% = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   octave = oct% - 4 '440 is in the 4th octave, 9th note   [COLOR](/qb64wiki/index.php/COLOR "COLOR") oct% + 1   [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") "Octave: ##"; oct%   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") Note = 0 [TO](/qb64wiki/index.php/TO "TO") 11  'notes C to B     fq = FreQ(octave, Note, note$)     [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") "#####.## \\"; fq, note$     PlaySound fq     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") > "" [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   [NEXT](/qb64wiki/index.php/NEXT "NEXT") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") FreQ (octave, note, note$) FreQ = 440 * 2 ^ (octave + (note + 3) / 12 - 1) '* 12 note octave starts at C (3 notes up) note$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")("C C#D D#E F F#G G#A A#B ", note * 2 + 1, 2) [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  [SUB](/qb64wiki/index.php/SUB "SUB") PlaySound (frq!)    ' plays sine wave fading in and out SndLoop! = 0 [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") SndLoop! < rate&   _SNDRAW [SIN](/qb64wiki/index.php/SIN "SIN")((2 * 4 * [ATN](/qb64wiki/index.php/ATN "ATN")(1) * SndLoop! / rate&) * frq!) * [EXP](/qb64wiki/index.php/EXP "EXP")(-(SndLoop! / rate&) * 3)   SndLoop! = SndLoop! + 1 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [_SNDRAWDONE](/qb64wiki/index.php/SNDRAWDONE "SNDRAWDONE") [DO](/qb64wiki/index.php/DO "DO"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN")   'flush the sound playing buffer [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by CodeGuy
  




## See also


* [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE"), [\_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN")
* [\_SNDOPENRAW](/qb64wiki/index.php/SNDOPENRAW "SNDOPENRAW"), [\_SNDRAWDONE](/qb64wiki/index.php/SNDRAWDONE "SNDRAWDONE")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")
* [PLAY](/qb64wiki/index.php/PLAY "PLAY"), [BEEP](/qb64wiki/index.php/BEEP "BEEP")
* [DTMF Phone Demo](/qb64wiki/index.php/DTMF_Phone_Demo "DTMF Phone Demo")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDRAW&oldid=8786>"




## Navigation menu








### Search





















