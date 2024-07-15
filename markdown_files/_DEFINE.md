<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DEFINE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEFINE rootpage-DEFINE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DEFINE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">_DEFINE</a> defines a set of variable names according to their first character as a specified data type.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_DEFINE</a> <i>letter</i>[<i>-range</i>, ...] <a href="AS" title="AS">AS</a> [[[_UNSIGNED] data<a href="Variable_Types" title="Variable Types">type</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Variable start <i>letter range</i> is in the form firstletter-endingletter (like A-C) or just a single letter.</li>
<li><i>Data types</i>: <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a>, <a href="LONG" title="LONG">LONG</a>, <a href="STRING" title="STRING">STRING</a>, <a href="BIT" title="BIT">_BIT</a>, <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>, <a href="FLOAT" title="FLOAT">_FLOAT</a>, <a href="OFFSET" title="OFFSET">_OFFSET</a>, <a href="MEM" title="MEM">_MEM</a></li>
<li>Can also use the <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> definition for positive whole <a href="INTEGER" title="INTEGER">INTEGER</a> type numerical values.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>When a variable has not been defined or has no type suffix, the value defaults to a <a href="SINGLE" title="SINGLE">SINGLE</a> precision floating point value.</b></li>
<li>_DEFINE sets the <a href="Variable_Types" title="Variable Types">type</a> of all variable names with the starting letter(s) or letter ranges  when encountered in the progression of the program (even in conditional statement blocks not executed and subsequent <a href="SUB" title="SUB">SUB</a> procedures).</li>
<li><b>NOTE: Many QBasic keyword variable names CAN be used with a <a href="STRING" title="STRING">STRING</a> suffix ($)! You cannot use them without the suffix, use a numerical suffix or use <a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a>, <a class="mw-selflink selflink">_DEFINE</a>, <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> or <a href="TYPE" title="TYPE">TYPE</a> variable <a href="AS" title="AS">AS</a> statements.</b></li>
<li><b>QBasic's IDE</b> added DEF statements before any <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a>. <b>QB64</b> (like QB) will change all variable types in subsequent sub-procedures to that default variable type without giving a <a href="ERROR_Codes" title="ERROR Codes">"Parameter Type Mismatch"</a> warning or adding the proper DEF statement to subsequent procedures. If you do not want that to occur, either remove that DEF statement or add the proper DEF type statements to subsequent procedures.</li>
<li>May also affect <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> procedures.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Defining variables that start with the letters A, B, C or F as unsigned integers, including the <i>Add2</i> <a href="FUNCTION" title="FUNCTION">FUNCTION</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_DEFINE</span></a> A-C, F <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#55FF55;">Add2</span>(<span style="color:#F580B1;">-1.1</span>, <span style="color:#F580B1;">-2.2</span>)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">Add2</span> (one, two)
    <span style="color:#55FF55;">Add2</span> = one + two
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">65533
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Unsigned integers can only return positive values while ordinary <a href="INTEGER" title="INTEGER">integers</a> can also return negative values.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEFSTR" title="DEFSTR">DEFSTR</a>, <a href="DEFLNG" title="DEFLNG">DEFLNG</a>, <a href="DEFINT" title="DEFINT">DEFINT</a>, <a href="DEFSNG" title="DEFSNG">DEFSNG</a>, <a href="DEFDBL" title="DEFDBL">DEFDBL</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a></li>
<li><a href="COMMON" title="COMMON">COMMON</a>, <a href="SHARED" title="SHARED">SHARED</a></li>
<li><a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034323
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 128/1000000
Post‐expand include size: 1414/2097152 bytes
Template argument size: 173/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.027      1 -total
 10.02%    2.007      1 Template:PageSyntax
  8.23%    1.648      8 Template:Cl
  7.84%    1.570      2 Template:Parameter
  7.38%    1.477      5 Template:Text
  7.03%    1.407      1 Template:CodeStart
  6.89%    1.380      1 Template:PageParameters
  6.70%    1.341      1 Template:PageDescription
  6.60%    1.321      1 Template:PageExamples
  6.45%    1.291      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:110-0!canonical and timestamp 20240715034323 and revision id 8703.
 -->
</div>
</div>
</div>
</div>
</body>
</html>