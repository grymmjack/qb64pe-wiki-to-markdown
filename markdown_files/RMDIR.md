<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RMDIR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RMDIR rootpage-RMDIR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RMDIR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">RMDIR</a> statement deletes an empty directory using a designated path relative to the present path location.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">RMDIR</a> <i>directory$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>directory$</i> is a relative path to the directory to delete.</li>
<li>Directory path must be a literal or variable <a href="STRING" title="STRING">STRING</a> value designating the folder to be deleted.</li>
<li>If the directory contains files or folders, a <a href="ERROR_Codes" title="ERROR Codes">file/path access error</a> will occur.</li>
<li>If the directory path cannot be found, a <a href="ERROR_Codes" title="ERROR Codes">path not found</a> error occurs.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
<a href="ON_ERROR" title="ON ERROR"><span style="color:#4593D8;">ON ERROR GOTO</span></a> ErrorHandler
 DO
 ERRcode = 0
 <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter path and name of directory to delete: "; directory$
 IF <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(directory$) THEN      'valid user entry or quits
   <a class="mw-selflink selflink"><span style="color:#4593D8;">RMDIR</span></a> directory$    'removes empty folder without a prompt
   IF ERRcode = 0 THEN PRINT "Folder "; directory$; " removed."
 END IF
 LOOP UNTIL ERRcode = 0 OR LEN(directory$) = 0
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
ErrorHandler:
ERRcode = <a href="ERR" title="ERR"><span style="color:#4593D8;">ERR</span></a>    'get error code returned
<a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> ERRcode
<a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 75
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> directory$ + " is not empty!"
<a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 76
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> directory$ + " does not exist!"
<a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Error"; ERRcode; "attempting to delete " + directory$
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="RESUME" title="RESUME"><span style="color:#4593D8;">RESUME NEXT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd>This Windows-specific output from two runs of the above program is typical, though your output may vary. User-entered text is in italics.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">
Enter path and name of directory to delete: <i>Some\Folder\That\Doesnt\Exist</i>
Some\folder\That\Doesnt\Exist does not exist!
Enter path and name of directory to delete: <i>C:\temp</i>
C:\temp is not empty!
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MKDIR" title="MKDIR">MKDIR</a>, <a href="CHDIR" title="CHDIR">CHDIR</a></li>
<li><a href="KILL" title="KILL">KILL</a>, <a href="FILES" title="FILES">FILES</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192537
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 145/1000000
Post‐expand include size: 1603/2097152 bytes
Template argument size: 218/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.801      1 -total
 10.82%    3.007      1 Template:PageSyntax
 10.77%    2.994     16 Template:Cl
  8.59%    2.387      1 Template:PageDescription
  8.31%    2.309      2 Template:Parameter
  8.18%    2.273      1 Template:PageSeeAlso
  7.86%    2.185      1 Template:OutputEnd
  7.80%    2.168      1 Template:PageNavigation
  7.80%    2.168      1 Template:CodeStart
  7.64%    2.125      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:259-0!canonical and timestamp 20240714192537 and revision id 6610.
 -->
</div>
</div>
</div>
</div>
</body>
</html>