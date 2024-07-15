<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LINE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LINE rootpage-LINE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LINE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LINE</a> statement is used in graphic <a href="SCREEN" title="SCREEN">SCREEN</a> modes to create lines or boxes.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">LINE</a> [STEP] [<b>(</b><i>column1</i><b>,</b> <i>row1</i><b>)</b>]<b>-</b>[STEP] <b>(</b><i>column2</i>, <i>row2</i><b>),</b> <i>color</i>[, [{B|BF}], <i>style%</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <a href="STEP" title="STEP">STEP</a> keyword make <i>column</i> and <i>row</i> coordinates relative to the previously coordinates set by any graphic statement.</li>
<li>The optional parameters (<i>column1</i>, <i>row1</i>) set the line's starting point.</li>
<li>The dash and second coordinate parameters (<i>column2</i>, <i>row2</i>) must be designated to complete the line or box.</li>
<li>The <a href="INTEGER" title="INTEGER">INTEGER</a> <i>color</i> attribute or <a href="LONG" title="LONG">LONG</a> <a href="RGB32" title="RGB32">_RGB32</a> 32 bit color value sets the drawing color.  If omitted, the current <a href="DEST" title="DEST">destination</a> page's <a href="DEFAULTCOLOR" title="DEFAULTCOLOR">_DEFAULTCOLOR</a> is used.</li>
<li>Optional <b>B</b> keyword creates a rectangle (<b>b</b>ox) using the start and end coordinates as diagonal corners. <b>BF</b> creates a <b>b</b>ox <b>f</b>illed.</li>
<li>The <i>style%</i> signed <a href="INTEGER" title="INTEGER">INTEGER</a> value sets a dotted pattern to draw the line or rectangle outline.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Creates a colored line between the given coordinates. Can be drawn partially off screen.</li>
<li><b>B</b> creates a box outline with each side parallel to the program screen sides. <b>BF</b> creates a filled box.</li>
<li><i>style%</i> can be used to create a dotted pattern to draw the line.
<ul><li><b>B</b> can be used with a <i>style%</i> to draw the rectangle outline using the desired pattern.</li>
<li><b>BF</b> ignores the <i>style%</i> parameter. See examples 2, 3 and 4 below.</li></ul></li>
<li>The graphic cursor is set to the center of the program window on program start. Using the <a href="STEP" title="STEP">STEP</a> keyword makes the coordinates relative to the current graphic cursor.</li>
<li><a class="mw-selflink selflink">LINE</a> <b>can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Following one line with another by omitting the second line's first coordinate parameter bracket entirely:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (100, 100)-(200, 200), 10    'creates a line
<a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> -(400, 200), 12              'creates a second line from end of first
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The full equivalent LINE statement would be: <b><span style="color:green;">LINE(200, 200)-(400, 200), 12</span></b></dd></dl>
<p>
<i>Example 2:</i> Creating styled lines and boxes with the LINE statement. Different style values create different dashed line spacing.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (100, 100)-(300, 300), 10, , 63    'creates a styled line
<a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (100, 100)-(300, 300), 12, B, 255  'creates styled box shape
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The first diagonal dashed green line bisects the red dashed square from Top Left to Bottom Right Corners.</dd></dl>
<p>
<i>Example 3:</i> The <i>style</i> value sets each 16 pixel line section as the value's bits are set on or off:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
<a href="FULLSCREEN" title="FULLSCREEN"><span style="color:#4593D8;">_FULLSCREEN</span></a> 'required in QB64 only
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 5
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 2 ^ 15 'use exponential value instead of -32768
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15:<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 5: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i%;
    <a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (10, 60)-(300, 60), 0 'erase previous lines
    <a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (10, 60)-(300, 60), 12, , i%
    tmp$ = ""
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> b% = 15 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -1 'create binary text value showing bits on as <span style="color:red;">█</span>, off as space
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> i% <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> 2 ^ b% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> tmp$ = tmp$ + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(219) <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> tmp$ = tmp$ + <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(1)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12:<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 20: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> tmp$;
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> 'any key exit
    <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> .001 'set delay time as required
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <i>style</i> value's Most Significant Bit (MSB) is set to the left with LSB on right as 16 text blocks are set on or off.</dd></dl>
<p>
<i>Example 4:</i> Using <a href="%26B" title="&amp;B">binary code</a> to design a style pattern:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (100, 100)-(300, 100), 10, , &amp;B0000111100001111 '16-bits
<a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (100, 110)-(300, 110), 11, , &amp;B0011001100110011
<a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (100, 120)-(300, 120), 12, , &amp;B0101010101010101
<a class="mw-selflink selflink"><span style="color:#4593D8;">LINE</span></a> (100, 130)-(300, 130), 13, , &amp;B1000100010001000
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The binary pattern created with 0s and 1s using the <a href="%26B" title="&amp;B">&amp;B</a> number prefix define the pattern to draw the colored lines.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="COLOR" title="COLOR">COLOR</a></li>
<li><a href="DRAW" title="DRAW">DRAW</a>, <a href="CIRCLE" title="CIRCLE">CIRCLE</a>, <a href="STEP" title="STEP">STEP</a></li>
<li><a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a></li>
<li><a href="AND" title="AND">AND</a>, <a href="OR" title="OR">OR</a> <span style="color:#777777;">(logical operators)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714153928
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.051 seconds
Preprocessor visited node count: 365/1000000
Post‐expand include size: 3252/2097152 bytes
Template argument size: 490/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.347      1 -total
 15.29%    3.571     43 Template:Cl
  8.79%    2.052      1 Template:PageSyntax
  8.75%    2.042      4 Template:CodeStart
  8.28%    1.934      3 Template:Text
  8.01%    1.870      4 Template:CodeEnd
  7.80%    1.822      1 Template:PageExamples
  6.70%    1.564      3 Template:Parameter
  6.64%    1.551      1 Template:PageSeeAlso
  6.29%    1.468      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:437-0!canonical and timestamp 20240714153928 and revision id 7898.
 -->
</div>
</div>
</div>
</div>
</body>
</html>