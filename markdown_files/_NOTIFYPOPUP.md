<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_NOTIFYPOPUP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-NOTIFYPOPUP rootpage-NOTIFYPOPUP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_NOTIFYPOPUP</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_NOTIFYPOPUP</b> statement shows a system notification.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>_NOTIFYPOPUP</b> [<i>title$</i>][, <i>message$</i>][, <i>iconType$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>title$</i> is the notification title (usually appears above message and in bold)</li>
<li><i>message$</i> is the notification message</li>
<li><i>iconType$</i> is the notification icon type (this can be <b>"info"</b>, <b>"warning"</b>, or <b>"error"</b>)</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All parameters are optional</li>
<li>Not using any parameters will show a blank notification</li>
<li>The notification popup will show where OS notifications are expected / configured by the system</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64-PE v3.4.0 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Show a system notification after completing a lengthy task</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_NOTIFYPOPUP</span></a> "My Cool App", "Conversion complete!", "info"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2843" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="MESSAGEBOX" title="MESSAGEBOX">_MESSAGEBOX</a></li>
<li><a href="MESSAGEBOX_(function)" title="MESSAGEBOX (function)">_MESSAGEBOX (function)</a></li>
<li><a href="INPUTBOX$" title="INPUTBOX$">_INPUTBOX$</a></li>
<li><a href="SELECTFOLDERDIALOG$" title="SELECTFOLDERDIALOG$">_SELECTFOLDERDIALOG$</a></li>
<li><a href="COLORCHOOSERDIALOG" title="COLORCHOOSERDIALOG">_COLORCHOOSERDIALOG</a></li>
<li><a href="OPENFILEDIALOG$" title="OPENFILEDIALOG$">_OPENFILEDIALOG$</a></li>
<li><a href="SAVEFILEDIALOG$" title="SAVEFILEDIALOG$">_SAVEFILEDIALOG$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714214356
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 58/1000000
Post‐expand include size: 865/2097152 bytes
Template argument size: 70/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.564      1 -total
 11.68%    2.051      1 Template:PageSyntax
  9.38%    1.648      6 Template:Parameter
  8.85%    1.555      1 Template:PageNavigation
  8.36%    1.469      1 Template:Cl
  8.36%    1.469      1 Template:CodeStart
  8.30%    1.458      1 Template:PageParameters
  8.23%    1.446      1 Template:PageExamples
  7.99%    1.403      1 Template:PageDescription
  7.96%    1.398      1 Template:PageAvailability
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1161-0!canonical and timestamp 20240714214356 and revision id 9022.
 -->
</div>
</div>
</div>
</div>
</body>
</html>