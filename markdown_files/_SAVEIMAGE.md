<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SAVEIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SAVEIMAGE rootpage-SAVEIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SAVEIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>_SAVEIMAGE</b> saves the contents of an image or screen page to an image file.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SAVEIMAGE</a> <i>fileName$</i>[, <i>imageHandle&amp;</i>][, <i>requirements$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>fileName$</i> is literal or variable <a href="STRING" title="STRING">STRING</a> file name value.</li>
<li>Optional <i>imageHandle&amp;</i> is a <a href="LONG" title="LONG">LONG</a> image handle or a valid screen page number.</li>
<li>Optional <i>requirements$</i> <a href="STRING" title="STRING">STRING</a> values can be:
<ul><li><b>PNG</b>: Saves the image as Portable Network Graphics format if no file extension is specified.</li>
<li><b>QOI</b>: Saves the image as Quite OK Image format if no file extension is specified.</li>
<li><b>BMP</b>: Saves the image as Windows Bitmap format if no file extension is specified.</li>
<li><b>TGA</b>: Saves the image as Truevision TARGA format if no file extension is specified.</li>
<li><b>JPG</b>: Saves the image as Joint Photographic Experts Group format if no file extension is specified.</li>
<li><b>HDR</b>: Saves the image as Radiance HDR format if no file extension is specified.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>fileName$</i> extension name takes precedence over <i>requirements$</i></li>
<li>If no file extension is specified in <i>fileName$</i> and no format is specified in <i>requirements$</i>, then the PNG format is used by default.</li>
<li>If <i>imageHandle&amp;</i> is omitted then the image handle returned by <a href="DISPLAY_(function)" title="DISPLAY (function)">_DISPLAY (function)</a> is used.</li>
<li>All attempts are made to ensure the image is saved in the best possible quality in 32-bit RGBA format. Alpha channel information is preserved wherever the format allows.</li>
<li>SCREEN 0 (text mode) screen and "images" can also be saved. Text surfaces are internally rendered using the master QB64-PE VGA fonts before saving.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="none"><img alt="none" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>none</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.9.0"><img alt="v3.9.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.9.0</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Apix.png"><img alt="Apix.png" decoding="async" height="48" src="/qb64wiki/images/5/5f/Apix.png" width="48"/></a></div></div>
<div class="gallerytext">
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Win.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/29/Win.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
</ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>It's possible to use <b>_SAVEIMAGE</b> with text screens.</dd>
<dd>This demo draws a Mandelbrot in <a href="SCREEN" title="SCREEN">SCREEN</a> 0 and then saves the screen as a .jpg image.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> X_MIN = <span style="color:#F580B1;">-2!</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> X_MAX = <span style="color:#F580B1;">1!</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> Y_MIN = <span style="color:#F580B1;">-1!</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> Y_MAX = <span style="color:#F580B1;">1!</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MAX_ITER = <span style="color:#F580B1;">100</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> PIX_CHAR = <span style="color:#F580B1;">48</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">0</span>
<a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">WIDTH</span></a> <span style="color:#F580B1;">160</span>, <span style="color:#F580B1;">100</span>
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <span style="color:#F580B1;">8</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> w <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: w = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> h <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: h = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> maxX <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: maxX = w - <span style="color:#F580B1;">1</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> maxY <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: maxY = h - <span style="color:#F580B1;">1</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> maxY
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> maxX
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> cx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: cx = X_MIN + (x / w) * (X_MAX - X_MIN)
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> cy <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: cy = Y_MIN + (y / h) * (Y_MAX - Y_MIN)
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> zx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: zx = <span style="color:#F580B1;">0</span>
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> zy <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: zy = <span style="color:#F580B1;">0</span>
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: i = <span style="color:#F580B1;">0</span>
        <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO UNTIL</span></a> zx * zx + zy * zy &gt;= <span style="color:#F580B1;">4</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> i &gt;= MAX_ITER
            <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> temp <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: temp = zx * zx - zy * zy + cx
            zy = <span style="color:#F580B1;">2</span> * zx * zy + cy
            zx = temp
            i = i + <span style="color:#F580B1;">1</span>
        <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
        <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> i <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">16</span>
        <a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (x + <span style="color:#F580B1;">1</span>, y + <span style="color:#F580B1;">1</span>), <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(PIX_CHAR)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SAVEIMAGE</span></a> <span style="color:#FFB100;">"TextMandelbrot!.jpg"</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Saving a graphics image to a .png file. This is much like example one. However, it renders the graphics to an 8-bit offscreen image and then passes the image handle to <b>_SAVEIMAGE</b>.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> X_MIN = <span style="color:#F580B1;">-2!</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> X_MAX = <span style="color:#F580B1;">1!</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> Y_MIN = <span style="color:#F580B1;">-1!</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> Y_MAX = <span style="color:#F580B1;">1!</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MAX_ITER = <span style="color:#F580B1;">100</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> img <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: img = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span> * <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">400</span> * <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">256</span>)
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> img
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> w <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: w = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> h <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: h = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> maxX <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: maxX = w - <span style="color:#F580B1;">1</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> maxY <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: maxY = h - <span style="color:#F580B1;">1</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> maxY
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> maxX
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> cx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: cx = X_MIN + (x / maxX) * (X_MAX - X_MIN)
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> cy <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: cy = Y_MIN + (y / maxY) * (Y_MAX - Y_MIN)
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> zx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: zx = <span style="color:#F580B1;">0</span>
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> zy <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: zy = <span style="color:#F580B1;">0</span>
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: i = <span style="color:#F580B1;">0</span>
        <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO UNTIL</span></a> zx * zx + zy * zy &gt;= <span style="color:#F580B1;">4</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> i &gt;= MAX_ITER
            <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> temp <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: temp = zx * zx - zy * zy + cx
            zy = <span style="color:#F580B1;">2</span> * zx * zy + cy
            zx = temp
            i = i + <span style="color:#F580B1;">1</span>
        <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
        <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (x, y), (i <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">16</span>) * <span style="color:#F580B1;">16</span> + (i <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">8</span>)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SAVEIMAGE</span></a> <span style="color:#FFB100;">"Mandelbrot"</span>, img
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <span style="color:#F580B1;">0</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Saved image."</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2749" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="ICON" title="ICON">_ICON</a>, <a href="$EXEICON" title="$EXEICON">$EXEICON</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="TYPE" title="TYPE">TYPE</a>, <a href="MKI$" title="MKI$">MKI$</a>, <a href="MKL$" title="MKL$">MKL$</a></li>
<li><a href="Program_ScreenShots" title="Program ScreenShots">Program ScreenShots</a></li>
<li><a href="ThirtyTwoBit_SUB" title="ThirtyTwoBit SUB">ThirtyTwoBit SUB</a></li>
<li><a href="ThirtyTwoBit_MEM_SUB" title="ThirtyTwoBit MEM SUB">ThirtyTwoBit MEM SUB</a></li>
<li><a href="SaveIcon32" title="SaveIcon32">SaveIcon32</a></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a>, <a href="Icons_and_Cursors" title="Icons and Cursors">Icons and Cursors</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<!-- 
NewPP limit report
Cached time: 20240714193342
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.103 seconds
Real time usage: 0.126 seconds
Preprocessor visited node count: 1349/1000000
Post‐expand include size: 8980/2097152 bytes
Template argument size: 1737/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2415/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   76.499      1 -total
 16.27%   12.446      1 Template:PageSyntax
  9.56%    7.311    130 Template:Cl
  4.83%    3.693     50 Template:Text
  4.41%    3.371     11 Template:Parameter
  3.81%    2.911      1 Template:PageExamples
  3.61%    2.765      2 Template:CodeEnd
  3.46%    2.648      1 Template:PageSeeAlso
  3.21%    2.455      1 Template:PageParameters
  3.17%    2.428      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:466-0!canonical and timestamp 20240714193342 and revision id 8953.
 -->
</div>
</div>
</div>
</div>
</body>
</html>