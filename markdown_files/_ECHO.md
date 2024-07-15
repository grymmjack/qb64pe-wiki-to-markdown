<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ECHO - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ECHO rootpage-ECHO skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ECHO</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ECHO</a> statement allows outputting text to a <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> window without having to alternate between <a href="DEST" title="DEST">_DEST</a> pages.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_ECHO</a> {<i>"text to output"</i> | <i>textVariable$</i>}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">_ECHO</a> is a shorthand to saving current <a href="DEST" title="DEST">_DEST</a>, switching to <a href="DEST" title="DEST">_DEST</a> <a href="CONSOLE" title="CONSOLE">_CONSOLE</a>, <a href="PRINT" title="PRINT">PRINTing</a>, then switching back to the previous <a href="DEST" title="DEST">_DEST</a>.</li>
<li>To output numbers, use the <a href="STR$" title="STR$">STR$</a> function.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.3 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$CONSOLE" title="$CONSOLE"><span style="color:#55FF55;">$CONSOLE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"this will show in the main window"</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_ECHO</span></a> <span style="color:#FFB100;">"this will show in the console"</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEST" title="DEST">_DEST</a></li>
<li><a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a>, <a href="CONSOLE" title="CONSOLE">_CONSOLE</a></li>
<li><a href="STR$" title="STR$">STR$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062538
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.042 seconds
Real time usage: 0.068 seconds
Preprocessor visited node count: 69/1000000
Post‐expand include size: 1007/2097152 bytes
Template argument size: 131/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 66/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.265      1 -total
 10.13%    3.270      1 Template:PageSyntax
  8.25%    2.663      1 Template:Parameter
  8.05%    2.597      2 Template:Text
  8.01%    2.584      2 Template:Cl
  7.72%    2.491      1 Template:Cm
  7.66%    2.473      1 Template:CodeStart
  7.66%    2.470      1 Template:PageDescription
  7.57%    2.443      1 Template:PageNavigation
  7.54%    2.432      1 Template:PageAvailability
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:129-0!canonical and timestamp 20240715062538 and revision id 8318.
 -->
</div>
</div>
</div>
</div>
</body>
</html>