<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PALETTECOLOR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PALETTECOLOR rootpage-PALETTECOLOR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PALETTECOLOR</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_PALETTECOLOR</a> statement sets the color value of a palette entry of an image using 256 color modes or less (4 or 8 BPP).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_PALETTECOLOR</a> <i>attribute%</i>, <i>newColor&amp;</i>[, <i>destHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>attribute%</i> is the palette index number of the color to set, ranging from 0 to 15 (4 bit) or 0 to 255 (8 bit) color modes.</li>
<li>The <a href="LONG" title="LONG">LONG</a> <i>newColor&amp;</i> is the new color value to set using <a href="RGB32" title="RGB32">_RGB32</a> or <a href="RGBA32" title="RGBA32">_RGBA32</a> values or using <a href="HEX$_32_Bit_Values" title="HEX$ 32 Bit Values">HEX$ 32 Bit Values</a>.</li>
<li>If <i>destHandle&amp;</i> is omitted, <a href="DEST" title="DEST">destination</a> is assumed to be the current write page or screen surface.</li>
<li>If <i>attribute%</i> is outside of image or <a href="SCREEN" title="SCREEN">screen</a> mode attribute range (0 to 15 or 0 to 255), an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error will occur.</li>
<li>If <i>destHandle&amp;</i> does not use a palette, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error occurs. <b>Will not work in 24/32 bit color palette modes.</b></li>
<li>If <i>destHandle&amp;</i> is an invalid handle value, an <a href="ERROR_Codes" title="ERROR Codes">invalid handle</a> error occurs.</li></ul>
<p>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="color:Gold;">     Attribute        Description     Red   Green   Blue   32 HEX    HTML Name </span>
         0            Black            0      0       0    000000    Black
<span style="color:#00208B;">         1            Dark Blue        0      0      42    00008B    DarkBlue</span>
<span style="color:#006400;">         2            Dark Green       0     42       0    006400    DarkGreen</span>
<span style="color:#008B8B;">         3            Dark Cyan        0     42      42    008B8B    DarkCyan</span>
<span style="color:#8B0000;">         4            Dark Red        42      0       0    8B0000    DarkRed</span>
<span style="color:#8B008B;">         5            Dark Magenta    42      0      42    8B008B    DarkMagenta</span>
<span style="color:#DAA520;">         6            Dark Yellow     42     21       0    DAA520    GoldenRod</span>
<span style="color:#D3D3D3;">         7            Light Grey      42     42      42    D3D3D3    LightGrey</span>
<span style="color:#696969;">         8            Dark Grey       21     21      21    696969    DimGray</span>
<span style="color:#1515FF;">         9            Blue            21     21      63    0000FF    Blue</span>
<span style="color:#15FF15;">        10            Green           21     63      21    15FF15    Lime</span>
<span style="color:#15FFFF;">        11            Cyan            21     63      63    15FFFF    Cyan</span>
<span style="color:#FF1515;">        12            Red             63     21      21    FF1515    Red</span>
<span style="color:#FF15FF;">        13            Magenta         63     21      63    FF15FF    Magenta</span>
<span style="color:#FFFF00;">        14            Yellow          63     63      21    FFFF00    Yellow</span>
<span style="color:#FFFFFF;">        15            White           63     63      63    FFFFFF    White</span>
</pre>
</td></tr></tbody></table>
<dl><dd><dl><dd><dl><dd><i>Note:</i> <b>QB64</b> 32 bit color intensity values from 0 to 255 can be found by multiplying above values by 4.</dd></dl></dd></dl></dd></dl>
<p><i>Summary:</i> The red, green, and blue intensity values can be changed using <a href="OUT" title="OUT">OUT</a> or <a href="PALETTE" title="PALETTE">PALETTE</a> statements. Some <b>QBasic</b> RGB color attribute values can be changed in <a href="DAC" title="DAC">DAC</a> <a href="SCREEN" title="SCREEN">SCREEN</a> modes and the <a href="DAC" title="DAC">DAC</a> RGB intensity settings may be different.
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Creating custom background colors in SCREEN 0 that follow the text. <a href="CLS" title="CLS">CLS</a> makes entire background one color.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_PALETTECOLOR</span></a> 1, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(255, 255, 255) ' white.
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PALETTECOLOR</span></a> 2, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(255, 170, 170) ' lighter red.
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PALETTECOLOR</span></a> 3, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(255, 85, 85) ' light red.
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PALETTECOLOR</span></a> 4, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(255, 0, 0) ' red.
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PALETTECOLOR</span></a> 5, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(170, 0, 0) ' dark red.
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PALETTECOLOR</span></a> 6, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(85, 0, 0) ' darker red.
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "black on white."
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0, 2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "black on lighter red."
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0, 3: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "black on light red."
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0, 4: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "black on red."
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0, 5: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "black on dark red."
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0, 6: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "black on darker red.
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 1, 6: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "white on darker red"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 2, 6: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "ligher red on darker red"
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> <a class="mw-selflink selflink">_PALETTECOLOR</a> expects <a href="LONG" title="LONG">LONG</a> <a href="RGB32" title="RGB32">_RGB32</a> or <a href="RGBA32" title="RGBA32">_RGBA32</a> 32 bit color values, not <a href="RGB" title="RGB">_RGB</a> or <a href="RGBA" title="RGBA">_RGBA</a> palette attribute values.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="COLOR" title="COLOR">COLOR</a>, <a href="RGB32" title="RGB32">_RGB32</a>, <a href="RGBA32" title="RGBA32">_RGBA32</a></li>
<li><a href="PALETTECOLOR_(function)" title="PALETTECOLOR (function)">_PALETTECOLOR (function)</a></li>
<li><a href="PALETTE" title="PALETTE">PALETTE</a>, <a href="OUT" title="OUT">OUT</a>, <a href="INP" title="INP">INP</a></li>
<li><a href="Images" title="Images">Images</a></li>
<li><a href="HEX$_32_Bit_Values" title="HEX$ 32 Bit Values">HEX$ 32 Bit Values</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034431
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 370/1000000
Post‐expand include size: 4193/2097152 bytes
Template argument size: 1824/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.660      1 -total
 10.58%    2.503     28 Template:Cl
  8.10%    1.917      1 Template:CodeEnd
  8.01%    1.894     16 Template:Text
  7.97%    1.886      1 Template:PageSyntax
  7.38%    1.746      9 Template:Parameter
  7.19%    1.701      1 Template:OutputStart
  6.85%    1.620      1 Template:PageNavigation
  6.84%    1.617      1 Template:OutputEnd
  6.45%    1.526      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:244-0!canonical and timestamp 20240715034431 and revision id 7921.
 -->
</div>
</div>
</div>
</div>
</body>
</html>