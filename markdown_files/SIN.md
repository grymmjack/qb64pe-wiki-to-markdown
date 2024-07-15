<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SIN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SIN rootpage-SIN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SIN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">SIN</a> function returns the vertical component or sine of an angle measured in radians.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><dl><dd>value! = <b>SIN(</b><i>radian_angle!</i><b>)</b></dd></dl></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>radian_angle</i> must be measured in radians from 0 to 2 * Pi.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>To convert from degrees to radians, multiply degrees * π/180.</li>
<li><a class="mw-selflink selflink">SIN</a>E is the vertical component of a unit vector in the direction theta (θ).</li>
<li>Accuracy can be determined as <a href="SINGLE" title="SINGLE">SINGLE</a> by default or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> by following the parameter value with a # suffix.</li></ul>
<p>
<i>Example 1:</i> Converting degree angles to radians for QBasic's trig functions and drawing the line at the angle.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
PI = 4 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "PI = 4 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1) ="; PI
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "COS(PI) = "; <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(PI)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "SIN(PI) = "; <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>(PI)
DO
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
  <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter the degree angle (0 quits): ", DEGREES%
  RADIANS = DEGREES% * PI / 180
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "RADIANS = DEGREES% * PI / 180 = "; RADIANS
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "X = COS(RADIANS) = "; <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(RADIANS)
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Y = SIN(RADIANS) = "; <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>(RADIANS)
  <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (400, 240), 2, 12
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (400, 240)-(400 + (50 * <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>(RADIANS)), 240 + (50 * <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(RADIANS))), 11
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
<dl><dd><i>Explanation:</i> When 8.742278E-08(.00000008742278) is returned by SIN or <a href="COS" title="COS">COS</a> the value  is essentially zero.</dd></dl>
<p>
<i>Example 2:</i> Displays rotating gears made using SIN and <a href="COS" title="COS">COS</a> to place the teeth lines.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 9
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> Pi <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
Pi = 4 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1)
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> G = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> Pi * 2 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> Pi / 100
        <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>                                   'erase previous
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> GEARZ(160, 60, 40, 20, 4, G, 10)
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> GEARZ(240, 60, 40, 20, 4, -G, 11)
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> GEARZ(240, 140, 40, 20, 4, G, 12)
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> GEARZ(320, 140, 40, 20, 4, -G, 13)
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> GEARZ(320 + 57, 140 + 57, 40, 20, 4, G, 14)
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> GEARZ(320 + 100, 140 + 100, 20, 10, 4, -G * 2 - 15, 15)
        <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
        <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 20                 'regulates gear speed and CPU usage
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> G
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> GEARZ (XP, YP, RAD, Teeth, TH, G, CLR)
t = 0
x = XP + (RAD + TH * <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>(0)) * <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(0)
y = YP + (RAD + TH * <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>(0)) * <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>(0)
<a href="PRESET" title="PRESET"><span style="color:#4593D8;">PRESET</span></a> (x, y)
m = Teeth * G
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> t = -Pi / 70 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 2 * Pi <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> Pi / 70
    x = XP + (RAD + TH * <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>((Teeth * t + m)) ^ 3) * <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(t)
    y = YP + (RAD + TH * <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>((Teeth * t + m)) ^ 3) * <a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>(t)
    <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> -(x, y), CLR
    IF <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; "" THEN <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> t
<a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> (XP, YP), CLR            'gear colors optional
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Displaying the current seconds for an analog clock. See <a href="COS" title="COS">COS</a> for the clock face hour markers.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
Pi2! = 8 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1): sec! = Pi2! / 60  ' (2 * pi) / 60 movements per rotation
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (320, 240), 80, 1
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>
  Seconds% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2)) - 15 ' update seconds
  S! = Seconds% * sec! ' radian from the TIME$ value
  Sx% = <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(<a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(S!) * 60)   ' pixel columns (60 = circular radius)
  Sy% = <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">SIN</span></a>(S!) * 60)   ' pixel rows
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (320, 240)-(Sx% + 320, Sy% + 240), 12
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: Check% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2)) - 15: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> UNTIL Check% &lt;&gt; Seconds%  ' wait loop
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (320, 240)-(Sx% + 320, Sy% + 240), 0 ' erase previous line
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> UNTIL <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) ' escape keypress exits
</pre>
</td></tr></tbody></table>
<p>The value of 2 π is used to determine the sec! multiplier that determines the radian value as S! The value is divided by 60 second movements. To calculate the seconds the <a href="TIME$" title="TIME$">TIME$</a> function is used and that value is subtracted 15 seconds because the 0 value of pi is actually the 3 hour of the clock (15 seconds fast). SIN and COS will work with negative values the same as positive ones! Then the column and row coordinates for one end of the line are determined using SIN and <a href="COS" title="COS">COS</a> multiplied by the radius of the circular line movements. The minute and hour hands could use similar procedures to read different parts of TIME$.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PI" title="PI">_PI</a></li>
<li><a href="COS" title="COS">COS</a></li>
<li><a href="ATN" title="ATN">ATN</a></li>
<li><a href="TAN" title="TAN">TAN</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a href="Mathematical_Operations#Derived_Mathematical_Functions" title="Mathematical Operations">Derived Mathematical Functions</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714171753
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.067 seconds
Real time usage: 0.082 seconds
Preprocessor visited node count: 664/1000000
Post‐expand include size: 5554/2097152 bytes
Template argument size: 804/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   42.584      1 -total
 18.17%    7.738     89 Template:Cl
  7.97%    3.396      2 Template:Small
  7.08%    3.016      1 Template:PageParameters
  6.88%    2.929      3 Template:CodeEnd
  6.62%    2.821      1 Template:OutputStart
  6.58%    2.803      1 Template:OutputEnd
  6.30%    2.685      1 Template:PageSeeAlso
  6.15%    2.620      1 Template:PageNavigation
  5.95%    2.533      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:490-0!canonical and timestamp 20240714171752 and revision id 7957.
 -->
</div>
</div>
</div>
</div>
</body>
</html>