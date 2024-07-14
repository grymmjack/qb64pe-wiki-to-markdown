


PLAY - QB64 Phoenix Edition Wiki








# PLAY



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**PLAY** is a statement that plays notes of sound through the sound card in QB64 using a command [STRING](/qb64wiki/index.php/STRING "STRING").


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


PLAY *commandstring$*
  




## Parameters


* The *commandstring$* can be any literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") consisting of the following commands:
	+ Command string values are not case sensitive and spacing is ignored. Use upper or lower case as desired.


* **O**n - Sets the current octave (from 0 to 6). Example: **PLAY "O3"**
* **<** - Down one octave (cannot be below zero). Example: **PLAY "<<"** 'goes down two octaves.
* **>** - Up one octave (cannot be above 6). Example: **PLAY ">>"** ' goes up two octaves.
* **A**, **B**, **C**, **D**, **E**, **F** or **G** are the notes in the current octave. Can use the following suffixes:


* **+** or **#** for a sharp note. Example: **PLAY "C#"**
* **-** for a flat note. Example: **PLAY "C-"**

* **N**n - Plays a note n by number(n can be between 0 to 84 in the 7 octaves, where 0 is a rest). Example: **PLAY "N42"**
* **L**n - Sets length of a note (n can be 1 to 64 where 1 is a whole note and 4 is a quarter of a note etc.). Example: **PLAY "L4"**


* **MS** - Each note plays 3/4 of length set by L (staccato)
* **MN** - Each note plays 7/8 of length set by L (normal)
* **ML** - Each note plays full length set by L (legato)
* **P**n - Specifies a pause (1 - 64). P1 is a whole-note pause, P2 is a half-note pause, etc. (The pause is 1/n notes in length.) Example: **PLAY "P32"**
* **T**n - Tempo sets number of L4 quarter notes per minute (n can be 32 to 255 where 120 is the default). Example: **PLAY "T180"**


* **.**  - period after a note plays 1½ times the note length determined by L \* T.
* **..**  - two periods plays 1-3/4 times the note length determined by L \* T.

* **,**  - **commas in QB64** stop play advancement to allow more than one note to be played simultaneously. Example: **PLAY "C,E,G,"**
* **V**n - Volume in **QB64 only** can be any volume from 0 (none) to 100 (full). The default level is 50 when **n** is not specified.
* **MF** - Play music in the foreground (each note must be completed before another can start).
* **MB** - Play music in the background while program code execution continues (QB64 has no note buffer limits).
* **X** **+** [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$")(string-expression) - executes a command string variable. **MUST be used with variables!**.
* **@**n - Select waveform in **QB64-PE only** can be (**1** for square waveform, **2** for sawtooth waveform, **3** for triangle waveform (default), **4** for sine waveform or **5** for white noise)
* **Q**n - Volume ramp in **QB64-PE only** can be any duration (ms) from 0 to 100.
* Numeric values "n" listed above can also be fetched from numeric variables using **"="** + [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$")(numeric\_variable).

  




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


* Complete **X** **+** [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$")(string-expression) support was added in **QB64-PE v3.8.0**. Earlier versions of QB64-PE and QB64 only had **=** + [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$")(numeric\_variable) support.
* Support for **@**n and **Q**n was added in **QB64-PE v3.8.0**.


  




## Examples


Example 1
Plays a sound with the volume and note varying from 0 to 50. Maximum note can only be 84.


| ``` PLAY "q0mll64" [DO](/qb64wiki/index.php/DO "DO")     [FOR](/qb64wiki/index.php/FOR "FOR") x = 1 [TO](/qb64wiki/index.php/TO "TO") 50         a$ = a$ + "v" + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(x)) + "n" + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(x))     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [FOR](/qb64wiki/index.php/FOR "FOR") x = 50 [TO](/qb64wiki/index.php/TO "TO") 1 [STEP](/qb64wiki/index.php/STEP "STEP") -1         a$ = a$ + "v" + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(x)) + "n" + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(x))     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     PLAY a$     a$ = "" [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" PLAY "v10l1c,l4egl2o5c,o4l4eg"  ``` |
| --- |


Code by Galleon


---


Example 2
Plays "Frosty the snowman". The lyric printing is not delayed by PLAY in QB64.


| ``` [CLS](/qb64wiki/index.php/CLS "CLS"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Frosty the Snow Man" [FOR](/qb64wiki/index.php/FOR "FOR") X = 1 [TO](/qb64wiki/index.php/TO "TO") 2     [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [IF](/qb64wiki/index.php/IF "IF") X = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Fros-ty the Snow man was a jolly happy soul,"     [IF](/qb64wiki/index.php/IF "IF") X = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Fros-ty the Snow man knew the sun was hot that day"     PLAY "t140o2p4g2e4.f8g4o3c2o2b8o3c8d4c4o2b4a8g2." 'MB removed to print song one line at a time     [IF](/qb64wiki/index.php/IF "IF") X = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "with a corn cob pipe and a button nose and two eyes made out of coal."     [IF](/qb64wiki/index.php/IF "IF") X = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "so he said Let's run and we'll have some fun now before I melt away."     PLAY "o2b8o3c8d4c4o2b4a8a8g8o3c4o2e8e4g8a8g4f4e4f4g2."     [IF](/qb64wiki/index.php/IF "IF") X = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Fros-ty the Snow Man is a fair-y tale, they say,"     [IF](/qb64wiki/index.php/IF "IF") X = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Down to the vil-lage, with a broom-stick in his hand,"     PLAY "g2e4.f8g4o3c2o2b8o3c8d4c4o2b4a8g2."     [IF](/qb64wiki/index.php/IF "IF") X = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "He was made of snow but the chil-dren knew how he come to life one day."     [IF](/qb64wiki/index.php/IF "IF") X = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "run-ning here and there all a-round the square, say-in' catch me if you can."     PLAY "o2b8o3c8d4c4o2b4a8a8g8o3c4o2e8e4g8a8g4f4e4d4c2."     [IF](/qb64wiki/index.php/IF "IF") X = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "There must have been some magic in that old silk hat they found."     [IF](/qb64wiki/index.php/IF "IF") X = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "He led them down the streets of town right to the traffic cop."     PLAY "c4a4a4o3c4c4o2b4a4g4e4f4a4g4f4e2."     [IF](/qb64wiki/index.php/IF "IF") X = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "For when they placed it on his head he be-gan to dance a round."     [IF](/qb64wiki/index.php/IF "IF") X = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "And he on-ly paused a moment when he heard him hol-ler Stop!"     PLAY "e8e8d4d4g4g4b4b4o3d4d8o2b8o3d4c4o2b4a4g4p4"     [IF](/qb64wiki/index.php/IF "IF") X = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Oh, Fros-ty the Snow Man was a-live as he could be,"     [IF](/qb64wiki/index.php/IF "IF") X = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "For, Fros-ty the Snow Man had to hur-ry on his way"     PLAY "g2g2e4.f8g4o3c2o2b8o3c8d4c4o2b4a8g8g2."     [IF](/qb64wiki/index.php/IF "IF") X = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "and the chil-dren say he could laugh and play just the same as you and me."     [IF](/qb64wiki/index.php/IF "IF") X = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "but he waved good-bye say-in' Don't you cry, I'll be back a-gain some day."     PLAY "o2b8o3c8d4c4o2b4a8a8g8o3c4o2e8e4g8a8g4f4e4d4c2.p4" [NEXT](/qb64wiki/index.php/NEXT "NEXT") X [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Thump-et-y thump thump, thump-et-y thump thump, look at Fros-ty go." PLAY "t180g8g8g4g4g4a8g8g4g4g4a4g4e4g4d1" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Thump-et-y thump thump, thump-et-y thump thump, ov-er the hills of snow." PLAY "t180g8g8g4g4g4a8g8g4g4g4g8g8g4a4b4o3c2c4p1" [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Greg Rismoen


---


Example 3
Clicking on the grid enables various notes to be played simultaneously.


| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") grid(16, 16), grid2(16, 16), cur [CONST](/qb64wiki/index.php/CONST "CONST") maxx = 512 [CONST](/qb64wiki/index.php/CONST "CONST") maxy = 512 [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(maxx, maxy, 32) [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "MusicGrid" cleargrid [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF "IF") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") - t# > 1 / 8 [THEN](/qb64wiki/index.php/THEN "THEN") cur = (cur + 1) [AND](/qb64wiki/index.php/AND "AND") 15: t# = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")     [IF](/qb64wiki/index.php/IF "IF") cur <> oldcur [THEN](/qb64wiki/index.php/THEN "THEN")         figuregrid         drawgrid         playgrid         oldcur = cur     [END IF](/qb64wiki/index.php/END_IF "END IF")     domousestuff     in$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")     [IF](/qb64wiki/index.php/IF "IF") in$ = "C" [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") in$ = "c" [THEN](/qb64wiki/index.php/THEN "THEN") cleargrid [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") in$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  [SUB](/qb64wiki/index.php/SUB "SUB") drawgrid     scale! = maxx / 16     scale2 = maxx \ 16 - 2     [FOR](/qb64wiki/index.php/FOR "FOR") y = 0 [TO](/qb64wiki/index.php/TO "TO") 15         y1 = y * scale!         [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") 15             x1 = x * scale!             c& = [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(grid2(x, y) * 64 + 64, 0, 0)             [LINE](/qb64wiki/index.php/LINE "LINE") (x1, y1)-(x1 + scale2, y1 + scale2), c&, BF         [NEXT](/qb64wiki/index.php/NEXT "NEXT") x     [NEXT](/qb64wiki/index.php/NEXT "NEXT") y [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") figuregrid     [FOR](/qb64wiki/index.php/FOR "FOR") y = 0 [TO](/qb64wiki/index.php/TO "TO") 15         [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") 15             grid2(x, y) = grid(x, y)         [NEXT](/qb64wiki/index.php/NEXT "NEXT") x     [NEXT](/qb64wiki/index.php/NEXT "NEXT") y     [FOR](/qb64wiki/index.php/FOR "FOR") y = 1 [TO](/qb64wiki/index.php/TO "TO") 14         [FOR](/qb64wiki/index.php/FOR "FOR") x = 1 [TO](/qb64wiki/index.php/TO "TO") 14             [IF](/qb64wiki/index.php/IF "IF") grid(x, y) = 1 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") cur = x [THEN](/qb64wiki/index.php/THEN "THEN")                 grid2(x, y) = 2                 [IF](/qb64wiki/index.php/IF "IF") grid(x - 1, y) = 0 [THEN](/qb64wiki/index.php/THEN "THEN") grid2(x - 1, y) = 1                 [IF](/qb64wiki/index.php/IF "IF") grid(x + 1, y) = 0 [THEN](/qb64wiki/index.php/THEN "THEN") grid2(x + 1, y) = 1                 [IF](/qb64wiki/index.php/IF "IF") grid(x, y - 1) = 0 [THEN](/qb64wiki/index.php/THEN "THEN") grid2(x, y - 1) = 1                 [IF](/qb64wiki/index.php/IF "IF") grid(x, y + 1) = 0 [THEN](/qb64wiki/index.php/THEN "THEN") grid2(x, y + 1) = 1             [END IF](/qb64wiki/index.php/END_IF "END IF")         [NEXT](/qb64wiki/index.php/NEXT "NEXT") x     [NEXT](/qb64wiki/index.php/NEXT "NEXT") y [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") domousestuff     [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")         [IF](/qb64wiki/index.php/IF "IF") [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1) [THEN](/qb64wiki/index.php/THEN "THEN")             x = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX") \ (maxx \ 16)             y = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY") \ (maxy \ 16)             grid(x, y) = 1 - grid(x, y)         [END IF](/qb64wiki/index.php/END_IF "END IF")     [LOOP](/qb64wiki/index.php/LOOP "LOOP") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") playgrid     n$ = "L16 "     'scale$ = "O1CO1DO1EO1FO1GO1AO1BO2CO2DO2EO2FO2GO2AO2BO3CO3D"     scale$ = "o1fo1go1ao2co2do2fo2go2ao3co3do3fo3go3ao4co4do4fo"     [FOR](/qb64wiki/index.php/FOR "FOR") y = 15 [TO](/qb64wiki/index.php/TO "TO") 0 [STEP](/qb64wiki/index.php/STEP "STEP") -1         [IF](/qb64wiki/index.php/IF "IF") grid(cur, y) = 1 [THEN](/qb64wiki/index.php/THEN "THEN")             note$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(scale$, 1 + (15 - y) * 3, 3)             n$ = n$ + note$ + "," 'comma plays 2 or more column notes simultaneously         [END IF](/qb64wiki/index.php/END_IF "END IF")     [NEXT](/qb64wiki/index.php/NEXT "NEXT") y     n$ = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(n$, [LEN](/qb64wiki/index.php/LEN "LEN")(n$) - 1)     PLAY n$ [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") cleargrid     [FOR](/qb64wiki/index.php/FOR "FOR") y = 0 [TO](/qb64wiki/index.php/TO "TO") 15         [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") 15             grid(x, y) = 0         [NEXT](/qb64wiki/index.php/NEXT "NEXT") x     [NEXT](/qb64wiki/index.php/NEXT "NEXT") y [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by JP


---


Example 4
Play strings starting with MB allow program code to run while music plays in background.


| ``` ' 2012, 2013 mennonite ' license: creative commons cc0 1.0 universal ' (public domain) http://creativecommons.org/publicdomain/zero/1.0/  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 ' the following works in other screen modes, too [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")  PLAY "mb l4cf.l8el4fag.l8fl4gl8agl4f.l8fl4a>cl2dl4dl4c.<l8al4afg.l8fl4gl8agl4f.l8dl4dcl2f>l4dc.<l8al4afg.l8fl4g>dc.<l8al4a>cl2dl4dc.<l8al4afg.l8fl4gl8agl4f.l8dl4dcl1f"  [DIM](/qb64wiki/index.php/DIM "DIM") ccs(1 [TO](/qb64wiki/index.php/TO "TO") 9, 1 [TO](/qb64wiki/index.php/TO "TO") 2) ccs(1, 1) = 415: ccs(1, 2) = 289 ccs(2, 1) = 185: ccs(2, 2) = 128 ccs(3, 1) = 108: ccs(3, 2) = 75 ccs(4, 1) = 70: ccs(4, 2) = 48 ccs(5, 1) = 48: ccs(5, 2) = 32 ccs(6, 1) = 32: ccs(6, 2) = 20 ccs(7, 1) = 20: ccs(7, 2) = 12 ccs(8, 1) = 10: ccs(8, 2) = 6 ccs(9, 1) = 2: ccs(9, 2) = 2  [FOR](/qb64wiki/index.php/FOR "FOR") extra = 1 [TO](/qb64wiki/index.php/TO "TO") 23     [FOR](/qb64wiki/index.php/FOR "FOR") p = 1 [TO](/qb64wiki/index.php/TO "TO") 9         gcolor [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 9 + 14 - 9)         [_DELAY](/qb64wiki/index.php/DELAY "DELAY") .04         [CLS](/qb64wiki/index.php/CLS "CLS")         gscale p         row = ccs(p, 1)         cl = ccs(p, 2)         glocate row, cl         gprint "000000000000000000000000000000000000000000000000000000000000000000000"         glocate row + 1, cl         gprint "0x00x0xxxx0xxxx0xxxx0x0x000x00x0xxxx0x000x000x0x0xxxx0xxxx0xxxx000x00"         glocate row + 2, cl         gprint "0x00x0x00x0x00x0x00x0x0x000xx0x0x0000x000x000x0x0x0000x00x0x00x000x00"         glocate row + 3, cl         gprint "0xxxx0xxxx0xxxx0xxxx0x0x000x0xx0xxx00x0x0x000x0x0xxx00xxxx0xxxx000x00"         glocate row + 4, cl         gprint "0x00x0x00x0x0000x00000x0000x00x0x0000x0x0x0000x00x0000x00x0x0x0000000"         glocate row + 5, cl         gprint "0x00x0x00x0x0000x00000x0000x00x0xxxx0xx0xx0000x00xxxx0x00x0x00x000x00"         glocate row + 6, cl         gprint "000000000000000000000000000000000000000000000000000000000000000000000"     [NEXT](/qb64wiki/index.php/NEXT "NEXT") p     [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 1     [IF](/qb64wiki/index.php/IF "IF") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT FOR](/qb64wiki/index.php/EXIT_FOR "EXIT FOR") [NEXT](/qb64wiki/index.php/NEXT "NEXT") extra  [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") gscale (s):     [SHARED](/qb64wiki/index.php/SHARED "SHARED") gscalep     gscalep = [INT](/qb64wiki/index.php/INT "INT")(s) [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") gcolor (c):     [SHARED](/qb64wiki/index.php/SHARED "SHARED") gcolorp     gcolorp = c [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") gbackcolor (c):     [SHARED](/qb64wiki/index.php/SHARED "SHARED") gbackcolorp     gbackcolorp = c [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") glocate (row, column):     [SHARED](/qb64wiki/index.php/SHARED "SHARED") gposxp     [SHARED](/qb64wiki/index.php/SHARED "SHARED") gposyp     gposyp = row     gposxp = column [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") gprint (p$):     [SHARED](/qb64wiki/index.php/SHARED "SHARED") gscalep     [SHARED](/qb64wiki/index.php/SHARED "SHARED") gposxp, gposyp     [SHARED](/qb64wiki/index.php/SHARED "SHARED") gcolorp, gbackcolorp     ' # means "use the foreground color here."     ' . means "use the background color here."     ' _ means "transparent - don't draw this block at all" (you can layer!)     ' 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f means "do color attribute 0 to 15."     ' any letter after f: "use the foreground color here."     [IF](/qb64wiki/index.php/IF "IF") gscalep < 1 [THEN](/qb64wiki/index.php/THEN "THEN") gscalep = 1     pcolorp = gcolorp     [FOR](/qb64wiki/index.php/FOR "FOR") p = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(p$):         [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(p$, p, 1))             [CASE](/qb64wiki/index.php/CASE "CASE") "#", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"                 pcolorp = gcolorp             [CASE](/qb64wiki/index.php/CASE "CASE") "."                 pcolorp = gbackcolorp             [CASE](/qb64wiki/index.php/CASE "CASE") "_"                 pcolorp = -1             [CASE](/qb64wiki/index.php/CASE "CASE") "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"                 pcolorp = [INSTR](/qb64wiki/index.php/INSTR "INSTR")("0123456789abcdef", [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(p$, p, 1))) - 1         [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")         [IF](/qb64wiki/index.php/IF "IF") [NOT](/qb64wiki/index.php/NOT "NOT") pcolorp = -1 [THEN](/qb64wiki/index.php/THEN "THEN")             [IF](/qb64wiki/index.php/IF "IF") gscalep > 1 [THEN](/qb64wiki/index.php/THEN "THEN")                 [LINE](/qb64wiki/index.php/LINE "LINE") ((gposxp - 1) * gscalep, (gposyp - 1) * gscalep)-[STEP](/qb64wiki/index.php/STEP "STEP")(gscalep - 1, gscalep - 1), pcolorp, BF             [ELSE](/qb64wiki/index.php/ELSE "ELSE"):                 [PSET](/qb64wiki/index.php/PSET "PSET") (gposxp, gposyp), pcolorp             [END IF](/qb64wiki/index.php/END_IF "END IF")         [END IF](/qb64wiki/index.php/END_IF "END IF")         glocate gposyp, gposxp + 1     [NEXT](/qb64wiki/index.php/NEXT "NEXT") p     gposxp = 1     glocate gposyp + 1, 1 'gposyp = gposyp + 1 [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Mennonite


---


Example 5
This example uses [PRINT](/qb64wiki/index.php/PRINT "PRINT") to good effect as string spacing is ignored by **PLAY**.


| ``` [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") 59, 28 [PRINT](/qb64wiki/index.php/PRINT "PRINT") x$ = x$ + "   o3    l4         t         0120c    ml<f1   ,a      1,  " x$ = x$ + "   >c    1,        mnf        .e  8f   am  l<   e1    ,g   " x$ = x$ + "   1,    >c       1, mn       g.   f8  ga   8g   8m  l<    " x$ = x$ + "   f2.,a2.,      >c   2.      ,m  nf   .f  8a     ml<f     " x$ = x$ + "   ,a,>c,mn     >cd2.,<f2     .,d2     .,<b        -2      " x$ = x$ + "   .m    lb    -,>d,f,mn>d    ml       <c          1,      " x$ = x$ + "   <a    1,   f1         ,m   n>       >c          .<      " x$ = x$ + "   a8    af  ml           c1  ,<       e1          ,g      " x$ = x$ + "                                                           " x$ = x$ + "      1,m      n>  g.f8ga8g8m  l<                   f1     " x$ = x$ + "      ,d1,     <b  -1           ,m                 n>      " x$ = x$ + "      >f .d    8d  c<            f2               .,       " x$ = x$ + "      a2  .,   c2  .,>f2.         ml      <      b-        " x$ = x$ + "      ,>   d,  f,  mn>dml          <c    1,<    a1         " x$ = x$ + "      ,f    1, mn  >>               c.  <a 8a  fm          " x$ = x$ + "      lc     2.,<  e2                .,g2   .,mn           " x$ = x$ + "      >g      .f8  gml<b-,>d,         f,     mn            " x$ = x$ + "                                                           " x$ = x$ + ">d      ml  <<f2.,a2.,         >         c2.,m       n>  c." x$ = x$ + " <a    8a   ml                <e,        g,  >c      ,m  n>" x$ = x$ + "  cm  l<    <b               -2 .,       >d   2.     ,f  2." x$ = x$ + "   ,mn>     d2.ml<          <b   -,      >d  ,f      ,m  n>" x$ = x$ + "    dm      l<<f1,         a1,>c1,mn     >c.<a       8a  fm" x$ = x$ + "    lc      1,            <e1,g1,mn>g    .f  8g      a8  g8" x$ = x$ + "    ml      <<           b-         1,   >d   1,           " x$ = x$ + "    f1      ,mn>f.d8dc  l1           ml  f,    c,    <a  ,f" [PRINT](/qb64wiki/index.php/PRINT "PRINT") x$; PLAY x$  ``` |
| --- |


Code by Luke


---


Example 6
Demonstrates usage of [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$") with **PLAY**.


| ``` 'Play scale in 7 different octaves scale$ = "CDEFGAB"  play$ = "L16O=" + [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$")(i%) + "X" + [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$")(scale$)  [FOR](/qb64wiki/index.php/FOR "FOR") i% = 0 [TO](/qb64wiki/index.php/TO "TO") 6     PLAY play$ [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |


  




## See also


* [PLAY (function)](/qb64wiki/index.php/PLAY_(function) "PLAY (function)")
* [SOUND](/qb64wiki/index.php/SOUND "SOUND"), [DRAW](/qb64wiki/index.php/DRAW "DRAW")
* [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PLAY&oldid=8783>"




## Navigation menu








### Search





















