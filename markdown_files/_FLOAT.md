<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FLOAT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FLOAT rootpage-FLOAT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FLOAT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>_FLOAT</b> numerical values offer the maximum floating-point decimal precision available using <b>QB64</b>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><a href="DIM" title="DIM">DIM</a> <i>variable</i> AS <a class="mw-selflink selflink">_FLOAT</a></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>QB64</b> always allocates 32 bytes to store this value.</li>
<li>It is safe to assume this value is at least as precise as <a href="DOUBLE" title="DOUBLE">DOUBLE</a>.</li>
<li>Under the current implementation it is stored in a 10-byte floating point variable.</li>
<li><a class="mw-selflink selflink">_FLOAT</a> variables can also use the ## variable name type suffix.</li>
<li>Values returned may be expressed using exponential or <a href="Scientific_notation" title="Scientific notation">scientific notation</a> using <b>E</b> for SINGLE or <b>D</b> for DOUBLE precision.</li>
<li>According to <a class="external text" href="http://babbage.cs.qc.edu/courses/cs341/IEEE-754references.html" rel="nofollow">IEEE-754</a> this can store a value of up to 1.1897E+4932 compared to a DOUBLE which goes up to 1.7976E+308.</li>
<li>Floating decimal point numerical values cannot be <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li>Values can be converted to 32 byte <a href="ASCII" title="ASCII">ASCII</a> strings using <a href="MK$" title="MK$">_MK$</a> and back with <a href="CV" title="CV">_CV</a>.</li>
<li><b>When a variable has not been assigned or has no type suffix, the value defaults to <a href="SINGLE" title="SINGLE">SINGLE</a>.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DOUBLE" title="DOUBLE">DOUBLE</a>, <a href="SINGLE" title="SINGLE">SINGLE</a></li>
<li><a href="MK$" title="MK$">_MK$</a>, <a href="CV" title="CV">_CV</a></li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a>, <a href="DIM" title="DIM">DIM</a></li>
<li><a href="PDS(7.1)_Procedures#CURRENCY" title="PDS(7.1) Procedures">CURRENCY</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034340
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.019 seconds
Real time usage: 0.023 seconds
Preprocessor visited node count: 17/1000000
Post‐expand include size: 557/2097152 bytes
Template argument size: 8/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   10.666      1 -total
 22.75%    2.427      1 Template:PageSyntax
 19.70%    2.101      1 Template:PageNavigation
 18.93%    2.019      1 Template:Parameter
 17.73%    1.891      1 Template:PageDescription
 16.40%    1.749      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:144-0!canonical and timestamp 20240715034340 and revision id 7570.
 -->
</div>
</div>
</div>
</div>
</body>
</html>