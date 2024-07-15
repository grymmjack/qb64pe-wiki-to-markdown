<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>END - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-END rootpage-END skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">END</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">END</a> statement terminates a program without an immediate exit or ends a procedure or statement block.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">END</a> [<i>returnCode%</i>]</dd>
<dd><a class="mw-selflink selflink">END</a> <a href="IF...THEN" title="IF...THEN">IF</a></dd>
<dd><a class="mw-selflink selflink">END</a> <a href="TYPE" title="TYPE">TYPE</a></dd>
<dd><a class="mw-selflink selflink">END</a> <a href="SELECT_CASE" title="SELECT CASE">SELECT</a></dd>
<dd><a class="mw-selflink selflink">END</a> <a href="SUB" title="SUB">SUB</a></dd>
<dd><a class="mw-selflink selflink">END</a> <a href="FUNCTION" title="FUNCTION">FUNCTION</a></dd>
<dd>END <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>In <b>QB64</b>, <a class="mw-selflink selflink">END</a> can be followed by a code that can be read by another module using the <a href="SHELL_(function)" title="SHELL (function)">_SHELL</a> or <a href="SHELLHIDE" title="SHELLHIDE">_SHELLHIDE</a> function (known as <a class="external text" href="https://blogs.msdn.microsoft.com/oldnewthing/20080926-00/?p=20743" rel="nofollow"><b>errorlevel</b></a>)</li>
<li>When END is used to end a program, there is a pause and the message "Press any key to continue..." is displayed at the bottom of the program's window.</li>
<li>If the program does not use END or <a href="SYSTEM" title="SYSTEM">SYSTEM</a>, the program will still end with a pause and display "Press any key to continue...".</li>
<li>In <b>QB64</b>, <a href="SYSTEM" title="SYSTEM">SYSTEM</a> will end the program immediately and close the window.</li>
<li>The <b>QB64</b> <a href="EXIT_(function)" title="EXIT (function)">_EXIT (function)</a> can block a user's Ctrl + Break key presses and clicks on the window's close button (X button) until the program is ready to close.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> In QB64 you won't return to the IDE unless you are using it to run or edit the program module.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hello world!"
<a class="mw-selflink selflink"><span style="color:#4593D8;">END</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hello no one!"
</pre>
</td></tr></tbody></table>
<p><i>Returns:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Hello world!
Press any key to continue...
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i>"Hello no one!" isn't returned because the program ended with the END statement no matter what is after that.</dd>
<dd>The message "Press any key to continue..." is displayed after the program ends, both in QBasic and in <b>QB64</b>.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SYSTEM" title="SYSTEM">SYSTEM</a> <span style="color:#777777;">(immediate exit)</span></li>
<li><a href="SHELL_(function)" title="SHELL (function)">SHELL (function)</a>, <a href="SHELLHIDE" title="SHELLHIDE">_SHELLHIDE</a></li>
<li><a href="EXIT" title="EXIT">EXIT</a> (statement), <a href="EXIT_(function)" title="EXIT (function)">_EXIT (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192424
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.037 seconds
Real time usage: 0.057 seconds
Preprocessor visited node count: 56/1000000
Post‐expand include size: 937/2097152 bytes
Template argument size: 53/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   36.777      1 -total
 27.59%   10.148      1 Template:PageExamples
  8.24%    3.031      1 Template:CodeStart
  7.59%    2.790      1 Template:Parameter
  6.95%    2.557      1 Template:PageSyntax
  6.54%    2.406      3 Template:Cl
  6.13%    2.254      1 Template:PageSeeAlso
  5.86%    2.155      1 Template:PageNavigation
  5.62%    2.066      1 Template:OutputEnd
  5.57%    2.048      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:460-0!canonical and timestamp 20240714192424 and revision id 7869.
 -->
</div>
</div>
</div>
</div>
</body>
</html>