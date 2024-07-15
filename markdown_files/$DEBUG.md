<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$DEBUG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_DEBUG rootpage-_DEBUG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$DEBUG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>$DEBUG</b> is precompiler <a href="Metacommand" title="Metacommand">metacommand</a>, which enables debugging features, allowing you to step through your code running line by line and to inspect variables and change their values in real time.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$DEBUG</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>$DEBUG</b> injects extra code in the resulting binary, allowing the IDE to control the execution flow of your program.</li>
<li>When <b>$DEBUG</b> is used, the IDE will connect to your running program using a local TCP/IP connection.
<ul><li>You may get a prompt from your Operating System regarding this, so it may be necessary to allow the IDE to receive connections.</li>
<li>No external connections are created, and your running program will only attempt to connect locally to the IDE.</li></ul></li>
<li>The default TCP/IP port starts at 9001. Multiple running instances of the IDE will attempt to open ports 9002 and up.
<ul><li>You can change the base port in the Debug menu.</li></ul></li>
<li>The metacommand is supposed to be removed once your program is ready for release, although leaving it in won't have any effect if your program isn't run from the IDE.
<ul><li>The only drawback of leaving the metacommand in is that your binary will end up being larger than required.</li></ul></li></ul>
<p>
</p>
<h2><span id=".24DEBUG_Mode_Operation"></span><span class="mw-headline" id="$DEBUG_Mode_Operation">$DEBUG Mode Operation</span></h2>
<ul><li>To start execution in pause mode, you can use <b>F7</b> or <b>F8</b>.</li>
<li>There will be an arrow next to the line number where execution is paused, indicating the next line that will be run.</li>
<li>When you enable <b>$DEBUG</b> mode, you can set breakpoints by clicking the line number at which you wish to stop execution. This can also be achieved by using the <b>F9</b> key.
<ul><li>Breakpoints are indicated by a red dot next to the line number.</li>
<li>To clear all breakpoints, hit <b>F10</b>.</li></ul></li>
<li>To skip a line during execution, shift-click a line number
<ul><li>Lines marked for skipping are indicated by an exclamation mark next to the line number.</li></ul></li>
<li><b>F4</b> opens the Variable List dialog, which allows you to add variables to the Watch List.</li>
<li>During execution, the Variable List dialog also allows you to set the values of variables and also to create Watchpoints.</li>
<li>Watchpoints halt execution, similarly to breakpoints, but do so when a variable matches the condition you specify.
<ul><li>You can use relational operators (=, &lt;&gt;, &gt;=, &lt;=, &gt;, &lt;) to create watchpoint conditions.</li></ul></li>
<li>After a breakpoint or a watchpoint is reached, <b>F5</b> can be used to continue execution.</li>
<li><b>F6</b> can be used when the execution pointer is inside a sub/function. When used, execution will proceed until the procedure is ended.</li>
<li><b>F7</b> can be used to run line by line, and can be used to debug code inside subs/functions (Step Into).</li>
<li><b>F8</b> can be used to run line by line without entering sub/function calls (Step Over).</li>
<li><b>F12</b> can be used to show the current call stack (which procedure calls led to the current line).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Metacommand" title="Metacommand">Metacommands</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062607
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.019 seconds
Real time usage: 0.024 seconds
Preprocessor visited node count: 20/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    8.899      1 -total
 28.34%    2.522      1 Template:PageSyntax
 24.16%    2.150      1 Template:PageNavigation
 22.36%    1.990      1 Template:PageDescription
 21.01%    1.870      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:738-0!canonical and timestamp 20240715062607 and revision id 7476.
 -->
</div>
</div>
</div>
</div>
</body>
</html>