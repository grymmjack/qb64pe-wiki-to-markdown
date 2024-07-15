<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$COLOR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_COLOR rootpage-_COLOR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$COLOR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>$COLOR</b> is a metacommand that adds named color constants into a program, which then can be used instead of hardcoded literal color values.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$COLOR</a><b>:</b>{0|32}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The one and only parameter is a literal number designating either to include <a href="SCREEN" title="SCREEN">SCREEN 0</a> based color indexes, or full <a href="RGB32" title="RGB32">_RGB32</a> color values with full (opaque) alpha.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>$COLOR:0</b> adds constants for the colors 0-15 available in <b>SCREEN 0</b>, these do also match for the first 16 colors on 8-Bit (256 colors) graphic screens as long as they are not changed using <a href="PALETTE" title="PALETTE">PALETTE</a> or <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a>. For the actual constant names see <a class="external text" href="https://qb64phoenix.com/qb64wiki/resources/Color0.html" rel="nofollow">$COLOR:0 Name Table</a>.</li>
<li><b>$COLOR:32</b> adds constants for full 32-Bit color values as used on 32-Bit screens created via <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, similar to HTML color names. For the actual constant names see <a class="external text" href="https://qb64phoenix.com/qb64wiki/resources/Color32.html" rel="nofollow">$COLOR:32 Name Table</a>.</li>
<li>Prior to QB64-PE v0.5.0, <b>$COLOR</b> was not compatible with <a href="$NOPREFIX" title="$NOPREFIX">$NOPREFIX</a>.</li>
<li>Since QB64-PE v0.5.0, <b>$COLOR</b> can now be used with <a href="$NOPREFIX" title="$NOPREFIX">$NOPREFIX</a>, with a few notable differences to three conflicting colors -- Red, Green, Blue.</li></ul>
<dl><dd>Red would conflict with <a href="RED" title="RED">_RED</a>, Green would conflict with <a href="GREEN" title="GREEN">_GREEN</a>, and Blue would conflict with <a href="BLUE" title="BLUE">_BLUE</a>, once the underscore was removed from those commands with <a href="$NOPREFIX" title="$NOPREFIX">$NOPREFIX</a>.</dd>
<dd></dd>
<dd>To prevent these conflicts, the <a href="COLOR" title="COLOR">COLOR</a> values have had <b>NP_</b> prepended to the front of them, to distinguish them from the non-prefixed command names.  All other color names remain the same, with only the three colors in conflict having to use <b>NP_</b> (for <b>N</b>o <b>P</b>refix) in front of them.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Adding named color constants for SCREEN 0.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#55FF55;">$COLOR</span></a>:<span style="color:#F580B1;">0</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> BrightWhite, Red
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Bright white on red."</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="background-color: #aa0000; color:#ffffff;">Bright white on red.</span>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Adding named color constants for 32-bit modes.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">400</span>, <span style="color:#F580B1;">32</span>)
<a class="mw-selflink selflink"><span style="color:#55FF55;">$COLOR</span></a>:<span style="color:#F580B1;">32</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> CrayolaGold, DarkCyan
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"CrayolaGold on DarkCyan."</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="background-color: #008B8B; color:#E7C697;">CrayolaGold on DarkCyan.</span>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 3</dt>
<dd>Adding named color constants for 32-bit modes (with $NOPREFIX in effect).</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$NOPREFIX" title="$NOPREFIX"><span style="color:#55FF55;">$NOPREFIX</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">400</span>, <span style="color:#F580B1;">32</span>)
<a class="mw-selflink selflink"><span style="color:#55FF55;">$COLOR</span></a>:<span style="color:#F580B1;">32</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> NP_Red, White <span style="color:#919191;">'notice the NP_ in front of Red?</span>
<span style="color:#919191;">'This is to distinguish the color from the command with $NOPREFIX.</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Red on White."</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="background-color: #ffffff; color:#ff0000;">Red on White.</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="COLOR" title="COLOR">COLOR</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></li>
<li><a href="Metacommand" title="Metacommand">Metacommand</a></li>
<li><a class="external text" href="https://qb64phoenix.com/qb64wiki/resources/Color0.html" rel="nofollow">$COLOR:0 Name Table</a></li>
<li><a class="external text" href="https://qb64phoenix.com/qb64wiki/resources/Color32.html" rel="nofollow">$COLOR:32 Name Table</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193331
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.042 seconds
Preprocessor visited node count: 278/1000000
Post‐expand include size: 2725/2097152 bytes
Template argument size: 560/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 161/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.250      1 -total
  8.43%    2.129      3 Template:OutputStartBG0
  7.62%    1.924     14 Template:Text
  7.43%    1.875      3 Template:Ot
  7.06%    1.783     10 Template:Cl
  6.82%    1.721      1 Template:PageSyntax
  6.66%    1.681      1 Template:PageSeeAlso
  6.23%    1.572      1 Template:PageExamples
  5.96%    1.506      4 Template:Cm
  5.87%    1.481      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:91-0!canonical and timestamp 20240714193331 and revision id 8975.
 -->
</div>
</div>
</div>
</div>
</body>
</html>