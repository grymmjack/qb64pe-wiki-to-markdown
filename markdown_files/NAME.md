<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>NAME - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-NAME rootpage-NAME skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">NAME</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">NAME</a> statement changes the name of a file or directory to a new name.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">NAME</a> <i>oldFileOrFolderName$</i> <b>AS</b> <i>newFileOrFolderName$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>oldFileOrFolderName$</i> and <i>newFileOrFolderName$</i> are variables or literal <a href="STRING" title="STRING">STRINGs</a> in quotes. Paths can be included.</li>
<li>If the two paths are different, the statement moves the original file to the new path and renames it.</li>
<li>If the path is the same or a path is not included, the original file is just renamed.</li>
<li><a href="SHELL" title="SHELL">SHELL</a> can use <i>"REN " + filename$ + " " + newname$</i> for the same purpose (Windows).</li>
<li>Path or filename <a href="ERROR_Codes" title="ERROR Codes">errors</a> are possible and should be handled in the program.</li>
<li><b>Caution: There is no prompt to continue or execution verification.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-selflink selflink"><span style="color:#4593D8;">NAME</span></a> "BIGBAD.TXT" <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> "BADWOLF.TXT"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHELL" title="SHELL">SHELL</a>, <a href="MKDIR" title="MKDIR">MKDIR</a>, <a href="FILES" title="FILES">FILES</a></li>
<li><a href="CHDIR" title="CHDIR">CHDIR</a>, <a href="KILL" title="KILL">KILL</a>, <a href="RMDIR" title="RMDIR">RMDIR</a></li>
<li><a href="Windows_Libraries#File_Dialog_Boxes" title="Windows Libraries">Windows Open and Save Dialog Boxes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061345
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.018 seconds
Real time usage: 0.026 seconds
Preprocessor visited node count: 50/1000000
Post‐expand include size: 840/2097152 bytes
Template argument size: 92/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.307      1 -total
 12.62%    2.184      1 Template:PageSyntax
 12.08%    2.090      4 Template:Parameter
 11.15%    1.930      2 Template:Cl
 10.30%    1.782      1 Template:PageSeeAlso
  9.97%    1.726      1 Template:PageNavigation
  9.91%    1.716      1 Template:PageDescription
  9.90%    1.714      1 Template:PageExamples
  9.68%    1.675      1 Template:CodeEnd
  9.23%    1.598      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:504-0!canonical and timestamp 20240715061345 and revision id 7345.
 -->
</div>
</div>
</div>
</div>
</body>
</html>