<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_NEGATE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-NEGATE rootpage-NEGATE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_NEGATE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">_NEGATE</a> is a <a href="Boolean" title="Boolean">boolean</a> logical operator that will change a false statement to a true one and vice-versa.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_NEGATE</a> <i>value</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Unlike <a href="NOT" title="NOT">NOT</a>, which evaluates a value and returns the bitwise opposite, <a class="mw-selflink selflink">_NEGATE</a> returns the logical opposite. Meaning that <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">_NEGATE <i>non_zero_value</i> = 0</span>.</li>
<li>Often called a negative logic operator, it returns the opposite of a value as true or false.</li></ul>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.13.0"><img alt="v3.13.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.13.0</b>
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
<p><i>Example:</i> NOT versus _NEGATE
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE LIBRARY</span></a>
    <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">isdigit&amp;</span> (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
<a class="mw-redirect" href="END_DECLARE" title="END DECLARE"><span style="color:#4593D8;">END DECLARE</span></a>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <span style="color:#55FF55;">isdigit</span>(<a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<span style="color:#FFB100;">"1"</span>)) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"NOT: 1 is not a digit."</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"NOT: 1 is a digit."</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_NEGATE</span></a> <span style="color:#55FF55;">isdigit</span>(<a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<span style="color:#FFB100;">"1"</span>)) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_NEGATE: 1 is not a digit."</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_NEGATE: 1 is a digit."</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">NOT: 1 is not a digit.
_NEGATE: 1 is a digit.
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> NOT is a bitwise operator that inverts all the bits in an integer, whereas _NEGATE is a logical operator that flips the truth value of a boolean expression.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2671" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="BIT" title="BIT">_BIT</a>, <a href="%26B" title="&amp;B">&amp;B</a>, <a href="BYTE" title="BYTE">_BYTE</a></li>
<li><a href="AND" title="AND">AND</a>, <a class="mw-redirect" href="XOR" title="XOR">XOR</a>, <a href="OR" title="OR">OR</a></li>
<li><a href="AND_(boolean)" title="AND (boolean)">AND (boolean)</a>, <a href="XOR_(boolean)" title="XOR (boolean)">XOR (boolean)</a>, <a href="OR_(boolean)" title="OR (boolean)">OR (boolean)</a></li>
<li><a href="ANDALSO" title="ANDALSO">_ANDALSO</a>, <a href="ORELSE" title="ORELSE">_ORELSE</a></li>
<li><a href="Binary" title="Binary">Binary</a>, <a href="Boolean" title="Boolean">Boolean</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062619
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.055 seconds
Real time usage: 0.068 seconds
Preprocessor visited node count: 296/1000000
Post‐expand include size: 2749/2097152 bytes
Template argument size: 568/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2473/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   47.435      1 -total
  5.11%    2.425     23 Template:Cl
  4.84%    2.295      1 Template:PageSyntax
  4.53%    2.147      3 Template:Parameter
  4.42%    2.096      1 Template:PageExamples
  4.39%    2.083      1 Template:PageDescription
  4.10%    1.945      1 Template:CodeStart
  3.95%    1.873      9 Template:Text
  3.84%    1.822      1 Template:PageAvailability
  3.76%    1.784      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1235-0!canonical and timestamp 20240715062619 and revision id 8941.
 -->
</div>
</div>
</div>
</div>
</body>
</html>