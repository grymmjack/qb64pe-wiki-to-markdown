<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>KILL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-KILL rootpage-KILL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">KILL</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">KILL</a> statement deletes a file designated by a <a href="STRING" title="STRING">STRING</a> value or variable.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">KILL</a> <i>fileSpec$</i></dd></dl>
<p>
</p>
<ul><li><i>fileSpec$</i> is a literal or variable string path and filename. Wildcards * and ? can be used with caution.</li></ul>
<dl><dd><dl><dd><b>*</b> denotes one or more wildcard letters of a name or extension</dd>
<dd><b>?</b> denotes one wildcard letter of a name or extension</dd></dl></dd></dl>
<ul><li><i>fileSpec$</i> can include a path that can be either relative to the program's current location or absolute, from the root drive.</li>
<li><a class="mw-selflink selflink">KILL</a> cannot remove an <a href="OPEN" title="OPEN">OPEN</a> file. The program must <a href="CLOSE" title="CLOSE">CLOSE</a> it first.</li>
<li>If the path or file does not exist, a "File not found" or "Path not found" <a href="ERROR_Codes" title="ERROR Codes">error</a> will result. See <a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a>.</li>
<li><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="SHELL" title="SHELL">SHELL</a> "DEL /Q " + fileName$</span> does the same without a prompt or verification for wildcard deletions.</li>
<li><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="SHELL" title="SHELL">SHELL</a> "DEL /P " + fileName$</span> will ask for user verification.</li>
<li>Cannot delete folders or directories. Use <a href="RMDIR" title="RMDIR">RMDIR</a> to remove empty folders.</li>
<li><b>Warning: files deleted with <a class="mw-selflink selflink">KILL</a> will not go to the Recycle Bin and they cannot be restored.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">KILL "C:\QBasic\data\2000data.dat"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RMDIR" title="RMDIR">RMDIR</a>, <a href="FILES" title="FILES">FILES</a>, <a href="SHELL" title="SHELL">SHELL</a>, <a href="OPEN" title="OPEN">OPEN</a></li>
<li><a href="CHDIR" title="CHDIR">CHDIR</a>, <a href="MKDIR" title="MKDIR">MKDIR</a>, <a href="NAME" title="NAME">NAME</a></li>
<li><a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a>, <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192454
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.036 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 37/1000000
Post‐expand include size: 1055/2097152 bytes
Template argument size: 27/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.625      1 -total
 13.96%    3.855      2 Template:InlineCodeEnd
 11.93%    3.295      1 Template:PageSeeAlso
 11.24%    3.106      2 Template:InlineCode
 10.65%    2.942      1 Template:PageSyntax
 10.54%    2.913      1 Template:PageNavigation
  9.14%    2.526      1 Template:PageExamples
  9.02%    2.491      3 Template:Parameter
  8.93%    2.468      1 Template:CodeStart
  8.80%    2.432      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:483-0!canonical and timestamp 20240714192454 and revision id 6059.
 -->
</div>
</div>
</div>
</div>
</body>
</html>