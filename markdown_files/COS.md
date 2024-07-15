<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>COS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-COS rootpage-COS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">COS</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">COS</a> function returns the horizontal component or the cosine of an angle measured in radians.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>value!</i> = <a class="mw-selflink selflink">COS</a>(<i>radianAngle!</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>radianAngle!</i> must be measured in radians.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>To convert from degrees to radians, multiply degrees * π / 180.</li>
<li><a class="mw-selflink selflink">COS</a>INE is the horizontal component of a unit vector in the direction theta (θ).</li>
<li>COS(x) can be calculated in either <a href="SINGLE" title="SINGLE">SINGLE</a> or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> precision depending on its argument.</li></ul>
<dl><dd><dl><dd><dl><dd>COS(4) = -.6536436 ...... COS(4#) = -.6536436208636119</dd></dl></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Converting degree angles to radians for QBasic's trig functions and drawing the line at the angle.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
PI = 4 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "PI = 4 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1) ="; PI
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "COS(PI) = "; <a class="mw-selflink selflink"><span style="color:#4593D8;">COS</span></a>(PI)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "SIN(PI) = "; <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(PI)
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
  <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter the degree angle (0 quits): ", DEGREES%
  RADIANS = DEGREES% * PI / 180
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "RADIANS = DEGREES% * PI / 180 = "; RADIANS
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "X = COS(RADIANS) = "; <a class="mw-selflink selflink"><span style="color:#4593D8;">COS</span></a>(RADIANS)
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Y = SIN(RADIANS) = "; <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(RADIANS)
  <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (400, 240), 2, 12
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (400, 240)-(400 + (50 * <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(RADIANS)), 240 + (50 * <a class="mw-selflink selflink"><span style="color:#4593D8;">COS</span></a>(RADIANS))), 11
  DEGREES% = RADIANS * 180 / PI
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "DEGREES% = RADIANS * 180 / PI ="; DEGREES%
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> DEGREES% = 0
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">PI = 4 * ATN(1) = 3.141593
COS(PI) = -1
SIN(PI) = -8.742278E-08
Enter the degree angle (0 quits): 45
RADIANS = DEGREES% * PI / 180 = .7853982
X = COS(RADIANS) = .7071068
Y = SIN(RADIANS) = .7071068
DEGREES% = RADIANS * 180 / PI = 45
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> When 8.742278E-08(.00000008742278) is returned by <a href="SIN" title="SIN">SIN</a> or COS the value  is essentially zero.</dd></dl>
<p>
<i>Example 2:</i> Creating 12 analog clock hour points using <a href="CIRCLE" title="CIRCLE">CIRCLEs</a> and <a href="PAINT" title="PAINT">PAINT</a>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> PI2 = 8 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1)                  '2 * π
 arc! = PI2 / 12                          'arc interval between hour circles
 <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
 FOR t! = 0 TO PI2 STEP arc!
   cx% = <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">COS</span></a>(t!) * 70) ' pixel columns (circular radius = 70)
   cy% = <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(<a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(t!) * 70) ' pixel rows
   <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (cx% + 320, cy% + 240), 3, 12
   <a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(0, 0), 9, 12
 NEXT
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> The 12 circles are placed at radian angles that are 1/12 of 6.28318 or .523598 radians apart.
<i>Example 3:</i> Creating a rotating spiral with COS and <a href="SIN" title="SIN">SIN</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (0, 0)-(640, 480), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 0, 0), BF
  j = j + 1
  <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (320, 240)
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> .1
    <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> -(.05 * i * i * <a class="mw-selflink selflink"><span style="color:#4593D8;">COS</span></a>(j + i) + 320, .05 * i * i * <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(j + i) + 240)
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (320, 240)
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> .1
    <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> -(.05 * i * i * <a class="mw-selflink selflink"><span style="color:#4593D8;">COS</span></a>(j + i + 10) + 320, .05 * i * i * <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(j + i + 10) + 240)
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (320, 240)
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> .1
    <a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> (.05 * i * i * <a class="mw-selflink selflink"><span style="color:#4593D8;">COS</span></a>(j + i + 5) + 320, .05 * i * i * <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(j + i + 5) + 240)
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
  <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 30
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>60) = 1 'escape exit
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PI" title="PI">_PI</a> <span style="color:#777777;">(QB64 function)</span></li>
<li><a href="SIN" title="SIN">SIN</a> <span style="color:#777777;">(sine)</span></li>
<li><a href="ATN" title="ATN">ATN</a> <span style="color:#777777;">(arctangent)</span></li>
<li><a href="TAN" title="TAN">TAN</a> <span style="color:#777777;">(tangent)</span></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a href="Mathematical_Operations#Derived_Mathematical_Functions" title="Mathematical Operations">Derived Mathematical Functions</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061243
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.071 seconds
Real time usage: 0.089 seconds
Preprocessor visited node count: 549/1000000
Post‐expand include size: 4720/2097152 bytes
Template argument size: 679/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   51.503      1 -total
 12.65%    6.516      3 Template:Parameter
 10.59%    5.455     67 Template:Cl
  8.77%    4.518      1 Template:PageSyntax
  7.02%    3.613      1 Template:PageParameters
  5.61%    2.890      3 Template:CodeEnd
  5.19%    2.673      1 Template:PageNavigation
  4.98%    2.566      2 Template:Small
  4.94%    2.543      3 Template:CodeStart
  4.93%    2.538      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:443-0!canonical and timestamp 20240715061243 and revision id 7844.
 -->
</div>
</div>
</div>
</div>
</body>
</html>