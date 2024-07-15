<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>WIDTH - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WIDTH rootpage-WIDTH skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">WIDTH</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>WIDTH</b> statement changes the text dimensions of certain <b>SCREEN</b> modes or devices.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dt>For SCREEN</dt>
<dd><ul><li><b>WIDTH</b> [<i>columns%</i>] [,<i>rows%</i>]</li></ul></dd></dl>
<dl><dt>For CONSOLE (Windows Console Only)</dt>
<dd><ul><li><b>WIDTH</b> [<i>columns%</i>] [,<i>rows%</i>] [,<i>buffer_columns%</i>] [,<i>buffer_rows%</i>]</li></ul></dd></dl>
<dl><dt>For Files</dt>
<dd><ul><li><b>WIDTH</b> <i>file_number | device</i>, <i>columnwidth%</i></li></ul></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>When parameters are not specified, columns defaults to 80 with 25 (30 in <a href="SCREEN" title="SCREEN">SCREEN</a> 11 or 12) rows.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>WIDTH</b> should be used after a program <a href="SCREEN" title="SCREEN">SCREEN</a> statement. It does not affect screen graphics or graphic coordinates.</li>
<li>Affects SCREEN 0 Window size and alters the text block size of each screen mode listed in QBasic:</li></ul>
<dl><dd><ul><li>SCREEN 0 can use 80 or 40 columns and 25, 43 or 50 rows. Default is <b>WIDTH</b> 80, 25.</li>
<li>SCREEN 9 can use 80 columns and 25 or 43(not supported on many monitors) rows. Default <b>WIDTH</b> 80, 25 fullscreen.</li>
<li>SCREEN 10 can use 80 columns and 25 or 43 rows. Default is <b>WIDTH</b> 80, 25 fullscreen.</li>
<li>SCREEN 11 and 12 can use 80 columns and 30 or 60 rows. Default is <b>WIDTH</b> 80, 30 fullscreen.</li></ul></dd></dl>
<ul><li><b>QB64</b> can alter all <a href="SCREEN" title="SCREEN">SCREEN</a> mode widths and heights which may also affect text or <a href="FONT" title="FONT">_FONT</a> block sizes.</li>
<li>If a <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> window is active and you set <a href="DEST" title="DEST">_DEST</a> <a href="CONSOLE" title="CONSOLE">_CONSOLE</a>, <b>WIDTH</b> will affect the console output window size (Windows only), with the last two optional parameters setting the buffer size for the console.  (For example, you can set a console to be 80 characters x 25 lines for the display, with a buffer size of 300 characters and 100 lines, which allows you to display that much information and navigate the visible display with the scroll bars.)</li></ul>
<dl><dt>Note</dt>
<dd><ul><li><b>WIDTH</b> changes may change screen color settings in QBasic. Use <a href="PALETTE" title="PALETTE">PALETTE</a> to reset to default colors.</li>
<li><b>WIDTH LPRINT</b> is not supported in QB64.</li></ul></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd><ul><li>Showing the use of the buffer parameters for <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> usage.</li>
<li>The program creates more output than fits to the display, but the buffer preserves the output and you can scroll back and forth.</li></ul></dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$CONSOLE" title="$CONSOLE"><span style="color:#4593D8;">$CONSOLE:ONLY</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">WIDTH</span></a> 80, 25, 300, 100
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">TO</span></a> 97
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(100, "0") + <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(100, "1") + <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(100, "2") 'print the 100's placeholders
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> j = 1 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">TO</span></a> 3
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">TO</span></a> 9
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(10, <a href="TRIM$" title="TRIM$"><span style="color:#4593D8;">_TRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(i))); 'print the 10's placeholders
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> j = 1 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">TO</span></a> 30
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">TO</span></a> 9
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="TRIM$" title="TRIM$"><span style="color:#4593D8;">_TRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(i)); 'print the 1's placeholders.
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1276" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="COLOR" title="COLOR">COLOR</a>, <a href="OUT" title="OUT">OUT</a></li>
<li><a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a></li>
<li><a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH (function)</a>, <a href="HEIGHT" title="HEIGHT">_HEIGHT</a></li>
<li><a href="FONT" title="FONT">_FONT</a>, <a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a>, <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714160850
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.044 seconds
Real time usage: 0.055 seconds
Preprocessor visited node count: 275/1000000
Post‐expand include size: 2458/2097152 bytes
Template argument size: 466/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 1/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.909      1 -total
 10.83%    3.130     31 Template:Cl
 10.71%    3.097      1 Template:PageSyntax
 10.34%    2.990      8 Template:Parameter
  9.00%    2.602      1 Template:CodeStart
  8.89%    2.569      1 Template:PageExamples
  8.51%    2.461      1 Template:PageParameters
  8.38%    2.421      1 Template:PageDescription
  7.68%    2.221      1 Template:PageNavigation
  7.54%    2.179      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:427-0!canonical and timestamp 20240714160850 and revision id 8922.
 -->
</div>
</div>
</div>
</div>
</body>
</html>