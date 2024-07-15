<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CONSOLETITLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CONSOLETITLE rootpage-CONSOLETITLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CONSOLETITLE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CONSOLETITLE</a> statement creates the title of the console window using a literal or variable <a href="STRING" title="STRING">string</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_CONSOLETITLE</a> <i>text$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>text$</i> used can be a literal or variable <a href="STRING" title="STRING">STRING</a> value.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Hiding the main program window while displaying the console window with a title.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$SCREENHIDE" title="$SCREENHIDE"><span style="color:#55FF55;">$SCREENHIDE</span></a>
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">4</span>
<a href="$CONSOLE" title="$CONSOLE"><span style="color:#55FF55;">$CONSOLE</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CONSOLETITLE</span></a> <span style="color:#FFB100;">"Error Log"</span>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <a href="CONSOLE" title="CONSOLE"><span style="color:#4593D8;">_CONSOLE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Errors go here! (fyi, this line is not an error)"</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> You can also use <a href="SHELL" title="SHELL">SHELL</a> "title consoletitle" to set the title of the console window. However, <b>the recommended practice is to use <a class="mw-selflink selflink">_CONSOLETITLE</a></b>.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a>, <a href="CONSOLE" title="CONSOLE">_CONSOLE</a></li>
<li><a href="$SCREENHIDE" title="$SCREENHIDE">$SCREENHIDE</a>, <a href="$SCREENSHOW" title="$SCREENSHOW">$SCREENSHOW</a></li>
<li><a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a>, <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062304
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.077 seconds
Preprocessor visited node count: 108/1000000
Post‐expand include size: 1282/2097152 bytes
Template argument size: 213/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 61/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   51.353      1 -total
 19.11%    9.815      1 Template:CodeStart
 12.80%    6.572      1 Template:PageNavigation
 10.35%    5.317      1 Template:PageDescription
  9.82%    5.042      2 Template:Cm
  7.14%    3.665      1 Template:PageExamples
  6.89%    3.541      3 Template:Text
  6.78%    3.483      1 Template:PageSeeAlso
  6.10%    3.135      6 Template:Cl
  5.95%    3.057      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:99-0!canonical and timestamp 20240715062304 and revision id 8292.
 -->
</div>
</div>
</div>
</div>
</body>
</html>