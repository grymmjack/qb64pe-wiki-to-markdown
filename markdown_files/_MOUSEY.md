<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MOUSEY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOUSEY rootpage-MOUSEY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MOUSEY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MOUSEY</a> function returns the current vertical (row) mouse cursor position when read after <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixelRow%</i> = <a class="mw-selflink selflink">_MOUSEY</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a href="SCREEN" title="SCREEN">SCREEN</a> 0 returns the <a href="INTEGER" title="INTEGER">INTEGER</a> vertical text row position (from build 20170817/62 onward); older versions return a <a href="SINGLE" title="SINGLE">SINGLE</a> vertical text row position. Use <a href="INTEGER" title="INTEGER">INTEGER</a> variables to avoid floating decimal returns.</li>
<li>Graphic screen modes 1, 2 and 7 to 13 and <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> 32 bit return the <a href="INTEGER" title="INTEGER">INTEGER</a> pixel columns.</li>
<li>To calculate text rows in graphic modes divide the return by 16 or the <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a> of <a href="FONT" title="FONT">_FONT</a> characters.</li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> must be used to detect any changes in the mouse position and is <b>required</b> for any coordinate returns.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>In <a href="SCREEN" title="SCREEN">SCREEN</a> 0, QBasic's <a href="CALL_ABSOLUTE" title="CALL ABSOLUTE">ABSOLUTE</a> returned graphic coordinates. QB64 mouse functions return the text coordinates.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Highlighting a row of text in Screen 0.
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
    x = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
    y = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEY</span></a>
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
  <a href="POKE" title="POKE"><span style="color:#4593D8;">POKE</span></a> addr&amp;, oldCol <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> ((col <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>111) * <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>10000) ' Apply background color
  addr&amp; = addr&amp; + 2
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a>, <a href="MOUSEWHEEL" title="MOUSEWHEEL">_MOUSEWHEEL</a></li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>, <a href="MOUSEMOVE" title="MOUSEMOVE">_MOUSEMOVE</a></li>
<li><a href="MOUSESHOW" title="MOUSESHOW">_MOUSESHOW</a>, <a href="MOUSEHIDE" title="MOUSEHIDE">_MOUSEHIDE</a></li>
<li><a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a>, <a href="MOUSEMOVEMENTY" title="MOUSEMOVEMENTY">_MOUSEMOVEMENTY</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714213002
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.077 seconds
Real time usage: 0.105 seconds
Preprocessor visited node count: 382/1000000
Post‐expand include size: 3096/2097152 bytes
Template argument size: 474/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   37.705      1 -total
 15.29%    5.767     48 Template:Cl
 14.84%    5.596      1 Template:PageSyntax
 12.23%    4.611      1 Template:PageDescription
  9.22%    3.478      1 Template:PageExamples
  7.79%    2.939      1 Template:CodeStart
  7.66%    2.890      1 Template:CodeEnd
  7.40%    2.790      1 Template:Parameter
  7.22%    2.721      1 Template:PageSeeAlso
  6.92%    2.608      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:198-0!canonical and timestamp 20240714213002 and revision id 7625.
 -->
</div>
</div>
</div>
</div>
</body>
</html>