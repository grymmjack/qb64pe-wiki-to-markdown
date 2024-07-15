<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>GOSUB - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-GOSUB rootpage-GOSUB skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">GOSUB</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">GOSUB</a> sends the program flow to a sub procedure identified by a line number or label.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>GOSUB {<i>lineNumber</i>|<i>label</i>}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use <a href="RETURN" title="RETURN">RETURN</a> in a sub procedure to return to the next line of code after the original <a class="mw-selflink selflink">GOSUB</a> call. <a href="END" title="END">END</a> or <a href="SYSTEM" title="SYSTEM">SYSTEM</a> can also be used to end program.</li>
<li>GOSUB and GOTO can be used <b>within</b> <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures, but cannot refer to a label located outside the procedure.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>Too many GOSUBs without a <a href="RETURN" title="RETURN">RETURN</a> can eventually cause "Out of Stack Errors" in QBasic as each GOSUB uses memory to store the location to return to. Each <a href="RETURN" title="RETURN">RETURN</a> frees the memory of the GOSUB it returns to.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Simple usage of GOSUB
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "1. It goes to the subroutine."
<a class="mw-selflink selflink"><span style="color:#4593D8;">GOSUB</span></a> subroutine
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "3. And it returns."
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
subroutine:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "2. It is at the subroutine."
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">1. It goes to the subroutine.
2. It is at the subroutine.
3. And it returns.
</pre>
</td></tr></tbody></table>
<p>
<i>Example:</i> What happens if two GOSUB executes then two RETURN's?
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">start:
a = a + 1
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> a = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">GOSUB</span></a> here: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "It returned to IF a = 1": <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> a = 2 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">GOSUB</span></a> there: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "It returned to IF a = 2": <a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
here:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "It went here."
<a href="GOTO" title="GOTO"><span style="color:#4593D8;">GOTO</span></a> start
there:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "It went there."
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">It went here.
It went there.
It returned to IF a = 2
It returned to IF a = 1
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> When a = 1 it uses GOSUB to go to "here:", then it uses GOTO to go back to "start:". a is increased by one so when a = 2 it uses GOSUB to go to "there:", and uses RETURN to go the last GOSUB (which is on the IF a = 2 line), it then encounters another RETURN which makes it return to the first GOSUB call we used on the IF a = 1 line.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON...GOSUB" title="ON...GOSUB">ON...GOSUB</a></li>
<li><a href="ON...GOTO" title="ON...GOTO">ON...GOTO</a>, <a href="GOTO" title="GOTO">GOTO</a></li>
<li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a>, <a href="RESUME" title="RESUME">RESUME</a></li>
<li><a href="ON_TIMER(n)" title="ON TIMER(n)">ON TIMER(n)</a></li>
<li><a href="Line_number" title="Line number">Line number</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714082938
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.047 seconds
Real time usage: 0.072 seconds
Preprocessor visited node count: 205/1000000
Post‐expand include size: 2171/2097152 bytes
Template argument size: 241/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   46.931      1 -total
 18.18%    8.530      2 Template:OutputStart
 11.72%    5.501      2 Template:Small
  8.34%    3.915      1 Template:PageSyntax
  8.19%    3.845      1 Template:PageExamples
  7.87%    3.695     20 Template:Cl
  6.62%    3.106      1 Template:PageSeeAlso
  6.11%    2.866      2 Template:CodeEnd
  5.87%    2.757      2 Template:CodeStart
  5.11%    2.399      2 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:389-0!canonical and timestamp 20240714082938 and revision id 8038.
 -->
</div>
</div>
</div>
</div>
</body>
</html>