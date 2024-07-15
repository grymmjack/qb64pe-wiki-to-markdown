<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FREETIMER - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FREETIMER rootpage-FREETIMER skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FREETIMER</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_FREETIMER</a> function returns a free <a href="TIMER" title="TIMER">TIMER</a> number for multiple <a href="ON_TIMER(n)" title="ON TIMER(n)">ON TIMER(n)</a> events.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>timerhandle%</i> = <a class="mw-selflink selflink">_FREETIMER</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>QB64 can use an unlimited number of ON TIMER (number, seconds!) event <a href="INTEGER" title="INTEGER">INTEGER</a> values at once.</li>
<li>Every time _FREETIMER is called the <a href="INTEGER" title="INTEGER">INTEGER</a> value returned will increase by one, starting at 1, whether it is used or not.</li>
<li>Store multiple returns in different variable names to refer to separate events later.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON_TIMER(n)" title="ON TIMER(n)">ON TIMER(n)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062336
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.014 seconds
Real time usage: 0.020 seconds
Preprocessor visited node count: 17/1000000
Post‐expand include size: 561/2097152 bytes
Template argument size: 12/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   11.430      1 -total
 20.85%    2.383      1 Template:PageSyntax
 20.45%    2.337      1 Template:PageNavigation
 19.60%    2.240      1 Template:Parameter
 18.16%    2.076      1 Template:PageDescription
 16.53%    1.889      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:151-0!canonical and timestamp 20240715062336 and revision id 6007.
 -->
</div>
</div>
</div>
</div>
</body>
</html>