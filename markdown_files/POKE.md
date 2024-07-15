<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>POKE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-POKE rootpage-POKE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">POKE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>POKE</b> statement sets the value of a specified memory address offset. <b>QB64 currently has limited access!</b>
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>POKE <i>segment_offset</i>, <i>offset_value</i></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Writes a value to the <i>segment_offset</i> address in memory.</li>
<li>POKE can only be used to set a value from 0 to 255 (one byte).</li>
<li>A segment should be defined using <a href="DEF_SEG" title="DEF SEG">DEF SEG</a>, if you don't define a segment QBasic's ordinary segment will be used.</li>
<li>POKE sends byte values to memory areas. It does not directly access registers.</li>
<li>Important <a href="SCREEN" title="SCREEN">SCREEN</a> segments using <a href="PEEK" title="PEEK">PEEK</a> and <a class="mw-selflink selflink">POKE</a> include &amp;HB800 (text segment) and &amp;HA000 (graphics segment).</li>
<li><a href="DEF_SEG" title="DEF SEG">DEF SEG</a> should always be used to reset the default segment when access to other memory is no longer necessary.</li>
<li>POKE is safer to use than <a href="OUT" title="OUT">OUT</a> which could damage a PC register.</li>
<li><b>Warning: DEF SEG, VARSEG , VARPTR, PEEK or POKE access QB64's emulated 16 bit conventional memory block!</b></li></ul>
<dl><dd><b>It is highly recommended that QB64's <a href="MEM" title="MEM">_MEM</a> memory system be used to avoid running out of memory.</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dd><i>Example 1:</i> Turning keyboard Lock and Insert modes on and off.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> DEF SEG = 0
 oldsetting% = PEEK(1047)
 POKE 1047,PEEK(1047) OR 16 ' ENABLES SCROLL LOCK
 POKE 1047,PEEK(1047) OR 32 ' ENABLES NUMBER LOCK
 POKE 1047,PEEK(1047) OR 64 ' ENABLES CAPS LOCK
 POKE 1047,PEEK(1047) OR 128 ' ENABLES INSERT MODE
 DEF SEG
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note: Use <a class="mw-redirect" href="XOR" title="XOR">XOR</a> instead of <a href="OR" title="OR">OR</a> above to alternate between on and off modes.</i></dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = 0
 oldsetting% = <a href="PEEK" title="PEEK"><span style="color:#4593D8;">PEEK</span></a>(1047)
 POKE 1047,PEEK(1047) AND 239 ' TURNS OFF SCROLL LOCK (239 = 255 - 16)
 POKE 1047,PEEK(1047) AND 223 ' TURNS OFF NUMBER LOCK (223 = 255 - 32)
 POKE 1047,PEEK(1047) AND 191 ' TURNS OFF CAPS LOCK (191 = 255 - 64)
 POKE 1047,PEEK(1047) AND 127 ' TURNS OFF INSERT MODE (127 = 255 - 128)
 <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note: Using <a href="AND" title="AND">AND</a> requires that the bit value is subtracted from 255 to turn off a bit.</i> The above examples won't work in NT.</dd></dl>
<dl><dd><b>Warning: The keyboard lights may NOT change so it is a good idea to restore the original settings!</b></dd></dl>
<p>
<i>Example 2:</i> A small PEEK and POKE fractal program.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>A000     'set to read screen buffer
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> a&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 65535
        <a class="mw-selflink selflink"><span style="color:#4593D8;">POKE</span></a> a&amp;, <a href="PEEK" title="PEEK"><span style="color:#4593D8;">PEEK</span></a>((a&amp; * 2) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FFFF&amp;) + 1
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 25
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Highlighting a row of text in Screen 0
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">minX = 20: maxX = 60: minY = 10: maxY = 24
selection = 0 'the screen Y coordinate of the previously highlighted item
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i% = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 25: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> i%, 40: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i%;: <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 100
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    'Un-highlight any selected row
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> selection <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> selectRow selection, minX, maxX, 0
    x = <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(<a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>)
    y = <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(<a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &gt;= minX <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x &lt;= maxX <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y &gt;= minY <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y &lt;= maxY <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      selection = y
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
      selection = 0
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    'Highlight any selected row
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> selection <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> SelectRow selection, minX, maxX, 2
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x, y, selection
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> SelectRow (y, x1, x2, col)
<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>B800
addr&amp; = (x1 - 1 + (y - 1) * <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>) * 2 + 1
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = x1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> x2
  oldCol = <a href="PEEK" title="PEEK"><span style="color:#4593D8;">PEEK</span></a>(addr&amp;) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>10001111   ' Mask foreground color and blink bit
  <a class="mw-selflink selflink"><span style="color:#4593D8;">POKE</span></a> addr&amp;, oldCol <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> ((col <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>111) * <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>10000) ' Apply background color
  addr&amp; = addr&amp; + 2
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="More_Examples">More Examples</span></h3>
<ul><li><a href="SelectScreen" title="SelectScreen">SelectScreen</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEF_SEG" title="DEF SEG">DEF SEG</a>, <a href="DEF_SEG_%3D_0" title="DEF SEG = 0">DEF SEG = 0</a></li>
<li><a href="PEEK" title="PEEK">PEEK</a>, <a href="OUT" title="OUT">OUT</a></li>
<li><a href="VARSEG" title="VARSEG">VARSEG</a>, <a href="VARPTR" title="VARPTR">VARPTR</a></li>
<li><a href="MEMGET_(function)" title="MEMGET (function)">_MEMGET (function)</a>, <a href="MEMPUT" title="MEMPUT">_MEMPUT</a></li>
<li><a href="Scancodes" title="Scancodes">Scancodes</a>, <a href="Screen_Memory" title="Screen Memory">Screen Memory</a></li>
<li><a href="PEEK_and_POKE_Library" title="PEEK and POKE Library">PEEK and POKE Library</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061359
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.056 seconds
Real time usage: 0.089 seconds
Preprocessor visited node count: 684/1000000
Post‐expand include size: 4351/2097152 bytes
Template argument size: 668/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.028      1 -total
 17.60%    4.934     69 Template:Cl
 10.90%    3.055      1 Template:PageSyntax
 10.88%    3.050      1 Template:PageSeeAlso
 10.61%    2.975      1 Template:PageExamples
  9.35%    2.621      1 Template:PageNavigation
  8.90%    2.494      1 Template:PageDescription
  8.54%    2.394      4 Template:CodeStart
  7.51%    2.104      4 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:500-0!canonical and timestamp 20240715061359 and revision id 7715.
 -->
</div>
</div>
</div>
</div>
</body>
</html>