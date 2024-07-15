<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_TITLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TITLE rootpage-TITLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_TITLE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_TITLE</a> statement provides the program name in the title bar of the program window.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_TITLE</a> <i>text$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>text$</i> can be any literal or variable <a href="STRING" title="STRING">STRING</a> or <a href="ASCII" title="ASCII">ASCII</a> character value.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The title can be changed anywhere in a program procedure.</li>
<li>The title bar will say "Untitled" if a title is not set.</li>
<li>Change the title of the <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> windows created using <a href="CONSOLETITLE" title="CONSOLETITLE">_CONSOLETITLE</a></li>
<li><b>Note: A <a href="DELAY" title="DELAY">delay</a> may be required before the title can be set.</b> See <a href="SCREENEXISTS" title="SCREENEXISTS">_SCREENEXISTS</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> How to create the window title bar.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_TITLE</span></a> "My New Program"
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> How to find the currently running program module name and current path using a Windows API Library.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_TITLE</span></a> "My program"
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 5             '5 second delay
<a class="mw-selflink selflink"><span style="color:#4593D8;">_TITLE</span></a> <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(TITLE$, 1, <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(TITLE$, ".") - 1)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> PATH$
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> TITLE$ '=== SHOW CURRENT PROGRAM
<a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> PATH$
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE LIBRARY</span></a> 'Directory Information using KERNEL32 provided by Dav
  <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> GetModuleFileNameA (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> Module <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, FileName <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> nSize <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">END DECLARE</span></a>
FileName$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(256)
Result = GetModuleFileNameA(0, FileName$, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(FileName$))
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Result <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  PATH$ = <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(FileName$, Result)
  start = 1
  DO
    posit = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(start, PATH$, "\")
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> posit <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> last = posit
    start = posit + 1
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> posit = 0
  TITLE$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(PATH$, last + 1)
  PATH$ = <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(PATH$, last)
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> TITLE$ = "": PATH$ = ""
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The actual module file name is returned. Not necessarily the Title value. The value returned can be used however.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="TITLE$" title="TITLE$">_TITLE$</a></li>
<li><a href="ICON" title="ICON">_ICON</a></li>
<li><a href="DELAY" title="DELAY">_DELAY</a></li>
<li><a href="ASCII" title="ASCII">ASCII</a></li>
<li><a href="CONSOLETITLE" title="CONSOLETITLE">_CONSOLETITLE</a></li>
<li><a href="SCREENEXISTS" title="SCREENEXISTS">_SCREENEXISTS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062513
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.051 seconds
Real time usage: 0.076 seconds
Preprocessor visited node count: 280/1000000
Post‐expand include size: 2624/2097152 bytes
Template argument size: 424/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.144      1 -total
 14.16%    4.693     35 Template:Cl
  9.40%    3.114      1 Template:PageSyntax
  8.86%    2.936      1 Template:PageSeeAlso
  8.26%    2.738      1 Template:PageDescription
  8.21%    2.721      2 Template:Parameter
  8.19%    2.715      2 Template:CodeStart
  7.84%    2.598      2 Template:CodeEnd
  7.67%    2.541      1 Template:PageExamples
  7.63%    2.529      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:356-0!canonical and timestamp 20240715062513 and revision id 8176.
 -->
</div>
</div>
</div>
</div>
</body>
</html>