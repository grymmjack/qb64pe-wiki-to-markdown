<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>STEP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STEP rootpage-STEP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">STEP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>STEP</b> keyword is used in <a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a> loops to skip through the count or to count down instead of up. Used in graphics to designate a relative coordinate position of a graphics object function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>FOR counter_variable = start_point TO stop_point [<b>STEP <i>interval</i></b>]</dd></dl></dd></dl>
<dl><dd><dl><dd>CIRCLE <b>STEP(0, 0)</b>, 10, 12</dd></dl></dd></dl>
<p>
</p>
<ul><li>The FOR counter variable is used to designate and pass the current FOR incremented value.</li>
<li>FOR loops without the optional STEP value increment by + 1 every loop.</li>
<li>The STEP increment value can be any literal or variable numerical type. It cannot be changed inside of the loop!</li>
<li>Start and stop point values can be any literal or variable type and they cannot be changed inside of the loop.</li>
<li>STEP interval designates the portion to add or subtract from the FOR variable value.</li></ul>
<dl><dd><ul><li>When the STEP interval is positive, the start value should be less than the stop value ot the loop will be ignored.</li>
<li>When the STEP interval is negative, the start value should be greater than the stop value or the loop will be ignored.</li></ul></dd></dl>
<ul><li>In graphics statements, STEP can be used before a pair of coordinate brackets to indicate that the coordinates are relative to the last graphics statement position. IE the position will be that number of pixels away from the last graphical object.</li></ul>
<p>
<i>Example:</i> Stepping down 2 in a FOR counter loop.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR...NEXT</span></a> i = 10 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 <a class="mw-selflink selflink"><span style="color:#4593D8;">STEP</span></a> -2
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i;
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">10 8 6 4 2 0
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The value of i = -2 after the loop is done.</dd></dl>
<p>
</p>
<dl><dd><dl><dd><i>Graphics Syntax:</i> LINE STEP(column1%, row1%)-(column2%, row2%), color_attribute%</dd></dl></dd></dl>
<p>
</p>
<ul><li>STEP coordinate positions are relative positive or negative pixel moves from the previous graphics object's last coordinate. After a CIRCLE statement, the relative coordinates would be from its center.</li>
<li>STEP can be used before the <a href="LINE" title="LINE">LINE</a>, <a href="CIRCLE" title="CIRCLE">CIRCLE</a>, <a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a>, <a href="PAINT" title="PAINT">PAINT</a> or <a href="DRAW" title="DRAW">DRAW</a> graphics object coordinates.</li></ul>
<p>
<i>Graphics Example:</i> Using STEP coordinates to PAINT a circle's interior.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (100, 100), 50, 12
<a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">STEP</span></a>(0, 0), 13, 12
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> PAINT uses the CIRCLE's center coordinate position to paint the interior.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a></li>
<li><a href="DRAW" title="DRAW">DRAW</a></li>
<li><a href="LINE" title="LINE">LINE</a>, <a href="CIRCLE" title="CIRCLE">CIRCLE</a>, <a href="PSET" title="PSET">PSET</a>, <a href="PAINT" title="PAINT">PAINT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192552
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 85/1000000
Post‐expand include size: 1173/2097152 bytes
Template argument size: 92/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.269      1 -total
 13.14%    2.269      1 Template:PageSyntax
 12.98%    2.242      9 Template:Cl
 12.53%    2.163      1 Template:PageNavigation
 12.12%    2.093      2 Template:CodeEnd
 11.64%    2.010      2 Template:CodeStart
 10.60%    1.831      1 Template:OutputStart
 10.14%    1.751      1 Template:OutputEnd
  9.96%    1.719      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:310-0!canonical and timestamp 20240714192552 and revision id 7684.
 -->
</div>
</div>
</div>
</div>
</body>
</html>