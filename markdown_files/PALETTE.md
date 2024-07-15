<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PALETTE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PALETTE rootpage-PALETTE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PALETTE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">PALETTE</a> statement can swap color settings, set colors to default or set the red, green and blue color components of palette colors.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dt>Screens 11, 12, 13, 256</dt>
<dd><a class="mw-selflink selflink">PALETTE</a> [<i>attribute%</i>, <i>red%</i> + (<i>green%</i> * 256) + (<i>blue%</i> * 65536)]</dd>
<dt>Screen 10</dt>
<dd><a class="mw-selflink selflink">PALETTE</a> [<i>existingAttribute%</i>, <i>newAttribute%</i> (value from 0 to 7)]</dd>
<dt>Screens 0 and 9</dt>
<dd><a class="mw-selflink selflink">PALETTE</a> [<i>existingAttribute%</i>, <i>newAttribute%</i> (value from 0 to 63)]</dd>
<dt>Screens 1, 2, 7, and 8</dt>
<dd><a class="mw-selflink selflink">PALETTE</a> [<i>existingAttribute%</i>, <i>newAttribute%</i> (value from 0 to 15)]</dd>
<dt>Screen 32</dt>
<dd>No Palette available as all 32-bit colors are available.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>red%</i>, <i>green%</i> and <i>blue%</i> values can range from 0 to 63. Many color shades are possible in non-<a href="DAC" title="DAC">DAC</a> color attributes.  (Valid for screens 11, 12, 13, and 256 only.)</li>
<li>If the <i>red%</i>, <i>green%</i> and <i>blue%</i> color intensity settings are all the same value the resulting color is a shade of grey.  (Valid for screens 11, 12, 13, and 256 only.)</li>
<li>A swap is often used with <a href="DAC" title="DAC">DAC</a> color attributes that cannot change RGB settings. Only the RGB color settings are swapped from original <i>existingAttribute%</i> to <i>newAttribute%</i>. Screens 0 thru 9 support swaps.</li>
<li>PALETTE without any value sets any changed RGB settings back to the default color settings, including <a href="DAC" title="DAC">DAC</a> colors.</li>
<li><a href="PALETTE_USING" title="PALETTE USING">PALETTE USING</a> can be used when color intensity values are stored in an <a href="Arrays" title="Arrays">array</a>.</li>
<li>QB64 implements the <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a> statement to provide extended palette functionality.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>Screens 0, 7 and 9 (<a href="DAC" title="DAC">DAC</a>) colors could not be changed using the first syntax, but the program could use <a href="OUT" title="OUT">OUT</a> to change intensity settings of attributes 1 thru 5.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Displaying all 64 DAC color hues as backgrounds in SCREEN 9 using a PALETTE swap.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">  <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 9 ' background is default black
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 33: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press any Key!"
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 63
   a$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1) ' wait for a keypress
   <a class="mw-selflink selflink"><span style="color:#4593D8;">PALETTE</span></a> 0, i
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Other attributes (1 to 15) can also be swapped for DAC foreground colors.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a></li>
<li><a href="PALETTE_USING" title="PALETTE USING">PALETTE USING</a></li>
<li><a href="COLOR" title="COLOR">COLOR</a></li>
<li><a href="OUT" title="OUT">OUT</a>, <a href="INP" title="INP">INP</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192522
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.024 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 183/1000000
Post‐expand include size: 1287/2097152 bytes
Template argument size: 249/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   14.710      1 -total
 11.79%    1.734      1 Template:PageSyntax
 11.66%    1.714     15 Template:Parameter
 11.22%    1.651      8 Template:Cl
  9.75%    1.434      1 Template:PageDescription
  9.48%    1.394      1 Template:CodeStart
  9.01%    1.325      1 Template:CodeEnd
  9.00%    1.324      1 Template:PageNavigation
  8.97%    1.320      1 Template:PageExamples
  8.89%    1.308      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:575-0!canonical and timestamp 20240714192522 and revision id 8587.
 -->
</div>
</div>
</div>
</div>
</body>
</html>