<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CLIPBOARDIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CLIPBOARDIMAGE rootpage-CLIPBOARDIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CLIPBOARDIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CLIPBOARDIMAGE</a> statement copies a valid QB64 image to the clipboard.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_CLIPBOARDIMAGE</a> = <i>existingImageHandle&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>existingImageHandle&amp;</i> is a valid handle to a graphic QB64 image in memory, created with <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> or <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a>.</li>
<li>You can pass <a href="SOURCE" title="SOURCE">_SOURCE</a>, <a href="DEST" title="DEST">_DEST</a> or <a href="DISPLAY" title="DISPLAY">_DISPLAY</a> to copy the current source, destination or active display pages, as long as they are valid graphic images.</li>
<li>SCREEN 0 handles (created either with <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> or passed using _DEST while in a text screen) are not valid and will create an <a href="ERROR_Codes" title="ERROR Codes">Illegal Function Call</a> or <a href="ERROR_Codes" title="ERROR Codes">Invalid Handle</a> error.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v1.2"><img alt="v1.2" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v1.2</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="all"><img alt="all" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>all</b>
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
<ul><li>Available for <i>macOS</i> and <i>Linux</i> since <b>QB64-PE v3.13.0</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Create a sample image and copy it to the clipboard:</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">800</span>, <span style="color:#F580B1;">600</span>, <span style="color:#F580B1;">32</span>)
<span style="color:#919191;">'Create image in memory:</span>
canvas&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">300</span>, <span style="color:#F580B1;">200</span>, <span style="color:#F580B1;">32</span>)
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> canvas&amp;
<span style="color:#919191;">'Draw some random rectangles:</span>
<a href="RANDOMIZE" title="RANDOMIZE"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">100</span>
    <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">-100</span> + <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>, <span style="color:#F580B1;">-100</span> + <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>)-<a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">150</span>, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">150</span>), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">255</span>, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">255</span>, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">255</span>), BF
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)-(<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> - <span style="color:#F580B1;">1</span>, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> - <span style="color:#F580B1;">1</span>), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>), B
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>)
m$ = <span style="color:#FFB100;">" Hello, world! "</span>
<a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> / <span style="color:#F580B1;">2</span> - <a href="PRINTWIDTH" title="PRINTWIDTH"><span style="color:#4593D8;">_PRINTWIDTH</span></a>(m$) / <span style="color:#F580B1;">2</span>, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> / <span style="color:#F580B1;">2</span> - <a href="FONTHEIGHT" title="FONTHEIGHT"><span style="color:#4593D8;">_FONTHEIGHT</span></a> / <span style="color:#F580B1;">2</span>), m$
<span style="color:#919191;">'Show the image:</span>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <span style="color:#F580B1;">0</span>
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> / <span style="color:#F580B1;">2</span> - <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(canvas&amp;) / <span style="color:#F580B1;">2</span>, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> / <span style="color:#F580B1;">2</span> - <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(canvas&amp;) / <span style="color:#F580B1;">2</span>), canvas&amp;
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Image generated."</span>
<span style="color:#919191;">'Copy to the clipboard:</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CLIPBOARDIMAGE</span></a> = canvas&amp;
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Image copied to clipboard."</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CLIPBOARDIMAGE_(function)" title="CLIPBOARDIMAGE (function)">_CLIPBOARDIMAGE</a> <span style="color:#777777;">(function - used to paste an image from the clipboard)</span></li>
<li><a href="CLIPBOARD$" title="CLIPBOARD$">_CLIPBOARD$</a>, <a href="CLIPBOARD$_(function)" title="CLIPBOARD$ (function)">_CLIPBOARD$ (function)</a> <span style="color:#777777;">(used to copy/paste text)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211313
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.073 seconds
Real time usage: 0.090 seconds
Preprocessor visited node count: 680/1000000
Post‐expand include size: 5212/2097152 bytes
Template argument size: 1322/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2514/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   68.061      1 -total
  7.42%    5.047     42 Template:Cl
  6.96%    4.738     46 Template:Text
  6.09%    4.143      1 Template:CodeStart
  4.09%    2.784      1 Template:PageExamples
  3.88%    2.640      1 Template:CodeEnd
  3.63%    2.471      1 Template:PageSyntax
  3.33%    2.269      2 Template:Parameter
  3.25%    2.214      1 Template:PageNavigation
  3.16%    2.150      1 Template:Small
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:90-0!canonical and timestamp 20240714211313 and revision id 8844.
 -->
</div>
</div>
</div>
</div>
</body>
</html>