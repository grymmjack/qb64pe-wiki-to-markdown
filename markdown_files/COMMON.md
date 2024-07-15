<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>COMMON - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-COMMON rootpage-COMMON skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">COMMON</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">COMMON</a> shares common variable values with other linked or <a href="CHAIN" title="CHAIN">CHAINed</a> modules.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">COMMON</a> [SHARED] variableList</dd></dl>
<h3><span class="mw-headline" id="Legacy_support">Legacy support</span></h3>
<ul><li>The multi-modular technique goes back to when <b>QBasic</b> and <b>QuickBASIC</b> had module size constraints. In <b>QB64</b> the <a class="mw-selflink selflink">COMMON</a> statement has been implemented so that that older code can still be compiled, though it is advisable to use single modules for a single project (not counting <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> libraries), for ease of sharing and also because the module size constraints no longer exist.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>COMMON must be called before any executable statements.</li>
<li><a href="SHARED" title="SHARED">SHARED</a> makes the variables shared within <a href="SUB" title="SUB">SUB</a> and <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures within that module.</li>
<li>variableList is the list of common variables made available separated by commas.</li>
<li>Remember to keep the variable type <i>order</i> the same in all modules, as the variables names don't matter.</li>
<li><a href="COMMON_SHARED" title="COMMON SHARED">COMMON SHARED</a> is most commonly used to share the variables with subs and functions of that module.</li>
<li><b>Note: Values assigned to shared variables used as procedure call parameters will not be passed to other procedures. The shared variable value must be assigned inside of the <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedure to be passed.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="COMMON_SHARED" title="COMMON SHARED">COMMON SHARED</a>, <a href="CHAIN" title="CHAIN">CHAIN</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a>, <a href="SHARED" title="SHARED">SHARED</a></li>
<li><a href="DEFSTR" title="DEFSTR">DEFSTR</a>, <a href="DEFLNG" title="DEFLNG">DEFLNG</a>, <a href="DEFINT" title="DEFINT">DEFINT</a>, <a href="DEFSNG" title="DEFSNG">DEFSNG</a>, <a href="DEFDBL" title="DEFDBL">DEFDBL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714180637
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.017 seconds
Real time usage: 0.021 seconds
Preprocessor visited node count: 18/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    8.329      1 -total
 28.07%    2.338      1 Template:PageSyntax
 22.93%    1.910      1 Template:PageNavigation
 22.49%    1.873      1 Template:PageDescription
 21.86%    1.821      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:418-0!canonical and timestamp 20240714180637 and revision id 7240.
 -->
</div>
</div>
</div>
</div>
</body>
</html>