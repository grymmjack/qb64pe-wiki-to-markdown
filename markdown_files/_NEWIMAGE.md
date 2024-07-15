<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_NEWIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-NEWIMAGE rootpage-NEWIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_NEWIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_NEWIMAGE</a> function prepares a window image surface and returns the <a href="LONG" title="LONG">LONG</a> <a href="Handle" title="Handle">handle</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>handle&amp;</i> = <a class="mw-selflink selflink">_NEWIMAGE</a>(<i>width&amp;</i>, <i>height&amp;</i>[, {<i>0</i>|<i>1</i>|<i>2</i>|<i>7</i>|<i>8</i>|<i>9</i>|<i>10</i>|<i>11</i>|<i>12</i>|<i>13</i>|<i>256</i>|<i>32</i>}])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Minimum <a href="LONG" title="LONG">LONG</a> screen dimensions are <i>width&amp;</i> &gt;= 1, <i>height&amp;</i> &gt;= 1 measured in pixels as <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="LONG" title="LONG">LONG</a> values.
<ul><li>For mode 0 (text), <i>width&amp;</i> and <i>height&amp;</i> are measured in character blocks, not pixels.</li></ul></li>
<li>Mode is either a QBasic type <a href="SCREEN" title="SCREEN">screen</a> mode (0 to 2 or 7 to 13), 256 colors or 32 bit (16 million colors) compatible.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If the mode is omitted, an image will be created with the same BPP mode, font (which may block freeing of that font), palette, selected colors, transparent color, blend state and print method settings as the current <a href="DEST" title="DEST">_DESTination</a> image/<a href="SCREEN" title="SCREEN">screen</a> page.</li>
<li>Valid <a href="LONG" title="LONG">LONG</a> <a href="Handle" title="Handle">handle</a> returns are less than -1. Invalid handles equal -1 and a zero or positive value is also invalid.</li>
<li>You can create any sized window (limited by the OS) in any emulated <a href="SCREEN" title="SCREEN">SCREEN</a> mode or 32 bit using this function.</li>
<li>Default text block size in emulated <a href="SCREEN" title="SCREEN">SCREEN</a> modes 1, 2, 7, 8 and 13 is 8 X 8; 9 and 10 is 8 X 14; 11, 12, 256 and 32 bit is 8 X 16. The text block pixel size will allow you to calculate the available text rows and columns in a custom sized screen.</li>
<li>To view the image page, just use <a href="SCREEN" title="SCREEN">SCREEN</a> <i>handle&amp;</i>. Even if another procedure changes the screen mode and clears the screen, the image can be restored later by using the same SCREEN handle mode.</li>
<li>Use the <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a> function to preserve a SCREEN handle value when changing to another screen mode to restore it later.</li>
<li><b>32 bit screen surface backgrounds (black) have zero <a href="ALPHA" title="ALPHA">_ALPHA</a> so that they are transparent when placed over other surfaces.</b></li></ul>
<dl><dd>Use <a href="CLS" title="CLS">CLS</a> or <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> to make a new surface background <a href="ALPHA" title="ALPHA">_ALPHA</a> 255 or opague.</dd></dl>
<ul><li><b>Images are not deallocated when the <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> they are created in ends. Free them with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a>.</b></li>
<li><b>It is important to free unused or uneeded images with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a> to prevent CPU <a href="ERROR_Codes#Other_Errors" title="ERROR Codes">memory overflow errors</a>.</b></li>
<li><b>Do not try to free image handles currently being used as the active <a href="SCREEN" title="SCREEN">SCREEN</a>. Change screen modes first.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Shrinking a SCREEN 0 text window's size:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_NEWIMAGE</span></a>(28, 25, 0)
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Creating an 800 by 600 window version of SCREEN 12 with 256 colors (text 37 X 100):
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">handle&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 256)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> handle&amp;
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Setting up a 32 bit SCREEN with _NEWIMAGE for page flipping in QB64.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">SCREEN _NEWIMAGE(640, 480, 32), , 1, 0
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> <a href="DISPLAY" title="DISPLAY">_DISPLAY</a> may be used as a substitute for page flipping or <a href="PCOPY" title="PCOPY">PCOPY</a>.</dd></dl>
<p>
<i>Example 4:</i> Switching between two different SCREEN modes
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "Switching <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> modes"
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_NEWIMAGE</span></a> (800, 600, 256)
mode1&amp; = <a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a>               'get current screen mode handle
mode2&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_NEWIMAGE</span></a> (300, 200, 13)
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> mode2&amp;                  'prepare small window
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 10: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 13: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "mode2&amp; = "; mode2&amp;
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 13: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 16, 16: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "First"
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> mode1&amp;  'work in main window
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 5
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> c = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 248
   Color c: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> c;
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 44: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "mode1&amp; = "; mode1&amp;
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 11: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 30, 34: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press a key to goto Pop-up Window"
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> mode2&amp;  'switch to small window
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> mode1&amp;  'back to main window
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 37, 43: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "One more time!"
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> mode2&amp;  'back to small window
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 16, 16: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "LAST "
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="DEST_(function)" title="DEST (function)">_DEST</a> function can determine the present screen mode destination handle. The second _NEWIMAGE  handle is created using a SCREEN 13 palette(256 colors also). Each SCREEN is worked on after changing the destination with <a href="DEST" title="DEST">_DEST</a> <i>handle&amp;</i> statement. Images can be created before viewing them. When a key is pressed the second SCREEN created is displayed and so on.</dd></dl>
<dl><dd><b>Legacy SCREEN modes can also return a _DEST value, but the value will create a handle error.</b> To restore legacy screens get the<a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a> function value before changing screens. Then restore it using SCREEN oldmode&amp;.</dd></dl>
<h3><span class="mw-headline" id="More_examples">More examples</span></h3>
<ul><li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="PIXELSIZE" title="PIXELSIZE">_PIXELSIZE</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li><a href="SAVEIMAGE" title="SAVEIMAGE">_SAVEIMAGE</a></li>
<li><a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a></li>
<li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li>
<li><a href="CLIPBOARDIMAGE_(function)" title="CLIPBOARDIMAGE (function)">_CLIPBOARDIMAGE (function)</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192824
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.055 seconds
Real time usage: 0.065 seconds
Preprocessor visited node count: 616/1000000
Post‐expand include size: 3741/2097152 bytes
Template argument size: 643/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.416      1 -total
 15.59%    4.740     53 Template:Cl
 10.22%    3.110      1 Template:PageSeeAlso
  8.39%    2.553      1 Template:PageSyntax
  7.52%    2.286      8 Template:Parameter
  7.48%    2.276      4 Template:CodeEnd
  7.46%    2.269      1 Template:PageNavigation
  7.11%    2.163      4 Template:CodeStart
  6.99%    2.127      1 Template:PageParameters
  6.99%    2.126      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:199-0!canonical and timestamp 20240714192824 and revision id 8724.
 -->
</div>
</div>
</div>
</div>
</body>
</html>