<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>STOP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STOP rootpage-STOP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">STOP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>STOP</b> statement is used to stop program execution when troubleshooting a program or to suspend event trapping.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>STOP</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>STOP used in the QBasic IDE does not close any files or go to the operating system. It returns to the IDE.</li>
<li>In the QB64 compiler, STOP closes the program window and returns to the IDE when the code is compiled from there.</li>
<li>STOP is ONLY used for debugging purposes and should not be used to exit programs!</li>
<li>STOP can also be used to suspend an event trap in the following statements: <a href="KEY(n)" title="KEY(n)">KEY(n)</a>, <a href="STRIG(n)" title="STRIG(n)">STRIG(n)</a> and <a href="TIMER" title="TIMER">TIMER(n)</a>. The trap can be turned back on with <a href="ON" title="ON">ON</a> and returns any trap events since <b>STOP</b> was used.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> When run in the QBasic IDE, the program will return to the IDE at STOP. Press F5 to finish the program.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "start"
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 3
<a class="mw-selflink selflink"><span style="color:#4593D8;">STOP</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "resumed"
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> QB64 will STOP the program and close the window as it does not have an interpreter to run the rest of the code.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="END" title="END">END</a>, <a href="SYSTEM" title="SYSTEM">SYSTEM</a></li>
<li><a href="ON" title="ON">ON</a>, <a href="OFF" title="OFF">OFF</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034224
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.058 seconds
Preprocessor visited node count: 48/1000000
Post‐expand include size: 852/2097152 bytes
Template argument size: 38/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.803      1 -total
 30.16%    7.783      1 Template:PageDescription
 10.71%    2.764      1 Template:PageSyntax
 10.19%    2.629      4 Template:Cl
  9.07%    2.340      1 Template:CodeEnd
  8.99%    2.320      1 Template:CodeStart
  8.96%    2.312      1 Template:PageExamples
  8.84%    2.282      1 Template:PageNavigation
  8.30%    2.141      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:525-0!canonical and timestamp 20240715034224 and revision id 8066.
 -->
</div>
</div>
</div>
</div>
</body>
</html>