<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_HEIGHT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-HEIGHT rootpage-HEIGHT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_HEIGHT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_HEIGHT</a> function returns the height of an image handle or of the current write page.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>columns&amp;</i> = <a class="mw-selflink selflink">_HEIGHT</a>[(<i>imageHandle&amp;</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If <i>imageHandle&amp;</i> is omitted, it's assumed to be the handle of the current <a href="SCREEN" title="SCREEN">SCREEN</a> or write page.</li>
<li>To get the height of the current program <a href="SCREEN" title="SCREEN">screen</a> window use zero for the handle value or nothing: <i>lines&amp;</i> = <a class="mw-selflink selflink">_HEIGHT</a>(0) <i>or</i> <i>lines&amp;</i> = <a class="mw-selflink selflink">_HEIGHT</a></li>
<li>If the image specified by <i>imageHandle&amp;</i> is in text only(<a href="SCREEN" title="SCREEN">SCREEN</a> 0) mode, the number of lines of rows of characters are returned.</li>
<li>If the image specified by <i>imageHandle&amp;</i> is in graphics mode, the number rows of pixels is returned.</li>
<li>If <i>imageHandle&amp;</i> is an invalid handle, then an <a href="ERROR_Codes" title="ERROR Codes">invalid handle error</a> is returned.</li>
<li>The last visible pixel coordinate of a program <a href="SCREEN" title="SCREEN">screen</a> is <b><a class="mw-selflink selflink">_HEIGHT</a> - 1</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH (function)</a>, <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062342
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.014 seconds
Real time usage: 0.019 seconds
Preprocessor visited node count: 45/1000000
Post‐expand include size: 657/2097152 bytes
Template argument size: 80/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   10.359      1 -total
 20.36%    2.109      8 Template:Parameter
 20.32%    2.105      1 Template:PageSyntax
 17.69%    1.832      1 Template:PageNavigation
 17.32%    1.794      1 Template:PageSeeAlso
 16.98%    1.759      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:138-0!canonical and timestamp 20240715062342 and revision id 7305.
 -->
</div>
</div>
</div>
</div>
</body>
</html>