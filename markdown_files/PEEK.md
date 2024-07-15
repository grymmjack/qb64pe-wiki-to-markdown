<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PEEK - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PEEK rootpage-PEEK skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PEEK</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>PEEK</b> function returns the value that is contained at a certain memory address offset. <b>QB64 currently has limited access!</b>
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>variable = PEEK(<i>segment_offset</i>)</dd></dl></dd></dl>
<p>
</p>
<ul><li>Reads the specified memory <i>segment_offset</i> value.</li>
<li>Use <a href="DEF_SEG" title="DEF SEG">DEF SEG</a> before PEEK to specify which memory segment to work in.</li>
<li>PEEK only reads the memory byte value. Not certain bits. (See <a href="AND" title="AND">AND</a>)</li>
<li>Important <a href="SCREEN" title="SCREEN">SCREEN</a> segments using <a class="mw-selflink selflink">PEEK</a> and <a href="POKE" title="POKE">POKE</a> include &amp;HB800 (text segment) and &amp;HA000 (graphics segment).</li>
<li>To return to Basic default segment use <a href="DEF_SEG" title="DEF SEG">DEF SEG</a> without any arguments.</li>
<li><b>Warning: DEF SEG, VARSEG , VARPTR, PEEK or POKE access QB64's emulated 16 bit conventional memory block!</b></li></ul>
<dl><dd><b>It is highly recommended that QB64's <a href="MEM" title="MEM">_MEM</a> memory system be used to avoid running out of memory.</b></dd></dl>
<p>
<i>Example:</i> Checking the 8 keyboard bit settings using a PEEK return value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> SCREEN 12
 <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = 0 ' BIOS area
 oldvalue = PEEK(1047) ' IMPORTANT! save initial setting to reset later
 DO: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 100
   port = <a class="mw-selflink selflink"><span style="color:#4593D8;">PEEK</span></a>(1047)
   IF port &gt; 0 THEN LOCATE 26, 19: COLOR 11:
      PRINT "Turn ALL Locks off to see each key's bit value!"
   END IF
 COLOR 14:LOCATE 2, 25
 PRINT "PEEK(1047) ="; port; "present keyboard port byte value"
 LOCATE 5, 35
 IF (port <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> 1) = 1 THEN COLOR 10: PRINT "R SHIFT PRESSED  " ELSE COLOR 12: PRINT "R SHIFT RELEASED"
 LOCATE 7, 35
 IF (port AND 2) = 2 THEN COLOR 10: PRINT "L SHIFT PRESSED  " ELSE COLOR 12: PRINT "L SHIFT RELEASED"
 LOCATE 9, 35
 IF (port AND 4) = 4 THEN COLOR 10: PRINT "CTRL KEY PRESSED " ELSE COLOR 12: PRINT "CTRL KEY RELEASED"
 LOCATE 11, 35
 IF (port AND 8) = 8 THEN COLOR 10: PRINT "ALT KEY PRESSED " ELSE COLOR 12: PRINT "ALT KEY RELEASED"
 LOCATE 13, 35
 IF (port AND 16) = 16 THEN COLOR 10: PRINT "SCROLL LOCK ON " ELSE COLOR 12: PRINT "SCROLL LOCK OFF"
 LOCATE 15, 35
 IF (port AND 32) = 32 THEN COLOR 10: PRINT "NUMBER LOCK ON " ELSE COLOR 12: PRINT "NUMBER LOCK OFF"
 LOCATE 17, 35
 IF (port AND 64) = 64 THEN COLOR 10: PRINT "CAPS LOCK ON " ELSE COLOR 12: PRINT "CAPS LOCK OFF"
 LOCATE 19, 35
 IF (port AND 128) = 128 THEN COLOR 10: PRINT "INSERT MODE ON " ELSE COLOR 12: PRINT "INSERT MODE OFF"
 COLOR 11: LOCATE 21, 20: PRINT "Press mode keys to change or [ESC] to quit!";
 LOOP UNTIL <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(&amp;H60) = 1 ' escape key exit
 <a href="POKE" title="POKE"><span style="color:#4593D8;">POKE</span></a> 1047, oldvalue      ' IMPORTANT reset to original settings
 <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><b>NOTE: Keyboard Port function key settings cannot be reset on NT machines!</b></dd></dl>
<h3><span class="mw-headline" id="More_Examples">More Examples</span></h3>
<ul><li><a href="SelectScreen" title="SelectScreen">SelectScreen</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="POKE" title="POKE">POKE</a>, <a href="INP" title="INP">INP</a></li>
<li><a href="DEF_SEG" title="DEF SEG">DEF SEG</a>, <a href="VARSEG" title="VARSEG">VARSEG</a>, <a href="VARPTR" title="VARPTR">VARPTR</a></li>
<li><a href="MEMGET_(function)" title="MEMGET (function)">_MEMGET (function)</a>, <a href="MEMPUT" title="MEMPUT">_MEMPUT</a></li>
<li><a href="DEF_SEG_%3D_0" title="DEF SEG = 0">DEF SEG = 0</a>, <a href="Scancodes" title="Scancodes">Scancodes</a></li>
<li><a href="PEEK_and_POKE_Library" title="PEEK and POKE Library">PEEK and POKE Library</a></li>
<li><a href="Screen_Memory" title="Screen Memory">Screen Memory</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192524
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.021 seconds
Real time usage: 0.026 seconds
Preprocessor visited node count: 92/1000000
Post‐expand include size: 928/2097152 bytes
Template argument size: 68/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   11.704      1 -total
 18.11%    2.120      7 Template:Cl
 17.80%    2.083      1 Template:PageSyntax
 14.99%    1.755      1 Template:CodeStart
 14.85%    1.738      1 Template:CodeEnd
 13.52%    1.582      1 Template:PageNavigation
 12.99%    1.520      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:501-0!canonical and timestamp 20240714192524 and revision id 7643.
 -->
</div>
</div>
</div>
</div>
</body>
</html>