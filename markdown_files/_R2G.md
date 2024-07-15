<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_R2G - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-R2G rootpage-R2G skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_R2G</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_R2G</a> function converts a <b>radian</b> value into a <b>gradient</b> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result!</i> = <a class="mw-selflink selflink">_R2G</a>(<i>num</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.0 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Coverting Radian into Gradient.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Give me an angle in Radians "</span>, R
G = <a class="mw-selflink selflink"><span style="color:#4593D8;">_R2G</span></a>(R)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"That angle in Gradient is "</span>; G
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Give me an angle in Radians 0.5
That angle in Gradient is   31.83099
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="D2G" title="D2G">_D2G</a>, <a href="D2R" title="D2R">_D2R</a></li>
<li><a href="G2D" title="G2D">_G2D</a>, <a href="G2R" title="G2R">_G2R</a></li>
<li><a href="R2D" title="R2D">_R2D</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062430
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.038 seconds
Preprocessor visited node count: 75/1000000
Post‐expand include size: 1031/2097152 bytes
Template argument size: 120/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 58/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.205      1 -total
 10.68%    2.693      1 Template:PageSyntax
  8.32%    2.097      1 Template:PageExamples
  8.21%    2.069      3 Template:Cl
  7.91%    1.994      1 Template:PageAvailability
  7.84%    1.975      2 Template:Parameter
  7.60%    1.916      2 Template:Text
  7.51%    1.894      1 Template:CodeStart
  7.46%    1.880      1 Template:PageNavigation
  7.32%    1.844      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:77-0!canonical and timestamp 20240715062430 and revision id 8347.
 -->
</div>
</div>
</div>
</div>
</body>
</html>