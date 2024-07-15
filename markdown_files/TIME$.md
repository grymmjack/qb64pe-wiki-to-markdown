<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>TIME$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TIME rootpage-TIME skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">TIME$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>TIME$</b> Function returns a <a href="STRING" title="STRING">STRING</a> representation of the current computer time in a 24 hour format.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>PRINT "Present time = "; <b>TIME$</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the present computer time in hh:mm:ss 24 hour format: "19:20:33"</li>
<li>Uses 2 colon (:) separators between hours, minutes and seconds</li>
<li>Hour values range from "00" to "23" starting from midnite.</li>
<li>Minutes and seconds range from "00" to "59"</li>
<li>Continuous TIME$ calls may lag if a QBasic program is minimized to the taskbar!</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> A simple clock using <a href="DRAW" title="DRAW">DRAW</a> with Turn Angle.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    t$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">TIME$</span></a>: h = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(t$): m = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(t$, 4, 2)): s = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(t$, 7, 2))
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> t$
    <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(0, 0), 200, 8
    <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "c12ta" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>((h <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 12) * -30) + "nu133"
    <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "c14ta" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(m * -6) + "nu200"
    <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "c9ta" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(s * -6) + "nu200"
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 1
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
</pre>
</td></tr></tbody></table>
<dl><dd>Explanation: Note that <a href="VAL" title="VAL">VAL</a>(TIME$) can just return the hour number 0 to 23 as the read stops at the first colon.</dd></dl>
<p>
<i>Example 2:</i> The following Function converts TIME$ to normal 12 hour AM-PM digital clock  format.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">PRINT TIME$
PRINT Clock$
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> Clock$
hour$ = <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(TIME$, 2): H% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(hour$)
min$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(TIME$, 3, 3)
IF H% &gt;= 12 THEN ampm$ = " PM" ELSE ampm$ = " AM"
IF H% &gt; 12 THEN
  IF H% - 12 &lt; 10 THEN hour$ = <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(H% - 12) ELSE hour$ = <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(H% - 12))
ELSEIF H% = 0 THEN hour$ = "12"          ' midnight hour
ELSE : IF H% &lt; 10 THEN hour$ = <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(H%)  ' eliminate leading zeros
END IF
Clock$ = hour$ + min$ + ampm$
END FUNCTION
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">14:13:36
 2:13 PM
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> When hours are less than 10 (but not 0), <a href="STR$" title="STR$">STR$</a>(H%) alone keeps a space ahead of the hour. For 2 digit hours, <a href="LTRIM$" title="LTRIM$">LTRIM$</a> is used to remove that leading space. For the hours of 10 AM to 12 PM, the hour <a href="STRING" title="STRING">STRING</a> value is passed from <a href="LEFT$" title="LEFT$">LEFT$</a>(TIME$, 2) at the beginning of the function.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="TIMER_(function)" title="TIMER (function)">TIMER (function)</a></li>
<li><a href="DATE$" title="DATE$">DATE$</a>, <a href="IF...THEN" title="IF...THEN">IF...THEN</a></li>
<li><a href="VAL" title="VAL">VAL</a>, <a href="STR$" title="STR$">STR$</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li>
<li><a href="LEFT$" title="LEFT$">LEFT$</a>, <a href="RIGHT$" title="RIGHT$">RIGHT$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061432
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.036 seconds
Real time usage: 0.049 seconds
Preprocessor visited node count: 264/1000000
Post‐expand include size: 2603/2097152 bytes
Template argument size: 340/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.794      1 -total
 13.41%    4.129     33 Template:Cl
 11.30%    3.479      1 Template:PageSyntax
  8.07%    2.484      1 Template:PageDescription
  8.00%    2.462      2 Template:CodeEnd
  7.93%    2.441      2 Template:CodeStart
  7.81%    2.405      1 Template:Small
  7.17%    2.208      1 Template:PageExamples
  7.00%    2.157      1 Template:OutputStart
  6.68%    2.057      1 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:489-0!canonical and timestamp 20240715061432 and revision id 8175.
 -->
</div>
</div>
</div>
</div>
</body>
</html>