<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SYSTEM - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SYSTEM rootpage-SYSTEM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SYSTEM</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">SYSTEM</a> statement immediately closes a program and returns control to the operating system.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>SYSTEM</b> [return_code%]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>QB64 allows a <i>code</i> number to be used after SYSTEM to be read in another program module by the <a href="SHELL" title="SHELL">SHELL</a> or <a href="SHELLHIDE" title="SHELLHIDE">_SHELLHIDE</a> functions.</li></ul>
<p>
<i>Usage:</i>
</p>
<ul><li>This command should be used to close a program quickly instead of pausing with <a href="END" title="END">END</a> or nothing at all.</li>
<li>A code can be added after the statement to send a value to the <a href="SHELL_(function)" title="SHELL (function)">SHELL (function)</a> or <a href="SHELLHIDE" title="SHELLHIDE">_SHELLHIDE</a> function in another module.</li>
<li>SYSTEM ends the program and closes the window immediately. The last screen image may not be displayed.</li></ul>
<p>
<i>QBasic or QuickBASIC:</i>
</p>
<ul><li><b>QBasic BAS files can be run like compiled programs without returning to the IDE when <a class="mw-selflink selflink">SYSTEM</a> is used to <a href="END" title="END">end</a> them!</b></li>
<li>If a program BAS module is run from the IDE, stopped by Ctrl-Break or an error occurs the QB program will exit to the IDE.</li>
<li>To run a QuickBASIC program without the IDE use the following DOS command line: <span style="color:green;">QB.EXE /L /RUN filename.BAS</span></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHELL_(function)" title="SHELL (function)">SHELL (function)</a></li>
<li><a href="SHELLHIDE" title="SHELLHIDE">_SHELLHIDE</a></li>
<li><a href="EXIT_(function)" title="EXIT (function)">_EXIT (function)</a>, <a href="END" title="END">END</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034230
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.018 seconds
Real time usage: 0.032 seconds
Preprocessor visited node count: 19/1000000
Post‐expand include size: 605/2097152 bytes
Template argument size: 32/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   14.676      1 -total
 32.58%    4.781      1 Template:PageNavigation
 18.64%    2.735      1 Template:PageSeeAlso
 18.40%    2.700      1 Template:PageSyntax
 14.25%    2.091      1 Template:Text
 13.23%    1.942      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:516-0!canonical and timestamp 20240715034230 and revision id 7968.
 -->
</div>
</div>
</div>
</div>
</body>
</html>