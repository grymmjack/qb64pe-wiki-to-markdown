<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SETBIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SETBIT rootpage-SETBIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SETBIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SETBIT</a> function is used to set a specified bit of a numerical value to 1 (on state).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_SETBIT</a>(<i>numericalVariable</i>, <i>numericalValue</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>numericalVariable</i> is the variable to set the bit of and can be of the following types: <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>.</li>
<li>Integer values can be signed or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li><i>numericalValue</i> the number of the bit to be set.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Can be used to manually manipulate individual bits of an integer value by setting them to 1 (on state).</li>
<li>Setting a bit that is already set to 1 will have no effect.</li>
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
A~%% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SETBIT</span></a>(A~%%,6) 'set the seventh bit of A~%%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A~%%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 0
 64
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHL" title="SHL">_SHL</a>, <a href="SHR" title="SHR">_SHR</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a></li>
<li><a href="READBIT" title="READBIT">_READBIT</a>, <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li>
<li><a href="RESETBIT" title="RESETBIT">_RESETBIT</a>, <a href="TOGGLEBIT" title="TOGGLEBIT">_TOGGLEBIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062556
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.041 seconds
Real time usage: 0.062 seconds
Preprocessor visited node count: 87/1000000
Post‐expand include size: 1156/2097152 bytes
Template argument size: 130/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   40.443      1 -total
  9.64%    3.899      1 Template:PageSyntax
  9.46%    3.828      5 Template:Parameter
  8.16%    3.300      5 Template:Cl
  8.14%    3.291      1 Template:PageAvailability
  7.31%    2.955      1 Template:CodeStart
  6.90%    2.789      1 Template:PageExamples
  6.89%    2.785      1 Template:OutputStart
  6.55%    2.648      1 Template:PageParameters
  6.37%    2.578      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:325-0!canonical and timestamp 20240715062556 and revision id 7405.
 -->
</div>
</div>
</div>
</div>
</body>
</html>