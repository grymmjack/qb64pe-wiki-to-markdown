<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DISPLAYORDER - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DISPLAYORDER rootpage-DISPLAYORDER skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DISPLAYORDER</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DISPLAYORDER</a> statement defines the order to render software, hardware and custom-OpenGL-code.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_DISPLAYORDER</a> [{_SOFTWARE|_HARDWARE|_HARDWARE1|_GLRENDER}][, ...][, ...][, ...][, ...]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>_SOFTWARE refers to software created surfaces or <a href="SCREEN" title="SCREEN">SCREENs</a>.</li>
<li>_HARDWARE and _HARDWARE1 refer to surfaces created by OpenGL hardware acceleration.</li>
<li>_GLRENDER refers to OpenGL code rendering order</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The default on program start is: _DISPLAYORDER _SOFTWARE, _HARDWARE, _GLRENDER, _HARDWARE1</li>
<li>Any content or combination order is allowed, except listing the same content twice consecutively.</li>
<li>Simply using <a class="mw-selflink selflink">_DISPLAYORDER</a> _HARDWARE will render hardware surfaces only.</li>
<li>Use an <a href="Underscore" title="Underscore">underscore</a> to continue a code line on a new text row in the IDE.</li>
<li>After _DISPLAYORDER has been used, it must be used to make any changes, even to default.</li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li>If a rendering content is not listed it will not be rendered except when using the startup default.</li>
<li>Rendering the same content twice consecutively in a combination is not allowed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.000 and up.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DISPLAY" title="DISPLAY">_DISPLAY</a></li>
<li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li><a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a></li>
<li><a href="Hardware_images" title="Hardware images">Hardware images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062325
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.015 seconds
Real time usage: 0.019 seconds
Preprocessor visited node count: 33/1000000
Post‐expand include size: 625/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   10.772      1 -total
 18.79%    2.024      1 Template:PageSyntax
 16.58%    1.786      1 Template:PageAvailability
 15.82%    1.704      1 Template:PageDescription
 15.54%    1.674      1 Template:PageParameters
 15.15%    1.632      1 Template:PageSeeAlso
 13.37%    1.440      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:125-0!canonical and timestamp 20240715062325 and revision id 7494.
 -->
</div>
</div>
</div>
</div>
</body>
</html>