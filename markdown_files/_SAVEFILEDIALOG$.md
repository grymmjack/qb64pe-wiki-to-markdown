<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SAVEFILEDIALOG$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SAVEFILEDIALOG rootpage-SAVEFILEDIALOG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SAVEFILEDIALOG$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_SAVEFILEDIALOG$</b> function displays a standard dialog box that prompts the user to save a file. The returned string is an empty string (<b>""</b>) if the user cancelled.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">_SAVEFILEDIALOG$</a>([<i>title$</i>][, <i>defaultPathAndFile$</i>][, <i>filterPatterns$</i>][, <i>singleFilterDescription$</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>title$</i> is the dialog box title</li>
<li><i>defaultPathAndFile$</i> is the default path that will be used by the dialog box if not changed by the user</li>
<li><i>filterPatterns$</i> are the file filters separated using <b>"|"</b> (e.g., "*.png|*.jpg|*.gif")</li>
<li><i>singleFilterDescription$</i> is the single filter description (e.g., "Image files")</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All parameters accept an empty string (<b>""</b>) in which case system defaults are used</li>
<li>If <i>singleFilterDescription$</i> is an empty string (<b>""</b>), then <i>filterPatterns$</i> will be shown in it's place</li>
<li>The dialog box automatically becomes a modal window if the application window is visible</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64-PE v3.4.0 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Simple save file dialog example</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> filesaved&amp; <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    textfile$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SAVEFILEDIALOG$</span></a>("Save File", "", "*.txt|*.doc", "Text files")
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> textfile$ &lt;&gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        filesaved&amp; = -1
        <a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> "Information", "File will be saved to " + textfile$
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
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
<li><a href="COLORCHOOSERDIALOG" title="COLORCHOOSERDIALOG">_COLORCHOOSERDIALOG</a></li>
<li><a href="OPENFILEDIALOG$" title="OPENFILEDIALOG$">_OPENFILEDIALOG$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062616
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.034 seconds
Preprocessor visited node count: 134/1000000
Post‐expand include size: 1425/2097152 bytes
Template argument size: 282/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.784      1 -total
 11.43%    2.376     11 Template:Parameter
 10.48%    2.178      1 Template:PageSyntax
  9.35%    1.944      1 Template:PageParameters
  9.00%    1.871      9 Template:Cl
  8.18%    1.701      1 Template:PageAvailability
  8.15%    1.693      1 Template:PageDescription
  7.71%    1.603      1 Template:PageExamples
  7.21%    1.499      1 Template:CodeStart
  6.41%    1.332      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1167-0!canonical and timestamp 20240715062616 and revision id 8453.
 -->
</div>
</div>
</div>
</div>
</body>
</html>