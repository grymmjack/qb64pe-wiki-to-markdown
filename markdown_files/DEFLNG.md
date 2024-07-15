<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DEFLNG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEFLNG rootpage-DEFLNG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DEFLNG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">DEFLNG</a> statement defines all variables with names starting with the specified letter (or letter range) AS <a href="LONG" title="LONG">LONG</a> variables instead of the <a href="SINGLE" title="SINGLE">SINGLE</a> type default.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">DEFLNG</a> <i>letter</i>[-<i>range</i>], <i>letter2</i>[-<i>range2</i>], [...]</dd></dl>
<h3><span class="mw-headline" id="Legacy_support">Legacy support</span></h3>
<ul><li><b>DEF</b> statements (<a href="DEFDBL" title="DEFDBL">DEFDBL</a>, <a href="DEFSNG" title="DEFSNG">DEFSNG</a>, <a class="mw-selflink selflink">DEFLNG</a>, <a href="DEFINT" title="DEFINT">DEFINT</a>, <a href="DEFSTR" title="DEFSTR">DEFSTR</a>) were used when storage space was a concern in older computers, as their usage could save up typing. Instead of <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">DIM a AS LONG, a2 AS LONG, a3 AS LONG</span>, simply having <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">DEFLNG A</span> in the code before using variables starting with letter <b>A</b> would do the same job.</li>
<li>For clarity, it is recommended to declare variables with meaningful names.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>letter</i> (or <i>range</i>) can be from A-Z or any other range, like <b>G-M</b>.</li>
<li>You can also use commas for specific undefined variable first letters.</li>
<li>Variables <a href="DIM" title="DIM">DIMensioned</a> as another variable type or that use type suffixes are not affected by <a class="mw-selflink selflink">DEFLNG</a>.</li>
<li><a class="mw-selflink selflink">DEFLNG</a> sets the <a href="Variable_Types" title="Variable Types">type</a> of all variable names with the starting letter(s) or letter ranges when encountered in the progression of the program (even in conditional statement blocks not executed and subsequent <a href="SUB" title="SUB">SUB</a> procedures).</li>
<li>For <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a>, use <a href="DEFINE" title="DEFINE">_DEFINE</a></li>
<li><b>Warning: QBasic keyword names cannot be used as numerical variable names with or without the type suffix.</b></li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>QBasic's IDE would add DEF statements before any <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a>. QB64 (like QBasic) will change all variable types in subsequent sub-procedures to that default variable type without giving a <a href="ERROR_Codes" title="ERROR Codes">"Parameter Type Mismatch"</a> warning or adding DEF statement to subsequent procedures. If you do not want that to occur, either remove that DEF statement or add the proper DEF type statements to subsequent procedures. May also affect <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> procedures.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">DEFLNG</span></a> A, F-H, M
'With the above, all variables with names starting with A, F, G, H and M
'will be of type LONG, unless they have a type suffix
'indicating another type or they are <a href="DIM" title="DIM"><span style="color:#4593D8;">dimensioned</span></a> differently
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEFSNG" title="DEFSNG">DEFSNG</a>, <a href="DEFDBL" title="DEFDBL">DEFDBL</a>, <a href="DEFINT" title="DEFINT">DEFINT</a>, <a href="DEFSTR" title="DEFSTR">DEFSTR</a></li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192415
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.038 seconds
Preprocessor visited node count: 112/1000000
Post‐expand include size: 1223/2097152 bytes
Template argument size: 61/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.877      1 -total
 10.67%    2.335      1 Template:PageSyntax
  9.26%    2.026      1 Template:CodeStart
  9.09%    1.988      6 Template:Parameter
  8.82%    1.930      2 Template:InlineCode
  8.71%    1.906      2 Template:InlineCodeEnd
  8.43%    1.844      2 Template:Cl
  7.98%    1.745      1 Template:PageDescription
  7.91%    1.730      1 Template:CodeEnd
  7.53%    1.648      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:455-0!canonical and timestamp 20240714192415 and revision id 8705.
 -->
</div>
</div>
</div>
</div>
</body>
</html>