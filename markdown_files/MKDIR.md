<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>MKDIR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MKDIR rootpage-MKDIR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">MKDIR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">MKDIR</a> statement creates a new folder (<b>dir</b>ectory) at a specified path.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">MKDIR</a> pathSpec$</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The path specification (pathSpec$) is a literal or variable <a href="STRING" title="STRING">STRING</a> expression that also specifies the new folder's name.</li>
<li>If no path is given the directory will become a sub-directory of the present directory where the program is currently running.</li>
<li><b>QB64</b> can use both long or short path and file names with spaces when required.</li>
<li>The new folder will be created without a user prompt or verification.</li>
<li>If a path is specified, the path must exist or a <a href="ERROR_Codes" title="ERROR Codes">"Path not found" error</a> will occur. See <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a>.</li>
<li><a href="SHELL" title="SHELL">SHELL</a> can use the DOS command "MD " or "MKDIR " + path$ + newfolder$ to do the same thing.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHELL" title="SHELL">SHELL</a>, <a href="CHDIR" title="CHDIR">CHDIR</a>, <a href="FILES" title="FILES">FILES</a></li>
<li><a href="NAME" title="NAME">NAME</a>, <a href="KILL" title="KILL">KILL</a>, <a href="RMDIR" title="RMDIR">RMDIR</a></li>
<li><a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a></li>
<li><a href="Windows_Libraries#File_Dialog_Boxes" title="Windows Libraries">Windows Open and Save Dialog Boxes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061341
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.017 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 12/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.895      1 -total
 35.32%    9.146      1 Template:PageSyntax
 24.78%    6.417      1 Template:PageDescription
 23.25%    6.021      1 Template:PageSeeAlso
 14.17%    3.670      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:580-0!canonical and timestamp 20240715061341 and revision id 6470.
 -->
</div>
</div>
</div>
</div>
</body>
</html>