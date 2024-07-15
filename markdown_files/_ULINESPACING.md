<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ULINESPACING - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ULINESPACING rootpage-ULINESPACING skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ULINESPACING</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_ULINESPACING</b> function returns the vertical line spacing (distance between two consecutive baselines) in pixels.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixels&amp;</i> = <a class="mw-selflink selflink">_ULINESPACING</a>[(<i>fontHandle&amp;</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>fontHandle&amp;</i> is an optional font handle.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the vertical line spacing of the last font used if a handle is not designated.</li>
<li>If no font is set, it returns the current screen mode's text block height.</li>
<li>This can be used to leave the correct amount of line gap between lines.</li></ul>
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
<dd>How to use <a class="mw-selflink selflink">_ULINESPACING</a>.</dd></dl>
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
    <a href="UPRINTSTRING" title="UPRINTSTRING"><span style="color:#4593D8;">_UPRINTSTRING</span></a> (<span style="color:#F580B1;">0</span>, <a class="mw-selflink selflink"><span style="color:#4593D8;">_ULINESPACING</span></a> * i), l
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
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2819" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="UPRINTWIDTH" title="UPRINTWIDTH">_UPRINTWIDTH</a>, <a href="UFONTHEIGHT" title="UFONTHEIGHT">_UFONTHEIGHT</a>, <a href="UPRINTSTRING" title="UPRINTSTRING">_UPRINTSTRING</a>, <a href="UCHARPOS" title="UCHARPOS">_UCHARPOS</a></li>
<li><a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a>, <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>, <a href="FONT" title="FONT">_FONT</a></li>
<li><a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a>, <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062626
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.052 seconds
Real time usage: 0.071 seconds
Preprocessor visited node count: 474/1000000
Post‐expand include size: 3702/2097152 bytes
Template argument size: 834/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2634/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   45.026      1 -total
  6.84%    3.080     37 Template:Cl
  5.29%    2.382      1 Template:CodeStart
  5.19%    2.337     21 Template:Text
  4.88%    2.199      1 Template:PageNavigation
  4.56%    2.055      1 Template:CodeEnd
  4.54%    2.044      1 Template:PageSyntax
  4.47%    2.015      1 Template:PageExamples
  4.26%    1.920      3 Template:Parameter
  4.24%    1.907      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1217-0!canonical and timestamp 20240715062625 and revision id 9014.
 -->
</div>
</div>
</div>
</div>
</body>
</html>