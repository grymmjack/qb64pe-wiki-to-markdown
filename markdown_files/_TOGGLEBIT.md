<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_TOGGLEBIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TOGGLEBIT rootpage-TOGGLEBIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_TOGGLEBIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_TOGGLEBIT</a> function is used to toggle a specified bit of a numerical value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_TOGGLEBIT</a>(<i>numericalVariable</i>, <i>numericalValue</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>numericalVariable</i> is the variable to toggle the bit of and can be of the following types: <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>.</li>
<li>Integer values can be signed or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li><i>numericalValue</i> the number of the bit to be set.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Can be used to manually manipulate individual bits of an integer value by toggling their state.</li>
<li>A bit set to 1 is changed to 0 and a bit set to 0 is changed to 1.</li>
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
A~%% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_TOGGLEBIT</span></a>(A~%%,4) 'toggle the fourth bit of A~%%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A~%%
A~%% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_TOGGLEBIT</span></a>(A~%%,4) 'toggle the fourth bit of A~%%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A~%%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 0
 16
 0
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1310" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="SHL" title="SHL">_SHL</a>, <a href="SHR" title="SHR">_SHR</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a></li>
<li><a href="SETBIT" title="SETBIT">_SETBIT</a>, <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li>
<li><a href="RESETBIT" title="RESETBIT">_RESETBIT</a>, <a href="READBIT" title="READBIT">_READBIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062557
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.036 seconds
Real time usage: 0.047 seconds
Preprocessor visited node count: 101/1000000
Post‐expand include size: 1274/2097152 bytes
Template argument size: 166/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.102      1 -total
  8.83%    2.482      5 Template:Parameter
  8.28%    2.326      1 Template:PageNavigation
  7.75%    2.178      1 Template:PageSyntax
  7.69%    2.160      1 Template:PageDescription
  7.65%    2.150      7 Template:Cl
  7.50%    2.109      1 Template:OutputStart
  7.10%    1.994      1 Template:PageAvailability
  6.80%    1.910      1 Template:PageSeeAlso
  6.49%    1.824      1 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:358-0!canonical and timestamp 20240715062556 and revision id 8930.
 -->
</div>
</div>
</div>
</div>
</body>
</html>