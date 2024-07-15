<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_KEYHIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-KEYHIT rootpage-KEYHIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_KEYHIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_KEYHIT</a> function returns <a href="ASCII" title="ASCII">ASCII</a> one and two byte, OpenGL Virtual Key and Unicode keyboard key press codes.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>keycode&amp;</i> = <a class="mw-selflink selflink">_KEYHIT</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Return values range up to &amp;H40000000 so use a <a href="LONG" title="LONG">LONG</a> or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> variable type. See the <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a> code list:</li></ul>
<dl><dd><ul><li>0-255: <a href="ASCII" title="ASCII">ASCII</a> values (Refer to <a class="extiw" href="https://en.wikipedia.org/wiki/Code_page_437" title="wikipedia:Code page 437">CP437</a>).</li>
<li>256-65535: <a href="ASCII#Two_Byte_Codes" title="ASCII">2-byte</a> character codes : code = <a href="CVI" title="CVI">CVI</a>(<a href="CHR$" title="CHR$">CHR$</a>(0) + <a href="CHR$" title="CHR$">CHR$</a>(scancode)) (unaffected by SHIFT/ALT/CTRL modifiers).</li>
<li>65536-&amp;H40000000: <a href="KEYDOWN" title="KEYDOWN">QB64-specific Virtual Key codes</a> (designated with + for 100000 on keyboard below)</li>
<li><b>Negative</b> <a href="LONG" title="LONG">LONG</a> values returned indicate that a key was released or a lock function key has been turned off.</li></ul></dd></dl>
<ul><li><b>Note: _KEYHIT can only return one value at a time so use the <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a> keyhit value to find key combinations.</b></li>
<li>To receive input from a <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> window, use <a href="CINP" title="CINP">_CINP</a>.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">'                                <b>_KEYHIT Keyboard Codes</b>
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
'     <b>    Lower value = LCase/NumLock On __________________ + = add 100000 </b>
</pre>
</td></tr></tbody></table>
<p>
</p>
<dl><dd><ul><li>&gt;= &amp;H40000000: <a href="Unicode" title="Unicode">Unicode</a>.</li></ul></dd></dl>
<ul><li>Font <b>cyberbit.ttf</b>, included with QB64 (<b>version 0.92 and up</b>), is required to facilitate the <b>IME</b>(in Chinese settings) only. The 12.7 MB font is free for <b>non-commercial</b> use and is not loaded unless the user switches to the <b>Input Mode Editor</b>. Set to "UNICODE".</li></ul>
<ul><li>QB64 can use several Windows fonts when <b>cyberbit</b> is not present so it is not necessary to include with program packages.</li>
<li>An <b>important difference</b> between <a href="INKEY$" title="INKEY$">INKEY$</a> and _KEYHIT is how they work when <b>CTRL, ALT</b> or <b>SHIFT</b> are used. INKEY$ returns a different code if you hold down CTRL, ALT or SHIFT before pressing  F1 (for example). _KEYHIT will return the same code regardless of which modifiers were used but you can check <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a> to see which modifying keys are being used.</li>
<li><b>Keyboards with an Alt Gr key note:</b> _KEYHIT may return both Alt (100307) and Ctrl (100306) codes when AltGr key is pressed or released.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> This routine will return the codes for any keyboard presses.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFLNG" title="DEFLNG"><span style="color:#4593D8;">DEFLNG</span></a> A-Z
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 8)
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , 1
font = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>("cyberbit.ttf", 24)
unifont = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>("cyberbit.ttf", 24, "UNICODE")
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> font
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  x = <a class="mw-selflink selflink"><span style="color:#4593D8;">_KEYHIT</span></a>
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &lt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>  'negative value means key released
      <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 2
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Released ";
      x = -x
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
      <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 10
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Pressed ";   'positive value means key pressed
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &lt; 256 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>    'ASCII code values
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "ASCII "; x;
      <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &gt;= 32 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x &lt;= 255 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[" + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(x) + "]" <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &gt;= 256 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x &lt; 65536 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> '2 byte key codes
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "2-BYTE-COMBO "; x <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> 255; x \ 256;
      x2 = x \ 256
      <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x2 &gt;= 32 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x2 &lt;= 255 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[" + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(x2) + "]" <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &gt;= 100000 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x &lt; 200000 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>      'QB84 Virtual Key codes
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "SDL VK"; x - 100000
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
      <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &gt;= 200000 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x &lt; <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>40000000 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "QB64 VK"; x - 200000
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &gt;= <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>40000000 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>              'Unicode values (IME Input mode)
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "UNICODE "; x - <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>40000000; "0x" + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(x - <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>40000000) + " ...";
      cx = <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(1): cy = <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a>
      <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> unifont
      <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> cy, cx
      <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15
      z$ = <a href="MKL$" title="MKL$"><span style="color:#4593D8;">MKL$</span></a>(x - <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>40000000) + <a href="MKL$" title="MKL$"><span style="color:#4593D8;">MKL$</span></a>(0)
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> z$ + z$ + z$;
      <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> font
      <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> cy, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a>, <a href="CINP" title="CINP">_CINP</a></li>
<li><a href="MAPUNICODE" title="MAPUNICODE">_MAPUNICODE</a>, <a href="MAPUNICODE_(function)" title="MAPUNICODE (function)">_MAPUNICODE (function)</a></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a>, <a href="ASCII" title="ASCII">ASCII</a> <span style="color:#777777;">(code table)</span>,</li>
<li><a href="Unicode" title="Unicode">Unicode</a>, <a href="Code_Pages" title="Code Pages">Code Pages</a> <span style="color:#777777;">(by region)</span></li>
<li><a href="INP" title="INP">INP</a>(<a href="%26H" title="&amp;H">&amp;H60</a>), <a href="Scancodes" title="Scancodes">Scancodes</a></li>
<li><a href="ON_KEY(n)" title="ON KEY(n)">ON KEY(n)</a>, <a href="KEY(n)" title="KEY(n)">KEY(n)</a>, <a href="KEY_n" title="KEY n">KEY n</a></li>
<li><a href="Windows_Libraries#Hot_Keys_(maximize)" title="Windows Libraries">Windows hot keys</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034357
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.066 seconds
Real time usage: 0.077 seconds
Preprocessor visited node count: 584/1000000
Post‐expand include size: 4998/2097152 bytes
Template argument size: 843/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   39.384      1 -total
 15.67%    6.173     76 Template:Cl
  7.35%    2.893      1 Template:PageSyntax
  6.48%    2.554      1 Template:CodeEnd
  6.03%    2.373      2 Template:Text
  5.84%    2.300      1 Template:PageSeeAlso
  5.80%    2.286      1 Template:PageNavigation
  5.69%    2.241      1 Template:Parameter
  5.52%    2.175      1 Template:FixedStart
  5.40%    2.126      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:162-0!canonical and timestamp 20240715034357 and revision id 8988.
 -->
</div>
</div>
</div>
</div>
</body>
</html>