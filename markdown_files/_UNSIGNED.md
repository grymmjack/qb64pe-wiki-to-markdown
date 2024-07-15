<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_UNSIGNED - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-UNSIGNED rootpage-UNSIGNED skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_UNSIGNED</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">_UNSIGNED</a> defines a numerical value as being only positive.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DIM" title="DIM">DIM</a> <i>variable</i> <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <i>datatype</i></dd></dl>
<dl><dd><a href="DEFINE" title="DEFINE">_DEFINE</a> <i>letterRange</i> <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <i>datatype</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Datatype can be any of the following: <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, <a href="BIT" title="BIT">_BIT</a>, <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>, <a href="OFFSET" title="OFFSET">_OFFSET</a></li>
<li><b><a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a> and <a href="FLOAT" title="FLOAT">_FLOAT</a> variable types cannot be _UNSIGNED.</b></li>
<li><a class="mw-selflink selflink">_UNSIGNED</a> can be used in a <a href="DEFINE" title="DEFINE">_DEFINE</a> statement to set undefined variable name first letters as all positive-only values.</li>
<li>Can also be used in <a href="DIM" title="DIM">DIM</a> statements or subprocedure parameter definitions following <a href="AS" title="AS">AS</a>.</li>
<li><a class="mw-selflink selflink">_UNSIGNED</a> allows larger positive numerical variable value limits than signed ones.</li>
<li>The unsigned variable type suffix used is the <b>tilde (~)</b>, right before the number's own type suffix: <i>variableName~&amp;</i></li></ul>
<p>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">                        00000001 - unsigned &amp; signed are both 1
                        01111111 - unsigned &amp; signed are both 127
                        11111111 - unsigned is 255 but signed is -1
                        11111110 - unsigned is 254 but signed is -2
                        11111101 - unsigned is 253 but signed is -3
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i>  In <b>QB64</b>, when a signed <a href="INTEGER" title="INTEGER">INTEGER</a> value exceeds 32767, the value may become a negative value:
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
<dl><dd><i>Explanation:</i> Use an <a class="mw-selflink selflink">_UNSIGNED</a> <a href="INTEGER" title="INTEGER">INTEGER</a> or a ~% variable type suffix for only positive integer values up to 65535.</dd></dl>
<p>
<i>Example 2:</i> In <b>QB64</b>, <a class="mw-selflink selflink">_UNSIGNED</a> <a href="INTEGER" title="INTEGER">INTEGER</a> values greater than 65535 cycle over again from zero:
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
<i>Example 3:</i> Demonstrating how _UNSIGNED variables expand the <a href="INTEGER" title="INTEGER">INTEGER</a> range.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> pn <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 3, 6: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press Esc to exit loop"
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> n = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 80000
  <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 10000 ' 6.5 second loop
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 12, 37: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> n ' display current value
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> n &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> pn = n ' find highest value
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> n = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> Count = Count + 1: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 14, 37: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Count:"; Count; "Max:"; pn
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(&amp;H60) = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT FOR</span></a> ' escape key exit
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> n
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">
   Press Esc to exit loop
                           65462
                          Count: 13 Max: 65535
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> The maximum value can only be 65535 (32767 + 32768) so the FOR loop repeats itself. Remove the <a class="mw-selflink selflink">_UNSIGNED</a> parts and run it again.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li>DECLARE, <a href="SUB" title="SUB">SUB</a>, <a href="FUNCTION" title="FUNCTION">FUNCTION</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="DEFINE" title="DEFINE">_DEFINE</a></li>
<li><a href="DEFSTR" title="DEFSTR">DEFSTR</a>, <a href="DEFLNG" title="DEFLNG">DEFLNG</a>, <a href="DEFINT" title="DEFINT">DEFINT</a>, <a href="DEFSNG" title="DEFSNG">DEFSNG</a>, <a href="DEFDBL" title="DEFDBL">DEFDBL</a></li>
<li><a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li>
<li><a href="ABS" title="ABS">ABS</a>, <a href="SGN" title="SGN">SGN</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034521
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.046 seconds
Real time usage: 0.057 seconds
Preprocessor visited node count: 266/1000000
Post‐expand include size: 2618/2097152 bytes
Template argument size: 337/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.126      1 -total
 11.70%    3.875     29 Template:Cl
  7.78%    2.577      1 Template:PageSyntax
  7.61%    2.519      5 Template:Parameter
  7.21%    2.387      3 Template:CodeEnd
  6.90%    2.285      1 Template:PageSeeAlso
  6.02%    1.993      1 Template:PageDescription
  5.94%    1.967      3 Template:OutputEnd
  5.91%    1.959      3 Template:OutputStart
  5.89%    1.951      1 Template:FixedStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:235-0!canonical and timestamp 20240715034521 and revision id 7457.
 -->
</div>
</div>
</div>
</div>
</body>
</html>