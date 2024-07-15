<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>REM - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-REM rootpage-REM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">REM</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>REM</b> or an apostrophe is used for programmer remarks, comments or to stop the execution of program code.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>REM program comment or ignore code</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Comments cannot be read by QBasic correctly and may cause syntax and other errors without REM!</li>
<li>Instead of REM you can use the <a class="mw-selflink selflink">'</a> symbol which can be put anywhere.</li>
<li>Code can also be commented out for program testing purposes.</li>
<li>QBasic Metacommands such as <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> and <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> require the use of REM or the apostrophe.</li></ul>
<p>
<i>Example:</i> Avoiding an END IF error.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">REM</span></a> This is a remark...
' This is also a remark...
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> a = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">REM</span></a> (REM follows syntax rules)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> a = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> '(apostrophe doesn't follow syntax rules, so use END IF after this)
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1130" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="Apostrophe" title="Apostrophe">Apostrophe</a></li>
<li><a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a>, <a href="$STATIC" title="$STATIC">$STATIC</a>, <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034203
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.021 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 66/1000000
Post‐expand include size: 962/2097152 bytes
Template argument size: 62/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   15.604      1 -total
 16.23%    2.533      1 Template:PageSyntax
 15.07%    2.352      7 Template:Cl
 14.34%    2.238      1 Template:PageDescription
 13.75%    2.145      1 Template:CodeStart
 12.34%    1.926      1 Template:PageSeeAlso
 11.34%    1.770      1 Template:CodeEnd
 11.14%    1.739      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:243-0!canonical and timestamp 20240715034203 and revision id 8889.
 -->
</div>
</div>
</div>
</div>
</body>
</html>