<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_OPENFILEDIALOG$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OPENFILEDIALOG rootpage-OPENFILEDIALOG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_OPENFILEDIALOG$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_OPENFILEDIALOG$</b> function displays a standard dialog box that prompts the user to open a file. The returned string is an empty string (<b>""</b>) if the user cancelled. The returned string will contain file paths delimited using <b>"|"</b> if allowMultipleSelects&amp; is passed as <b>-1</b> (true) and multiple files are selected by the user.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">_OPENFILEDIALOG$</a>([<i>title$</i>][, <i>defaultPathAndFile$</i>][, <i>filterPatterns$</i>][, <i>singleFilterDescription$</i>][, <i>allowMultipleSelects&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>title$</i> is the dialog box title</li>
<li><i>defaultPathAndFile$</i> is the default path that will be used by the dialog box if not changed by the user</li>
<li><i>filterPatterns$</i> are the file filters separated using <b>"|"</b> (e.g., "*.png|*.jpg|*.gif")</li>
<li><i>singleFilterDescription$</i> is the single filter description (e.g., "Image files")</li>
<li><i>allowMultipleSelects&amp;</i> can be <b>0</b> (false) or <b>-1</b> (true) if multiple file selection is to be allowed. If omitted, then this defaults to <b>0</b> (false)</li></ul>
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
<dd>Simple open file dialog example</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">audiofiles$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_OPENFILEDIALOG$</span></a>("Open File", "", "*.mp3|*.ogg|*.wav|*.flac", "Audio files", -1)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> audiofiles$ &lt;&gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> "Information", "You selected " + audiofiles$
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
<li><a href="SAVEFILEDIALOG$" title="SAVEFILEDIALOG$">_SAVEFILEDIALOG$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062615
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 107/1000000
Post‐expand include size: 1228/2097152 bytes
Template argument size: 282/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.303      1 -total
 12.25%    2.978     13 Template:Parameter
 12.16%    2.956      4 Template:Cl
 10.21%    2.481      1 Template:PageSyntax
  7.87%    1.913      1 Template:PageSeeAlso
  7.76%    1.887      1 Template:PageParameters
  7.58%    1.842      1 Template:PageDescription
  7.31%    1.777      1 Template:CodeEnd
  7.24%    1.760      1 Template:PageExamples
  7.23%    1.758      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1166-0!canonical and timestamp 20240715062615 and revision id 8452.
 -->
</div>
</div>
</div>
</div>
</body>
</html>