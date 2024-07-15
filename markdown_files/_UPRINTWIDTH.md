<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_UPRINTWIDTH - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-UPRINTWIDTH rootpage-UPRINTWIDTH skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_UPRINTWIDTH</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_UPRINTWIDTH</b> function returns the width in pixels of the text <a href="STRING" title="STRING">string</a> specified. The function supports Unicode encoded text.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixelWidth&amp;</i> = <a class="mw-selflink selflink">_UPRINTWIDTH</a>(<i>text$</i>[, <i>utfEncoding&amp;</i>][, <i>fontHandle&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>text$</i> is any literal or variable <a href="STRING" title="STRING">STRING</a> value.</li>
<li><i>utfEncoding&amp;</i> is an optional UTF encoding of <i>text$</i>. This can be 0 for ASCII, 8 for UTF-8, 16 for UTF-16 or 32 for UTF-32.</li>
<li><i>fontHandle&amp;</i> is an optional font handle.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If the <i>utfEncoding&amp;</i> is omitted, then it is assumed to be 0 (ASCII).</li>
<li>If <i>fontHandle&amp;</i> is omitted, then the current write page font is used.</li>
<li>All multi-byte UTF encodings are expected in little-endian.</li>
<li>Unicode byte order mark (BOM) is not processed and must be handled by user code.</li>
<li>This can be useful to find the width of the font print <a href="STRING" title="STRING">string</a> before actually printing it.</li>
<li>Can be used with variable-width fonts or built-in fonts, unlike <a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a> which requires a MONOSPACE font handle.</li>
<li>Unlike <a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a>, <a class="mw-selflink selflink">_UPRINTWIDTH</a> always returns the width of the text string in pixels.</li></ul>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.7.0"><img alt="v3.7.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.7.0</b>
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
<dd>Centers and prints a Russian text on a graphics screen.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">800</span>, <span style="color:#F580B1;">600</span>, <span style="color:#F580B1;">32</span>)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> fh <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: fh = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"cyberbit.ttf"</span>, <span style="color:#F580B1;">21</span>)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> fh &lt;= <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Failed to load font file!"</span>
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> fh
<a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> text_data
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> myString <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>: myString = <span style="color:#55FF55;">LoadUData$</span>
<a href="UPRINTSTRING" title="UPRINTSTRING"><span style="color:#4593D8;">_UPRINTSTRING</span></a> (<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> \ <span style="color:#F580B1;">2</span> - <a class="mw-selflink selflink"><span style="color:#4593D8;">_UPRINTWIDTH</span></a>(myString, <span style="color:#F580B1;">8</span>, fh) \ <span style="color:#F580B1;">2</span>, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> \ <span style="color:#F580B1;">2</span> - <a href="UFONTHEIGHT" title="UFONTHEIGHT"><span style="color:#4593D8;">_UFONTHEIGHT</span></a> \ <span style="color:#F580B1;">2</span>), myString, <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>, <span style="color:#F580B1;">8</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
text_data:
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">6F</span>,D0,<span style="color:#F580B1;">91</span>,D1,<span style="color:#F580B1;">8B</span>,D1,<span style="color:#F580B1;">81</span>,D1,<span style="color:#F580B1;">82</span>,D1,<span style="color:#F580B1;">80</span>,D0,B0,D1,<span style="color:#F580B1;">8F</span>,<span style="color:#F580B1;">20</span>,D0,BA,D0,BE,D1,<span style="color:#F580B1;">80</span>,D0,B8,D1
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">87</span>,D0,BD,D0,B5,D0,B2,D0,B0,D1,<span style="color:#F580B1;">8F</span>,<span style="color:#F580B1;">20</span>,D0,BB,D0,B8,D1,<span style="color:#F580B1;">81</span>,D0,B0,<span style="color:#F580B1;">20</span>,D0,BF,D0,B5
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> D1,<span style="color:#F580B1;">80</span>,D0,B5,D0,BF,D1,<span style="color:#F580B1;">80</span>,D1,<span style="color:#F580B1;">8B</span>,D0,B3,D0,B8,D0,B2,D0,B0,D0,B5,D1,<span style="color:#F580B1;">82</span>,<span style="color:#F580B1;">20</span>,D1,<span style="color:#F580B1;">87</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> D0,B5,D1,<span style="color:#F580B1;">80</span>,D0,B5,D0,B7,<span style="color:#F580B1;">20</span>,D0,BB,D0,B5,D0,BD,D0,B8,D0,B2,D1,<span style="color:#F580B1;">83</span>,D1,<span style="color:#F580B1;">8E</span>,<span style="color:#F580B1;">20</span>,D1
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">81</span>,D0,BE,D0,B1,D0,B0,D0,BA,D1,<span style="color:#F580B1;">83</span>,<span style="color:#F580B1;">2E</span>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">LoadUData$</span>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> i, s
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> d <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> buffer <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
    <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> d
    s = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<span style="color:#FFB100;">"&amp;h"</span> + d)
    buffer = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(s)
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> s
        <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> d
        <a href="ASC" title="ASC"><span style="color:#4593D8;">ASC</span></a>(buffer, i) = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<span style="color:#FFB100;">"&amp;h"</span> + d)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <span style="color:#55FF55;">LoadUData</span> = buffer
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2782" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="UFONTHEIGHT" title="UFONTHEIGHT">_UFONTHEIGHT</a>, <a href="ULINESPACING" title="ULINESPACING">_ULINESPACING</a>, <a href="UPRINTSTRING" title="UPRINTSTRING">_UPRINTSTRING</a>, <a href="UCHARPOS" title="UCHARPOS">_UCHARPOS</a></li>
<li><a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a>, <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>, <a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li>
<li><a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a>, <a href="FONT" title="FONT">_FONT</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062625
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.069 seconds
Real time usage: 0.088 seconds
Preprocessor visited node count: 773/1000000
Post‐expand include size: 5433/2097152 bytes
Template argument size: 1209/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2417/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   60.553      1 -total
 10.53%    6.377     47 Template:Text
  8.80%    5.330     51 Template:Cl
  5.40%    3.271     10 Template:Parameter
  4.86%    2.942      1 Template:PageSyntax
  4.63%    2.804      1 Template:CodeEnd
  4.60%    2.788      1 Template:PageExamples
  4.51%    2.730      1 Template:PageAvailability
  4.07%    2.464      1 Template:CodeStart
  3.90%    2.361      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1216-0!canonical and timestamp 20240715062625 and revision id 8971.
 -->
</div>
</div>
</div>
</div>
</body>
</html>