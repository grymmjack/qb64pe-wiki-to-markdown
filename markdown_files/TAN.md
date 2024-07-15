<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>TAN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TAN rootpage-TAN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">TAN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">TAN</a> function returns the ratio of <a href="SIN" title="SIN">SINe</a> to <a href="COS" title="COS">COSine</a> or tangent value of an angle measured in radians.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>tangent! = <b>TAN(</b><i>radian_angle!</i><b>)</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>radian_angle</i> must be measured in radians.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>To convert from degrees to radians, multiply degrees * π/180.</li>
<li>TANGENT is the gradient or slope of the circle or arc at <a href="SIN" title="SIN">SIN</a>(θ) / <a href="COS" title="COS">COS</a>(θ). Do not use division when the <a href="COS" title="COS">COS</a> = 0 to avoid <a href="ERROR_Codes" title="ERROR Codes">errors</a>.</li></ul>
<p>
<i>Example:</i> Spiraling text using the <a href="SIN" title="SIN">SIN</a> and <a class="mw-selflink selflink">TAN</a> functions.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> text <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
text$ = "S P I R A L"
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> word(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(text$) * 8, 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 16)
<a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> analyse
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> redraw
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> analyse
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 2: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> text$
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> px <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, py <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, cnt <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, ltrcnt <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
px = 1: py = 1
DO
  word(px, py) = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(px, py)
  <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (px, py), 1
  px = px + 1
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> px = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(text$) * 8 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    px = 1
    py = py + 1
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> py = 16
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> redraw
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> row <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, cnt <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, cstart <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>, cend <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> xrot <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, yrot <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, SCALE <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, pan <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
cstart = 0: cend = 6.2
xrot = 6: yrot = 6: SCALE = 3: pan = 30
<a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C8, 1: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 10: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 10: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 60
DO
  row = 2
  DO
    DO
      <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = cend <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> cstart <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -.03
        x = (SCALE * 60 - (row * xrot / 4)) * <a class="mw-selflink selflink"><span style="color:#4593D8;">TAN</span></a>(<a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(i))
        y = <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(SCALE * 60 - (row * yrot)) * <a class="mw-selflink selflink"><span style="color:#4593D8;">TAN</span></a>(<a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(i)) * pan
        cnt = cnt + 1
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> word(cnt, row) &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
          <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (x + 320, y + 220), SCALE + 1, 1              'circled letters
          '<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (x + 320, y + 220)-<a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(12, 12), 1, BF  'boxed letters
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> cnt = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(text$) * 8 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> cnt = 0: <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
      <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
    row = row + 1
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> row = 16
  cend = cend + .1
  cstart = cstart + .1
  now! = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
  DO
    newnow! = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> newnow! - now! &gt;= .15
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (1, 100)-(639, 280), 0, BF
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PI" title="PI">_PI</a></li>
<li><a href="SIN" title="SIN">SIN</a>, <a href="COS" title="COS">COS</a></li>
<li><a href="ATN" title="ATN">ATN</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li>
<li><a href="Mathematical_Operations#Derived_Mathematical_Functions" title="Mathematical Operations">Derived Mathematical Functions</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192559
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.046 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 697/1000000
Post‐expand include size: 5551/2097152 bytes
Template argument size: 842/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   29.762      1 -total
 16.68%    4.965     96 Template:Cl
 15.53%    4.623      1 Template:PageSyntax
 10.33%    3.074      1 Template:PageNavigation
  8.10%    2.412      1 Template:CodeEnd
  8.10%    2.412      1 Template:Small
  6.99%    2.080      1 Template:PageSeeAlso
  6.13%    1.823      1 Template:PageParameters
  5.57%    1.657      1 Template:PageDescription
  5.32%    1.583      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:488-0!canonical and timestamp 20240714192559 and revision id 8070.
 -->
</div>
</div>
</div>
</div>
</body>
</html>