<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DESKTOPHEIGHT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DESKTOPHEIGHT rootpage-DESKTOPHEIGHT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DESKTOPHEIGHT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DESKTOPHEIGHT</a> function returns the height of the users current desktop.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>y&amp;</i> = <a class="mw-selflink selflink">_DESKTOPHEIGHT</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>No parameters are needed for this function.</li>
<li>This returns the height of the user's desktop, not the size of any screen or window which might be open on that desktop.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.0 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">s&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">800</span>, <span style="color:#F580B1;">600</span>, <span style="color:#F580B1;">256</span>)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> s&amp;
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="DESKTOPWIDTH" title="DESKTOPWIDTH"><span style="color:#4593D8;">_DESKTOPWIDTH</span></a>, <a class="mw-selflink selflink"><span style="color:#4593D8;">_DESKTOPHEIGHT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> This will print the size of the user desktop (for example <i>1920, 1080</i> for a standard hdmi monitor), and then the size of the current <a href="SCREEN" title="SCREEN">screen</a> (800, 600).</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="HEIGHT" title="HEIGHT">_HEIGHT</a>, <a href="DESKTOPWIDTH" title="DESKTOPWIDTH">_DESKTOPWIDTH</a></li>
<li><a href="WIDTH" title="WIDTH">_WIDTH</a>, <a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062317
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 105/1000000
Post‐expand include size: 1283/2097152 bytes
Template argument size: 173/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   44.925      1 -total
 40.50%   18.193      1 Template:PageSeeAlso
  7.26%    3.260      1 Template:PageSyntax
  6.62%    2.975      8 Template:Cl
  6.51%    2.925      1 Template:PageNavigation
  5.94%    2.668      3 Template:Text
  5.45%    2.446      1 Template:PageExamples
  5.35%    2.405      1 Template:CodeStart
  5.25%    2.359      1 Template:PageAvailability
  5.07%    2.276      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:114-0!canonical and timestamp 20240715062317 and revision id 8305.
 -->
</div>
</div>
</div>
</div>
</body>
</html>