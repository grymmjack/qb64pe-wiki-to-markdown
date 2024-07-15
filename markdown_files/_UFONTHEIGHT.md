<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_UFONTHEIGHT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-UFONTHEIGHT rootpage-UFONTHEIGHT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_UFONTHEIGHT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_UFONTHEIGHT</b> function returns the global glyph height (incl. ascender/descender) of a font loaded by <a href="LOADFONT" title="LOADFONT">_LOADFONT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixelHeight&amp;</i> = <a class="mw-selflink selflink">_UFONTHEIGHT</a>[(<i>fontHandle&amp;</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>fontHandle&amp;</i> is an optional font handle.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the height of the last font used if a handle is not designated.</li>
<li>If no font is set, it returns the current screen mode's text block height.</li>
<li>This is different from <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a> as it may return larger values when using scalable fonts.</li></ul>
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
<dd>Show the difference of <b>_UFONTHEIGHT</b> vs. <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> fh <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: fh = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"LHANDW.TTF"</span>, <span style="color:#F580B1;">23</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_FONTHEIGHT ="</span>; <a href="FONTHEIGHT" title="FONTHEIGHT"><span style="color:#4593D8;">_FONTHEIGHT</span></a>(fh)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_UFONTHEIGHT ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_UFONTHEIGHT</span></a>(fh)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="background-color: #000000; color:#a9a9a9;">_FONTHEIGHT = 23</span>
<span style="background-color: #000000; color:#a9a9a9;">_UFONTHEIGHT = 32</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2810" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="UPRINTWIDTH" title="UPRINTWIDTH">_UPRINTWIDTH</a>, <a href="ULINESPACING" title="ULINESPACING">_ULINESPACING</a>, <a href="UPRINTSTRING" title="UPRINTSTRING">_UPRINTSTRING</a>, <a href="UCHARPOS" title="UCHARPOS">_UCHARPOS</a></li>
<li><a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a>, <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>, <a href="FONT" title="FONT">_FONT</a></li>
<li><a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a>, <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193351
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.058 seconds
Real time usage: 0.078 seconds
Preprocessor visited node count: 167/1000000
Post‐expand include size: 1719/2097152 bytes
Template argument size: 350/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2444/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   60.147      1 -total
  6.60%    3.971      1 Template:PageNavigation
  5.75%    3.456      2 Template:Ot
  5.12%    3.080      1 Template:PageSyntax
  4.60%    2.769      8 Template:Cl
  4.47%    2.686      1 Template:PageExamples
  4.40%    2.647      3 Template:Parameter
  4.18%    2.515      4 Template:Text
  4.04%    2.431      1 Template:PageParameters
  3.98%    2.392      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1215-0!canonical and timestamp 20240714193351 and revision id 9008.
 -->
</div>
</div>
</div>
</div>
</body>
</html>