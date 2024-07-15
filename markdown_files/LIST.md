<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>KEY LIST - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-KEY_LIST rootpage-KEY_LIST skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">KEY LIST</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a href="KEY_n" title="KEY n">KEY n</a> statement is used to assign a "soft key" string or a flag and scan code to a function key or display function soft key assignments.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>KEY <i>n%</i>, <i>textString$</i></b></dd></dl>
<dl><dd><b>KEY <i>n%</i>, CHR$(<i>keyFlag%</i>) + CHR$(<i>scanCode</i>)</b></dd></dl>
<p>
</p>
<h2><span id="Function_Soft_Key_Strings_.281_to_10.2C_30_.26_31.29"></span><span class="mw-headline" id="Function_Soft_Key_Strings_(1_to_10,_30_&amp;_31)">Function Soft Key Strings (1 to 10, 30 &amp; 31)</span></h2>
<ul><li>n% is the number 1 to 10 (F1 to F10), 30 or 31 (F11 or F12) of the function key to assign the soft key string.</li>
<li>Instead of using an <a href="ON_KEY(n)" title="ON KEY(n)">ON KEY(n)</a> <a href="GOSUB" title="GOSUB">GOSUB</a> statement, Function keys F1 to F12 can be assigned a "soft key" string value to return.</li>
<li><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">KEY n, text$</span> defines a literal or variable <a href="STRING" title="STRING">STRING</a> "soft key" function key return value.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">        <b>KEY 1, "Help"</b> 'returns the string "Help" to <a href="INPUT" title="INPUT">INPUT</a> variable when F1 is pressed</pre>
</td></tr></tbody></table>
<ul><li><a class="mw-selflink selflink">KEY LIST</a> displays each of the 12 softkey <b>function key</b> (F1 to F12) string values going down left side of screen.</li>
<li><a class="mw-selflink selflink">KEY {ON|OFF}</a> displays or hides the softkey values of function keys F1 to F10 at the bottom of the screen.</li></ul>
<p>
</p>
<h2><span id="Number_Pad_Arrow_Keys_.2811_to_14.29"></span><span class="mw-headline" id="Number_Pad_Arrow_Keys_(11_to_14)">Number Pad Arrow Keys (11 to 14)</span></h2>
<ul><li>Arrow keys on the Number Pad are predefined KEY numbers 11 to 14 and only work with Number Lock off.</li>
<li>Soft Key <a href="STRING" title="STRING">STRINGs</a> cannot be assigned to these key numbers!</li>
<li>To use the extended arrow keys on a keyboard use the Extended Key Flag 128 with corresponding Scan code as User Defined Keys.</li></ul>
<p>
</p>
<h2><span id="User_Defined_Keys_.2815_to_29.29"></span><span class="mw-headline" id="User_Defined_Keys_(15_to_29)">User Defined Keys (15 to 29)</span></h2>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">                   <b>Function Key Flag Combination Values</b>
                  <b>0</b> = no function key combination flag(single key)
                  <b>1</b> = Left Shift key flag
                  <b>2</b> = Right Shift key flag
                  <b>4</b> = Ctrl flag
                  <b>8</b> = Alt flag
                 <b>32</b> = Number Lock flag
                 <b>64</b> = Caps Lock flag
                <b>128</b> = Extended keys (see trapping extended keys below)
          Flag values can be added to monitor multiple function key combinations.
</pre>
</td></tr></tbody></table>
<ul><li>After the keyflag code character the <a href="Scancodes" title="Scancodes">scancode</a> character is added using one of the two <b>trapping methods</b> that follow:</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">'                           <b>Soft Key Scan Code Values</b>
'
'      <span style="color:red;">1  2  3  4  5  6  7  8  9  10   30  31                       Predefined Keys</span>
' <b>Esc  F1 F2 F3 F4 F5 F6 F7 F8 F9 F10  F11 F12   SysReq ScrL Pause</b>
'  1   59 60 61 62 63 64 65 66 67 68   87  88     --    70    29
' <b>`~  1! 2@ 3# 4$ 5% 6^ 7&amp; 8* 9( 0) -_ =+ BkSpc  Insert Home PgUp   NumL   /     *    -</b>
'  41 2  3  4  5  6  7  8  9  10 11 12 13  14     <span style="color:blue;">82    71    73</span>    <span style="color:purple;">32</span>/69  <span style="color:blue;">53</span>    55   74
' <b>Tab  Q  W  E  R  T  Y  U  I  O  P  [{ ]} \|    Delete End  PgDn   7/Home 8/▲  9/PU  + </b>
'  15  16 17 18 19 20 21 22 23 24 25 26 27 43     <span style="color:blue;">83    79    81</span>     71   <span style="color:red;">11</span>/72  73   78
' <b>CapL  A  S  D  F  G  H  J  K  L  ;: '"  Enter                     4/◄-   5    6/-►  E</b>
' <span style="color:purple;">64</span>/58 30 31 32 33 34 35 36 37 38 39 40   28                       <span style="color:red;">12</span>/75  76   <span style="color:red;">13</span>/77 <b>n</b>
' <b>Shift  Z  X  C  V  B  N  M  ,&lt; .&gt; /?    Shift         ▲           1/End  2/▼  3/PD  t</b>
' <span style="color:purple;">1</span>/42   44 45 46 47 48 49 50 51 52 53    <span style="color:purple;">2</span>/54          <span style="color:blue;">72</span>           79   <span style="color:red;">14</span>/80  81   <b>e</b>
' <b>Ctrl Win Alt    Spacebar    Alt Win Menu Ctrl     ◄-  ▼   -►      0/Insert    ./Del r</b>
' <span style="color:purple;">4</span>/29  <span style="color:orange;">91</span> <span style="color:purple;">8</span>/56      57       <span style="color:blue;">56</span>  <span style="color:orange;">92   93</span>  <span style="color:blue;">29       75  80  77</span>       82          83   <span style="color:blue;">28</span>
'
'  <b>Keyflag:</b> <span style="color:purple;">Function(0, 1, 2, 4, 8, 32, 64)</span>, <span style="color:blue;">Extended(128)</span> <b>Scan Code: </b>1-88, <span style="color:orange;">QB64 only(91-93)</span>
'
'        Reserved and function key combinations can be made using the scan code instead.
'             Add function flag values to 128 for Extended key combinations.
</pre>
</td></tr></tbody></table>
<p>
</p>
<dl><dd>Keyboard Flag values can be added to monitor more than one control key. For example, flag combination 12 would flag both the Ctrl and Alt key presses. Since the flag already determines the function key to monitor, you don't necessarily have to use it's scancode. You can look for a key combination such as Ctrl + by using the plus key's scancode which is 13 as shown below:</dd></dl>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">      <b>KEY 15, CHR$(4) + CHR$(13)</b> 'enabled event when Ctrl and + key are pressed</pre>
</td></tr></tbody></table>
<p>
</p>
<ul><li>On a 101-key keyboard, you can trap any of the keys on the dedicated cursorpad by assigning the string to any of the keynumber values from 15 to 25 using the 128 keyboard flag. The cursor arrows are not the same as the pre-assigned number pad arrows:</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">      <b>KEY n, <a href="CHR$" title="CHR$">CHR$</a>(128) + <a href="CHR$" title="CHR$">CHR$</a>(scancode) ' where n = 15 to 29. See: <a href="Scancodes" title="Scancodes">Scancodes</a></b>
              KEY 15, CHR$(128) + CHR$(75)  'left arrow cursor pad 
              KEY 16, CHR$(128) + CHR$(72)  'up arrow cursor pad  
              KEY 17, CHR$(128) + CHR$(77)  'right arrow cursor pad
              KEY 18, CHR$(128) + CHR$(80)  'down arrow cursor pad
</pre>
</td></tr></tbody></table>
<p>
</p>
<p style="text-align: center">(<a href="#toc">Return to Table of Contents</a>)</p>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Shows a list of all the string assignments to the function keys F1-F12 (Prints help every time F1 is pressed in the input)
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="KEY_n" title="KEY n"><span style="color:#4593D8;">KEY</span></a> 1, "Help"
<a class="mw-selflink selflink"><span style="color:#4593D8;">KEY LIST</span></a>
INPUT "Press F1 or to quit press ENTER: ", a$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">F1 Help
F2
F3
F4
F5
F6
F7
F8
F9
F10
F11
F12
Press F1 or to quit press ENTER: HelpHelpHelpHelp
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Trapping the Control + key combination. Use the Control Keyboard flag 4 and + key scancode 13.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="KEY_n" title="KEY n"><span style="color:#4593D8;">KEY</span></a> 15, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(4) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(13)     'scancode for "=" or "+" key is 13
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(15) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> control       'action of user defined key press
<a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(15) ON                     'turn ON event trapping for key combination
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press Ctrl and plus key combination, escape quits!"
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
count = count + 1
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> count;
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="END" title="END"><span style="color:#4593D8;">END</span></a>  'escape key exit
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
control:                             'NUMBER LOCK MUST BE OFF!
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Control and + keys pressed!";
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Differentiating the extended cursor keypad arrows from the predefined Number Pad arrow keys.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">'predefined keys 11 to 14 for number pad arrows only
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(11) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> UpNum: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(11) ON 'up
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(12) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> LNum: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(12) ON  'left
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(13) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> RNum: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(13) ON  'right
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(14) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> DnNum: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(14) ON 'down
'user defined keys use extended key flag 128 + scan code
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(15) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> UpPad
<a href="KEY_n" title="KEY n"><span style="color:#4593D8;">KEY</span></a> 15, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(128) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(72): <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(15) ON 'cursor up
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(16) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> LPad
<a href="KEY_n" title="KEY n"><span style="color:#4593D8;">KEY</span></a> 16, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(128) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(75): <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(16) ON 'cursor left
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(17) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> RPad
<a href="KEY_n" title="KEY n"><span style="color:#4593D8;">KEY</span></a> 17, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(128) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(77): <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(17) ON 'cursor right
<a href="ON_KEY(n)" title="ON KEY(n)"><span style="color:#4593D8;">ON KEY</span></a>(18) <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> DnPad
<a href="KEY_n" title="KEY n"><span style="color:#4593D8;">KEY</span></a> 18, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(128) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(80): <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(18) ON 'cursor down
<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = 0
DO
  numL = <a href="PEEK" title="PEEK"><span style="color:#4593D8;">PEEK</span></a>(1047) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> 32 '32 if on
  capL = <a href="PEEK" title="PEEK"><span style="color:#4593D8;">PEEK</span></a>(1047) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> 64 '64 on
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> numL <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> capL <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 13, 50: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Turn Num or Cap Lock OFF!"
  <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> : <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 10: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 13, 50: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Number and Cap Lock OK!  "
    <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>                  ' <a href="KEY_n" title="KEY n"><span style="color:#4593D8;">KEY</span></a> or <a href="TIMER" title="TIMER"><span style="color:#4593D8;">TIMER</span></a> event breaks a sleep
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
<a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(15) OFF: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(16) OFF: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(17) OFF: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(18) OFF
<a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(11) OFF: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(12) OFF: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(13) OFF: <a href="KEY(n)" title="KEY(n)"><span style="color:#4593D8;">KEY</span></a>(14) OFF
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
UpPad:
COLOR 14: LOCATE 11, 26: PRINT " Up cursor pad  "
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
LPad:
COLOR 14: LOCATE 11, 26: PRINT "Left cursor pad "
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
RPad:
COLOR 14: LOCATE 11, 26: PRINT "Right cursor pad"
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
DnPad:
COLOR 14: LOCATE 11, 26: PRINT "Down cursor pad "
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
UpNum:
COLOR 11: LOCATE 11, 26: PRINT " Up number pad  "
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
LNum:
COLOR 11: LOCATE 11, 26: PRINT "Left number pad "
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
RNum:
COLOR 11: LOCATE 11, 26: PRINT "Right number pad"
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
DnNum:
COLOR 11: LOCATE 11, 26: PRINT "Down number pad "
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The Number Lock or Caps Lock keys ON may hinder extended key reads in QBasic but not QB64!</dd></dl>
<p>
</p>
<p style="text-align: center">(<a href="#toc">Return to Table of Contents</a>)</p>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="mw-selflink selflink">KEY LIST</a>, <a href="ON_KEY(n)" title="ON KEY(n)">ON KEY(n)</a></li>
<li><a href="KEY(n)" title="KEY(n)">KEY(n)</a>, <a href="INKEY$" title="INKEY$">INKEY$</a></li>
<li><a href="KEYHIT" title="KEYHIT">_KEYHIT</a>, <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a></li>
<li><a href="Keyboard_scancodes" title="Keyboard scancodes">Keyboard scancodes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192500
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.076 seconds
Real time usage: 0.098 seconds
Preprocessor visited node count: 936/1000000
Post‐expand include size: 7722/2097152 bytes
Template argument size: 1420/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   52.328      1 -total
 11.17%    5.843     98 Template:Cl
  9.76%    5.105      2 Template:Small
  7.18%    3.757     23 Template:Text
  6.59%    3.450      1 Template:PageSyntax
  5.57%    2.915      5 Template:FixedEnd
  5.53%    2.893      5 Template:FixedStart
  4.96%    2.593      1 Template:PageExamples
  4.51%    2.362      1 Template:OutputStart
  4.51%    2.361      3 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:482-0!canonical and timestamp 20240714192500 and revision id 8041.
 -->
</div>
</div>
</div>
</div>
</body>
</html>