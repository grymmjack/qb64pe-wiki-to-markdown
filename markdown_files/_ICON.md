<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ICON - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ICON rootpage-ICON skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ICON</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ICON</a> statement uses an image handle from <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> for the program header and icon image in the OS.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_ICON</a> [<i>mainImageHandle&amp;</i>[, <i>smallImageHandle&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>mainImageHandle&amp;</i>  is the <a href="LONG" title="LONG">LONG</a> handle value of the OS icon and title bar image pre-loaded with <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> when used alone.</li>
<li><i>smallImageHandle&amp;</i> is the <a href="LONG" title="LONG">LONG</a> handle value of a different title bar image pre-loaded with <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> when used.</li>
<li>No image handle designates use of the default QB64 icon or the embedded icon set by <a href="$EXEICON" title="$EXEICON">$EXEICON</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If no image handle is passed, the default QB64 icon will be used (all versions). If the <a href="$EXEICON" title="$EXEICON">$EXEICON</a> metacommand is used, <a class="mw-selflink selflink">_ICON</a> without an image handle uses the embedded icon from the binary (Windows only).</li>
<li>Beginning with <b>version 1.000</b>, the following is considered:</li></ul>
<dl><dd><dl><dd><dl><dd><i>mainImageHandle&amp;</i> creates the image as the icon in the OS and the image in the program header (title bar).</dd>
<dd><i>smallImageHandle&amp;</i> can be used for a different image in the program header bar.</dd></dl></dd></dl></dd></dl>
<ul><li>The header image will automatically be resized to fit the icon size of 16 X 16 if smaller or larger.</li>
<li>Once the program's icon is set, the image handle can be discarded with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a>.</li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li><b>NOTE: Icon files are not supported with <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> and an error will occur. See Example 2.</b></li>
<li>Images used can be smaller or larger than 32 X 32 pixels, but image resolution may be affected.</li>
<li>It is important to free unused or uneeded images with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a> to prevent memory overflow errors.</li>
<li>In <b>SCREEN 0</b> (default text mode) you need to specify 32-bit mode in <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> to load images.<b></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Loading an image to a 32 bit palette in SCREEN 0 (the default screen mode).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">i&amp; =<a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("RDSWU16.BMP", 32) '&lt;&lt;&lt;&lt;&lt;&lt;&lt; use your image file name here
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> i&amp; &lt; -1 THEN
  <a class="mw-selflink selflink"><span style="color:#4593D8;">_ICON</span></a> i&amp;
  <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> i&amp; ' release image handle after setting icon
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> _ICON images can be freed if the <a href="SCREEN" title="SCREEN">SCREEN</a> mode stays the same. Freed image handles can on longer be referenced.</dd></dl>
<p>
<i>Example 2:</i> Function that converts an icon into a temporary bitmap for use in QB64. Function returns the available image count.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 256)
<a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "Icon Converter"
icon$ = "daphne.ico"     '&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; change icon file name
bitmap$ = "tempfile.bmp"
indx% = 6  '1 minimum &lt;&lt;&lt;&lt;&lt;&lt;&lt; higher values than count get highest entry image in icon file
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Icon2BMP(icon$, bitmap$, indx%) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  img&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(bitmap$) '  use 32 as color mode in SCREEN 0
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> img&amp; &lt; -1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> '           check that handle value is good before loading
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_ICON</span></a> img&amp; '                place image in header
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (300, 250), img&amp; 'place image on screen
    <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> img&amp; '           always free unused handles to save memory
    <a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> bitmap$ '              comment out and/or rename to save the bitmaps
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
'                ----------------------------------------------------
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> Icon2BMP% (filein <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, fileout <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, index <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>)
'function creates a bitmap of the icon and returns the icon count
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> byte <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>, word <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, dword <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> wide <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, high <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, BM <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, bpp <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
rf = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LCASE$" title="LCASE$"><span style="color:#4593D8;">LCASE$</span></a>(<a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(filein, 4)) = ".ico" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'check file extension is ICO only
  <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> filein <a href="OPEN" title="OPEN"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> <a class="mw-redirect" href="ACCESS" title="ACCESS"><span style="color:#4593D8;">ACCESS</span></a> <a class="mw-redirect" href="ACCESS" title="ACCESS"><span style="color:#4593D8;">READ</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> rf
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , word
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , word: icon = word
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , word: count = word
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> icon &lt;&gt; 1 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> count = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> rf: <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
'<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> icon, count
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> index &gt; 0 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> index &lt;= count <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> entry = 16 * (index - 1) <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> entry = 16 * (count - 1)
<a href="SEEK" title="SEEK"><span style="color:#4593D8;">SEEK</span></a> rf, 1 + 6 + entry 'start of indexed Entry header
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , byte: wide = byte ' use this unsigned for images over 127
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , byte: high = byte ' use this unsigned because it isn't doubled
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , word 'number of 4 BPP colors(256 &amp; 32 = 0) &amp; reserved bytes
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , dword '2 hot spots both normally 0 in icons, used for cursors
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , dword: size = dword 'this could be used, doesn't seem to matter
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , dword: offset = dword 'find where the specific index BMP header is
'<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> wide; "X"; high, size, offset
<a href="SEEK" title="SEEK"><span style="color:#4593D8;">SEEK</span></a> rf, 1 + offset + 14 'only read the BPP in BMP header
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , word: bpp = word
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> bpp = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> rf: <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> bpp &lt;= 24 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> pixelbytes = bpp / 8 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> pixelbytes = 3
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> bpp &gt; 1 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> bpp &lt;= 8 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> palettebytes = 4 * (2 ^ bpp) <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> palettebytes = 0
datasize&amp; = (wide * high * pixelbytes) + palettebytes 'no padder should be necessary
filesize&amp; = datasize&amp; + 14 + 40 '                      data and palette + header
bmpoffset&amp; = palettebytes + 54 '                       data offset from start of bitmap
readbytes&amp; = datasize&amp; + 28 ' (40 - 12) bytes left to read in BMP header and <a class="mw-redirect" href="XOR" title="XOR"><span style="color:#4593D8;">XOR</span></a> mask only
'<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> bpp, bmpoffset&amp;, filesize&amp;
BM = <a href="CVI" title="CVI"><span style="color:#4593D8;">CVI</span></a>("BM") 'this will create "BM" in file like <a href="MKI$" title="MKI$"><span style="color:#4593D8;">MKI$</span></a> would
wf = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a>
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> fileout <a href="OPEN" title="OPEN"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> wf
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> wf, , BM
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> wf, , filesize&amp;
dword = 0
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> wf, , dword
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> wf, , bmpoffset&amp; 'byte location of end of palette or BMP header
dword = 40
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> wf, , dword '              start of 40 byte BMP header
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> wf, , wide
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> wf, , high
<a href="SEEK" title="SEEK"><span style="color:#4593D8;">SEEK</span></a> rf, 1 + offset + 12 '     after 12 bytes start copy of BMP header starting at planes
dat$ = <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(readbytes&amp;, 0) 'create string to hold remaining bytes needed w/o <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> mask data
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> rf, , dat$ '               copy lower header, palette(if used) and <a class="mw-redirect" href="XOR" title="XOR"><span style="color:#4593D8;">XOR</span></a> mask
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> wf, , dat$ '               put all of the string data in the bitmap all at once
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> rf, wf
Icon2BMP = count '             return the number of icons available in the icon file
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Once the file has been loaded into memory, the image handle can still be used even after the file has been deleted.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="TITLE" title="TITLE">_TITLE</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li><a href="$EXEICON" title="$EXEICON">$EXEICON</a></li>
<li><a href="Creating_Icon_Bitmaps" title="Creating Icon Bitmaps">Creating Icon Bitmaps</a> <span style="color:#777777;">(member-contributed program)</span></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a>, <a href="Icons_and_Cursors" title="Icons and Cursors">Icons and Cursors</a></li>
<li><a href="Resource_Table_extraction#Extract_Icon" title="Resource Table extraction">Icon Extraction</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034352
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.058 seconds
Real time usage: 0.076 seconds
Preprocessor visited node count: 906/1000000
Post‐expand include size: 6986/2097152 bytes
Template argument size: 1292/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   44.206      1 -total
 19.73%    8.720      1 Template:PageDescription
 18.38%    8.126    116 Template:Cl
  5.35%    2.365      2 Template:CodeEnd
  5.31%    2.346      1 Template:Small
  4.77%    2.110      1 Template:PageSeeAlso
  4.43%    1.959      2 Template:CodeStart
  4.36%    1.929      1 Template:PageSyntax
  4.27%    1.886      1 Template:Text
  4.07%    1.798      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:155-0!canonical and timestamp 20240715034352 and revision id 7882.
 -->
</div>
</div>
</div>
</div>
</body>
</html>