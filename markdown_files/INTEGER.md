<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>INTEGER - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INTEGER rootpage-INTEGER skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">INTEGER</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">INTEGER</a> is a 2-byte number type definition that can hold whole numerical values.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DIM" title="DIM">DIM</a> <i>variable</i> AS <a class="mw-selflink selflink">INTEGER</a></dd></dl>
<p>
</p>
<ul><li>Integers do not use decimal point values but will round those off to the nearest even whole number.</li>
<li>QBasic integer values can range from -32768 to 32767 without an "overflow" error.</li>
<li>For larger integer values use the <a href="LONG" title="LONG">LONG</a> integer type.</li>
<li><b>QB64</b> <a class="mw-selflink selflink">INTEGER</a> values greater than 32767 become negative signed values instead of throwing an "overflow" error, as the top bit designates a negative value. See example 1 below.</li>
<li><b>QB64</b> <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> integers can range from  0 to 65535.</li>
<li><b>QB64</b> _UNSIGNED <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> values range from 0 to 18446744073709551615</li>
<li>Many graphic programs require <a class="mw-selflink selflink">INTEGER</a> arrays.</li>
<li>Variable type suffix is % or ~% for <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>. Suffix can also be placed after a literal or hexadecimal numerical value.</li>
<li><a href="LONG" title="LONG">LONG</a> integers use the <b>&amp;</b> suffix and <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> use the <b>&amp;&amp;</b> suffix.</li>
<li>Values can be converted to 2 byte <a href="ASCII" title="ASCII">ASCII</a> string values using <a href="MKI$" title="MKI$">MKI$</a> and back with <a href="CVI" title="CVI">CVI</a>.</li>
<li><b>When a variable has not been defined or has no type suffix, the value defaults to <a href="SINGLE" title="SINGLE">SINGLE</a>.</b></li>
<li><b>Warning: QBasic keyword names cannot be used as numerical variable names with or without the type suffix.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> QBasic signed integers were limited from -32768 to 32767, but could not exceed 32767 or it would error:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 2000
  i% = i% + 1
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i%
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> i% = 0
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> In <b>QB64</b> the count will go to 32767, then count up from -32768 to 0 before repeating the process without error.</dd></dl>
<p>
<i>Example 2:</i> When a signed <b>QB64</b> INTEGER value exceeds 32767, the value may become a negative value:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">i% = 38000
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">-27536
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Use an <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> INTEGER or a ~% variable type suffix for only positive integer values up to 65535.</dd></dl>
<p>
<i>Example 3:</i> In <b>QB64</b> <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> INTEGER values greater than 65535 cycle over again from zero:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">i~% = 70000
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i~%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 4464
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> In QB64 an unsigned integer value of 65536 would be 0 with values increasing by the value minus 65536.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DIM" title="DIM">DIM</a>, <a href="DEFINT" title="DEFINT">DEFINT</a></li>
<li><a href="LONG" title="LONG">LONG</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li>
<li><a href="LEN" title="LEN">LEN</a>, <a href="MKI$" title="MKI$">MKI$</a>, <a href="CVI" title="CVI">CVI</a></li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a>, <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li>
<li><a href="%26B" title="&amp;B">&amp;B</a> (binary), <a href="%26O" title="&amp;O">&amp;O</a> (octal), <a href="%26H" title="&amp;H">&amp;H</a> (hexadecimal)</li>
<li><a href="%5C" title="\">Integer Division</a>, <a href="MOD" title="MOD">MOD</a> (Integer remainder division)</li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714101113
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.039 seconds
Preprocessor visited node count: 80/1000000
Post‐expand include size: 1248/2097152 bytes
Template argument size: 71/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.547      1 -total
 11.98%    2.462      7 Template:Cl
 11.52%    2.367      1 Template:PageSyntax
 10.27%    2.111      1 Template:PageExamples
  9.95%    2.044      3 Template:CodeStart
  9.63%    1.978      1 Template:PageNavigation
  9.53%    1.957      1 Template:PageSeeAlso
  9.39%    1.929      3 Template:CodeEnd
  9.12%    1.875      2 Template:OutputStart
  9.08%    1.866      2 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:234-0!canonical and timestamp 20240714101113 and revision id 6045.
 -->
</div>
</div>
</div>
</div>
</body>
</html>