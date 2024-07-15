<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$SCREENHIDE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_SCREENHIDE rootpage-_SCREENHIDE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$SCREENHIDE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$SCREENHIDE</a> <a href="Metacommand" title="Metacommand">metacommand</a> can be used to hide the main program window throughout a program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$SCREENHIDE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>$SCREENHIDE may be used at the start of a program to hide the main program window when using a <a href="$CONSOLE" title="$CONSOLE">console</a> window.</li>
<li>The <a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a> statement must be used before <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a> can be used in sections of a program.</li>
<li><b>QB64 <a href="Metacommand" title="Metacommand">metacommands</a> cannot be commented out with <a href="Apostrophe" title="Apostrophe">apostrophe</a> or <a href="REM" title="REM">REM</a></b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Hiding a program when displaying a message box in Windows.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">$SCREENHIDE</span></a>
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE DYNAMIC LIBRARY</span></a> "user32"
  <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> MessageBoxA&amp; (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> hWnd%&amp;, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> lpText%&amp;, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> lpCaption%&amp;, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> uType~&amp;)
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">END DECLARE</span></a>
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE DYNAMIC LIBRARY</span></a> "kernel32"
  <a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> ExitProcess (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> uExitCode~&amp;)
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">END DECLARE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> s0 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> s1 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
s0 = "Text" + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0)
s1 = "Caption" + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0)
ExitProcess MessageBoxA(0, <a href="OFFSET_(function)" title="OFFSET (function)"><span style="color:#4593D8;">_OFFSET</span></a>(s0), <a href="OFFSET_(function)" title="OFFSET (function)"><span style="color:#4593D8;">_OFFSET</span></a>(s1), 0)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a>, <a href="$SCREENSHOW" title="$SCREENSHOW">$SCREENSHOW</a></li>
<li><a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a>, <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a></li>
<li><a href="CONSOLE" title="CONSOLE">_CONSOLE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061217
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.062 seconds
Preprocessor visited node count: 179/1000000
Post‐expand include size: 2028/2097152 bytes
Template argument size: 355/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   46.897      1 -total
 27.23%   12.770      1 Template:CodeEnd
 25.56%   11.987      1 Template:Small
 10.83%    5.079      1 Template:PageSeeAlso
  7.80%    3.658     22 Template:Cl
  6.66%    3.125      1 Template:PageExamples
  5.42%    2.543      1 Template:PageSyntax
  4.66%    2.185      1 Template:CodeStart
  3.70%    1.736      1 Template:PageNavigation
  3.56%    1.668      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:266-0!canonical and timestamp 20240715061217 and revision id 8791.
 -->
</div>
</div>
</div>
</div>
</body>
</html>