<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ACOS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ACOS rootpage-ACOS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ACOS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ACOS</a> function returns the angle measured in radians based on an input <a href="COS" title="COS">COSine</a> value ranging from -1 to 1.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>radian_angle!</i> = <a class="mw-selflink selflink">_ACOS</a>(<i>cosine_value!</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>cosine_value!</i> must be measured &gt;= -1 and &lt;= 1, or an error will be generated.  (PRINT _ACOS(1.2) would give the result of -1.#IND, which is basically QB64's way of telling us that the number doesn't exist, much like 1/0 would.)</li>
<li>ARCCOSINE is the inverse function of <a href="COS" title="COS">COSine</a>, which lets us turn a <a href="COS" title="COS">COSine</a> value back into an angle.</li>
<li>Note: Due to rounding with floating point math, the _ACOS may not always give a perfect match for the COS angle which generated this.  You can reduce the number of rounding errors by increasing the precision of your calculations by using <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a> precision variables instead of <a href="SINGLE" title="SINGLE">SINGLE</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.000 and up.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Converting a radian angle to its COSine and using that value to find the angle in degrees again using _ACOS:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFDBL" title="DEFDBL"><span style="color:#4593D8;">DEFDBL</span></a> A-Z
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Give me an Angle (in Degrees) =&gt; "</span>; Angle
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
C = <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(<a href="D2R" title="D2R"><span style="color:#4593D8;">_D2R</span></a>(Angle)) <span style="color:#919191;">'_D2R is the command to convert Degrees to Radians, which is what COS expects</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"The COSINE of the Angle is: "</span>; C
A = <a class="mw-selflink selflink"><span style="color:#4593D8;">_ACOS</span></a>(C)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"The ACOS of "</span>; C; <span style="color:#FFB100;">" is: "</span>; A
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Notice, A is the Angle in Radians.  If we convert it to degrees, the value is "</span>; <a href="R2D" title="R2D"><span style="color:#4593D8;">_R2D</span></a>(A)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Give me an Angle (in Degrees) =&gt; ? 60
The COSINE of the Angle is:  .5000000000000001
The ACOS of  .5000000000000001  is:  1.047197551196598
Notice, A is the Angle in Radians.  If we convert it to degrees, we discover the value is  60
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="D2G" title="D2G">_D2G</a> <span style="color:#777777;">(degree to gradient</span>, <a href="D2R" title="D2R">_D2R</a> <span style="color:#777777;">(degree to radian)</span></li>
<li><a href="G2D" title="G2D">_G2D</a> <span style="color:#777777;">(gradient to degree)</span>, <a href="G2R" title="G2R">_G2R</a> <span style="color:#777777;">(gradient to degree</span></li>
<li><a href="R2D" title="R2D">_R2D</a> <span style="color:#777777;">(radian to degree)</span>, <a href="R2G" title="R2G">_R2G</a> <span style="color:#777777;">(radian to gradient</span></li>
<li><a href="COS" title="COS">COS</a> <span style="color:#777777;">(cosine)</span>, <a href="SIN" title="SIN">SIN</a> <span style="color:#777777;">(sine)</span>, <a href="TAN" title="TAN">TAN</a> <span style="color:#777777;">(tangent)</span></li>
<li><a href="ASIN" title="ASIN">_ASIN</a> <span style="color:#777777;">(arc sine)</span>, <a href="ATN" title="ATN">ATN</a> <span style="color:#777777;">(arc tangent)</span></li>
<li><a href="ACOSH" title="ACOSH">_ACOSH</a> <span style="color:#777777;">(arc hyperbolic  cosine)</span>, <a href="ASINH" title="ASINH">_ASINH</a> <span style="color:#777777;">(arc hyperbolic  sine)</span>, <a href="ATANH" title="ATANH">_ATANH</a> <span style="color:#777777;">(arc hyperbolic  tangent)</span></li>
<li><a href="ATAN2" title="ATAN2">_ATAN2</a> <span style="color:#777777;">(Compute arc tangent with two parameters)</span></li>
<li><a href="HYPOT" title="HYPOT">_HYPOT</a> <span style="color:#777777;">(hypotenuse)</span></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a href="Mathematical_Operations#Derived_Mathematical_Functions" title="Mathematical Operations">Derived Mathematical Functions</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062234
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.050 seconds
Preprocessor visited node count: 268/1000000
Post‐expand include size: 2719/2097152 bytes
Template argument size: 668/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 246/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.752      1 -total
  8.68%    2.931     22 Template:Text
  7.10%    2.398      1 Template:OutputEnd
  6.95%    2.344      1 Template:PageSyntax
  6.94%    2.343      1 Template:PageDescription
  6.80%    2.295      1 Template:PageNavigation
  6.51%    2.199      1 Template:CodeStart
  6.49%    2.192      1 Template:Small
  6.41%    2.164      1 Template:OutputStart
  6.37%    2.150      2 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:37-0!canonical and timestamp 20240715062234 and revision id 8254.
 -->
</div>
</div>
</div>
</div>
</body>
</html>