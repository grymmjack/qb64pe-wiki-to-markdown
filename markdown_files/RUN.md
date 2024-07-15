<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RUN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RUN rootpage-RUN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RUN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>RUN</b> is a control flow statement that clears and restarts the program currently in memory or executes another specified program.
The multi-modular technique goes back to when QBasic and QuickBASIC had module size constraints. In QB64 it has been implemented so that that older code can still be compiled, though <b>it is advisable to use single modules for a single project (not counting <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> libraries), for ease of sharing and also because the module size constraints no longer exist.</b>
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><b>RUN</b> [{<i>line_number</i> | <i>filespec$</i>}] [<i>command_parameter(s)</i>]</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>line number</i> specifies a line number in the main module code.</li>
<li>An optional <i>filespec</i> specifies a program to load into memory and run.</li></ul>
<dl><dd>* BAS or EXE extensions are assumed to be the same as the calling module's extension, EXE or BAS (QBasic only).</dd>
<dd>* <i>file names specs</i> with other extensions must use the full filename. No extension requires a dot.</dd></dl>
<ul><li>In <b>QB64</b> <i>command line parameters</i> can follow the program file name and be read using the <a href="COMMAND$" title="COMMAND$">COMMAND$</a> function later.</li></ul>
<p>
<i>Usage:</i>
</p>
<ul><li>The starting <a href="Line_number" title="Line number">line number</a> MUST be one used in the main module code, even if RUN is called from within a SUB or FUNCTION.</li>
<li>If no line number is given the currently loaded program runs from the first executable line.</li>
<li>In <b>QB64</b> RUN can open any kind of executable program and provide case sensitive program specific parameters.
<ul><li>Recommended practice to run external programs is to use <a href="SHELL" title="SHELL">SHELL</a>.</li></ul></li>
<li>RUN closes all open files and closes the invoking program module before the called program starts.</li>
<li>RUN resets the <a href="RANDOMIZE" title="RANDOMIZE">RANDOMIZE</a> sequence to the starting <a href="RND" title="RND">RND</a> function value.</li>
<li><b>Note: Calling RUN repeatedly may cause a stack leak in QB64 if it is called from within a <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a>. Avoid when possible.</b></li></ul>
<p>
<i>Example 1:</i> Shows how RUN can reference multiple line numbers in the main module code. No line number executes first code line.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">PRINT " A", " B", " C", " D"
10 A = 1
20 B = 2
30 C = 3
40 D = 4
50 <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A, B, C, D
60 <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> A = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 70 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RUN</span></a> 20    'RUN clears all values
70 <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> B = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 80 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RUN</span></a> 30
80 <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> C = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 90 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RUN</span></a> 40
90 <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> D = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 100 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RUN</span></a> 50
100 <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Do you want to quit?(Y/N)", quit$
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(quit$) = "Y" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RUN</span></a>  'RUN without line number executes at first code line
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">A       B       C       D
1       2       3       4
0       2       3       4
0       0       3       4
0       0       0       4
0       0       0       0
Do you want to quit?(Y/N)_
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CHAIN" title="CHAIN">CHAIN</a>, <a href="SHELL" title="SHELL">SHELL</a></li>
<li><a href="COMMAND$" title="COMMAND$">COMMAND$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715060243
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.095 seconds
Preprocessor visited node count: 197/1000000
Post‐expand include size: 1921/2097152 bytes
Template argument size: 213/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   69.337      1 -total
 25.48%   17.670     25 Template:Cl
 15.01%   10.406      1 Template:PageParameters
 12.52%    8.678      1 Template:OutputEnd
 10.74%    7.449      1 Template:OutputStart
  9.24%    6.406      1 Template:PageSyntax
  7.72%    5.351      1 Template:CodeStart
  5.40%    3.742      1 Template:CodeEnd
  4.61%    3.196      1 Template:PageNavigation
  4.41%    3.060      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:265-0!canonical and timestamp 20240715060242 and revision id 7395.
 -->
</div>
</div>
</div>
</div>
</body>
</html>