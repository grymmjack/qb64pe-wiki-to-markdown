<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ATAN2 - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ATAN2 rootpage-ATAN2 skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ATAN2</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ATAN2</a> function returns the radian angle between the positive x-axis of a plane and the point given by the coordinates (x, y).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>angle!</i> = <a class="mw-selflink selflink">_ATAN2</a>(<i>y</i>, <i>x</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>y</i> is the vertical axis position (row) as a positive, zero or negative floating point value.</li>
<li><i>x</i> is the horizontal axis position (column) as a positive, zero or negative floating point value.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <a href="DOUBLE" title="DOUBLE">DOUBLE</a> radian angle returned is <b>positive</b> for upper row values where y &gt; 0.</li></ul>
<dl><dd><dl><dd><ul><li>_ATAN2(y, x) = <a href="ATN" title="ATN">ATN</a>(y# / x#) when x &gt; 0</li>
<li>_ATAN2(y, x) = <a href="ATN" title="ATN">ATN</a>(y# / x#) + <a href="PI" title="PI">_PI</a> when x &lt; 0</li>
<li>_ATAN2(y, x) = <a href="PI" title="PI">_PI</a> / 2 when x = 0</li></ul></dd></dl></dd></dl>
<ul><li>The <a href="DOUBLE" title="DOUBLE">DOUBLE</a> radian angle returned is 0 when x &gt; 0 and <a href="PI" title="PI">_PI</a> when x &lt; 0 where y = 0</li>
<li>The <a href="DOUBLE" title="DOUBLE">DOUBLE</a> radian angle returned is <b>negative</b> for lower row values where y &lt; 0.</li></ul>
<dl><dd><dl><dd><ul><li>_ATAN2(y, x) = <a href="ATN" title="ATN">ATN</a>(y# / x#) when x &gt; 0</li>
<li>_ATAN2(y, x) = <a href="ATN" title="ATN">ATN</a>(y# / x#) - <a href="PI" title="PI">_PI</a> when x &lt; 0</li>
<li>_ATAN2(y, x) = -<a href="PI" title="PI">_PI</a> / 2 when x = 0</li></ul></dd></dl></dd></dl>
<ul><li>_ATAN2(0, 0) is undefined and the function returns 0 instead of a division error.</li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li>With <a href="ATN" title="ATN">ATN</a>(y / x), x can never be 0 as that would create a Division by Zero <a href="ERROR_Codes" title="ERROR Codes">error</a> 11 or #IND.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ATN" title="ATN">ATN</a> <span style="color:#777777;">(arctangent)</span></li>
<li><a href="PI" title="PI">_PI</a> <span style="color:#777777;">(QB64 function)</span></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a class="extiw" href="https://en.wikipedia.org/wiki/Atan2" title="wikipedia:Atan2">Atan2 reference</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714164117
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 81/1000000
Post‐expand include size: 713/2097152 bytes
Template argument size: 37/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.801      1 -total
 19.37%    3.642      1 Template:PageSyntax
 18.76%    3.526      2 Template:Text
 12.64%    2.377      5 Template:Parameter
 10.99%    2.067      1 Template:PageNavigation
 10.72%    2.016      1 Template:PageSeeAlso
 10.63%    1.998      1 Template:PageParameters
 10.46%    1.966      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:47-0!canonical and timestamp 20240714164117 and revision id 8978.
 -->
</div>
</div>
</div>
</div>
</body>
</html>