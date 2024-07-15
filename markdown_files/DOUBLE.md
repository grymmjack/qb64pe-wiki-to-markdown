<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DOUBLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DOUBLE rootpage-DOUBLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DOUBLE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">DOUBLE</a> type floating point numerical values use 8 bytes per value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DIM" title="DIM">DIM</a> <i>variable</i> <a href="AS" title="AS">AS</a> <a class="mw-selflink selflink">DOUBLE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Literal or variable values can range up to 15 decimal point places.</li>
<li>The variable suffix type is <b>#</b>.</li>
<li>Use DOUBLE and <a href="FLOAT" title="FLOAT">_FLOAT</a> variables sparingly as they use a lot of program memory.</li>
<li>Values returned may be expressed using exponential or <a href="Scientific_notation" title="Scientific notation">scientific notation</a> using <b>E</b> for SINGLE or <b>D</b> for DOUBLE precision.</li>
<li>Floating decimal point numerical values cannot be <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li>Values can be converted to 8 byte <a href="ASCII" title="ASCII">ASCII</a> string values using <a href="MKD$" title="MKD$">_MKD$</a> and back with <a href="CVD" title="CVD">_CVD</a>.</li>
<li><b>When a variable has not been defined or has no type suffix, the value defaults to <a href="SINGLE" title="SINGLE">SINGLE</a>.</b></li>
<li><b>Warning: QBasic keyword names cannot be used as numerical variable names with or without the type suffix.</b></li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>Results of mathematical calculations may be approximate or slow in QuickBASIC 4.5.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DIM" title="DIM">DIM</a>, <a href="DEFDBL" title="DEFDBL">DEFDBL</a></li>
<li><a href="MKD$" title="MKD$">MKD$</a>, <a href="CVD" title="CVD">CVD</a></li>
<li><a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="FLOAT" title="FLOAT">_FLOAT</a></li>
<li><a href="LEN" title="LEN">LEN</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031552
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.020 seconds
Real time usage: 0.026 seconds
Preprocessor visited node count: 34/1000000
Post‐expand include size: 557/2097152 bytes
Template argument size: 8/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   12.171      1 -total
 20.45%    2.489      1 Template:PageSyntax
 19.37%    2.357      1 Template:Parameter
 19.28%    2.347      1 Template:PageDescription
 18.81%    2.289      1 Template:PageNavigation
 17.59%    2.141      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:278-0!canonical and timestamp 20240715031552 and revision id 6765.
 -->
</div>
</div>
</div>
</div>
</body>
</html>