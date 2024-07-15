<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_LIMIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LIMIT rootpage-LIMIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_LIMIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_LIMIT</a> statement sets the loop repeat rate of a program to so many per second, relinquishing spare CPU cycles to other applications.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_LIMIT</a> <i>framesPerSecond!</i></dd></dl>
<p>
</p>
<ul><li>The <i>framesPerSecond!</i> <a href="SINGLE" title="SINGLE">SINGLE</a> parameter value adjusts the loops per second of a program loop. <b>Do not use negative values.</b></li>
<li>The loop code is executed before the loop is delayed. Loop cycles below once per second may delay program <a href="EXIT" title="EXIT">_EXITs</a>.</li>
<li>_LIMIT measures its interval from the previous time that it was called and minor adjustments are automatically made to ensure that the number of times a loop is repeated is correct overall.</li>
<li>Loop cycle rates of 1000 or less can <b>significantly reduce CPU usage</b> in programs.</li>
<li>Do not use it to limit a loop to <b>run less than once every 60 seconds</b> (i.e. _LIMIT .0167 or _LIMIT 1/60) or an <a href="ERROR_Codes" title="ERROR Codes">ILLEGAL FUNCTION CALL error</a> will occur.</li>
<li>Do not use _LIMIT as a timing delay outside of loops. Use <a href="DELAY" title="DELAY">_DELAY</a> instead.</li>
<li>Use _LIMIT to slow down old QBasic program loops that run too fast and use too much CPU.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Limits loop execution to 30 frames per second and limits the program's CPU usage.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"To Quit press ESC key!"</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">26</span>);
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">To Quit press ESC key!
→→→→→→→→→→→→→→→→→→→→
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> In the above example, _LIMIT has to be within the loop.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DELAY" title="DELAY">_DELAY</a></li>
<li><a href="TIMER" title="TIMER">TIMER</a>, <a href="ON_TIMER(n)" title="ON TIMER(n)">ON TIMER(n)</a></li>
<li><a href="SLEEP" title="SLEEP">SLEEP</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062352
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.036 seconds
Real time usage: 0.062 seconds
Preprocessor visited node count: 139/1000000
Post‐expand include size: 1454/2097152 bytes
Template argument size: 198/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 24/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   46.160      1 -total
 17.71%    8.177      1 Template:CodeEnd
 15.24%    7.037      1 Template:PageSyntax
  7.20%    3.323      2 Template:Parameter
  6.78%    3.130     11 Template:Cl
  5.85%    2.701      4 Template:Text
  5.38%    2.483      1 Template:PageExamples
  5.12%    2.363      1 Template:OutputStart
  5.07%    2.339      1 Template:CodeStart
  4.61%    2.130      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:168-0!canonical and timestamp 20240715062352 and revision id 8372.
 -->
</div>
</div>
</div>
</div>
</body>
</html>