<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_BLEND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BLEND rootpage-BLEND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_BLEND</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_BLEND</a> statement turns on 32 bit alpha blending for an image or screen mode and is on by default.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_BLEND</a> [<i>imageHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>imageHandle&amp;</i> refers to an image in memory. If not specified, the current destination page (See <a href="DEST" title="DEST">_DEST</a>) is affected.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Alpha blending is on by default when loading a .PNG image to a 32-bit surface.</li>
<li>Normally it is used to turn blending on after a previous <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> call.</li>
<li><a class="mw-selflink selflink">_BLEND</a> can only be used on 32-bit surfaces, otherwise it will produce the error <a href="ERROR_Codes" title="ERROR Codes">Illegal Function Call</a>.</li>
<li><b>Note: <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> is faster than the default <a class="mw-selflink selflink">_BLEND</a> unless you really need to use it in 32 bit.</b></li>
<li><b>32 bit screen surface backgrounds (black) have zero <a href="ALPHA" title="ALPHA">_ALPHA</a> so that they are transparent when placed over other surfaces.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
<span style="color:#919191;">'CLS , _RGB(128, 128, 128) 'change background color for other results</span>
<a href="DONTBLEND" title="DONTBLEND"><span style="color:#4593D8;">_DONTBLEND</span></a>
bg&amp; = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RED" title="RED"><span style="color:#4593D8;">_RED</span></a>(bg&amp;), <a href="GREEN" title="GREEN"><span style="color:#4593D8;">_GREEN</span></a>(bg&amp;), <a href="BLUE" title="BLUE"><span style="color:#4593D8;">_BLUE</span></a>(bg&amp;), <a href="ALPHA" title="ALPHA"><span style="color:#4593D8;">_ALPHA</span></a>(bg&amp;)
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">100</span>, <span style="color:#F580B1;">100</span>)-(<span style="color:#F580B1;">200</span>, <span style="color:#F580B1;">200</span>), <a href="RGBA32" title="RGBA32"><span style="color:#4593D8;">_RGBA32</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">128</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">128</span>), BF
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">440</span>, <span style="color:#F580B1;">100</span>)-(<span style="color:#F580B1;">540</span>, <span style="color:#F580B1;">200</span>), <a href="RGBA32" title="RGBA32"><span style="color:#4593D8;">_RGBA32</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">64</span>), BF
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(<span style="color:#F580B1;">1</span>)
<a class="mw-selflink selflink"><span style="color:#4593D8;">_BLEND</span></a>
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">270</span>, <span style="color:#F580B1;">300</span>)-(<span style="color:#F580B1;">370</span>, <span style="color:#F580B1;">400</span>), <a href="RGBA32" title="RGBA32"><span style="color:#4593D8;">_RGBA32</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">128</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">128</span>), BF
m&amp; = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(<span style="color:#F580B1;">303</span>, <span style="color:#F580B1;">302</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RED" title="RED"><span style="color:#4593D8;">_RED</span></a>(m&amp;), <a href="GREEN" title="GREEN"><span style="color:#4593D8;">_GREEN</span></a>(m&amp;), <a href="BLUE" title="BLUE"><span style="color:#4593D8;">_BLUE</span></a>(m&amp;), <a href="ALPHA" title="ALPHA"><span style="color:#4593D8;">_ALPHA</span></a>(m&amp;)
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(<span style="color:#F580B1;">1</span>)
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">270</span>, <span style="color:#F580B1;">300</span>)-(<span style="color:#F580B1;">370</span>, <span style="color:#F580B1;">400</span>), <a href="RGBA32" title="RGBA32"><span style="color:#4593D8;">_RGBA32</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">64</span>), BF
m&amp; = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(<span style="color:#F580B1;">303</span>, <span style="color:#F580B1;">302</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RED" title="RED"><span style="color:#4593D8;">_RED</span></a>(m&amp;), <a href="GREEN" title="GREEN"><span style="color:#4593D8;">_GREEN</span></a>(m&amp;), <a href="BLUE" title="BLUE"><span style="color:#4593D8;">_BLUE</span></a>(m&amp;), <a href="ALPHA" title="ALPHA"><span style="color:#4593D8;">_ALPHA</span></a>(m&amp;)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a>, <a href="BLEND_(function)" title="BLEND (function)">_BLEND (function)</a></li>
<li><a href="Images" title="Images">Images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714200849
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.048 seconds
Real time usage: 0.056 seconds
Preprocessor visited node count: 567/1000000
Post‐expand include size: 4117/2097152 bytes
Template argument size: 832/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 69/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   34.894      1 -total
 11.96%    4.174     44 Template:Text
 11.00%    3.837     32 Template:Cl
  7.71%    2.689      1 Template:CodeEnd
  7.40%    2.583      1 Template:PageSyntax
  7.17%    2.502      2 Template:Parameter
  6.56%    2.289      1 Template:PageExamples
  6.55%    2.284      1 Template:PageParameters
  6.07%    2.117      1 Template:PageSeeAlso
  5.91%    2.063      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:54-0!canonical and timestamp 20240714200849 and revision id 8270.
 -->
</div>
</div>
</div>
</div>
</body>
</html>