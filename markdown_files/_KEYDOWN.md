<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_KEYDOWN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-KEYDOWN rootpage-KEYDOWN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_KEYDOWN</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_KEYDOWN</b> function returns whether modifying keys like CTRL, ALT, SHIFT, and any other keys are pressed.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>return% = <b>_KEYDOWN(</b><i>code&amp;</i><b>)</b></dd></dl></dd></dl>
<p>
</p>
<ul><li>The <i>return</i> value is -1 if a specified key is pressed or 0 if it was not pressed. It can be used to monitor key combinations.</li>
<li>The  POSITIVE <a href="LONG" title="LONG">LONG</a> <i>code</i> value can be from any function key that needs to be monitored in a key press combination.</li>
<li>Unicode references:</li></ul>
<dl><dd><ul><li>1) What is the glyph represented by that UNICODE value: <a class="external text" href="http://www.fileformat.info/info/unicode/char/search.htm" rel="nofollow">Unicode Format Info</a></li>
<li>2) Which fonts support the characters I want to use: <a class="extiw" href="https://en.wikipedia.org/wiki/Unicode_typefaces#Comparison_of_fonts" title="wikipedia:Unicode typefaces">Unicode Fonts</a></li>
<li>3) What was the format again?: <a class="external text" href="http://www.birds-eye.net/definition/u/unicode.shtml" rel="nofollow">Unicode Formats</a></li>
<li>A UTF32 value is usually(but by no means always!) the same as a UTF16 value just with the top 2 bytes set to 0.</li></ul></dd></dl>
<ul><li>An important difference between <a href="INKEY$" title="INKEY$">INKEY$</a> and <a href="KEYHIT" title="KEYHIT">_KEYHIT</a> is how they work when <b>CTRL, ALT</b> or <b>SHIFT</b> are used. <a href="INKEY$" title="INKEY$">INKEY$</a> returns a different code if you hold down CTRL, ALT or SHIFT before pressing F1 (for example). <a href="KEYHIT" title="KEYHIT">_KEYHIT</a> will return the same code regardless of which modifiers were used but you can check _KEYDOWN to see which modifying keys are being used.</li>
<li><b>Keyboards with Alt Gr key:</b> <a href="KEYHIT" title="KEYHIT">_KEYHIT</a> may return both Alt(100307) and Ctrl(100306) codes when key is pressed or released.</li>
<li><b>Linux with foreign keyboards:</b> <a href="SHELL" title="SHELL">SHELL</a> <a href="HIDE" title="HIDE">_HIDE</a> "setxkbmap us" will setup a keyboard to read US <a href="Scancodes" title="Scancodes">Scancodes</a>.</li></ul>
<p>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">                       <b>The QB64 Virtual Key constant values used: </b>
         <b>0-255</b>: <a href="ASCII" title="ASCII">ASCII and Extended code</a> values (Refer to <a class="extiw" href="https://en.wikipedia.org/wiki/Code_page_437" title="wikipedia:Code page 437">CP437</a>)
         <b>256-65535</b>: <a href="ASCII#Two_Byte_Codes" title="ASCII">ASCII 2-byte</a> character codes (unaffected by SHIFT/ALT/CTRL modifiers)
                  Use <a href="CVI" title="CVI">CVI</a> to convert ASCII 2-byte codes to _KEYDOWN values.
'                                <b>_KEYDOWN Keyboard Values</b>
'
' <b>Esc  F1    F2    F3    F4    F5    F6    F7    F8    F9    F10   F11   F12   Sys  ScL Pause</b>
'  27 15104 15360 15616 15872 16128 16384 16640 16896 17152 17408 34048 34304 +316 +302 +019
' <b>`~  1!  2@  3#  4$  5%  6^  7&amp;  8*  9(  0) -_ =+ BkSp   Ins   Hme   PUp   NumL   /     *    -</b>
' 126 33  64  35  36  37  94  38  42  40  41 95 43   8   20992 18176 18688 +300   47    42   45
' <i> 96 49  50  51  52  53  54  55  56  57  48 45 61</i>
' <b>Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del   End   PDn   7Hme  8/▲   9PU   + </b>
'  9  81  87  69  82  84  89  85  73  79  80 123 125 124 21248 20224 20736 18176 18432 18688 43
' <i>   113 119 101 114 116 121 117 105 111 112  91  93  92                    55    56    57 </i>
' <b>CapL   A   S   D   F   G   H   J   K   L   ;:  '" Enter                   4/◄-   5    6/-►</b>
' +301  65  83  68  70  71  72  74  75  76  58  34  13                     19200 19456 19712  <b>E</b>
' <i>      97 115 100 102 103 104 106 107 108  59  39                          52    53    54 </i>   <b>n</b>
' <b>Shift   Z   X   C   V   B   N   M   ,&lt;  .&gt;  /?    Shift       ▲           1End  2/▼   3PD   t</b>
' +304   90  88  67  86  66  78  77  60  62  63    +303       18432        20224 20480 20736  <b>e</b>
' <i>      122 120  99 118  98 110 109  44  46  47                             49    50    51 </i>   <b>r</b>
' <b>Ctrl   Win  Alt     Spacebar      Alt  Win  Menu  Ctrl   ◄-   ▼   -►      0Ins        .Del </b>
' +306  +311 +308       32         +307 +312 +319  +305 19200 20480 19712  20992       21248 13
'                                                                      <i>     48          46</i>
'
'      <b>    Lower value = LCase/NumLock On __________________ + = add 100000 </b>
</pre>
</td></tr></tbody></table>
<p>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">         <b>65536-&amp;H40000000: QB64-specific Virtual Key codes:</b>
                        CONST KEY_PAUSE&amp; = 100019
                        CONST KEY_NUMLOCK&amp; = 100300
                        CONST KEY_CAPSLOCK&amp; = 100301
                        CONST KEY_SCROLLOCK&amp; = 100302
                        CONST KEY_RSHIFT&amp; = 100303
                        CONST KEY_LSHIFT&amp; = 100304
                        CONST KEY_RCTRL&amp; = 100305
                        CONST KEY_LCTRL&amp; = 100306
                        CONST KEY_RALT&amp; = 100307
                        CONST KEY_LALT&amp; = 100308
                        CONST KEY_RMETA&amp; = 100309 'Left 'Apple' key (macOS)
                        CONST KEY_LMETA&amp; = 100310 'Right 'Apple' key (macOS)
                        CONST KEY_LSUPER&amp; = 100311 'Left "Windows" key
                        CONST KEY_RSUPER&amp; = 100312 'Right "Windows"key
                        CONST KEY_MODE&amp; = 100313 '"AltGr" key
                        CONST KEY_COMPOSE&amp; = 100314
                        CONST KEY_HELP&amp; = 100315
                        CONST KEY_PRINT&amp; = 100316
                        CONST KEY_SYSREQ&amp; = 100317
                        CONST KEY_BREAK&amp; = 100318
                        CONST KEY_MENU&amp; = 100319
                        CONST KEY_POWER&amp; = 100320
                        CONST KEY_EURO&amp; = 100321
                        CONST KEY_UNDO&amp; = 100322
                        CONST KEY_KP0&amp; = 100256
                        CONST KEY_KP1&amp; = 100257
                        CONST KEY_KP2&amp; = 100258
                        CONST KEY_KP3&amp; = 100259
                        CONST KEY_KP4&amp; = 100260
                        CONST KEY_KP5&amp; = 100261
                        CONST KEY_KP6&amp; = 100262
                        CONST KEY_KP7&amp; = 100263
                        CONST KEY_KP8&amp; = 100264
                        CONST KEY_KP9&amp; = 100265
                        CONST KEY_KP_PERIOD&amp; = 100266
                        CONST KEY_KP_DIVIDE&amp; = 100267
                        CONST KEY_KP_MULTIPLY&amp; = 100268
                        CONST KEY_KP_MINUS&amp; = 100269
                        CONST KEY_KP_PLUS&amp; = 100270
                        CONST KEY_KP_ENTER&amp; = 100271
                        CONST KEY_KP_INSERT&amp; = 200000
                        CONST KEY_KP_END&amp; = 200001
                        CONST KEY_KP_DOWN&amp; = 200002
                        CONST KEY_KP_PAGE_DOWN&amp; = 200003
                        CONST KEY_KP_LEFT&amp; = 200004
                        CONST KEY_KP_MIDDLE&amp; = 200005
                        CONST KEY_KP_RIGHT&amp; = 200006
                        CONST KEY_KP_HOME&amp; = 200007
                        CONST KEY_KP_UP&amp; = 200008
                        CONST KEY_KP_PAGE_UP&amp; = 200009
                        CONST KEY_KP_DELETE&amp; = 200010
                        CONST KEY_SCROLL_LOCK_MODE&amp; = 200011
                        CONST KEY_INSERT_MODE&amp; = 200012
         <b>&amp;H40000000 up</b>: <a href="Unicode" title="Unicode">Unicode</a> using the <b>cyberbit.ttf</b> font when available.
              <b>Use <a href="KEYHIT" title="KEYHIT">_KEYHIT</a> to find the key codes to be monitored by _KEYDOWN! </b>
</pre>
</td></tr></tbody></table>
<p><i>Example 1:</i> Comparing the _KEYDOWN returns using <a href="CONST" title="CONST">constant</a> values with 2 byte <a href="INKEY$" title="INKEY$">INKEY$</a> returns.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> RSHIFT&amp; = 100303
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> LSHIFT&amp; = 100304
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    x = <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x = <a href="CVI" title="CVI"><span style="color:#4593D8;">CVI</span></a>(<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(59)) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_KEYDOWN</span></a>(LSHIFT&amp;) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_KEYDOWN</span></a>(RSHIFT&amp;) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "KEYHIT: SHIFT + F1"
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "KEYHIT: F1"
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    k$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>         'compare key press return values
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> k$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(59) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "INKEY$: F1"
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> k$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(84) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "INKEY$: SHIFT+F1"
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> k$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)     'escape key exit
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> How to calculate the _KEYDOWN codes of the 2 byte INKEY$ arrow key codes using <a href="CVI" title="CVI">CVI</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
x = 320: y = 240
col = <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 0, 0)
radius = 20
DO
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Use the arrow keys to move the circle."
    <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (x, y), radius, col
    <a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> (x, y), col
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_KEYDOWN</span></a>(<a href="CVI" title="CVI"><span style="color:#4593D8;">CVI</span></a>(<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "P")) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> y = y + 1   '_KEYDOWN(20480)
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_KEYDOWN</span></a>(<a href="CVI" title="CVI"><span style="color:#4593D8;">CVI</span></a>(<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "H")) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> y = y - 1   '_KEYDOWN(18432)
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_KEYDOWN</span></a>(<a href="CVI" title="CVI"><span style="color:#4593D8;">CVI</span></a>(<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "K")) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> x = x - 1   '_KEYDOWN(19200)
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_KEYDOWN</span></a>(<a href="CVI" title="CVI"><span style="color:#4593D8;">CVI</span></a>(<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "M")) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> x = x + 1   '_KEYDOWN(19712)
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 100 'limit to 100 frames per second
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> When <a href="CVI" title="CVI">CVI</a> is used with a 2 byte code, the code of the first character(0) is added to the second character code which is multiplied by 256. In the example, code zero is added to the <a href="ASCII" title="ASCII">ASCII</a> code of "P" which is 80. CVI multiplies 80 * 256 = 20480.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="KEYHIT" title="KEYHIT">_KEYHIT</a>, <a href="Unicode" title="Unicode">Unicode</a>, <a href="Code_Pages" title="Code Pages">Code Pages</a> (by region)</li>
<li><a href="MAPUNICODE" title="MAPUNICODE">_MAPUNICODE</a>, <a href="MAPUNICODE_(function)" title="MAPUNICODE (function)">_MAPUNICODE (function)</a></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a>, <a href="ASCII" title="ASCII">ASCII</a>, <a href="CVI" title="CVI">CVI</a></li>
<li><a href="INP" title="INP">INP</a>(&amp;H60), <a href="Scancodes" title="Scancodes">Scancodes</a></li>
<li><a href="ON_KEY(n)" title="ON KEY(n)">ON KEY(n)</a>, <a href="KEY(n)" title="KEY(n)">KEY(n)</a>, <a href="KEY_n" title="KEY n">KEY n</a></li>
<li><a href="Windows_Libraries#Hot_Keys_(maximize)" title="Windows Libraries">Windows hot keys</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192734
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.054 seconds
Real time usage: 0.078 seconds
Preprocessor visited node count: 482/1000000
Post‐expand include size: 4440/2097152 bytes
Template argument size: 711/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   34.385      1 -total
 17.19%    5.910     63 Template:Cl
 11.12%    3.825      2 Template:FixedStart
 10.59%    3.642      2 Template:CodeEnd
  8.84%    3.040      1 Template:PageSyntax
  8.25%    2.837      3 Template:Small
  8.00%    2.751      1 Template:PageSeeAlso
  7.41%    2.547      2 Template:CodeStart
  6.76%    2.325      1 Template:PageNavigation
  6.38%    2.194      2 Template:FixedEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:163-0!canonical and timestamp 20240714192734 and revision id 8987.
 -->
</div>
</div>
</div>
</div>
</body>
</html>