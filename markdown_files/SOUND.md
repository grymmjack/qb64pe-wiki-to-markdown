


SOUND - QB64 Phoenix Edition Wiki








# SOUND



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**SOUND** sets frequency and duration of sounds from the internal PC speaker if the computer has one or the sound card in QB64.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 Errors](#Errors) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


SOUND *frequency#*, *duration#*[, *volume#*][, *panning#*][, *waveform&*]
  




## Description


* *frequency#* is any literal or variable value from 37 to 32767, but 0 is allowed for delays.
	+ Just like QuickBASIC 4.5 frequencies on or above 20000 produces silence.
* *duration#* is any literal or variable number of [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") ticks with a duration of 1/18th second. 18 = one second.
* Optional parameter *volume#* should be between 0.0 (muted) to 1.0 (full volume).
* Optional parameter *panning#* should be between -1.0 (hard left) to 1.0 (hard right). 0.0 being center.
* Optional parameter *waveform&* can be one of the following:
	+ **1** for square waveform
	+ **2** for sawtooth waveform
	+ **3** for triangle waveform (default)
	+ **4** for sine waveform
	+ **5** for white noise
* More waveform types may be introduced in the future.
* [PLAY](/qb64wiki/index.php/PLAY "PLAY") can be used for musical sounds.


Note
The last volume, panning and waveform settings will apply to subsequent calls to **SOUND** (when used without the optional parameters) and [PLAY](/qb64wiki/index.php/PLAY "PLAY").
### Errors


* Low *frequency#* values between 0 and 37 will create an [Illegal Function call error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes").
* Out of range values for *volume#*, *panning#* and *waveform&* will create an [Illegal Function call error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes").
* All audio related statements and functions work even if the program is not in focus. However, depending on the operating system and environment, this may not always be the case.
* **SOUND** may have clicks or pauses between the sounds generated.


Note
**SOUND** 0, 0 will not stop previous **QB64** sounds like it did in QBasic!


---


  






| ```          **The Seven Music Octaves**            **Note     Frequency      Note     Frequency      Note      Frequency**        **1*** D#1 ...... 39           G3 ....... 196          A#5 ...... 932           E1 ....... 41           G#3 ...... 208          B5 ....... 988           F1 ....... 44           A3 ....... 220       **6*** C6 ....... 1047           F#1 ...... 46           A#3 ...... 233          C#6 ...... 1109           G1 ....... 49           B3 ....... 247          D6 ....... 1175           G#1 ...... 51        **4*** C4 ....... 262          D#6 ...... 1245           A1 ....... 55           C#4 ...... 277          E6 ....... 1318           A#1 ...... 58           D4 ....... 294          F6 ....... 1397           B1 ....... 62           D#4 ...... 311          F#6 ...... 1480        **2*** C2 ....... 65           E4 ....... 330          G6 ....... 1568           C#2 ...... 69           F4 ....... 349          G# ....... 1661           D2 ....... 73           F#4 ...... 370          A6 ....... 1760           D#2 ...... 78           G4 ....... 392          A#6 ...... 1865           E2 ....... 82           G#4 ...... 415          B6 ....... 1976           F2 ....... 87           A4 ....... 440       **7*** C7 ....... 2093           F#2 ...... 92           A# ....... 466          C#7 ...... 2217           G2 ....... 98           B4 ....... 494          D7 ....... 2349           G#2 ...... 104       **5*** C5 ....... 523          D#7 ...... 2489           A2 ....... 110          C#5 ...... 554          E7 ....... 2637           A#2 ...... 117          D5 ....... 587          F7 ....... 2794           B2 ....... 123          D#5 ...... 622          F#7 ...... 2960        **3*** C3 ....... 131          E5 ....... 659          G7 ....... 3136           C#3 ...... 139          F5 ....... 698          G#7 ...... 3322           D3 ....... 147          F#5 ...... 740          A7 ....... 3520           D#3 ...... 156          G5 ....... 784          A#7 ...... 3729           E3 ....... 165          G#5 ...... 831          B7 ....... 3951           F3 ....... 175          A5 ....... 880       **8*** C8 ....... 4186           F#3 ...... 185                                  **# denotes sharp**  ``` |
| --- |


  




## Availability


* [![v0.610](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v0.610")

**v0.610**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* Support for *volume#*, *panning#*, *waveform&* was added in **QB64-PE v3.8.0**.


  




## Examples


Example 1
Playing the seven octaves based on the base note DATA \* 2 ^ (octave - 1).


| ``` notes$ = "C C#D D#E F F#G G#A A#B " [COLOR](/qb64wiki/index.php/COLOR "COLOR") 9: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 5, 20: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Select an octave (1 - 7) to play (8 quits):" [DO](/qb64wiki/index.php/DO "DO")     [DO](/qb64wiki/index.php/DO "DO"): octa$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")         [IF](/qb64wiki/index.php/IF "IF") octa$ <> "" [THEN](/qb64wiki/index.php/THEN "THEN")             [IF](/qb64wiki/index.php/IF "IF") [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(octa$) > 48 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(octa$) < 58 [THEN](/qb64wiki/index.php/THEN "THEN") octave% = [VAL](/qb64wiki/index.php/VAL "VAL")(octa$): [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")         [END IF](/qb64wiki/index.php/END_IF "END IF")     [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") octave% > 7     [IF](/qb64wiki/index.php/IF "IF") octave% > 0 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") octave% < 8 [THEN](/qb64wiki/index.php/THEN "THEN")         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 15, 6: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(70)         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 16, 6: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(70)         [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 15, 6: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Octave"; octave%; ":";         [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") Octaves         [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") 12             [READ](/qb64wiki/index.php/READ "READ") note!             snd% = [CINT](/qb64wiki/index.php/CINT "CINT")(note! * (2 ^ (octave% - 1))) 'calculate note frequency             [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STR$](/qb64wiki/index.php/STR$ "STR$")(snd%);             c0l = [POS](/qb64wiki/index.php/POS "POS")(0)             [COLOR](/qb64wiki/index.php/COLOR "COLOR") 11: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 16, c0l - 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(notes$, 1 + (2 * (i - 1)), 2)             [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 15, c0l             [IF](/qb64wiki/index.php/IF "IF") snd% > 36 [THEN](/qb64wiki/index.php/THEN "THEN") SOUND snd%, 12 'error if sound value is < 36             [_DELAY](/qb64wiki/index.php/DELAY "DELAY") .8         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") octave% > 7 [END](/qb64wiki/index.php/END "END")  Octaves: [DATA](/qb64wiki/index.php/DATA "DATA") 32.7,34.65,36.71,38.9,41.2,43.65,46.25,49,51.91,55,58.27,61.74  ``` |
| --- |


Code adapted by Ted Weissgerber


---


Example 2
Playing a song called "Bonnie" with **SOUND** frequencies.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") [OUT](/qb64wiki/index.php/OUT "OUT") &H3C8, 0: [OUT](/qb64wiki/index.php/OUT "OUT") &H3C9, 0: [OUT](/qb64wiki/index.php/OUT "OUT") &H3C9, 0: [OUT](/qb64wiki/index.php/OUT "OUT") &H3C9, 20 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 1 [FOR](/qb64wiki/index.php/FOR "FOR") i% = 1 [TO](/qb64wiki/index.php/TO "TO") 21     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2 + i%, 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(178)     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2 + i%, 39: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(178) [NEXT](/qb64wiki/index.php/NEXT "NEXT") i% [FOR](/qb64wiki/index.php/FOR "FOR") i% = 2 [TO](/qb64wiki/index.php/TO "TO") 39     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, i%: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(223)     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 23, i%: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(220) [NEXT](/qb64wiki/index.php/NEXT "NEXT") i% [COLOR](/qb64wiki/index.php/COLOR "COLOR") 9 [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 3, 16: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34); "MY BONNIE"; [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 3 [FOR](/qb64wiki/index.php/FOR "FOR") i% = 1 [TO](/qb64wiki/index.php/TO "TO") 34     [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") i%         [CASE](/qb64wiki/index.php/CASE "CASE") 1: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 5, 5         [CASE](/qb64wiki/index.php/CASE "CASE") 10: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 5         [CASE](/qb64wiki/index.php/CASE "CASE") 18: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 15, 5         [CASE](/qb64wiki/index.php/CASE "CASE") 27: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 5     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")     [READ](/qb64wiki/index.php/READ "READ") note%, duration%, word$     SOUND note%, duration%: [PRINT](/qb64wiki/index.php/PRINT "PRINT") word$; [NEXT](/qb64wiki/index.php/NEXT "NEXT") i% [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 2 [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 23, 16: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Thank You!" [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 4 [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")  [DATA](/qb64wiki/index.php/DATA "DATA") 392,8,"My ",659,8,"Bon-",587,8,"nie ",523,8,"lies ",587,8,"O-",523,8,"Ver ",440,8,"the " [DATA](/qb64wiki/index.php/DATA "DATA") 392,8,"O-",330,32,"cean ",392,8,"My ",659,8,"Bon-",587,8,"nie ",523,8,"lies " [DATA](/qb64wiki/index.php/DATA "DATA") 523,8,"O-",494,8,"ver ",523,8,"the ",587,40,"sea ",392,8,"My ",659,8,"Bon-",587,8,"nie" [DATA](/qb64wiki/index.php/DATA "DATA") 523,8," lies ",587,8,"O-",523,8,"ver ",440,8,"the ",392,8,"O-",330,32,"cean ",392,8,"Oh " [DATA](/qb64wiki/index.php/DATA "DATA") 440,8,"bring ",587,8,"back ",523,8,"my ",494,8,"Bon-",440,8,"nie ",494,8,"to ",523,32,"me..!"  ``` |
| --- |


Code adapted by Ted Weissgerber


---


Example 3
Playing sound effects using the new QB64-PE **SOUND** extensions.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [DIM](/qb64wiki/index.php/DIM "DIM") Q [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING")  ' Sound effects menu [DO](/qb64wiki/index.php/DO "DO")     [CLS](/qb64wiki/index.php/CLS "CLS")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Sound effects": [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "  B";: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 7, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ouncing"     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "  F";: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 7, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "alling"     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "  K";: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 7, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "laxon"     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "  S";: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 7, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "iren"     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "  Q";: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 7, 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "uit"     [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Select: ";      ' Get valid key     [DO](/qb64wiki/index.php/DO "DO")         Q = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")([INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1))     [LOOP WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INSTR](/qb64wiki/index.php/INSTR "INSTR")("BFKSQ", Q) = 0      ' Take action based on key     [CLS](/qb64wiki/index.php/CLS "CLS")     [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") Q         [CASE](/qb64wiki/index.php/CASE "CASE") [IS](/qb64wiki/index.php/IS "IS") = "B"             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Bouncing . . . "             Bounce 32767, 246 ' the 32767 will make the PSG generate silence (exactly like QB45 does)         [CASE](/qb64wiki/index.php/CASE "CASE") [IS](/qb64wiki/index.php/IS "IS") = "F"             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Falling . . . "             Fall 2000, 550, 500         [CASE](/qb64wiki/index.php/CASE "CASE") [IS](/qb64wiki/index.php/IS "IS") = "S"             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Wailing . . ."             [PRINT](/qb64wiki/index.php/PRINT "PRINT") " . . . press any key to end."             Siren 780, 650         [CASE](/qb64wiki/index.php/CASE "CASE") [IS](/qb64wiki/index.php/IS "IS") = "K"             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Oscillating . . ."             [PRINT](/qb64wiki/index.php/PRINT "PRINT") " . . . press any key to end."             Klaxon 987, 329         [CASE](/qb64wiki/index.php/CASE "CASE") [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") Q = "Q" [END](/qb64wiki/index.php/END "END")  ' Loop two sounds down at decreasing time intervals [SUB](/qb64wiki/index.php/SUB "SUB") Bounce (Hi [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Low [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [DIM](/qb64wiki/index.php/DIM "DIM") count [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")      [PLAY](/qb64wiki/index.php/PLAY "PLAY") "Q0" ' turn off volume ramping      [FOR](/qb64wiki/index.php/FOR "FOR") count = 60 [TO](/qb64wiki/index.php/TO "TO") 1 [STEP](/qb64wiki/index.php/STEP "STEP") -2         SOUND Low - count / 2, count / 20, 1.0!, 0.0!, 1         SOUND Hi, count / 15     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ' Loop down from a high sound to a low sound [SUB](/qb64wiki/index.php/SUB "SUB") Fall (Hi [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Low [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Del [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [DIM](/qb64wiki/index.php/DIM "DIM") vol [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")     [DIM](/qb64wiki/index.php/DIM "DIM") count [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")      [PLAY](/qb64wiki/index.php/PLAY "PLAY") "Q3" ' enable 3ms volume ramping      [FOR](/qb64wiki/index.php/FOR "FOR") count = Hi [TO](/qb64wiki/index.php/TO "TO") Low [STEP](/qb64wiki/index.php/STEP "STEP") -10         vol = 1.0! - vol         SOUND count, Del / count, vol, 0.0!, 3 ' triangle wave     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ' Alternate two sounds until a key is pressed [SUB](/qb64wiki/index.php/SUB "SUB") Klaxon (Hi [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Low [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [PLAY](/qb64wiki/index.php/PLAY "PLAY") "Q5" ' enable 5ms volume ramping      [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = ""         SOUND Hi, 5!, 1.0!, -1.0!, 4         SOUND Low, 5!, 1.0!, 1.0!, 4     [LOOP](/qb64wiki/index.php/LOOP "LOOP") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ' Loop a sound from low to high to low [SUB](/qb64wiki/index.php/SUB "SUB") Siren (Hi [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Range [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [DIM](/qb64wiki/index.php/DIM "DIM") count [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), pan [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")     [DIM](/qb64wiki/index.php/DIM "DIM") dir [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): dir = 0.01!      [PLAY](/qb64wiki/index.php/PLAY "PLAY") "Q0" ' disable volume ramping      [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = ""         [FOR](/qb64wiki/index.php/FOR "FOR") count = Range [TO](/qb64wiki/index.php/TO "TO") -Range [STEP](/qb64wiki/index.php/STEP "STEP") -4             pan = pan + dir             [IF](/qb64wiki/index.php/IF "IF") pan <= -1.0! [THEN](/qb64wiki/index.php/THEN "THEN") dir = 0.01!: pan = -1.0!             [IF](/qb64wiki/index.php/IF "IF") pan >= 1.0! [THEN](/qb64wiki/index.php/THEN "THEN") dir = -0.01!: pan = 1.0!              SOUND Hi - [ABS](/qb64wiki/index.php/ABS "ABS")(count), 0.3!, 1.0!, pan, 4 ' sine wave              count = count - 2 / Range         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [LOOP](/qb64wiki/index.php/LOOP "LOOP") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Samuel Gomes (a740g).
  




## See also


* [PLAY](/qb64wiki/index.php/PLAY "PLAY"), [BEEP](/qb64wiki/index.php/BEEP "BEEP")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")
* [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SOUND&oldid=8787>"




## Navigation menu








### Search





















