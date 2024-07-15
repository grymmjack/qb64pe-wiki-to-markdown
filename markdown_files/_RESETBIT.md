<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_RESETBIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RESETBIT rootpage-RESETBIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_RESETBIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_RESETBIT</a> function is used to set a specified bit of a numerical value to 0 (OFF state).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_RESETBIT</a>(<i>numericalVariable</i>, <i>numericalValue</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>numericalVariable</i> is the variable to set the bit of and can be of the following types: <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>.</li>
<li>Integer values can be signed or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li><i>numericalValue</i> the number of the bit to be set.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Can be used to manually manipulate individual bits of an integer value by setting them to 0 (OFF state).</li>
<li>Resetting a bit that is already set to 0 will have no effect.</li>
<li>Bits start at 0 (so a <a href="BYTE" title="BYTE">_BYTE</a> has bits 0 to 7, <a href="INTEGER" title="INTEGER">INTEGER</a> 0 to 15, and so on)</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.4 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">A~%% = 0 '<a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A~%%
A~%% = <a href="SETBIT" title="SETBIT"><span style="color:#4593D8;">_SETBIT</span></a>(A~%%,6) 'set the seventh bit of A~%%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A~%%
A~%% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_RESETBIT</span></a>(A~%%,6) 'Reset the seventh bit of A~%%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A~%%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 0
 64
 0
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHL" title="SHL">_SHL</a>, <a href="SHR" title="SHR">_SHR</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a></li>
<li><a href="SETBIT" title="SETBIT">_SETBIT</a>, <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li>
<li><a href="READBIT" title="READBIT">_READBIT</a>, <a href="TOGGLEBIT" title="TOGGLEBIT">_TOGGLEBIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062555
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.042 seconds
Real time usage: 0.091 seconds
Preprocessor visited node count: 101/1000000
Post‐expand include size: 1266/2097152 bytes
Template argument size: 158/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   56.937      1 -total
 27.43%   15.619      5 Template:Parameter
 12.04%    6.856      1 Template:OutputEnd
  8.31%    4.733      1 Template:PageParameters
  7.14%    4.067      1 Template:PageNavigation
  6.80%    3.872      1 Template:PageSyntax
  6.23%    3.545      1 Template:PageDescription
  5.49%    3.127      1 Template:PageSeeAlso
  4.11%    2.339      7 Template:Cl
  3.97%    2.258      1 Template:PageAvailability
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:220-0!canonical and timestamp 20240715062555 and revision id 7386.
 -->
</div>
</div>
</div>
</div>
</body>
</html>