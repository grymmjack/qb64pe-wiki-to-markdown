<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CHDIR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CHDIR rootpage-CHDIR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CHDIR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">CHDIR</a> statement changes the program's location from one working directory to another by specifying a literal or variable <a href="STRING" title="STRING">STRING</a> path.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CHDIR</a> <i>path$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>path$</i> is the new directory path the program will work in.</li>
<li><i>path$</i> can be an absolute path (starting from the root folder) or relative path (starting from the current program location).</li>
<li>If <i>path$</i> specifies a non-existing path, a <a href="ERROR_Codes" title="ERROR Codes">"Path not found"</a> error will occur.</li>
<li><b>A QB64 <a href="SHELL" title="SHELL">SHELL</a> statement cannot use "CD " or "CHDIR " + path$ to change directories.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> The following code is Windows-specific:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">CHDIR</span></a> "C:\"      'change to the root drive C (absolute path)
<a class="mw-selflink selflink"><span style="color:#4593D8;">CHDIR</span></a> "DOCUME~1" 'change to "C:\Documents and Settings" from root drive (relative path)
<a class="mw-selflink selflink"><span style="color:#4593D8;">CHDIR</span></a> "..\"      'change back to previous folder one up
</pre>
</td></tr></tbody></table>
<dl><dd><i>Details:</i> <b>QB64</b> can use long or short (8.3 notation) file and path names.</dd></dl>
<p>
<i>Example 2:</i> Using the Windows API to find the current program's name and root path. The PATH$ is a shared function value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "My program"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> TITLE$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> PATH$
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> TITLE$ <i>=== SHOW CURRENT PROGRAM</i>
<a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> PATH$           'optional path information shared with main module only
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE LIBRARY</span></a>        'Directory Information using KERNEL32 provided by Dav
  <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> GetModuleFileNameA (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> Module <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, FileName <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> nSize <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">END DECLARE</span></a>
FileName$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(256)
Result = GetModuleFileNameA(0, FileName$, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(FileName$))  '0 designates the current program
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Result <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>             'Result returns the length or bytes of the string information
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
<dl><dd><b>Note:</b> The program's <a href="TITLE" title="TITLE">_TITLE</a> name may be different from the actual program module's file name returned by Windows.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHELL" title="SHELL">SHELL</a>, <a href="FILES" title="FILES">FILES</a></li>
<li><a href="MKDIR" title="MKDIR">MKDIR</a>, <a href="RMDIR" title="RMDIR">RMDIR</a></li>
<li><a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061235
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.044 seconds
Real time usage: 0.067 seconds
Preprocessor visited node count: 277/1000000
Post‐expand include size: 2537/2097152 bytes
Template argument size: 409/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   40.247      1 -total
 27.83%   11.202      1 Template:PageNavigation
 12.71%    5.116      1 Template:PageSeeAlso
 10.56%    4.249     34 Template:Cl
  8.10%    3.259      1 Template:PageSyntax
  6.49%    2.614      4 Template:Parameter
  6.45%    2.596      2 Template:CodeStart
  5.90%    2.376      1 Template:PageDescription
  5.80%    2.336      1 Template:PageExamples
  5.78%    2.327      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:409-0!canonical and timestamp 20240715061235 and revision id 8112.
 -->
</div>
</div>
</div>
</div>
</body>
</html>