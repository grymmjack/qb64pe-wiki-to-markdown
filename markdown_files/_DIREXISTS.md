<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DIREXISTS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DIREXISTS rootpage-DIREXISTS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DIREXISTS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DIREXISTS</a> function determines if a designated file path or folder exists and returns true (-1) or false (0).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>dirExists%</i> = <a class="mw-selflink selflink">_DIREXISTS</a>(<i>filepath$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>filepath$</i> parameter can be a literal or variable <a href="STRING" title="STRING">string</a> path value.</li>
<li>The function returns -1 when a path or folder exists and 0 when it does not.</li>
<li>The function reads the system information directly without using a <a href="SHELL" title="SHELL">SHELL</a> procedure.</li>
<li>The function will use the appropriate Operating System path separators. <a href="OS$" title="OS$">_OS$</a> can determine the operating system.</li>
<li><b>This function does not guarantee that a path can be accessed, only that it exists.</b></li>
<li><b>NOTE: Checking if a folder exists in a CD drive may cause the tray to open automatically to request a disk when empty.</b> To find drives in Windows, use this API Library: <a href="Windows_Libraries#Disk_Drives" title="Windows Libraries">Disk Drives</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Checks if a folder exists before proceeding.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIREXISTS</span></a>(<span style="color:#FFB100;">"internal\temp"</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Folder found."</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a></li>
<li><a href="SHELL" title="SHELL">SHELL</a></li>
<li><a href="OS$" title="OS$">_OS$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062323
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.055 seconds
Preprocessor visited node count: 88/1000000
Post‐expand include size: 1089/2097152 bytes
Template argument size: 164/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 30/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.446      1 -total
 36.08%   12.069      1 Template:PageNavigation
  8.61%    2.880      1 Template:PageSyntax
  7.81%    2.611      3 Template:Parameter
  7.22%    2.416      1 Template:PageSeeAlso
  6.93%    2.319      1 Template:PageDescription
  6.33%    2.116      5 Template:Cl
  5.98%    2.001      1 Template:CodeStart
  5.94%    1.985      1 Template:PageExamples
  5.66%    1.892      2 Template:Text
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:122-0!canonical and timestamp 20240715062323 and revision id 8620.
 -->
</div>
</div>
</div>
</div>
</body>
</html>