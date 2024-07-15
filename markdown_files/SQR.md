<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SQR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SQR rootpage-SQR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SQR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>SQR</b> function returns the square root of a numerical value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>square_root = <b>SQR(</b>value<b>)</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>square root</i> returned is normally a <a href="SINGLE" title="SINGLE">SINGLE</a> or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> numerical value.</li>
<li>The <i>value</i> parameter can be any <b>positive</b> numerical type. <b>Negative parameter values will not work!</b></li>
<li>Other exponential root functions can use fractional exponents(<a href="%5E" title="^">^</a>) enclosed in <b>parenthesis only</b>. EX: <span style="color:green;">root  =  c ^ (a / b)</span></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Finding the hypotenuse of a right triangle:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> A% = 3: B% = 4
 PRINT "hypotenuse! ="; SQR((A% ^ 2) + (B% ^ 2))
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> hypotenuse = 5
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Finding the Cube root of a number.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> number = 8
 cuberoot = number <a href="%5E" title="^"><span style="color:#4593D8;">^</span></a> (1/3)
 PRINT cuberoot
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 2
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Negative roots return fractional values of one.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> number = 8
 negroot = number <a href="%5E" title="^"><span style="color:#4593D8;">^</span></a> -2
 PRINT negroot
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> .015625
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> A negative root means that the exponent value is actually inverted to a fraction of 1. So x ^ -2 actually means the result will be: 1 / (x ^ 2).</dd></dl>
<p>
<i>Example 4:</i> Fast Prime number checker limits the numbers checked to the square root (half way).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">DEFLNG P
DO
PRIME = -1   'set PRIME as True
INPUT "Enter any number to check up to 2 million (Enter quits): ", guess$
PR = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(guess$)
IF PR <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 2 THEN              'check for even number
  FOR P = 3 TO <a class="mw-selflink selflink"><span style="color:#4593D8;">SQR</span></a>(PR) STEP 2 'largest number that could be a multiple is the SQR
    IF PR <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> P = 0 THEN PRIME = 0: EXIT FOR 'MOD = 0 when evenly divisible by another
  NEXT
ELSE : PRIME = 0 'number to be checked is even so it cannot be a prime
END IF
IF PR = 2 THEN PRIME = -1 '2 is the ONLY even prime
IF PR = 1 THEN PRIME = 0  'MOD returns true but 1 is not a prime by definition
IF PRIME THEN PRINT "PRIME! How'd you find me? " ELSE PRINT "Not a prime, you lose!"
LOOP UNTIL PR = 0
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Enter any number to check up to 2 million (Enter quits): 12379
PRIME! How'd you find me?
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MOD" title="MOD">MOD</a></li>
<li><a href="%5E" title="^">^</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a href="Mathematical_Operations#Derived_Mathematical_Functions" title="Mathematical Operations">Derived Mathematical Functions</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061422
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 95/1000000
Post‐expand include size: 1497/2097152 bytes
Template argument size: 84/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 3/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.469      1 -total
 11.60%    3.187      4 Template:CodeEnd
 10.10%    2.775      4 Template:OutputStart
  9.35%    2.567      6 Template:Cl
  8.38%    2.303      1 Template:PageSyntax
  8.25%    2.265      1 Template:PageSeeAlso
  7.92%    2.176      4 Template:OutputEnd
  7.79%    2.140      4 Template:CodeStart
  7.68%    2.110      1 Template:PageNavigation
  6.99%    1.920      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:567-0!canonical and timestamp 20240715061422 and revision id 7965.
 -->
</div>
</div>
</div>
</div>
</body>
</html>