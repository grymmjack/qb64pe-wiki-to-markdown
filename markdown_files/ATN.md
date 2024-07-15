<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ATN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ATN rootpage-ATN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ATN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">ATN</a> or arctangent function returns the angle in radians of a numerical <a href="TAN" title="TAN">tangent</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>radianAngle</i> = <a class="mw-selflink selflink">ATN</a>(<i>tangent!</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The return is the <i>tangent!'</i>s angle in <b>radians</b>.</li>
<li><i>tangent!</i> <a href="SINGLE" title="SINGLE">SINGLE</a> or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> values are used by the function. EX:<b><span style="color:green;">Pi = 4 * ATN(1)</span></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>To convert from radians to degrees, multiply radians * (180 / π).</li>
<li>The <i>tangent</i> value would be equal to the tangent value of an angle. Ex: <b><span style="color:green;"><a href="TAN" title="TAN">TAN</a>(ATN(1)) = 1</span></b></li>
<li>The function return value is between -π / 2 and π / 2.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> When the <a href="TAN" title="TAN">TANgent</a> value equals 1, the line is drawn at a 45 degree angle (.7853982 radians) where <a href="SIN" title="SIN">SIN</a> / <a href="COS" title="COS">COS</a> = 1.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
x = 100 * <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">ATN</span></a>(1))
y = 100 * <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">ATN</span></a>(1))
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (200, 200)-(200 + x, 200 + y)
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> <a class="mw-selflink selflink">ATN</a> can be used to define π in <a href="SINGLE" title="SINGLE">SINGLE</a> or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> precision. The calculation cannot be used as a <a href="CONST" title="CONST">CONSTant</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">Pi = 4 * <a class="mw-selflink selflink"><span style="color:#4593D8;">ATN</span></a>(1)   '<a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a> precision
Pi# = 4 * <a class="mw-selflink selflink"><span style="color:#4593D8;">ATN</span></a>(1#) '<a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a> precision
PRINT Pi, Pi#
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> You can use QB64's native <a href="PI" title="PI">_PI</a> function.</dd></dl>
<p>
<i>Example 3:</i> Finds the angle from the center point to the mouse pointer.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
x1! = 320
y1! = 240
DO
  <a href="PRESET" title="PRESET"><span style="color:#4593D8;">PRESET</span></a> (x1!, y1!), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255)
  dummy% = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
  x2! = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
  y2! = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (x1, y1)-(x2, y2), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 0, 0)
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> getangle(x1!, y1!, x2!, y2!)
  <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
  <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 200
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> getangle# (x1#, y1#, x2#, y2#) 'returns 0-359.99...
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y2# = y1# <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x1# = x2# <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x2# &gt; x1# <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> getangle# = 90 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> getangle# = 270
  <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x2# = x1# <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y2# &gt; y1# <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> getangle# = 180
  <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y2# &lt; y1# <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x2# &gt; x1# <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    getangle# = <a class="mw-selflink selflink"><span style="color:#4593D8;">ATN</span></a>((x2# - x1#) / (y2# - y1#)) * -57.2957795131
  <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    getangle# = <a class="mw-selflink selflink"><span style="color:#4593D8;">ATN</span></a>((x2# - x1#) / (y2# - y1#)) * -57.2957795131 + 360
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
  getangle# = <a class="mw-selflink selflink"><span style="color:#4593D8;">ATN</span></a>((x2# - x1#) / (y2# - y1#)) * -57.2957795131 + 180
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PI" title="PI">_PI</a> <span style="color:#777777;">(QB64 function)</span></li>
<li><a href="ATAN2" title="ATAN2">_ATAN2</a> <span style="color:#777777;">((QB64 function)</span></li>
<li><a href="TAN" title="TAN">TAN</a> <span style="color:#777777;">(tangent function)</span></li>
<li><a href="SIN" title="SIN">SIN</a>, <a href="COS" title="COS">COS</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a href="Mathematical_Operations#Derived_Mathematical_Functions" title="Mathematical Operations">Derived Mathematical Functions</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061226
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 487/1000000
Post‐expand include size: 4307/2097152 bytes
Template argument size: 842/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   26.147      1 -total
 14.45%    3.779     57 Template:Cl
  8.22%    2.149      1 Template:PageSyntax
  7.32%    1.914      1 Template:Small
  6.96%    1.819      4 Template:Parameter
  6.85%    1.792      5 Template:Text
  6.64%    1.736      3 Template:CodeEnd
  6.11%    1.598      1 Template:PageSeeAlso
  6.10%    1.595      1 Template:PageParameters
  6.04%    1.578      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:398-0!canonical and timestamp 20240715061226 and revision id 8584.
 -->
</div>
</div>
</div>
</div>
</body>
</html>