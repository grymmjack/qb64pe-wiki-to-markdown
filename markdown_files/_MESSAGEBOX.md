<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MESSAGEBOX - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MESSAGEBOX rootpage-MESSAGEBOX skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MESSAGEBOX</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_MESSAGEBOX</b> statement displays a message dialog box, which presents a message to the user.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>_MESSAGEBOX</b> [<i>title$</i>][, <i>message$</i>][, <i>iconType$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>title$</i> is the dialog box title</li>
<li><i>message$</i> is the dialog box message</li>
<li><i>iconType$</i> is the icon type that is displayed inside the dialog box (this can be <b>"info"</b>, <b>"warning"</b>, or <b>"error"</b>)</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All parameters are optional</li>
<li>Not using any parameters will show a blank dialog box with an OK button</li>
<li>The dialog box automatically becomes a modal window if the application window is visible</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64-PE v3.4.0 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Hello, world with common dialogs</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">username$ = <a href="INPUTBOX$" title="INPUTBOX$"><span style="color:#4593D8;">_INPUTBOX$</span></a>("Hello App", "Enter your name:", "anonymous")
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> username$ &lt;&gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MESSAGEBOX</span></a> "Hello App", "Hello " + username$, "info"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="NOTIFYPOPUP" title="NOTIFYPOPUP">_NOTIFYPOPUP</a></li>
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
Cached time: 20240715062612
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.039 seconds
Preprocessor visited node count: 79/1000000
Post‐expand include size: 1018/2097152 bytes
Template argument size: 100/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.777      1 -total
  9.95%    2.365      1 Template:PageSyntax
  9.05%    2.153      1 Template:CodeStart
  8.99%    2.138      4 Template:Cl
  8.84%    2.101      6 Template:Parameter
  8.63%    2.053      1 Template:PageParameters
  8.39%    1.995      1 Template:PageNavigation
  8.26%    1.965      1 Template:PageSeeAlso
  8.14%    1.936      1 Template:PageAvailability
  8.12%    1.931      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1162-0!canonical and timestamp 20240715062612 and revision id 9017.
 -->
</div>
</div>
</div>
</div>
</body>
</html>