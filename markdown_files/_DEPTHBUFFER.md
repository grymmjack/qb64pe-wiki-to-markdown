<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DEPTHBUFFER - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEPTHBUFFER rootpage-DEPTHBUFFER skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DEPTHBUFFER</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DEPTHBUFFER</a> statement turns depth buffering ON or OFF, LOCKs or _CLEARS the buffer.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_DEPTHBUFFER</a> {ON|OFF|LOCK|_CLEAR}[,handle&amp;]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Depth buffers store the distance of each pixel on an image/surface. When 3D drawing occurs new pixels are only drawn if they are closer than the existing pixels. After all content is drawn, it results in a scene which looks correct because content which is closer hides content which is further away.</li>
<li>Depth buffers are automatically created for any hardware image or surface which is the target/destination of a 3D command (such as the 3D version of <a href="MAPTRIANGLE" title="MAPTRIANGLE">_MAPTRIANGLE</a>).</li>
<li>The buffering can be turned ON, OFF or LOCKed. The default state is ON.</li>
<li><a class="mw-selflink selflink">_DEPTHBUFFER</a> _CLEAR can be used to reset/erase the depth buffer, meaning that future drawing will not be blocked by existing/previously buffered depth content.</li>
<li>Whenever _DISPLAY is called the primary surface's depth buffer is automatically _CLEARed, so unless you are drawing onto a hardware image you may never need to use this option.</li>
<li>LOCKing the depth buffer makes it read only. New content cannot be drawn unless it is closer than existing content, but when that new content is drawn it will not update the depth buffer.</li>
<li>Turning OFF or LOCKing the depth buffer is typically performed when semi-transparent content is being drawn.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MAPTRIANGLE" title="MAPTRIANGLE">_MAPTRIANGLE</a></li>
<li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a></li>
<li><a href="DISPLAY" title="DISPLAY">_DISPLAY</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062316
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.014 seconds
Real time usage: 0.018 seconds
Preprocessor visited node count: 13/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    9.757      1 -total
 28.63%    2.793      1 Template:PageDescription
 24.83%    2.423      1 Template:PageSyntax
 22.16%    2.162      1 Template:PageNavigation
 20.36%    1.986      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:113-0!canonical and timestamp 20240715062316 and revision id 7262.
 -->
</div>
</div>
</div>
</div>
</body>
</html>