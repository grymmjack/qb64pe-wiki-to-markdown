<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>COLOR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-COLOR rootpage-COLOR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">COLOR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">COLOR</a> statement is used to change the foreground and background colors for printing text.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">COLOR</a> [<i>foreground&amp;</i>][, <i>background&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>background&amp;</i> colors are available in all QB64 color SCREEN modes.</li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a> mode 10 has only 3 white foreground attributes including flashing.</li>
<li>To change the <i>background&amp;</i> color only, use a comma and the desired color. Ex: <a class="mw-selflink selflink">COLOR</a> , <i>background&amp;</i></li>
<li>Graphic drawing statements like <a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a>, <a href="LINE" title="LINE">LINE</a>, etc, also use the colors set by the <a class="mw-selflink selflink">COLOR</a> statement if no color is passed when they are called.</li>
<li>The <a href="$COLOR" title="$COLOR">$COLOR</a> metacommand adds named color constants for both text and 32-bit modes.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Screen_Mode_Attributes">Screen Mode Attributes</span></h2>
<ul><li><b>SCREEN 0</b> <i>background&amp;</i> colors 0 to 7 can be changed each text character without affecting other text. Use <a href="CLS" title="CLS">CLS</a> after a background color statement to create a fullscreen background color. 64 <a href="DAC" title="DAC">DAC</a> hues with 16 high intensity blinking foreground (16 to 31) color attributes. See <a href="BLINK" title="BLINK">_BLINK</a>.
<ul><li>See example 7 below for more SCREEN 0 background colors.</li></ul></li>
<li><b>SCREEN 1</b> has <b>4 background color attributes</b>: 0 = black, 1 = blue, 2 = green, 3 = grey. White foreground color only.</li>
<li><b>SCREEN 2</b> is <b>monochrome</b> with white forecolor and black background.</li>
<li><b>SCREEN 7</b> can use 16 (<a href="DAC" title="DAC">DAC</a>) colors with background colors. RGB settings can be changed in colors 0 to 7 using <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a>.</li>
<li><b>SCREEN 8</b> has 16 color attributes with 16 background colors.</li>
<li><b>SCREEN 9</b> can use up to 64 <a href="DAC" title="DAC">DAC</a> color hues in 16 color attributes with background colors assigned to attribute 0 with a <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a> swap. RGB settings can be changed in colors 0 to 5 and 7 using <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a>.</li>
<li><b>SCREEN 10</b> has <b>only 4 color attributes</b> with black background. COLOR 0 = black, 1 = grey, 2 = flash white and 3 = bright white.</li>
<li><b>SCREEN 11</b> is <b>monochrome</b> with white forecolor and a black background.</li>
<li><b>SCREEN 12</b> can use 16 color attributes with a black background. 256K possible RGB color hues. Background colors can be used with QB64.</li>
<li><b>SCREEN 13</b> can use 256 color attributes with a black background. 256K possible RGB hues.</li>
<li><a href="PALETTE" title="PALETTE">PALETTE</a> swaps can be made in SCREEN 7 and 9 only. Those screens were <a href="DAC" title="DAC">DAC</a> screen modes in QBasic.</li>
<li><a href="DEST" title="DEST">_DEST</a> can be used to set the destination page or image to color using <b>QB64</b>.</li>
<li><a href="DEFAULTCOLOR" title="DEFAULTCOLOR">_DEFAULTCOLOR</a> returns the current color being used on an image or screen page handle.</li></ul>
<h3><span id="24.2F32-Bit_colors_using_QB64"></span><span class="mw-headline" id="24/32-Bit_colors_using_QB64">24/32-Bit colors using QB64</span></h3>
<ul><li>Pixel color intensities for red, green, blue and alpha range from 0 to 255 when used with <a href="RGB" title="RGB">_RGB</a>, <a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGB32" title="RGB32">_RGB32</a> and <a href="RGBA32" title="RGBA32">RGBA32</a>.</li>
<li>Combined RGB function values returned are <a href="LONG" title="LONG">LONG</a> values. <b>Blue intensity values may be cut off using <a href="SINGLE" title="SINGLE">SINGLE</a> variables.</b></li>
<li><a href="ALPHA" title="ALPHA">_ALPHA</a> transparency values can range from 0 as transparent up to 255 which is fully opaque.</li>
<li><a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a> can also be used to set a color as transparent.</li>
<li>Colors can be mixed by using <a href="BLEND" title="BLEND">_BLEND</a> (default) in 32-bit screen modes. <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> disables blending.</li>
<li><b>NOTE: Default 32-bit backgrounds are clear black or <a href="RGBA" title="RGBA">_RGBA</a>(0, 0, 0, 0). Use <a href="CLS" title="CLS">CLS</a> to make the black opaque.</b></li></ul>
<p style="text-align: center">(<a href="#toc">Return to Table of Contents</a>)</p>
<p>
</p>
<h2><span class="mw-headline" id="RGB_Palette_Intensities">RGB Palette Intensities</span></h2>
<p>RGB intensity values can be converted to hexadecimal values to create the <a href="LONG" title="LONG">LONG</a> <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a> value in non-32-bit screens:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
alpha$ = "FF" 'solid alpha colors only
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Attribute = Hex value      Red          Green         Blue "
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 7
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> attribute = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 15
  <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C7, attribute 'set color attribute to read
  red$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9) * 255 / 63) 'convert port setting to 32 bit values
  grn$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9) * 255 / 63)
  blu$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9) * 255 / 63)
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(red$) = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> red$ = "0" + red$ '2 hex digits required
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(grn$) = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> grn$ = "0" + grn$ 'for low or zero hex values
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(blu$) = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> blu$ = "0" + blu$
  hex32$ = "<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>" + alpha$ + red$ + grn$ + blu$
  <a href="PALETTECOLOR" title="PALETTECOLOR"><span style="color:#4593D8;">_PALETTECOLOR</span></a> attribute, <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(hex32$) 'VAL converts hex string to a LONG 32 bit value
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> attribute <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> attribute 'exclude black color print
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a>" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Attribute  Hex value      Red        Green       Blue
<span style="color:#0000AA;">COLOR 1 = &amp;HFF0000AA       00         00         AA</span>
<span style="color:#00AA00;">COLOR 2 = &amp;HFF00AA00       00         AA         00</span>
<span style="color:#00AAAA;">COLOR 3 = &amp;HFF00AAAA       00         AA         AA</span>
<span style="color:#AA0000;">COLOR 4 = &amp;HFFAA0000       AA         00         00</span>
<span style="color:#AA00AA;">COLOR 5 = &amp;HFFAA00AA       AA         00         AA</span>
<span style="color:#AA5500;">COLOR 6 = &amp;HFFAA5500       AA         55         00</span>
<span style="color:#AAAAAA;">COLOR 7 = &amp;HFFAAAAAA       AA         AA         AA</span>
<span style="color:#555555;">COLOR 8 = &amp;HFF555555       55         55         55</span>
<span style="color:#5555FF;">COLOR 9 = &amp;HFF5555FF       55         55         FF</span>
<span style="color:#55FF55;">COLOR 10 = &amp;HFF55FF55      55         FF         55</span>
<span style="color:#55FFFF;">COLOR 11 = &amp;HFF55FFFF      55         FF         FF</span>
<span style="color:#FF5555;">COLOR 12 = &amp;HFFFF5555      FF         55         55</span>
<span style="color:#FF55FF;">COLOR 13 = &amp;HFFFF55FF      FF         55         FF</span>
<span style="color:#FFFF55;">COLOR 14 = &amp;HFFFFFF55      FF         FF         55</span>
<span style="color:#F5F5F5;">COLOR 15 = &amp;HFFFFFFFF      FF         FF         FF</span>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The DAC intensity values are multiplied by (255 / 63) to get the <a href="RGB" title="RGB">_RGB</a> intensity values as <a href="HEX$" title="HEX$">hexadecimal</a> values. The individual 2 digit <a href="HEX$" title="HEX$">HEX$</a> intensity values can be added to "&amp;HFF" to make up the 32-bit hexadecimal string value necessary for <a href="VAL" title="VAL">VAL</a> to return to <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a>. The statement is only included in the example to show how that can be done with any 32-bit color value.</dd></dl>
<h3><span id="Read_.26_write_color_port_intensities_with_INP_.26_OUT"></span><span class="mw-headline" id="Read_&amp;_write_color_port_intensities_with_INP_&amp;_OUT">Read &amp; write color port intensities with <a href="INP" title="INP">INP</a> &amp; <a href="OUT" title="OUT">OUT</a></span></h3>
<ul><li>Legacy code may use <a href="INP" title="INP">INP</a> and <a href="OUT" title="OUT">OUT</a> to read or set color port intensities. <b>QB64</b> emulates VGA memory to maintain compatibility.</li>
<li>The same can be achieved using <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a> (<b>recommended practice</b>).</li></ul>
<dl><dd><b><span style="color:green;">OUT &amp;H3C7, attribute</span></b> 'Set port to read RGB settings with:</dd>
<dd><b><span style="color:green;">color_intensity = INP(&amp;H3C9)</span></b> 'reads present intensity setting</dd></dl>
<dl><dd><b><span style="color:green;">OUT &amp;H3C8, attribute</span></b> 'Set port to write RGB settings with:</dd>
<dd><b><span style="color:green;">OUT &amp;H3C9, color_intensity</span></b> 'writes new intensity setting</dd></dl>
<ul><li>After every 3 reads or writes, changes to next higher color attribute. Loops can be used to set more than one attribute's intensities.</li>
<li>Color port setting of red, green and blue intensities can be done in ascending order.</li>
<li>Color port attribute intensity values range from 0 to 63 (1/4 of the 32-bit values) in QBasic's legacy 4 and 8 bit screen modes.</li></ul>
<p style="text-align: center">(<a href="#toc">Return to Table of Contents</a>)</p>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Reading the default RGB color settings of color attribute 15.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> &amp;H3C7, 15
 red% = <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(&amp;H3C9)
 green% = <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(&amp;H3C9)
 blue% = <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(&amp;H3C9)
 <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> red%, green%, blue%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 63       63       63
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Changing the color settings of attribute 0 (the background) to blue in <a href="SCREEN" title="SCREEN">SCREENs</a> 12 or 13.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C8, 0          'set color port attribute to write
<a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 0          'red intensity
<a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 0          'green intensity
<a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 42         'blue intensity
<a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C7, 0
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9); <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9); <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt1"><span style="color:#FCFCFC;"> 0  0  42</span></pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Printing in fullscreen SCREEN 0 mode with a color background under the text only.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 0: <a href="FULLSCREEN" title="FULLSCREEN"><span style="color:#4593D8;">_FULLSCREEN</span></a> ' used for fullscreen instead of window
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 14, 6: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 4, 4: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hello!"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">
    <span style="background-color: #aa5500; color:#fcfc54;">Hello!</span>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 4:</i> Using <a href="CLS" title="CLS">CLS</a> after setting the background color in SCREEN 0 to make the color cover the entire screen.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 0: <a href="FULLSCREEN" title="FULLSCREEN"><span style="color:#4593D8;">_FULLSCREEN</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> , 7: <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 9: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hello"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt7"><span style="color:#5454fc;">Hello</span>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 5:</i> Using a different foreground color for each letter:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 0
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "H";
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 3: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "E";
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 4: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "L";
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 5: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "L";
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 6: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "O"
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 9: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "W";
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 11: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "O";
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 12: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "R";
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 13: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "L";
<a class="mw-selflink selflink"><span style="color:#4593D8;">COLOR</span></a> 14: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "D"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="color:#0000aa;">H</span><span style="color:#00aaaa;">E</span><span style="color:#aa0000;">L</span><span style="color:#aa00aa;">L</span><span style="color:#aa5500;">O</span>
<span style="color:#5454fc;">W</span><span style="color:#54fcfc;">O</span><span style="color:#fc5454;">R</span><span style="color:#fc54fc;">L</span><span style="color:#fcfc54;">D</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$COLOR" title="$COLOR">$COLOR</a> (metacommand)</li>
<li><a href="RGB" title="RGB">_RGB</a>, <a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGB32" title="RGB32">_RGB32</a>, <a href="RGBA32" title="RGBA32">RGBA32</a>.</li>
<li><a href="RED" title="RED">_RED</a>, <a href="GREEN" title="GREEN">_GREEN</a>, <a href="BLUE" title="BLUE">_BLUE</a></li>
<li><a href="RED32" title="RED32">_RED32</a>, <a href="GREEN32" title="GREEN32">_GREEN32</a>, <a href="BLUE32" title="BLUE32">_BLUE32</a></li>
<li><a href="ALPHA" title="ALPHA">_ALPHA</a>, <a href="ALPHA32" title="ALPHA32">_ALPHA32</a>, <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a></li>
<li><a href="PRINT" title="PRINT">PRINT</a>, <a href="LOCATE" title="LOCATE">LOCATE</a>, <a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="POINT" title="POINT">POINT</a>, <a href="SCREEN_(function)" title="SCREEN (function)">SCREEN (function)</a></li>
<li><a href="OUT" title="OUT">OUT</a>, <a href="INP" title="INP">INP</a>, <a href="PALETTE" title="PALETTE">PALETTE</a></li>
<li><a href="BLINK" title="BLINK">_BLINK</a></li>
<li><a href="DEFAULTCOLOR" title="DEFAULTCOLOR">_DEFAULTCOLOR</a></li>
<li><a href="BACKGROUNDCOLOR" title="BACKGROUNDCOLOR">_BACKGROUNDCOLOR</a></li>
<li><a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a></li>
<li><a href="Windows_Libraries#Color_Dialog_Box" title="Windows Libraries">Color Dialog Box</a></li>
<li><a class="external text" href="https://qb64phoenix.com/qb64wiki/resources/Color0.html" rel="nofollow">$COLOR:0 Name Table</a></li>
<li><a class="external text" href="https://qb64phoenix.com/qb64wiki/resources/Color32.html" rel="nofollow">$COLOR:32 Name Table</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714232003
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.110 seconds
Real time usage: 0.147 seconds
Preprocessor visited node count: 1179/1000000
Post‐expand include size: 8655/2097152 bytes
Template argument size: 2495/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 16/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   80.276      1 -total
 13.43%   10.779     92 Template:Cl
  8.43%    6.766     31 Template:Text
  7.70%    6.182      1 Template:PageSyntax
  5.53%    4.441      6 Template:CodeStart
  5.38%    4.321      6 Template:OutputEnd
  5.09%    4.088      6 Template:Parameter
  4.83%    3.876      1 Template:OutputStartBG1
  4.81%    3.865      1 Template:PageSeeAlso
  4.74%    3.803      4 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:416-0!canonical and timestamp 20240714232003 and revision id 8973.
 -->
</div>
</div>
</div>
</div>
</body>
</html>