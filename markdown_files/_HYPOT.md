<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_HYPOT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-HYPOT rootpage-HYPOT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_HYPOT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_HYPOT</a> function returns the hypotenuse of a right-angled triangle whose legs are x and y.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result!</i> = <a class="mw-selflink selflink">_HYPOT</a>(<i>x</i>, <i>y</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>x</i> and <i>y</i> are the floating point values corresponding to the legs of a right-angled (90 degree) triangle for which the hypotenuse is computed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function returns what would be the square root of the sum of the squares of x and y (as per the Pythagorean theorem).</li>
<li>The hypotenuse is the longest side between the two 90 degree angle sides</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> leg_x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, leg_y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, result <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>
leg_x = <span style="color:#F580B1;">3</span>
leg_y = <span style="color:#F580B1;">4</span>
result = <a class="mw-selflink selflink"><span style="color:#4593D8;">_HYPOT</span></a>(leg_x, leg_y)
<a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> <span style="color:#FFB100;">"## , ## and ## form a right-angled triangle."</span>; leg_x; leg_y; result
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 3 , 4 and 5 form a right-angled triangle.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1782" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="ATN" title="ATN">ATN</a> <span style="color:#777777;">(arctangent)</span></li>
<li><a href="PI" title="PI">_PI</a> <span style="color:#777777;">(function)</span></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a class="external text" href="http://www.cplusplus.com/reference/cmath/hypot/" rel="nofollow">C++ reference for hypot() - source of the text and sample above</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714154051
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.034 seconds
Preprocessor visited node count: 148/1000000
Post‐expand include size: 1486/2097152 bytes
Template argument size: 178/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 46/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.536      1 -total
  8.86%    1.908      1 Template:PageSyntax
  8.44%    1.817      5 Template:Text
  8.28%    1.782      9 Template:Cl
  7.86%    1.693      1 Template:OutputStart
  7.81%    1.683      1 Template:OutputEnd
  7.30%    1.572      5 Template:Parameter
  6.55%    1.411      1 Template:PageDescription
  6.54%    1.409      1 Template:CodeStart
  6.25%    1.345      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:141-0!canonical and timestamp 20240714154051 and revision id 8938.
 -->
</div>
</div>
</div>
</div>
</body>
</html>