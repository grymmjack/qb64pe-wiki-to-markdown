<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>BSAVE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BSAVE rootpage-BSAVE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">BSAVE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">BSAVE</a> saves the contents of an image array to a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">BSAVE</a> <i>saveFile$</i>, <a href="VARPTR" title="VARPTR">VARPTR</a>(<i>array(index)</i>), <i>fileSize&amp;</i></dd></dl>
<h3><span class="mw-headline" id="Legacy_support">Legacy support</span></h3>
<ul><li><b>QB64</b> can save larger arrays directly to binary files using <a href="PUT" title="PUT">PUT</a> # and <a href="GET" title="GET">GET</a> # without <b>BSAVE</b>. For that reason, <b>BSAVE</b> isn't recommended practice anymore and is supported to maintain compatibility with legacy code.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>saveFile$</i> is the STRING file name of the file designated to be created.</li>
<li><i>array(index)</i> is the image <a href="Arrays" title="Arrays">array</a> that already holds the <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> image data.</li>
<li><i>fileSize&amp;</i> must be a bit over twice the size of the elements used in an <a href="INTEGER" title="INTEGER">INTEGER</a> <a href="Arrays" title="Arrays">array</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>To place image data into the array, use <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> to store a box area image of the screen.</li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a> 12 can only GET 1/3 of the screen image at one time using a 26K array.</li>
<li>Image arrays are <a href="DIM" title="DIM">DIMensioned</a> as <a href="INTEGER" title="INTEGER">INTEGER</a>. Use <a href="DEFINT" title="DEFINT">DEFINT</a> when working with large graphic arrays.</li>
<li>Any arrays can be saved, but image arrays are most common.</li>
<li><a href="DEF_SEG" title="DEF SEG">DEF SEG</a> = <a href="VARSEG" title="VARSEG">VARSEG</a> must be used to designate the array segment position in memory.</li>
<li><a href="VARPTR" title="VARPTR">VARPTR</a> returns the array index offset of the memory segment. Array sizes are limited to 32767 Integer elements due to the use of <a href="VARPTR" title="VARPTR">VARPTR</a> in QBasic and <b>QB64'</b>s emulated conventional memory.</li>
<li><a class="mw-selflink selflink">BSAVE</a> files can later be opened with <a href="BLOAD" title="BLOAD">BLOAD</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Saving array data to a file quickly.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> LB% = <a href="LBOUND" title="LBOUND"><span style="color:#4593D8;">LBOUND</span></a>(Array)
 bytes% = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Array(LB%))
 filesize&amp; = ((<a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(Array) - LB%) + 1) * bytes%
 <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = <a href="VARSEG" title="VARSEG"><span style="color:#4593D8;">VARSEG</span></a>(Array(0))
  <a class="mw-selflink selflink"><span style="color:#4593D8;">BSAVE</span></a> filename$, <a href="VARPTR" title="VARPTR"><span style="color:#4593D8;">VARPTR</span></a>(Array(LB%)), filesize&amp;  ' changeable index
 <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Procedure determines the filesize from the array size automatically. <a href="LBOUND" title="LBOUND">LBOUND</a> is used with <a href="UBOUND" title="UBOUND">UBOUND</a> to determine array size and byte size. Works with any type of array except variable-length strings. Used for saving program data fast.</dd></dl>
<p>
<i>Example 2:</i> <a class="mw-selflink selflink">BSAVEing</a> a bitmap and calculating the file size
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = <a href="VARSEG" title="VARSEG"><span style="color:#4593D8;">VARSEG</span></a>(Image(0))
 <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a>(BMPHead.PWidth - 1, BMPHead.PDepth - 1)  'color lower right corner if black
 <a href="GET_(graphics_statement)" title="GET (graphics statement)"><span style="color:#4593D8;">GET</span></a> (0, 0)-(BMPHead.PWidth - 1, BMPHead.PDepth - 1), Image(NColors * 3) ' for 16 or 256 colors
 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> a&amp; = 26000 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -1
   <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Image(a&amp;) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ArraySize&amp; = a&amp;: <a href="EXIT_FOR" title="EXIT FOR"><span style="color:#4593D8;">EXIT FOR</span></a>
 <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
 <a class="mw-selflink selflink"><span style="color:#4593D8;">BSAVE</span></a> SaveName$, <a href="VARPTR" title="VARPTR"><span style="color:#4593D8;">VARPTR</span></a>(Image(0)), (2 * ArraySize&amp;) + 200 'file size
 <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="FOR...NEXT" title="FOR...NEXT">FOR</a> loop reads backwards through the image array until it finds a value not 0. The <a href="LONG" title="LONG">LONG</a> <i>ArraySize&amp;</i> value is doubled and 200 is added. <i>BMPhead.PWidth</i> and <i>BMPhead.PDepth</i> are found by reading the bitmap's information header using a <a href="TYPE" title="TYPE">TYPE</a> definition. See <a href="Bitmaps" title="Bitmaps">Bitmaps</a>.</dd></dl>
<p>
<i>Example 3:</i> Using <a href="PUT" title="PUT">PUT</a> and <a href="GET" title="GET">GET</a> to write and read array data from a file without using BSAVE or <a href="BLOAD" title="BLOAD">BLOAD</a>:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> "example2.BIN" 'removes old image file!
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
<a href="OPTION_BASE" title="OPTION BASE"><span style="color:#4593D8;">OPTION BASE</span></a> 0
<a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> Graphic%(1001) 'REDIM makes array resize-able later
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (0, 0)-(10, 10), 12, B 'create image
<a href="GET_(graphics_statement)" title="GET (graphics statement)"><span style="color:#4593D8;">GET</span></a>(0, 0)-<a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(10, 10), Graphic%() 'get image to array
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 1000 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -1 'reverse read array for size needed
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Graphic%(i%) &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> 'find image color not black
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
size% = i% + 4 'size plus 2 integers(4  bytes) for dimensions
<a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> <a href="PRESERVE" title="PRESERVE"><span style="color:#4593D8;">_PRESERVE</span></a> Graphic%(size%) 'resize existing array in QB64 only!
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "example2.BIN" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 ' <a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> to a file
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, , Graphic%()
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a>
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "example2.BIN" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #2 'GET array and <a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> to screen
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> CopyBin%(<a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(2) \ 2) 'create new array sized by half of file size
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #2, , CopyBin%()
<a href="PUT_(graphics_statement)" title="PUT (graphics statement)"><span style="color:#4593D8;">PUT</span></a>(100, 100), CopyBin%(), <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a>
fsize% = <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(2)
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a>
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1) 'Press any key
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 20 'read all 3 arrays
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Graphic%(i); CopyBin%(i)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Array:"; size%, "File:"; fsize%
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> A 10 by 10 pixel box is saved to an array using the <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a> and written to a BINARY file using <a href="PUT" title="PUT">PUT</a> #1. Then <a href="GET" title="GET">GET</a> #1 places the file contents into another INTEGER array and places it on the screen with the <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a>.</dd></dl>
<dl><dd>The array contents: 88 is the width in the GET array for <a href="SCREEN" title="SCREEN">SCREEN</a> 13 which needs divided by 8 in that mode only. The area is actually 11 X 11. The array size needed can be found by looping backwards through the array until a color value is found. <b><span style="color:green;">IF array(i) &lt;&gt; 0 THEN EXIT FOR</span></b> (66 integers) or by dividing the created BINARY file size in half (134 bytes) when known to be array sized already.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a>, <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="BLOAD" title="BLOAD">BLOAD</a>, <a href="OPEN" title="OPEN">OPEN</a>, <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a></li>
<li><a href="GET" title="GET">GET</a>, <a href="PUT" title="PUT">PUT</a> <span style="color:#777777;">(file statements)</span></li>
<li><a href="VARSEG" title="VARSEG">VARSEG</a>, <a href="VARPTR" title="VARPTR">VARPTR</a></li>
<li><a href="DEF_SEG" title="DEF SEG">DEF SEG</a>, <a href="TYPE" title="TYPE">TYPE</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192346
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.050 seconds
Real time usage: 0.073 seconds
Preprocessor visited node count: 544/1000000
Post‐expand include size: 4525/2097152 bytes
Template argument size: 854/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   40.216      1 -total
 12.61%    5.070     64 Template:Cl
 11.90%    4.784      1 Template:PageDescription
 10.48%    4.216      1 Template:PageExamples
  7.62%    3.066      1 Template:Small
  6.45%    2.596      3 Template:CodeEnd
  6.20%    2.492      1 Template:PageSyntax
  6.00%    2.414      3 Template:CodeStart
  5.91%    2.377      2 Template:Text
  5.51%    2.217      9 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:401-0!canonical and timestamp 20240714192346 and revision id 7825.
 -->
</div>
</div>
</div>
</div>
</body>
</html>