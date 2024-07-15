<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FONTWIDTH - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FONTWIDTH rootpage-FONTWIDTH skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FONTWIDTH</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_FONTWIDTH</a> function returns the font width of a MONOSPACE font handle created by <a href="LOADFONT" title="LOADFONT">_LOADFONT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixelWidth%</i> = <a class="mw-selflink selflink">_FONTWIDTH</a>[(<i>fontHandle&amp;</i>)]</dd></dl>
<p>
</p>
<ul><li>Returns the character width of the last font used if a handle is not specified.</li>
<li><b>Variable width fonts always return <i>pixelWidth%</i> = 0.</b> Even fixed width fonts return 0 unless the <a href="LOADFONT" title="LOADFONT">"MONOSPACE"</a> style option is used.</li>
<li>QB64 <b>version 1.000 and up</b> can load a variable width font as monospaced with the <a href="LOADFONT" title="LOADFONT">"MONOSPACE"</a> style parameter.</li>
<li>The font width is generally 3/4 of the <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a> specified when loading the font.</li>
<li>In <b>graphics</b> <a href="SCREEN" title="SCREEN">screen</a> modes, <a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a> can return the total <b>pixel width</b> of a literal or variable <a href="STRING" title="STRING">string</a> of text.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1145" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a></li>
<li><a href="FONT" title="FONT">_FONT</a></li>
<li><a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li>
<li><a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192719
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.014 seconds
Real time usage: 0.018 seconds
Preprocessor visited node count: 22/1000000
Post‐expand include size: 550/2097152 bytes
Template argument size: 33/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    7.369      1 -total
 26.79%    1.974      1 Template:PageSyntax
 24.42%    1.799      3 Template:Parameter
 22.20%    1.636      1 Template:PageNavigation
 21.98%    1.620      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:148-0!canonical and timestamp 20240714192719 and revision id 8894.
 -->
</div>
</div>
</div>
</div>
</body>
</html>