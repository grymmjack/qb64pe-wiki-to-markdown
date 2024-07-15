<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PRINTWIDTH - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PRINTWIDTH rootpage-PRINTWIDTH skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PRINTWIDTH</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_PRINTWIDTH</a> function returns the width in pixels of the text <a href="STRING" title="STRING">string</a> specified.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixelWidth%</i> = <a class="mw-selflink selflink">_PRINTWIDTH</a>(<i>textToPrint$</i>[, <i>destinationHandle&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>textToPrint$</i> is any literal or variable <a href="STRING" title="STRING">STRING</a> value.</li>
<li>If the <i>destinationHandle&amp;</i> is omitted, the current destination image or screen page is used.</li>
<li>Useful to find the width of the font print <a href="STRING" title="STRING">string</a> before actually printing it.</li>
<li>Can be used with variable-width fonts or built-in fonts, unlike <a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a> which requires a MONOSPACE font handle.</li>
<li>In SCREEN 0, _PRINTWIDTH returns the character length of a text string, exactly as <a href="LEN" title="LEN">LEN</a>(<i>textToPrint$</i>) (<b>version 1.000 and up</b>).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> SUB returns font or screen mode's text block size using _PRINTWIDTH and <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a> without a handle parameter.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter Screen mode 1, 2 or 7 to 13: ", scr$
  mode% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(scr$)
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> mode% &gt; 0
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> mode%
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter first name of TTF font to use or hit enter for text size: ", TTFont$
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(TTFont$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> "Enter font height: ", hi$
height&amp; = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(hi$)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> height&amp; &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>("C:\Windows\Fonts\" + TTFont$ + ".ttf", height&amp;, style$)
TextSize wide&amp;, high&amp;       'get the font or current screen mode's text block pixel size
<a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (20, 100), <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(1) + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(wide&amp;) + " X" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(high&amp;) + " " + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(2)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> TextSize (TextWidth&amp;, TextHeight&amp;)
TextWidth&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTWIDTH</span></a>("W")     'measure width of one font or text character
TextHeight&amp; = <a href="FONTHEIGHT" title="FONTHEIGHT"><span style="color:#4593D8;">_FONTHEIGHT</span></a>         'can measure normal text block heights also
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a>, <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li>
<li><a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a>, <a href="FONT" title="FONT">_FONT</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192834
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.042 seconds
Preprocessor visited node count: 232/1000000
Post‐expand include size: 2239/2097152 bytes
Template argument size: 378/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.584      1 -total
 25.29%    6.976      1 Template:Small
 10.52%    2.902      6 Template:Parameter
  9.27%    2.556      1 Template:PageSeeAlso
  9.03%    2.491     26 Template:Cl
  8.33%    2.298      1 Template:PageSyntax
  7.36%    2.029      1 Template:CodeEnd
  5.96%    1.643      1 Template:PageNavigation
  5.76%    1.589      1 Template:PageDescription
  5.43%    1.497      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:256-0!canonical and timestamp 20240714192834 and revision id 7932.
 -->
</div>
</div>
</div>
</div>
</body>
</html>