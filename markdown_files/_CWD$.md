<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CWD$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CWD rootpage-CWD skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CWD$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>
The <a class="mw-selflink selflink">_CWD$</a> function returns the current working directory path as a string value without a trailing path separator.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>workingDirectory$</i> = <a class="mw-selflink selflink">_CWD$</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>By default, the initial working directory path is usually the same as the directory of the executable file run.</li>
<li>The current working directory can be changed with the <a href="CHDIR" title="CHDIR">CHDIR</a> or <a href="SHELL" title="SHELL">SHELL</a> command; CHDIR sets it, _CWD$ returns it.</li>
<li>Path returns will change only when the working path has changed.  When in C:\ and run QB64\cwd.exe, it will still return C:\</li>
<li>The current working directory string can be used in <a href="OPEN" title="OPEN">OPEN</a> statements and <a href="SHELL" title="SHELL">SHELL</a> commands that deal with files.</li>
<li>Works in Windows, macOS and Linux. <a href="OS$" title="OS$">_OS$</a> can be used by a program to predict the proper slash separations in different OS's.</li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li>If an error occurs while obtaining the working directory from the operating system, <a href="ERROR_Codes" title="ERROR Codes">error code</a> 51 (Internal Error) will be generated.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Get the current working directory, and move around the file system:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">startdir$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_CWD$</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"We started at "</span>; startdir$
<a href="MKDIR" title="MKDIR"><span style="color:#4593D8;">MKDIR</span></a> <span style="color:#FFB100;">"a_temporary_dir"</span>
<a href="CHDIR" title="CHDIR"><span style="color:#4593D8;">CHDIR</span></a> <span style="color:#FFB100;">"a_temporary_dir"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"We are now in "</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_CWD$</span></a>
<a href="CHDIR" title="CHDIR"><span style="color:#4593D8;">CHDIR</span></a> startdir$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"And now we're back in "</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_CWD$</span></a>
<a href="RMDIR" title="RMDIR"><span style="color:#4593D8;">RMDIR</span></a> <span style="color:#FFB100;">"a_temporary_dir"</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">We started at C:\QB64
We are now in C:\QB64\a_temporary_dir
And now we're back in C:\QB64
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CHDIR" title="CHDIR">CHDIR</a> <span style="color:#777777;">(Change the current working directory)</span></li>
<li><a href="RMDIR" title="RMDIR">RMDIR</a> <span style="color:#777777;">(Remove a directory in the file system)</span></li>
<li><a href="KILL" title="KILL">KILL</a> <span style="color:#777777;">(Delete a file in the file system)</span></li>
<li><a href="MKDIR" title="MKDIR">MKDIR</a> <span style="color:#777777;">(Create a directory in the file system)</span></li>
<li><a href="OS$" title="OS$">_OS$</a> <span style="color:#777777;">(returns current OS to program)</span></li>
<li><a href="STARTDIR$" title="STARTDIR$">_STARTDIR$</a> <span style="color:#777777;">(returns path the user called program from)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035641
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 212/1000000
Post‐expand include size: 2112/2097152 bytes
Template argument size: 587/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 107/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.632      1 -total
 24.14%    6.671     12 Template:Text
  8.33%    2.301      1 Template:PageSyntax
  7.98%    2.204     10 Template:Cl
  6.42%    1.773      1 Template:CodeEnd
  6.12%    1.691      1 Template:Parameter
  6.01%    1.660      1 Template:CodeStart
  5.80%    1.602      1 Template:PageExamples
  5.76%    1.592      1 Template:OutputStart
  5.68%    1.570      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:106-0!canonical and timestamp 20240715035641 and revision id 8299.
 -->
</div>
</div>
</div>
</div>
</body>
</html>