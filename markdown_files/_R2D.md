<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_R2D - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-R2D rootpage-R2D skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_R2D</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_R2D</a> function converts a <b>radian</b> value into a <b>degree</b> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result!</i> = <a class="mw-selflink selflink">_R2D</a>(<i>num</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.0 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Coverting Radian into Degree.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Give me an angle in Radians "</span>, R
D = <a class="mw-selflink selflink"><span style="color:#4593D8;">_R2D</span></a>(R)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"That angle in Degrees is "</span>; D
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Give me an angle in Radians 0.5
That angle in Degrees is    28.64789
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="D2G" title="D2G">_D2G</a>, <a href="D2R" title="D2R">_D2R</a></li>
<li><a href="G2D" title="G2D">_G2D</a>, <a href="G2R" title="G2R">_G2R</a></li>
<li><a href="R2G" title="R2G">_R2G</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062429
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 75/1000000
Post‐expand include size: 1031/2097152 bytes
Template argument size: 120/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 57/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.690      1 -total
  9.95%    2.358      1 Template:CodeStart
  9.89%    2.343      1 Template:PageSyntax
  7.91%    1.875      1 Template:PageNavigation
  7.87%    1.865      2 Template:Text
  7.86%    1.861      2 Template:Parameter
  7.80%    1.847      3 Template:Cl
  7.57%    1.793      1 Template:PageSeeAlso
  7.43%    1.760      1 Template:PageAvailability
  7.36%    1.744      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:73-0!canonical and timestamp 20240715062429 and revision id 8346.
 -->
</div>
</div>
</div>
</div>
</body>
</html>