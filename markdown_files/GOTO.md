<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>GOTO - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-GOTO rootpage-GOTO skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">GOTO</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">GOTO</a> statement sends the procedure to a line label or a line number in the program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">GOTO</a> {<i>lineNumber</i>|<i>lineLabel</i>}</dd></dl>
<p>
<i><b>IF</b> Syntax:</i>
</p>
<dl><dd>IF condition <a class="mw-selflink selflink">GOTO</a> {<i>lineNumber</i>|<i>lineLabel</i>}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>lineNumber</i> or <i>lineLabel</i> must already exist or an IDE status error will be displayed until it is created.</li>
<li>Can be used in <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures using their own line labels or numbers.</li>
<li>The frequent use of GOTO statements can become confusing when trying to follow the code and it could also cause endless loops.</li>
<li><a class="mw-selflink selflink">GOTO</a> is an easy trap for new programmers. Use loops instead when possible.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">1 <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "first line": <a class="mw-selflink selflink"><span style="color:#4593D8;">GOTO</span></a> gohere
2 <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "second line": <a class="mw-selflink selflink"><span style="color:#4593D8;">GOTO</span></a> 3
gohere:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "third line"
<a class="mw-selflink selflink"><span style="color:#4593D8;">GOTO</span></a> 2
3 <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">first line
third line
second line
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> After it prints "first line" it goes to the line label "gohere" where it prints "third line", then it goes to the line that is numbered "2" and prints "second line" and goes to line number 3 and an <a href="END" title="END">END</a> statement which ends the program.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GOSUB" title="GOSUB">GOSUB</a>, <a href="ON_ERROR" title="ON ERROR">ON ERROR</a></li>
<li><a href="ON...GOTO" title="ON...GOTO">ON...GOTO</a>, <a href="ON...GOSUB" title="ON...GOSUB">ON...GOSUB</a></li>
<li><a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a>, <a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a></li>
<li><a href="IF...THEN" title="IF...THEN">IF...THEN</a>, <a href="SELECT_CASE" title="SELECT CASE">SELECT CASE</a></li>
<li><a href="Line_number" title="Line number">Line numbers and labels</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714184757
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 74/1000000
Post‐expand include size: 1068/2097152 bytes
Template argument size: 60/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   16.767      1 -total
 11.98%    2.008      1 Template:PageSyntax
 10.74%    1.801      1 Template:OutputStart
  9.96%    1.669      1 Template:OutputEnd
  9.86%    1.654      7 Template:Cl
  9.02%    1.513      1 Template:PageNavigation
  9.01%    1.511      1 Template:PageSeeAlso
  8.74%    1.465      1 Template:PageDescription
  8.12%    1.361      1 Template:CodeStart
  8.02%    1.344      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:388-0!canonical and timestamp 20240714184757 and revision id 6021.
 -->
</div>
</div>
</div>
</div>
</body>
</html>