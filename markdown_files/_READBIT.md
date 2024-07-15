<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_READBIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-READBIT rootpage-READBIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_READBIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_READBIT</a> function is used to check the state of a specified bit of a integer value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_READBIT</a>(<i>numericalVariable</i>, <i>numericalValue</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>numericalVariable</i> is the variable to read the state of a bit of and can be of the following types: <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>.</li>
<li>Integer values can be signed or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li><i>numericalValue</i> the number of the bit to be read.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Used to check the current state of a bit in an integer value.</li>
<li>Returns -1 if the bit is set(1), otherwise returns 0 if the bit is not set(0)</li>
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
<td><pre class="codeide">A~%% = <a href="SETBIT" title="SETBIT"><span style="color:#4593D8;">_SETBIT</span></a>(A~%%,4)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Bit 4 is currently ";
IF <a class="mw-selflink selflink"><span style="color:#4593D8;">_READBIT</span></a>(A~%%,4) = -1 THEN <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "ON" ELSE <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "OFF"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "And bit 2 is currently ";
IF <a class="mw-selflink selflink"><span style="color:#4593D8;">_READBIT</span></a>(A~%%,2) = -1 THEN <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "ON" ELSE <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "OFF"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Bit 4 is currently ON
And bit 2 is currently OFF
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">B&amp; = 12589575
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "B&amp; ="; B&amp;
FOR I%% = 31 TO 0 STEP -1 '32 bits for a <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> value
 Binary$ = Binary$ + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(<a href="ABS" title="ABS"><span style="color:#4593D8;">ABS</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_READBIT</span></a>(B&amp;, I%%))))
NEXT I%%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "B&amp; in binary is: "; Binary$</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">B&amp; = 12589575
B&amp; in binary is: 00000000110000000001101000000111
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHL" title="SHL">_SHL</a>, <a href="SHR" title="SHR">_SHR</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a></li>
<li><a href="SETBIT" title="SETBIT">_SETBIT</a>, <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li>
<li><a href="RESETBIT" title="RESETBIT">_RESETBIT</a>, <a href="TOGGLEBIT" title="TOGGLEBIT">_TOGGLEBIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062554
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.039 seconds
Real time usage: 0.055 seconds
Preprocessor visited node count: 170/1000000
Post‐expand include size: 1860/2097152 bytes
Template argument size: 244/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   36.103      1 -total
 22.71%    8.200      5 Template:Parameter
  7.64%    2.757      1 Template:PageSyntax
  7.39%    2.669     16 Template:Cl
  6.06%    2.189      2 Template:CodeStart
  5.86%    2.117      1 Template:PageDescription
  5.79%    2.092      1 Template:PageExamples
  5.68%    2.050      1 Template:PageParameters
  5.64%    2.038      1 Template:PageAvailability
  5.46%    1.970      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:219-0!canonical and timestamp 20240715062554 and revision id 7384.
 -->
</div>
</div>
</div>
</div>
</body>
</html>