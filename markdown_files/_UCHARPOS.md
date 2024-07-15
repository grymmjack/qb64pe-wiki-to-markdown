<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_UCHARPOS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-UCHARPOS rootpage-UCHARPOS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_UCHARPOS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_UCHARPOS</b> function calculates the starting pixel positions of every character of the text <a href="STRING" title="STRING">string</a> (0 being the starting pixel position of the first character). This information is returned in a <a href="LONG" title="LONG">long</a> array. The function also returns the number of characters in the text <a href="STRING" title="STRING">string</a>. The function supports Unicode encoded text.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>codepoints&amp;</i> = <a class="mw-selflink selflink">_UCHARPOS</a>(<i>text$</i>[, <i>posArray&amp;()</i>][, <i>utfEncoding&amp;</i>][, <i>fontHandle&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>text$</i> is any literal or variable <a href="STRING" title="STRING">STRING</a> value. This can be a Unicode encoded text.</li>
<li><i>posArray&amp;()</i> is a <a href="LONG" title="LONG">long</a> array that contains the pixel position information after a call to <b>_UCHARPOS</b>.</li>
<li><i>utfEncoding&amp;</i> is an optional UTF encoding of <i>text$</i>. This can be 0 for ASCII, 8 for UTF-8, 16 for UTF-16 or 32 for UTF-32.</li>
<li><i>fontHandle&amp;</i> is an optional font handle.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If <i>posArray&amp;()</i> is omitted, then the function simply returns the number of characters in the text <a href="STRING" title="STRING">string</a>.</li>
<li>If <i>utfEncoding&amp;</i> is omitted, then it is assumed to be 0 (ASCII).</li>
<li>If <i>fontHandle&amp;</i> is omitted, then the current write page font is used.</li>
<li><i>posArray&amp;(codepoints&amp;)</i> (assuming <i>posArray&amp;()</i> is declared (indexed) as 0 <a href="TO" title="TO">TO</a> <i>codepoints&amp;</i>) will hold the (ending pixel position of the last character) + 1.</li>
<li>All multi-byte UTF encodings are expected in little-endian.</li>
<li>Unicode byte order mark (BOM) is not processed and must be handled by user code.</li>
<li>This can be useful when the positions of every character in a string is required (e.g., when underling text or drawing a text cursor). This can be especially helpful when using variable width fonts.</li>
<li>When working with Unicode excoded text, instead of calling the function twice (first time to get the array size and then a second time to get the pixel positions), call it once with a large enough array (0 <a href="TO" title="TO">TO</a> <a href="LEN" title="LEN">LEN</a>(<i>text$</i>)) and then resize the array (0 <a href="TO" title="TO">TO</a> <i>codepoints&amp;</i>) using <a href="REDIM" title="REDIM">REDIM</a> <a href="PRESERVE" title="PRESERVE">PRESERVE</a>.</li></ul>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.8.0"><img alt="v3.8.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.8.0</b>
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
<dl><dt>Example</dt>
<dd>Underlines every character of a text printed using a variable width font.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">12</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> TEXT = <span style="color:#FFB100;">"Hello, world!"</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> TEXT_X = <span style="color:#F580B1;">220</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> TEXT_Y = <span style="color:#F580B1;">220</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> fh <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: fh = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"arial.ttf"</span>, <span style="color:#F580B1;">32</span>)
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> fh
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> arr(<span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(TEXT)) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Len of "</span>; TEXT; <span style="color:#FFB100;">" ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_UCHARPOS</span></a>(TEXT, arr())
<a href="UPRINTSTRING" title="UPRINTSTRING"><span style="color:#4593D8;">_UPRINTSTRING</span></a> (TEXT_X, TEXT_Y), TEXT
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <a href="LBOUND" title="LBOUND"><span style="color:#4593D8;">LBOUND</span></a>(arr) <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(arr) - <span style="color:#F580B1;">1</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> arr(i + <span style="color:#F580B1;">1</span>);
    <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (TEXT_X + arr(i), TEXT_Y + <a href="UFONTHEIGHT" title="UFONTHEIGHT"><span style="color:#4593D8;">_UFONTHEIGHT</span></a>)-(TEXT_X + arr(i + <span style="color:#F580B1;">1</span>) - <span style="color:#F580B1;">1</span>, TEXT_Y + <a href="UFONTHEIGHT" title="UFONTHEIGHT"><span style="color:#4593D8;">_UFONTHEIGHT</span></a>), <span style="color:#F580B1;">9</span> + i <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">7</span>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2826" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="UFONTHEIGHT" title="UFONTHEIGHT">_UFONTHEIGHT</a>, <a href="ULINESPACING" title="ULINESPACING">_ULINESPACING</a>, <a href="UPRINTWIDTH" title="UPRINTWIDTH">_UPRINTWIDTH</a>, <a href="UPRINTSTRING" title="UPRINTSTRING">_UPRINTSTRING</a></li>
<li><a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a>, <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>, <a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li>
<li><a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a>, <a href="FONT" title="FONT">_FONT</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193355
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.065 seconds
Real time usage: 0.079 seconds
Preprocessor visited node count: 448/1000000
Post‐expand include size: 3327/2097152 bytes
Template argument size: 778/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2407/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   50.351      1 -total
  6.65%    3.349     32 Template:Cl
  6.35%    3.195     15 Template:Text
  6.16%    3.103     18 Template:Parameter
  5.69%    2.864      1 Template:PageSyntax
  5.18%    2.606      1 Template:PageSeeAlso
  4.97%    2.504      1 Template:PageNavigation
  4.70%    2.366      1 Template:CodeEnd
  4.67%    2.354      1 Template:PageDescription
  4.65%    2.339      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1219-0!canonical and timestamp 20240714193355 and revision id 9015.
 -->
</div>
</div>
</div>
</div>
</body>
</html>