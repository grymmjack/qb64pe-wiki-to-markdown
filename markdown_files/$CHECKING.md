<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$CHECKING - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_CHECKING rootpage-_CHECKING skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$CHECKING</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$CHECKING</a> metacommand turns C++ event checking ON or OFF.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$CHECKING</a>:{ON|OFF}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The Metacommand does <b>not</b> require a comment or REM before it. There is no space after the colon.</li>
<li>The OFF action turns event checking off and should <b>only be used when running stable, errorless code.</b></li>
<li>The default <a class="mw-selflink selflink">$CHECKING</a>:ON action is only required when checking has been turned OFF previously.</li>
<li>When <a class="mw-selflink selflink">$CHECKING</a>:OFF is used, all error code and the reporting code is removed from the EXE program.</li>
<li><b>Warning: Turning OFF error checking could create a General Protection Fault (or segfault). Use only with 100% stable sections of code.</b></li></ul>
<h3><span class="mw-headline" id="Details">Details</span></h3>
<ul><li>After every QB64 command is translated to C++, the compiler adds special code sections to check for <a href="ON_TIMER(n)" title="ON TIMER(n)">ON TIMER(n)</a> events and errors that may have occured in the last function call. Disabling error checking with the <a class="mw-selflink selflink">$CHECKING</a>:OFF directive prevents the compiler from adding the extra code sections.</li>
<li>Setting <a class="mw-selflink selflink">$CHECKING</a>:OFF is only designed for 100% stable, errorless sections of code, where every CPU cycle saved counts, such as in a software 3D texture mapper, for example.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON_TIMER(n)" title="ON TIMER(n)">ON TIMER(n)</a></li>
<li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a></li>
<li><a href="Metacommand" title="Metacommand">Metacommand</a></li>
<li><a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715045312
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.017 seconds
Real time usage: 0.022 seconds
Preprocessor visited node count: 22/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   10.265      1 -total
 28.91%    2.968      1 Template:PageSyntax
 24.17%    2.481      1 Template:PageDescription
 23.68%    2.431      1 Template:PageNavigation
 19.51%    2.003      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:82-0!canonical and timestamp 20240715045312 and revision id 8027.
 -->
</div>
</div>
</div>
</div>
</body>
</html>