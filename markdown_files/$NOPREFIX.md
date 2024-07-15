<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$NOPREFIX - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_NOPREFIX rootpage-_NOPREFIX skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$NOPREFIX</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$NOPREFIX</a> metacommand allows all QB64 functions and statements to be used without the leading underscore (_).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$NOPREFIX</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>QB64-specific keywords are by default prefixed with an underscore, in order to differentiate them from legacy keywords inherited from QBasic/QuickBASIC 4.5.</li>
<li>The convention exists in order to allow older code to be loaded and compiled in QB64 without naming conflicts with existing variables or constants.</li>
<li>If you are writing new code with QB64, and <b>not importing code</b> from QBasic/QuickBASIC 4.5 nor any 3rd party .bi/.bm style libraries, then <a class="mw-selflink selflink">$NOPREFIX</a> allows you to reduce typing by not having to use underscores in modern keywords.</li></ul>
<dl><dt><span style="color:red;">!!! WARNING !!!</span></dt>
<dd>
<ul><li>Do not use <b>$NOPREFIX</b> when working with old QBasic/QuickBASIC 4.5 code or when your program depends on 3rd party library code, otherwise you risk a lot of <span style="color:red;">"Name already in use"</span> syntax errors, as the old code or libraries may use variable, SUB or FUNCTION names which conflict with new QB64 keywords if they are not prefixed with an underscore.</li>
<li>Once again, use <b>$NOPREFIX</b> only with new written QB64 code which is fully under your control without any 3rd party dependencies!</li></ul></dd></dl>
<ul><li><b>SUB _GL</b> is an internal routine and must <b>always</b> be prefixed.</li>
<li>When <a class="mw-selflink selflink">$NOPREFIX</a> is used, QB64 keywords can be used both with or without the leading underscore, so that both <a href="DISPLAY" title="DISPLAY">_DISPLAY</a> and <a href="DISPLAY" title="DISPLAY">DISPLAY</a> are valid in the same program, for example.</li>
<li><a class="mw-selflink selflink">$NOPREFIX</a> must be the first non-comment and non-whitespace line in a program.
<ul><li>Since QB64 v2.0 (incl. all QB64-PE versions) <a class="mw-selflink selflink">$NOPREFIX</a> can be placed anywhere in a program.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v1.4"><img alt="v1.4" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v1.4</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="all"><img alt="all" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>all</b>
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
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Keyword_Reference_-_Alphabetical" title="Keyword Reference - Alphabetical">Keyword Reference - Alphabetical</a></li>
<li><a href="Metacommand" title="Metacommand">Metacommand</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193331
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 37/1000000
Post‐expand include size: 686/2097152 bytes
Template argument size: 42/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2359/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.425      1 -total
 16.46%    4.680      1 Template:PageSyntax
  8.00%    2.274      1 Template:PageSeeAlso
  6.56%    1.864      1 Template:PageDescription
  5.92%    1.682      2 Template:Text
  5.44%    1.547      1 Template:PageNavigation
  5.21%    1.481      1 Template:PageAvailability
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:200-0!canonical and timestamp 20240714193331 and revision id 8497.
 -->
</div>
</div>
</div>
</div>
</body>
</html>