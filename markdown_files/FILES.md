<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>FILES - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FILES rootpage-FILES skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">FILES</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">FILES</a> statement is used to print a list of files in the current directory using a file specification.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">FILES</a> [<i>fileSpec$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>fileSpec$</i> is a string expression or variable containing a path when required.</li>
<li><i>fileSpec$</i> can use the * and ? wildcard specifications:
<ul><li><b>*</b> denotes one or more wildcard characters in a filename or path specification as any legal file name  character(s).</li>
<li><b>?</b> denotes one wildcard letter in a filename or path specification as any legal filename character.</li></ul></li>
<li>If <i>fileSpec$</i> is omitted, it is assumed to be <b>"*.*"</b> (all files and folders in the current directory).</li>
<li>Illegal filename characters in <b>QB64</b> include * &gt; &lt; : " | \ / with any amount of dot extensions being allowed in Windows.</li>
<li>FILES lists can make the screen roll up. Try using SHELL "DIR" with the /P option. <a class="external text" href="http://www.computerhope.com/dirhlp.htm" rel="nofollow">DIR command</a>.</li>
<li>To get individual directory entries use <a href="FILES$" title="FILES$">_FILES$</a> instead.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt><i>Example 1:</i> Finding a list of all BAS files in the current folder.</dt></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">FILES</span></a> "*.BAS"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FILES$" title="FILES$">_FILES$</a></li>
<li><a href="SHELL" title="SHELL">SHELL</a></li>
<li><a href="CHDIR" title="CHDIR">CHDIR</a>, <a href="MKDIR" title="MKDIR">MKDIR</a></li>
<li><a href="RMDIR" title="RMDIR">RMDIR</a>, <a href="KILL" title="KILL">KILL</a></li>
<li><a href="CWD$" title="CWD$">_CWD$</a>, <a href="STARTDIR$" title="STARTDIR$">_STARTDIR$</a></li>
<li><a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a>, <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a></li>
<li><a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192434
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 43/1000000
Post‐expand include size: 753/2097152 bytes
Template argument size: 46/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.302      1 -total
 12.77%    2.976      1 Template:PageSyntax
 10.84%    2.527      4 Template:Parameter
 10.58%    2.465      1 Template:CodeStart
 10.23%    2.383      1 Template:Cl
 10.12%    2.358      1 Template:PageExamples
 10.10%    2.354      1 Template:PageNavigation
 10.00%    2.331      1 Template:PageSeeAlso
  9.96%    2.321      1 Template:PageDescription
  9.75%    2.272      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:469-0!canonical and timestamp 20240714192434 and revision id 8625.
 -->
</div>
</div>
</div>
</div>
</body>
</html>