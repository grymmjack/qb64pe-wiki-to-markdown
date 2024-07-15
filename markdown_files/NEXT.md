<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>NEXT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-NEXT rootpage-NEXT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">NEXT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">NEXT</a> is used in a <a href="FOR...NEXT" title="FOR...NEXT">FOR</a> counter loop to progress through the loop count.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="FOR" title="FOR">FOR</a> <i>counterVariable</i> = <i>startValue</i> <a href="TO" title="TO">TO</a> <i>stopValue</i> [[[STEP <i>increment</i>]
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a class="mw-selflink selflink">NEXT</a> [<i>counterVariable</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">NEXT</a> is required in a FOR loop or a <a href="ERROR_Codes" title="ERROR Codes">"FOR without NEXT" error</a> will occur.</li>
<li>The FOR variable name is not required after <a class="mw-selflink selflink">NEXT</a>.</li>
<li><a class="mw-selflink selflink">NEXT</a> can be grouped with other NEXTs in nested FOR loops using colons like <a class="mw-selflink selflink">NEXT</a>: <a class="mw-selflink selflink">NEXT</a></li>
<li><a class="mw-selflink selflink">NEXT</a> can also end more than one nested <a href="FOR...NEXT" title="FOR...NEXT">FOR</a> loop using comma separated variables like <a class="mw-selflink selflink">NEXT</a> j, i</li>
<li><a class="mw-selflink selflink">NEXT</a> increases the FOR loop count, so after the loop is over the counterVariable's value will be stopValue + 1 (or stopValue + increment).</li>
<li><a class="mw-selflink selflink">NEXT</a>  is also used with the <a href="RESUME" title="RESUME">RESUME</a> statement.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Finding the FOR variable value AFTER a simple counter loop to 10.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">FOR i = 1 TO 10
PRINT i;
NEXT i
PRINT "AFTER the LOOP, NEXT makes the value of i ="; i
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">1 2 3 4 5 6 7 8 9 10 AFTER the LOOP, NEXT makes the value of i = 11
</pre>
</td></tr></tbody></table>
<p><i>Result:</i> The last value of i = 11 although FOR only looped 10 times. <b>Only use the count values while inside of the loop or compensate for this behavior in your code.</b>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a></li>
<li><a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a></li>
<li><a href="RESUME" title="RESUME">RESUME NEXT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714174233
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 45/1000000
Post‐expand include size: 799/2097152 bytes
Template argument size: 58/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.023      1 -total
 12.67%    2.791      1 Template:PageSyntax
 11.69%    2.575      5 Template:Parameter
 11.50%    2.532      1 Template:PageDescription
 11.07%    2.438      1 Template:PageExamples
  8.75%    1.927      1 Template:CodeStart
  7.82%    1.723      1 Template:PageNavigation
  7.70%    1.696      1 Template:PageSeeAlso
  7.66%    1.688      1 Template:OutputStart
  7.59%    1.672      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:307-0!canonical and timestamp 20240714174233 and revision id 6599.
 -->
</div>
</div>
</div>
</div>
</body>
</html>