<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>FOR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FOR rootpage-FOR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">FOR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">FOR</a> statement creates a counter loop using specified start and stop numerical boundaries. The default increment is + 1.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">FOR</a> <i>counterVariable</i> = <i>startValue</i> <a href="TO" title="TO">TO</a> <i>stopValue</i> [[[STEP <i>increment</i>]
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a href="NEXT" title="NEXT">NEXT</a> [<i>counterVariable</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <a class="mw-selflink selflink">FOR</a> <i>counterVariable</i> name is required to define the counter span and may also be used after the NEXT keyword.</li>
<li>The <i>startValue</i> <a href="TO" title="TO">TO</a> <i>stopValue</i> can be any literal or variable numerical type. Both values are  required.</li>
<li><a href="STEP" title="STEP">STEP</a> can be used for a loop <i>increment</i> other than the default <i>plus 1 and can be any positive or negative literal or variable numerical value as long as the STEP value corresponds to the loop's </i>startValue<i> and </i>stopValue<i>.</i></li>
<li><a href="NEXT" title="NEXT">NEXT</a> ends the <a class="mw-selflink selflink">FOR</a> loop code block and increments the counter to the next value even when it exceeds the stop limit.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a> counter loops must be within the proper start, stop and increment values or the entire loop code block will not be executed.</li>
<li>Avoid changing the FOR <i>counterVariable'</i>s value inside of the loop. This obfuscates code and is a poor programming practice.</li>
<li>Once the loop has been started, changing the variables holding the <i>startValue</i>, <i>stopValue</i> or <i>increment</i> value will not affect loop execution.</li>
<li><b>If the <a href="STEP" title="STEP">STEP</a> <i>increment</i> value does not match the <i>startValue</i> <a href="TO" title="TO">TO</a> <i>stopValue</i> the FOR loop block will be ignored.</b>
<ul><li>If <i>startValue</i> is less than <i>stopValue</i>, use the default increment or positive <a href="STEP" title="STEP">STEP</a> value or the loop will not be executed.</li>
<li>If <i>startValue</i> is more than <i>stopValue</i>, use a negative <a href="STEP" title="STEP">STEP</a> interval or the loop will not be executed.</li>
<li>The <a href="STEP" title="STEP">STEP</a> <i>increment</i> value cannot be changed inside of the loop.</li></ul></li>
<li>Use <b><a href="EXIT" title="EXIT">EXIT</a> FOR</b> to leave a FOR loop early when a certain condition is met inside of the loop.</li>
<li>The <a href="NEXT" title="NEXT">NEXT</a> counter variable name is not required. NEXT loop increments can be separated by colons in nested FOR loops.</li>
<li><b>NOTE: When the FOR loop is exited after the <i>stopValue</i> is reached, the <i>counterVariable</i></b><i>s value will be </i>stopValue<i> + 1 (or </i>stopValue<i> + </i>increment<i>)</i></li>
<li><b>Beware of FOR loop counts that exceed the <i>counterVariable</i> type limits and may repeat without error in QB64.</b>
<ul><li>For example, if <i>counterVariable</i> is of type <a href="INTEGER" title="INTEGER">INTEGER</a> and the stop limit exceeds 32767, the <i>counterVariable</i> will reset back to -32768 and loop endlessly.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Adding all of the even numbers from 10 to 0.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">FOR i = 10 TO 0 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -2
  totaleven% = i + totaleven%
  PRINT totaleven%;
NEXT
PRINT "After loop, i ="; i
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">10 18 24 28 30 30 After loop, i = -2
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The loop counts down from 10 to every even value below it. The counter keeps stepping down until the FOR stop limit is reached or exceeded. Note that the value of i is -2 after the loop is exited. <a href="NEXT" title="NEXT">NEXT</a> always increments the counter one last time.</dd></dl>
<p>
<i>Example 2:</i> How an entire FOR loop block is ignored when the start and stop limits do not match the default or <a href="STEP" title="STEP">STEP</a> increment.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "hi"
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 10 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 1 'requires a negative <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> value
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "lo"
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "bye"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">hi
bye </pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="STEP" title="STEP">STEP</a></li>
<li><a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a>, <a href="WHILE...WEND" title="WHILE...WEND">WHILE...WEND</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034109
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.037 seconds
Real time usage: 0.046 seconds
Preprocessor visited node count: 210/1000000
Post‐expand include size: 1743/2097152 bytes
Template argument size: 396/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   26.225      1 -total
 10.21%    2.679     30 Template:Parameter
  8.76%    2.298      1 Template:PageSyntax
  8.16%    2.140      8 Template:Cl
  7.18%    1.884      2 Template:OutputStart
  7.12%    1.868      1 Template:PageNavigation
  6.99%    1.833      1 Template:PageParameters
  6.78%    1.777      1 Template:PageExamples
  6.74%    1.767      1 Template:PageSeeAlso
  6.72%    1.762      2 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:309-0!canonical and timestamp 20240715034109 and revision id 7289.
 -->
</div>
</div>
</div>
</div>
</body>
</html>