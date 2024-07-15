<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>VARPTR$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-VARPTR rootpage-VARPTR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">VARPTR$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>VARPTR$</b> is a memory function that returns a <a href="STRING" title="STRING">STRING</a> representation of a variable's memory address value for use in a <a href="DRAW" title="DRAW">DRAW</a> or <a href="PLAY" title="PLAY">PLAY</a> statement.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>string_value$ = VARPTR$(<i>variable</i>)</dd></dl></dd></dl>
<p>
</p>
<ul><li>Can use any <a href="STRING" title="STRING">string</a> or numerical variable reference <b>existing</b> in memory.</li>
<li>If the parameter value is from an array it must be dimensioned already. Cannot use fixed length string arrays.</li>
<li>When using <b>numerical</b> <i>variable</i> values in <a href="DRAW" title="DRAW">DRAW</a> strings, use an = sign after the function letter. "TA=" + VARPTR$(<i>variable%</i>)</li>
<li>Always use variable X as in "X" + VARPTR$(<i>string_variable$</i>) to <a href="DRAW" title="DRAW">DRAW</a> or <a href="PLAY" title="PLAY">PLAY</a> another <a href="STRING" title="STRING">STRING</a> value.</li>
<li>DRAW relative Moves use a + or - before the equal sign. EX: DRAW "M+=" + VARPTR$(x%) + ",-=" + VARPTR$(y%)</li></ul>
<p>
<i>Example 1:</i> How VARPTR$ reads consecutive values from memory.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 2
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
WIND$ = "r10 d7 l10 u7 br20"   'create draw string to be read by function
ROW$ = "x"+<a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(WIND$)+"x"+<a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(WIND$)+"x"+<a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(WIND$)+" x"+<a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(WIND$)+"bl80 bd11"
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (100, 50)-(200, 160), , B
<a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "bm 115,52"
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> I = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
    <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "x" + <a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(ROW$)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>NOTE:</i> <b>GWBasic</b> allows <b>semicolons</b> to be used in the ROW$ definition, but QBasic and <b>QB64</b> MUST use <b>+</b> concatenation.</dd></dl>
<p>
<i>Example 2:</i> Using the function to change a Turn Angle value using DRAW.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
                           'Demonstrates how string DRAW angles are used with TA
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 360 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> 30           'mark clock hours every 30 degrees
  angle$ = <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(i)                 'change degree value i to a string
  <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (175, 250), 6               'clock center
  <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "TA" + angle$ + "BU100"     'add string angle to Turn Angle and draw blind up
  <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(0, 0), 5, 12         'place a circle at end of Up line
  <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "P9, 12"
  <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> .5
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
                            'Demonstrates how VARPTR$ is used with TA=
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: sec$ = <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2)        'get current second value from time
  degree = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(sec$) * -6          'use a negative value to Turn Angle clockwise
  <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (175, 250), 9               'clock center
  <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "TA=" + <a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(degree) + "U90"  'VARPTR$ value requires = in DRAW
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 30: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2) &lt;&gt; sec$  'loop until seconds value changes
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (175, 250), 0
  <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "TA=" + <a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(degree) + "U90"  'erase previous second hand draw
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> When the VARPTR$ value is used in DRAW, <b>=</b> MUST be used to pass the value to the draw! Negative Turn Angle values move clockwise and each second moves the hand 6 degrees. <b>TA</b> uses actual degree angles starting at 0 or noon.</dd></dl>
<p>
<i>Example 3:</i> Comparing DRAW moves using VARPTR$ and <a href="STR$" title="STR$">STR$</a> values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (200, 200), 12
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(0, 0), 5, 10
A = 100: B = 100
<a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "M+=" + <a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(A) + ",-=" + <a class="mw-selflink selflink"><span style="color:#4593D8;">VARPTR$</span></a>(B)
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (400, 400), 10
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(0, 0), 5, 12
C = 100: D = -100
<a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "M+" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(C) + "," + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(D) 'must add + for positive relative moves
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> A negative STR$ value will move the DRAW relatively where VARPTR$ won't without the sign before the equal.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="VARPTR" title="VARPTR">VARPTR</a>, <a href="STR$" title="STR$">STR$</a></li>
<li><a href="DRAW" title="DRAW">DRAW</a>, <a href="PLAY" title="PLAY">PLAY</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062228
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 440/1000000
Post‐expand include size: 3743/2097152 bytes
Template argument size: 574/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.872      1 -total
 22.94%    4.329     60 Template:Cl
 13.90%    2.624      1 Template:PageSyntax
 12.71%    2.398      3 Template:CodeEnd
 12.10%    2.284      1 Template:PageSeeAlso
 11.67%    2.202      3 Template:CodeStart
 10.41%    1.965      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:498-0!canonical and timestamp 20240715062228 and revision id 7464.
 -->
</div>
</div>
</div>
</div>
</body>
</html>