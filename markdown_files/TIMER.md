<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>TIMER - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TIMER rootpage-TIMER skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">TIMER</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>A <b>TIMER</b> statement enables, turns off or stops timer event trapping. QBasic only uses the base timer, but <b>QB64</b> can run many.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dt>QuickBASIC</dt>
<dd>TIMER {ON|STOP|OFF}</dd>
<dt>QB64</dt>
<dd>TIMER(<i>number%</i>) {ON|STOP|OFF|FREE}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>number</i> denotes a specific numbered timer event in <b>QB64 only</b>. QB64 can run many timer events at once including the base timer.</li>
<li>TIMER ON enables event trapping of an <a href="ON_TIMER(n)" title="ON TIMER(n)">ON TIMER(n)</a> statement. While enabled, a check is made after every code statement to see if the specified time has elapsed and the ON TIMER <a href="GOSUB" title="GOSUB">GOSUB</a> (or <a href="SUB" title="SUB">SUB</a> in QB64) procedure is executed.</li>
<li>TIMER STOP disables timer event trapping. When an event occurs while stopped, it is remembered. If timer events are turned back on later, any remembered events are immediately executed.</li>
<li>TIMER OFF turns timer event trapping completely off and no subsequent events are remembered.</li></ul>
<ul><li>Get a TIMER number from <a href="FREETIMER" title="FREETIMER">_FREETIMER</a> ONLY except when the base timer(no number or 0) is used. Use specific variables or an array to hold each event number value for later reference.</li>
<li>If the TIMER number is omitted or 0, the TIMER used is the base timer.</li>
<li>Specific TIMER events can be enabled, suspended, turned off or freed using <a class="mw-selflink selflink">TIMER(n)</a> ON, STOP, OFF or FREE.</li>
<li>TIMER(n) <b>FREE</b> clears a specific timer event when it is no longer needed. <b>The base TIMER or TIMER(0) cannot be freed!</b></li></ul>
<ul><li>The <a href="TIMER_(function)" title="TIMER (function)">TIMER (function)</a> can be used to find timed intervals down to 1 millisecond(.001) accuracy.</li>
<li>The <a href="DELAY" title="DELAY">_DELAY</a> statement can be used to delay program execution for intervals down to milliseconds.</li>
<li><a href="LIMIT" title="LIMIT">_LIMIT</a> can slow down loops to a specified number of frames per second. This can also alleviate a program's CPU usage.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> How to update the time while <a href="PRINT" title="PRINT">printing</a> at the same time in a program.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">  TIMER ON ' enable timer event trapping
  LOCATE 4, 2 ' set the starting PRINT position
  <a href="ON_TIMER(n)" title="ON TIMER(n)"><span style="color:#4593D8;">ON TIMER</span></a>(10) GOSUB Clock ' set procedure execution repeat time
  DO WHILE INKEY$ = "": PRINT "A"; : SLEEP 6: LOOP
  TIMER OFF
  <a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
 Clock:
  row = <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a> ' Save current print cursor row.
  col = <a href="POS" title="POS"><span style="color:#4593D8;">POS(0)</span></a> ' Save current print cursor column.
  LOCATE 2, 37: PRINT <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>; ' print current time at top of screen.
  LOCATE row, col ' return to last print cursor position
 <a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd>NOTE: SLEEP will be interrupted in QBasic.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON_TIMER(n)" title="ON TIMER(n)">ON TIMER(n)</a>, <a href="TIMER_(function)" title="TIMER (function)">TIMER (function)</a></li>
<li><a href="DELAY" title="DELAY">_DELAY</a>, <a href="LIMIT" title="LIMIT">_LIMIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715045249
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.024 seconds
Real time usage: 0.032 seconds
Preprocessor visited node count: 62/1000000
Post‐expand include size: 969/2097152 bytes
Template argument size: 74/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.347      1 -total
 13.94%    2.418      1 Template:PageSyntax
 12.06%    2.091      6 Template:Cl
 11.80%    2.047      1 Template:PageSeeAlso
 11.58%    2.009      1 Template:PageExamples
 11.33%    1.965      1 Template:CodeStart
 11.19%    1.942      1 Template:PageNavigation
 11.16%    1.936      1 Template:PageParameters
 10.77%    1.868      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:284-0!canonical and timestamp 20240715045249 and revision id 8072.
 -->
</div>
</div>
</div>
</div>
</body>
</html>