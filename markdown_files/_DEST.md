<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DEST - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEST rootpage-DEST skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DEST</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DEST</a> statement sets the current write image or page. All graphic and print changes will be done to this image.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_DEST</a> <i>imageHandle&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>imageHandle&amp;</i> is the handle of the image that will act as the current write page.</li>
<li><b>_DEST 0</b> refers to the present program <a href="SCREEN" title="SCREEN">SCREEN</a>. You can use 0 to refer to the present program <a href="SCREEN" title="SCREEN">SCREEN</a>.</li>
<li><a class="mw-selflink selflink">_DEST</a> <a href="CONSOLE" title="CONSOLE">_CONSOLE</a> can set the destination to send information to a console window using <a href="PRINT" title="PRINT">PRINT</a> or <a href="INPUT" title="INPUT">INPUT</a>.</li>
<li>If <i>imageHandle&amp;</i> is an invalid handle, an <a href="ERROR_Codes" title="ERROR Codes">invalid handle</a> error occurs. Always check for valid handle values first (<i>imageHandle&amp;</i> &lt; -1).</li>
<li><i>Note:</i> Use <a href="SOURCE" title="SOURCE">_SOURCE</a> when you need to read a page or image with <a href="POINT" title="POINT">POINT</a>, <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> or the <a href="SCREEN_(function)" title="SCREEN (function)">SCREEN</a> function.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Placing a center point and a circle using <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a> to eliminate the background color black.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">13</span> <span style="color:#919191;">'program screen can use 256 colors</span>
a&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">320</span>, <span style="color:#F580B1;">200</span>, <span style="color:#F580B1;">13</span>) <span style="color:#919191;">'create 2 screen page handles a&amp; and b&amp;</span>
b&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">320</span>, <span style="color:#F580B1;">200</span>, <span style="color:#F580B1;">13</span>)
<a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> a&amp; <span style="color:#919191;">'set destination image to handle a&amp;</span>
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (<span style="color:#F580B1;">100</span>, <span style="color:#F580B1;">100</span>), <span style="color:#F580B1;">15</span> <span style="color:#919191;">'draw a dot on the current destination handle a&amp;</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> b&amp; <span style="color:#919191;">'set destination image to handle b&amp;</span>
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (<span style="color:#F580B1;">100</span>, <span style="color:#F580B1;">100</span>), <span style="color:#F580B1;">50</span>, <span style="color:#F580B1;">15</span> <span style="color:#919191;">'draw a circle on the current destination handle b&amp;</span>
<a href="CLEARCOLOR" title="CLEARCOLOR"><span style="color:#4593D8;">_CLEARCOLOR</span></a> <span style="color:#F580B1;">0</span> <span style="color:#919191;">'make page b color 0 (black) transparent</span>
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , b&amp;, a&amp; <span style="color:#919191;">'put circle on image b to image a&amp; (a PSET dot)</span>
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , a&amp;, <span style="color:#F580B1;">0</span> <span style="color:#919191;">'put what is on image a&amp; to the screen (handle 0)</span>
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> Demonstrates how <a href="PRINT" title="PRINT">printed</a> text can be stretched using <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a> with <a class="mw-selflink selflink">_DEST</a> pages.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> a(<span style="color:#F580B1;">10</span>) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> b <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="REM" title="REM"><span style="color:#4593D8;">REM</span></a><span style="color:#919191;"> Sets up a newimage for B then sets the screen to that.</span>
b = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> b
<a href="REM" title="REM"><span style="color:#4593D8;">REM</span></a><span style="color:#919191;"> Make pages 48 pixels tall. If the image is not at least that it wont work</span>
a(<span style="color:#F580B1;">1</span>) = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">240</span>, <span style="color:#F580B1;">48</span>, <span style="color:#F580B1;">32</span>)
a(<span style="color:#F580B1;">2</span>) = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">240</span>, <span style="color:#F580B1;">48</span>, <span style="color:#F580B1;">32</span>)
a(<span style="color:#F580B1;">3</span>) = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">98</span>, <span style="color:#F580B1;">48</span>, <span style="color:#F580B1;">32</span>)
xa = <span style="color:#F580B1;">100</span>
ya = <span style="color:#F580B1;">120</span>
xm = <span style="color:#F580B1;">4</span>
ym = <span style="color:#F580B1;">4</span>
<a href="REM" title="REM"><span style="color:#4593D8;">REM</span></a><span style="color:#919191;"> Some fun things for the bouncing text.</span>
st$(<span style="color:#F580B1;">0</span>) = <span style="color:#FFB100;">"doo"</span>
st$(<span style="color:#F580B1;">1</span>) = <span style="color:#FFB100;">"rey"</span>
st$(<span style="color:#F580B1;">2</span>) = <span style="color:#FFB100;">"mee"</span>
st$(<span style="color:#F580B1;">3</span>) = <span style="color:#FFB100;">"faa"</span>
st$(<span style="color:#F580B1;">4</span>) = <span style="color:#FFB100;">"soo"</span>
st$(<span style="color:#F580B1;">5</span>) = <span style="color:#FFB100;">"laa"</span>
st$(<span style="color:#F580B1;">6</span>) = <span style="color:#FFB100;">"tee"</span>
sta$(<span style="color:#F580B1;">0</span>) = <span style="color:#FFB100;">"This is a demo"</span>
sta$(<span style="color:#F580B1;">1</span>) = <span style="color:#FFB100;">"showing how to use"</span>
sta$(<span style="color:#F580B1;">2</span>) = <span style="color:#FFB100;">"the _DEST command"</span>
sta$(<span style="color:#F580B1;">3</span>) = <span style="color:#FFB100;">"with PRINT"</span>
sta$(<span style="color:#F580B1;">4</span>) = <span style="color:#FFB100;">"and _PUTIMAGE"</span>
<a href="REM" title="REM"><span style="color:#4593D8;">REM</span></a><span style="color:#919191;"> prints to a(3) image then switches back to the default 0</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> a(<span style="color:#F580B1;">3</span>): f = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">6</span>): <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> st$(<span style="color:#F580B1;">3</span>): <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> <span style="color:#F580B1;">0</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="REM" title="REM"><span style="color:#4593D8;">REM</span></a><span style="color:#919191;"> prints to a(1) and a(2) then switches bac to 0</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> a(<span style="color:#F580B1;">1</span>)
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> sta(r)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> a(<span style="color:#F580B1;">2</span>)
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> sta(r + <span style="color:#F580B1;">1</span>)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> <span style="color:#F580B1;">0</span> <span style="color:#919191;">'destination zero is the main program page</span>
    <a href="REM" title="REM"><span style="color:#4593D8;">REM</span></a><span style="color:#919191;"> a loop to putimage the images in a(1) and a(2) in a way to make it look like its rolling</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> yat = <span style="color:#F580B1;">150</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">380</span> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> <span style="color:#F580B1;">4</span>
        <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
        <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<span style="color:#F580B1;">0</span>, yat)-(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">380</span>), a(<span style="color:#F580B1;">1</span>)
        <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">150</span>)-(<span style="color:#F580B1;">640</span>, yat), a(<span style="color:#F580B1;">2</span>)
        <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> bounce
        <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
        <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">20</span>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> yat
    r = r + <span style="color:#F580B1;">1</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> r = <span style="color:#F580B1;">4</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> r = <span style="color:#F580B1;">0</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
bounce:
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> xa &gt; <span style="color:#F580B1;">600</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> xa &lt; <span style="color:#F580B1;">20</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> xm = xm * <span style="color:#F580B1;">-1</span>: <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> a(<span style="color:#F580B1;">3</span>): f = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">6</span>): <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>: <a href="CLEARCOLOR" title="CLEARCOLOR"><span style="color:#4593D8;">_CLEARCOLOR</span></a> <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> st$(f): <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> <span style="color:#F580B1;">0</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> ya &gt; <span style="color:#F580B1;">400</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> ya &lt; <span style="color:#F580B1;">20</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ym = ym * <span style="color:#F580B1;">-1</span>: <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> a(<span style="color:#F580B1;">3</span>): f = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">7</span>): <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>: <a href="CLEARCOLOR" title="CLEARCOLOR"><span style="color:#4593D8;">_CLEARCOLOR</span></a> <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> st$(f): <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEST</span></a> <span style="color:#F580B1;">0</span>
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (xa, ya)-(xa + <span style="color:#F580B1;">150</span>, ya + <span style="color:#F580B1;">80</span>), a(<span style="color:#F580B1;">3</span>)
xa = xa + xm
ya = ya + ym
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEST_(function)" title="DEST (function)">_DEST (function)</a></li>
<li><a href="SOURCE" title="SOURCE">_SOURCE</a></li>
<li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a></li>
<li><a href="CONSOLE" title="CONSOLE">_CONSOLE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192703
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.060 seconds
Real time usage: 0.069 seconds
Preprocessor visited node count: 1490/1000000
Post‐expand include size: 10230/2097152 bytes
Template argument size: 2825/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 900/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   36.213      1 -total
 15.72%    5.693    117 Template:Text
 12.42%    4.497     77 Template:Cl
  7.07%    2.559      1 Template:PageSyntax
  6.65%    2.408      1 Template:Small
  5.29%    1.916      4 Template:Parameter
  5.10%    1.845      1 Template:PageSeeAlso
  4.90%    1.776      1 Template:PageExamples
  4.88%    1.767      1 Template:PageDescription
  4.82%    1.745      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:116-0!canonical and timestamp 20240714192703 and revision id 8307.
 -->
</div>
</div>
</div>
</div>
</body>
</html>