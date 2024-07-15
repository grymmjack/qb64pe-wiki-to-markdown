<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_COLORCHOOSERDIALOG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-COLORCHOOSERDIALOG rootpage-COLORCHOOSERDIALOG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_COLORCHOOSERDIALOG</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_COLORCHOOSERDIALOG</b> function displays a standard color picker dialog box. It returns a 32-bit RGBA color with the alpha channel set to &amp;HFF (255). A zero is returned if the user cancelled.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>color32bpp~&amp;</i> = <a class="mw-selflink selflink">_COLORCHOOSERDIALOG</a>([<i>title$</i>][, <i>defaultRGB~&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>title$</i> is the dialog box title</li>
<li><i>defaultRGB~&amp;</i> is the default 32-bit RGB color that is pre-selected</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>title$</i> accepts an empty string (<b>""</b>) in which case system defaults are used</li>
<li>The dialog box automatically becomes a modal window if the application window is visible</li>
<li><i>defaultRGB~&amp;</i> may be ignored on some platforms</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64-PE v3.4.0 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Color selection</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">mycolor~&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_COLORCHOOSERDIALOG</span></a>(<span style="color:#FFB100;">"Select a color"</span>, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>))
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> mycolor~&amp; &lt;&gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> <span style="color:#FFB100;">"Information"</span>, <span style="color:#FFB100;">"You selected "</span> + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(mycolor~&amp;)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="NOTIFYPOPUP" title="NOTIFYPOPUP">_NOTIFYPOPUP</a></li>
<li><a href="MESSAGEBOX" title="MESSAGEBOX">_MESSAGEBOX</a></li>
<li><a href="MESSAGEBOX_(function)" title="MESSAGEBOX (function)">_MESSAGEBOX (function)</a></li>
<li><a href="INPUTBOX$" title="INPUTBOX$">_INPUTBOX$</a></li>
<li><a href="SELECTFOLDERDIALOG$" title="SELECTFOLDERDIALOG$">_SELECTFOLDERDIALOG$</a></li>
<li><a href="OPENFILEDIALOG$" title="OPENFILEDIALOG$">_OPENFILEDIALOG$</a></li>
<li><a href="SAVEFILEDIALOG$" title="SAVEFILEDIALOG$">_SAVEFILEDIALOG$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062615
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 155/1000000
Post‐expand include size: 1524/2097152 bytes
Template argument size: 317/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 44/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   26.855      1 -total
  8.70%    2.338      6 Template:Cl
  8.60%    2.310      1 Template:PageSyntax
  8.51%    2.285      7 Template:Text
  8.19%    2.199      7 Template:Parameter
  7.79%    2.093      1 Template:CodeEnd
  7.36%    1.977      1 Template:PageDescription
  7.34%    1.972      1 Template:PageParameters
  7.33%    1.968      1 Template:CodeStart
  7.13%    1.915      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1168-0!canonical and timestamp 20240715062614 and revision id 8449.
 -->
</div>
</div>
</div>
</div>
</body>
</html>