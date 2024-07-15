<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_UPRINTSTRING - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-UPRINTSTRING rootpage-UPRINTSTRING skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_UPRINTSTRING</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_UPRINTSTRING</b> statement prints ASCII / UNICODE text <a href="STRING" title="STRING">strings</a> using graphic column and row coordinate positions.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_UPRINTSTRING</a> (<i>column</i>, <i>row</i>), <i>textExpression$</i>[, <i>maxWidth&amp;</i>][, <i>utfEncoding&amp;</i>][, <i>fontHandle&amp;</i>][, <i>imageHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>column</i> and <i>row</i> are <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="LONG" title="LONG">LONG</a> starting PIXEL (graphic) column and row coordinates to set text or custom fonts.</li>
<li><i>textExpression$</i> is any literal or variable <a href="STRING" title="STRING">string</a> value of text to be displayed.</li>
<li><i>maxWidth&amp;</i> is an optional horizontal pixel limit after which the text rendering will be clipped.</li>
<li><i>utfEncoding&amp;</i> is an optional UTF encoding of <i>textExpression$</i>. This can be 0 for ASCII, 8 for UTF-8, 16 for UTF-16 or 32 for UTF-32.</li>
<li><i>fontHandle&amp;</i> is an optional font handle.</li>
<li><i>imageHandle&amp;</i> is the optional image or destination to use. Zero designates current <a href="SCREEN" title="SCREEN">SCREEN</a> page.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The starting coordinate sets the top left corner of the text to be printed.</li>
<li>If <i>maxWidth&amp;</i> is omitted, then the entire <i>textExpression$</i> is rendered.</li>
<li>If <i>utfEncoding&amp;</i> is omitted, then it is assumed to be 0 (ASCII).</li>
<li>If <i>fontHandle&amp;</i> is omitted, then the current write page font is used.</li>
<li><a href="UPRINTWIDTH" title="UPRINTWIDTH">_UPRINTWIDTH</a> can be used to determine how wide a text print will be so that the screen width is not exceeded. Alternatively, <i>maxWidth&amp;</i> can be used to clip text rending after a certain amount of pixel width.</li>
<li><a href="ULINESPACING" title="ULINESPACING">_ULINESPACING</a> can be used to calculate the next <a href="FONT" title="FONT">font</a> vertical position.</li>
<li>Unicode byte order mark (BOM) is not processed and must be handled by user code except for UTF-16.</li>
<li>UTF-16 LE is assumed if BOM is absent in the string and <i>utfEncoding&amp;</i> is 16.</li>
<li>Can use the current font alpha blending with a designated image background. See the <a href="RGBA" title="RGBA">_RGBA</a> function example.</li>
<li>Use the <a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a> statement before printing to set how the background is rendered.
<ul><li>Use the <a href="PRINTMODE_(function)" title="PRINTMODE (function)">_PRINTMODE (function)</a> to find the current _PRINTMODE setting.</li></ul></li>
<li>SCREEN 0 (text only) mode is not supported. Attempting to use this in SCREEN 0 will generate an error.</li></ul>
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
<dl><dt>Example 1</dt>
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
<a class="mw-selflink selflink"><span style="color:#4593D8;">_UPRINTSTRING</span></a> (<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> \ <span style="color:#F580B1;">2</span> - <a href="UPRINTWIDTH" title="UPRINTWIDTH"><span style="color:#4593D8;">_UPRINTWIDTH</span></a>(myString, <span style="color:#F580B1;">8</span>, fh) \ <span style="color:#F580B1;">2</span>, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> \ <span style="color:#F580B1;">2</span> - <a href="UFONTHEIGHT" title="UFONTHEIGHT"><span style="color:#4593D8;">_UFONTHEIGHT</span></a> \ <span style="color:#F580B1;">2</span>), myString, <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>, <span style="color:#F580B1;">8</span>
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
<dl><dt>Example 2</dt>
<dd>Prints multiple lines of text using a recommended line gap.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">800</span>, <span style="color:#F580B1;">600</span>, <span style="color:#F580B1;">32</span>)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> fh <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: fh = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"LHANDW.TTF"</span>, <span style="color:#F580B1;">23</span>)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> fh &lt;= <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Failed to load font file!"</span>
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> fh
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">200</span>, <span style="color:#F580B1;">200</span>, <span style="color:#F580B1;">200</span>)
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)
<a href="PRINTMODE" title="PRINTMODE"><span style="color:#4593D8;">_PRINTMODE</span></a> <a class="mw-redirect" href="KEEPBACKGROUND" title="KEEPBACKGROUND"><span style="color:#4593D8;">_KEEPBACKGROUND</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> l <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">4</span>
    <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> l
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_UPRINTSTRING</span></a> (<span style="color:#F580B1;">0</span>, <a href="ULINESPACING" title="ULINESPACING"><span style="color:#4593D8;">_ULINESPACING</span></a> * i), l
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"We are not now that strength which in old days"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"Moved earth and heaven; that which we are,we are;"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"One equal temper of heroic hearts,"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"Made weak by time and fate,but strong in will"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"To strive,to seek,to find,and not to yield."</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2765" rel="nofollow">Featured in our "Keyword of the Day" series (Part 1)</a></li>
<li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2778" rel="nofollow">Featured in our "Keyword of the Day" series (Part 2)</a></li>
<li><a href="UPRINTWIDTH" title="UPRINTWIDTH">_UPRINTWIDTH</a>, <a href="UFONTHEIGHT" title="UFONTHEIGHT">_UFONTHEIGHT</a>, <a href="ULINESPACING" title="ULINESPACING">_ULINESPACING</a>, <a href="UCHARPOS" title="UCHARPOS">_UCHARPOS</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a>, <a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a></li>
<li><a href="CONTROLCHR" title="CONTROLCHR">_CONTROLCHR</a></li>
<li><a href="FONT" title="FONT">_FONT</a>, <a href="LOADFONT" title="LOADFONT">_LOADFONT</a>, <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>, <a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a>, <a href="SCREENPRINT" title="SCREENPRINT">_SCREENPRINT</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715004536
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.098 seconds
Real time usage: 0.116 seconds
Preprocessor visited node count: 1247/1000000
Post‐expand include size: 8600/2097152 bytes
Template argument size: 2138/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2683/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   76.144      1 -total
 10.06%    7.660     88 Template:Cl
  8.30%    6.318     68 Template:Text
  4.18%    3.186      2 Template:CodeEnd
  4.17%    3.175      1 Template:PageSeeAlso
  3.95%    3.005     21 Template:Parameter
  3.84%    2.926      1 Template:PageParameters
  3.49%    2.656      1 Template:PageSyntax
  3.48%    2.649      1 Template:PageExamples
  3.48%    2.648      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1218-0!canonical and timestamp 20240715004535 and revision id 8970.
 -->
</div>
</div>
</div>
</div>
</body>
</html>