<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_STARTDIR$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STARTDIR rootpage-STARTDIR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_STARTDIR$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_STARTDIR$</a> function returns the path a user called a QB64 program from as a string value without a trailing path separator.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>callPath$</i> = <a class="mw-selflink selflink">_STARTDIR$</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns a <a href="STRING" title="STRING">STRING</a> representing the user's program calling path.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.0 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Showcasing QB64 path functions:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$CONSOLE" title="$CONSOLE"><span style="color:#4593D8;">$CONSOLE</span></a>:ONLY
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <a href="CONSOLE" title="CONSOLE"><span style="color:#4593D8;">_CONSOLE</span></a>
<a href="SHELL" title="SHELL"><span style="color:#4593D8;">SHELL</span></a> "cd"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CWD$" title="CWD$"><span style="color:#4593D8;">_CWD$</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_STARTDIR$</span></a>
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CWD$" title="CWD$">_CWD$</a></li>
<li><a href="SHELL" title="SHELL">SHELL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192915
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.022 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 96/1000000
Post‐expand include size: 1323/2097152 bytes
Template argument size: 138/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.536      1 -total
 11.30%    2.320      1 Template:Small
 11.27%    2.314      9 Template:Cl
  9.44%    1.938      1 Template:PageSyntax
  8.87%    1.821      1 Template:PageSeeAlso
  8.23%    1.690      1 Template:CodeEnd
  7.77%    1.596      1 Template:Parameter
  7.41%    1.521      1 Template:CodeStart
  7.40%    1.519      1 Template:PageDescription
  7.29%    1.498      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:353-0!canonical and timestamp 20240714192915 and revision id 8621.
 -->
</div>
</div>
</div>
</div>
</body>
</html>