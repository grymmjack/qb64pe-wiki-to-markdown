<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ELSE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ELSE rootpage-ELSE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ELSE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">ELSE</a> is used in <a href="IF...THEN" title="IF...THEN">IF...THEN</a> or <a href="SELECT_CASE" title="SELECT CASE">SELECT CASE</a> statements to offer an alternative to other conditional statements.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<p><i>Single-line syntax:</i>
</p>
<dl><dd><a class="mw-redirect" href="IF" title="IF">IF</a> <i>condition</i> <a href="THEN" title="THEN">THEN</a> <i>{code}</i> <a class="mw-selflink selflink">ELSE</a> <i>{alternative-code}</i></dd></dl>
<p>
<i>Block syntax:</i>
</p>
<dl><dd><a class="mw-redirect" href="IF" title="IF">IF</a> <i>condition</i> <a href="THEN" title="THEN">THEN</a>
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a href="ELSEIF" title="ELSEIF">ELSEIF</a> <i>condition2</i> <a href="THEN" title="THEN">THEN</a>
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a class="mw-selflink selflink">ELSE</a>
<dl><dd><i>{alternative-code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a class="mw-redirect" href="END_IF" title="END IF">END IF</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>ELSE is used in a IF block statement to cover any remaining conditions not covered in the main block by IF or <a href="ELSEIF" title="ELSEIF">ELSEIF</a>.</li>
<li><a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE">CASE ELSE</a> covers any remaining conditions not covered by the other CASE statements.</li>
<li>ELSE can also be used as a false comparison to a true IF statement when a condition will only be true or false.</li>
<li>Other <a href="IF...THEN" title="IF...THEN">IF...THEN</a> statements can be inside of an ELSE statement.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> One line IF statement
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
IF x = 100 THEN PRINT "100" ELSE PRINT "Not 100"
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> Multiple line IF statement block
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
IF x = 100 THEN ' code executed MUST be on next statement line!
   PRINT "100"
ELSE PRINT "Not 100"
END IF
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> To alternate between any two values (as long as the value after ELSE is the same as the condition)
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
IF a = 3 THEN a = 5 ELSE a = 3
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ELSEIF" title="ELSEIF">ELSEIF</a></li>
<li><a href="IF...THEN" title="IF...THEN">IF...THEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714081859
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.031 seconds
Preprocessor visited node count: 38/1000000
Post‐expand include size: 826/2097152 bytes
Template argument size: 28/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.177      1 -total
 16.23%    2.788      1 Template:PageSyntax
 12.57%    2.159      3 Template:Parameter
 11.67%    2.005      1 Template:PageDescription
 11.38%    1.954      1 Template:PageSeeAlso
 10.90%    1.873      3 Template:CodeStart
 10.82%    1.858      1 Template:PageExamples
 10.21%    1.753      1 Template:PageNavigation
  9.91%    1.703      3 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:382-0!canonical and timestamp 20240714081859 and revision id 7268.
 -->
</div>
</div>
</div>
</div>
</body>
</html>