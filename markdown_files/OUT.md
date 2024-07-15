<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>OUT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OUT rootpage-OUT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">OUT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">OUT</a> writes values to register and port hardware addresses.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">OUT</a> <i>registerAddress%</i>, <i>value%</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>registerAddress%</i> is a value expressed as a decimal <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="%26H" title="&amp;H">hexadecimal</a>.</li>
<li>The <a href="INTEGER" title="INTEGER">INTEGER</a> <i>value%</i> sent is normally only 0 to 255 per byte register (8 bit) address.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>QB64 has limited access to registers. VGA memory and registers are emulated.</b></li>
<li>OUT can be used to change color port and a limited number of other port settings in QB64.</li>
<li>Some settings may be set in a specific order to gain access to settings and <a href="INP" title="INP">INP</a> reads.</li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a> modes determine the number of available color palette attributes from 2 to 256 in SCREEN 13.</li>
<li>Windows NT may block access to Parallel printer and Serial ports. See <a href="Port_Access_Libraries" title="Port Access Libraries">Port Access Libraries</a> or other DLLs.</li>
<li><a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a> can also be used to set RGB intensity values using <a href="RGB32" title="RGB32">32 bit color</a> values.</li>
<li>OUT can toggle the blinking attribute of SCREEN 0 color 16-31 for legacy code. <a href="BLINK" title="BLINK">_BLINK</a> is the preferred method. (starting with build 20170816/61).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Color_Port_Palette_access_using_OUT">Color Port Palette access using OUT</span></h2>
<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">OUT &amp;H3C7, attribute</span> : Set port to read RGB settings for start attribute</dd>
<dd><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="INP" title="INP">INP</a> &amp;H3C9, colorIntensity</span> : Reads RGB color intensity settings in order</dd></dl></dd></dl></dd></dl></dd></dl></dd></dl>
<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">OUT &amp;H3C8, attribute</span> : Set port to write RGB settings for start attribute</dd>
<dd><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">OUT &amp;H3C9, colorIntensity</span> : Writes RGB color intensity settings in order</dd></dl></dd></dl></dd></dl></dd></dl></dd></dl>
<dl><dd><dl><dd><dl><dd><dl><dd><ul><li>Every 3 reads or writes, changes to next color attribute without a set</li>
<li>Color setting is Red, Green and Blue attribute intensities in order.</li>
<li>Color attribute intensity values range from 0 to 63.</li>
<li>Some <a href="DAC" title="DAC">DAC</a> color attribute intensities cannot be changed using OUT.</li></ul></dd></dl></dd></dl></dd></dl></dd></dl>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>In DOS, OUT accesses memory and hardware directly, unlike <a href="POKE" title="POKE">POKE</a>, and could cause PC damage.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Reading the default RGB color settings of color attribute 15.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> &amp;H3C7, 15      'set color port attribute 15 for a read
red% = <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(&amp;H3C9)
green% = INP(&amp;H3C9)
blue% = INP(&amp;H3C9)
PRINT red%, green%, blue%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 63       63       63
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Changing the color intensity settings of the <a href="SCREEN" title="SCREEN">SCREEN</a> background <a href="COLOR" title="COLOR">COLOR</a> 0 to bright white.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> &amp;H3C8, 0  'attribute number. 0 for black screen background
<a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> &amp;H3C9, 63 'red
<a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> &amp;H3C9, 63 'green
<a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> &amp;H3C9, 63 'blue
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> In <a href="SCREEN" title="SCREEN">SCREEN</a> 0 this is one way to make high intensity background colors. <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="COLOR" title="COLOR">COLOR</a> ,15</span> is actually grey (7).</dd></dl>
<p>
<i>Example 3:</i> Toggling blinking colors in SCREEN beginning with build 20170816/61
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> &amp;H3C0, &amp;H10  'disables blinking and enables high intensity backgrounds (colors 16-31)
<a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> &amp;H3C0, 2 ^ 3 'reenables blinking and disables high intensity backgrounds  (colors 16-31)
</pre>
</td></tr></tbody></table>
<dl><dd>Note: In QB64, the recommended practice is to use the <a href="BLINK" title="BLINK">_BLINK</a> {ON|OFF} statement.</dd></dl>
<p>
<i>Example 4:</i> Restoring colors to a bitmap from the Red, Green and Blue <a href="BSAVE" title="BSAVE">BSAVEd</a> indexed array of color values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
 <a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C8, 0 ' set color port for output at attribute 0
 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 47 ' 48 RGB values is (3 * 16) -1 color attributes from 0 in screen 12
   <a class="mw-selflink selflink"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, Image%(i) ' changes to next attribute after 3 RGB loops
 <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
 <a href="PUT_(graphics_statement)" title="PUT (graphics statement)"><span style="color:#4593D8;">PUT</span></a>(clm, row), Image(48) PSET
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The color RGB intensity settings were imported from a file to the Image array using <a href="BLOAD" title="BLOAD">BLOAD</a>. The color attribute advances to the next one every 3 writes using OUT. The color information was indexed to the start of the array. The image is after the color settings at index 48. Index 48 is the <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> image width and 49 is the height.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PALETTE" title="PALETTE">PALETTE</a>, <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a></li>
<li><a href="INP" title="INP">INP</a></li>
<li><a href="PEEK" title="PEEK">PEEK</a></li>
<li><a href="POKE" title="POKE">POKE</a></li>
<li><a href="COLOR" title="COLOR">COLOR</a>, <a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="BSAVE" title="BSAVE">BSAVE</a>, <a href="BLOAD" title="BLOAD">BLOAD</a></li>
<li><a href="BLINK" title="BLINK">_BLINK</a>, <a href="BLINK_(function)" title="BLINK (function)">_BLINK (function)</a></li>
<li><a href="Port_Access_Libraries" title="Port Access Libraries">Port Access Libraries</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061351
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.053 seconds
Real time usage: 0.078 seconds
Preprocessor visited node count: 235/1000000
Post‐expand include size: 2868/2097152 bytes
Template argument size: 176/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   46.831      1 -total
 14.00%    6.557      5 Template:InlineCode
 10.02%    4.693      1 Template:PageNavigation
  7.51%    3.518     17 Template:Cl
  7.17%    3.358      4 Template:Parameter
  6.65%    3.116      1 Template:PageSyntax
  5.72%    2.677      1 Template:PageParameters
  5.57%    2.609      1 Template:PageDescription
  5.30%    2.482      5 Template:InlineCodeEnd
  5.23%    2.450      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:533-0!canonical and timestamp 20240715061351 and revision id 8991.
 -->
</div>
</div>
</div>
</div>
</body>
</html>