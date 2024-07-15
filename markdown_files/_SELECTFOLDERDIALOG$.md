<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SELECTFOLDERDIALOG$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SELECTFOLDERDIALOG rootpage-SELECTFOLDERDIALOG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SELECTFOLDERDIALOG$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_SELECTFOLDERDIALOG$</b> function displays a dialog box that enables the user to select a folder (directory). The returned string is a folder path or an empty string (<b>""</b>) if the user cancelled.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>folder$</i> = <a class="mw-selflink selflink">_SELECTFOLDERDIALOG$</a>([<i>title$</i>][, <i>defaultPath$</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>title$</i> is a string that is displayed above the folder tree view in the dialog box</li>
<li><i>defaultPath$</i> is the default folder that is pre-selected (if the folder exists)</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All parameters accept an empty string (<b>""</b>) in which case system defaults are used</li>
<li>Use the title$ to specify instructions to the user</li>
<li>The dialog box automatically becomes a modal window if the application window is visible</li>
<li>The folder selected must exist in the filesystem else an empty string is returned</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64-PE v3.4.0 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Folder selection</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">folder$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SELECTFOLDERDIALOG$</span></a>("Select a folder to scan:")
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> folder$ &lt;&gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> "Information", "You selected " + folder$
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="NOTIFYPOPUP" title="NOTIFYPOPUP">_NOTIFYPOPUP</a></li>
<li><a href="MESSAGEBOX" title="MESSAGEBOX">_MESSAGEBOX</a></li>
<li><a href="MESSAGEBOX_(function)" title="MESSAGEBOX (function)">_MESSAGEBOX (function)</a></li>
<li><a href="INPUTBOX$" title="INPUTBOX$">_INPUTBOX$</a></li>
<li><a href="COLORCHOOSERDIALOG" title="COLORCHOOSERDIALOG">_COLORCHOOSERDIALOG</a></li>
<li><a href="OPENFILEDIALOG$" title="OPENFILEDIALOG$">_OPENFILEDIALOG$</a></li>
<li><a href="SAVEFILEDIALOG$" title="SAVEFILEDIALOG$">_SAVEFILEDIALOG$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062614
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.045 seconds
Preprocessor visited node count: 75/1000000
Post‐expand include size: 1031/2097152 bytes
Template argument size: 117/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.108      1 -total
 15.46%    4.191      1 Template:PageSeeAlso
  9.60%    2.603      1 Template:CodeStart
  9.13%    2.475      4 Template:Cl
  8.09%    2.192      1 Template:PageSyntax
  8.07%    2.189      1 Template:PageAvailability
  7.94%    2.153      1 Template:PageExamples
  7.78%    2.108      1 Template:CodeEnd
  7.57%    2.052      5 Template:Parameter
  7.37%    1.997      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1164-0!canonical and timestamp 20240715062614 and revision id 8448.
 -->
</div>
</div>
</div>
</div>
</body>
</html>