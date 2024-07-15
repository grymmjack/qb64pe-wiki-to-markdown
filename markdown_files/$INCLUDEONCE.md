<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$INCLUDEONCE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_INCLUDEONCE rootpage-_INCLUDEONCE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$INCLUDEONCE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>$INCLUDEONCE</b> metacommand, when placed in include files, prevents that the file's contents is injected multiple times into a program, even if the file is <a href="$INCLUDE" title="$INCLUDE">included</a> multiple times directly or indirectly through other include files.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$INCLUDEONCE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>As QB64 <a href="Metacommand" title="Metacommand">metacommand</a> it does not require a comment <i><a href="Apostrophe" title="Apostrophe">'</a></i> or <a href="REM" title="REM">REM</a> before it.</li>
<li>It can be placed everywhere in an include file, but must be the <b>only</b> thing in the line, hence without additional whitespace or comments.
<ul><li>Even if placed in the middle or the end of the file, it always designates the <b>entire</b> file contents.</li></ul></li>
<li>If placed in the main program, <b>$INCLUDEONCE</b> does nothing and is simply ignored without error.</li>
<li><b>$INCLUDEONCE</b> will not work when placed inside pre-compiler <a href="$IF" title="$IF">$IF</a>..<a class="mw-redirect" href="$ELSE" title="$ELSE">$ELSE</a>...<a class="mw-redirect" href="$END_IF" title="$END IF">$END IF</a> blocks.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="none"><img alt="none" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>none</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.12.0"><img alt="v3.12.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.12.0</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Apix.png"><img alt="Apix.png" decoding="async" height="48" src="/qb64wiki/images/5/5f/Apix.png" width="48"/></a></div></div>
<div class="gallerytext">
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Win.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/29/Win.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
</ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd><ul><li>Show how the command prevents included code to be injected multiple times.</li>
<li>First save the include files in your qb64pe folder, then take the main program.</li></ul></dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><span style="color:#919191;">'included by test.bas and incl.bm</span>
<a class="mw-selflink selflink"><span style="color:#55FF55;">$INCLUDEONCE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This prints from file once.bm, and should appear only once on screen."</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><span style="color:#919191;">'included 2 times by test.bas</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This prints from file incl.bm, it should appear 2 times on screen."</span>
<span style="color:#919191;">'</span><a href="$INCLUDE" title="$INCLUDE"><span style="color:#55FF55;">$INCLUDE</span></a>: <span style="color:#919191;">'once.bm'</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><span style="color:#919191;">'this is a test for $INCLUDEONCE behavior</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This prints from the test.bas main program."</span>
<span style="color:#919191;">'</span><a href="$INCLUDE" title="$INCLUDE"><span style="color:#55FF55;">$INCLUDE</span></a>: <span style="color:#919191;">'incl.bm'</span>
<span style="color:#919191;">'</span><a href="$INCLUDE" title="$INCLUDE"><span style="color:#55FF55;">$INCLUDE</span></a>: <span style="color:#919191;">'once.bm'</span>
<span style="color:#919191;">'</span><a href="$INCLUDE" title="$INCLUDE"><span style="color:#55FF55;">$INCLUDE</span></a>: <span style="color:#919191;">'incl.bm'</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">This prints from the test.bas main program.
This prints from file incl.bm, it should appear 2 times on screen.
This prints from file once.bm, and should appear only once on screen.
This prints from file incl.bm, it should appear 2 times on screen.
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputplain"><b>Explanation</b>
 Even as the file <i>once.bm</i> is included 3 times into the <i>test.bas</i> program
 (2 times indirectly through <i>incl.bm</i> and 1 time directly), the contained
 PRINT statements are injected only once into the program due to the use
 of the $INCLUDEONCE metacommand.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2685" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a></li>
<li><a href="Metacommand" title="Metacommand">Metacommand</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062557
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.083 seconds
Real time usage: 0.113 seconds
Preprocessor visited node count: 297/1000000
Post‐expand include size: 2940/2097152 bytes
Template argument size: 876/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2698/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   86.358      1 -total
  7.74%    6.685      1 Template:PageAvailability
  6.38%    5.510      1 Template:PageDescription
  4.81%    4.154     18 Template:Text
  3.91%    3.374      1 Template:PageSyntax
  3.89%    3.363      1 Template:PageExamples
  3.56%    3.077      3 Template:CodeEnd
  3.47%    2.998      6 Template:Cl
  3.32%    2.867      5 Template:Cm
  3.31%    2.856      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1229-0!canonical and timestamp 20240715062557 and revision id 8947.
 -->
</div>
</div>
</div>
</div>
</body>
</html>