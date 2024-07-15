<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DATA - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DATA rootpage-DATA skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DATA</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">DATA</a> statement creates a line of fixed program information separated by commas. The DATA can be later READ by the program at runtime.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">DATA</a> [value1, value2, ...]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>DATA is used at the beginning of every data field line with commas separating the values that follow.</li>
<li>Values can be any <b>literal</b> <a href="STRING" title="STRING">STRING</a> or numerical type. <b>Variables cannot be used.</b></li>
<li>DATA fields can be placed and READ consecutively in the main program code body with or without line labels for <a href="RESTORE" title="RESTORE">RESTORE</a>.</li>
<li>DATA is best placed after the main program code.
<ul><li><b>QB64</b> DATA can be placed inside a <a href="SUB" title="SUB">SUB</a> or  <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures.</li></ul></li>
<li><a href="RESTORE" title="RESTORE">RESTORE</a> will only read the first data field if the DATA is not labeled or no label is specified in a RESTORE call.</li>
<li>When using multiple DATA fields, label each data field with a line label so that each data pointer can be reset for multiple reads with <b><a href="RESTORE" title="RESTORE">RESTORE</a> <i>linelabel</i></b>.</li>
<li>QBasic comma separations were flexible to allow column alignments when creating them. QB64 removes spacing between commas.</li>
<li><a href="STRING" title="STRING">STRING</a> DATA values with end spaces, QBasic keywords and values that include the comma character must be enclosed in quotation marks.</li>
<li>DATA fields can only be created by the programmer and cannot be changed by a user or lost.</li>
<li>Comments after a data line require a colon before the comment.</li>
<li>If a <a href="READ" title="READ">READ</a> statement attempts to read past the last data value, an <a href="ERROR_Codes" title="ERROR Codes">"Out of Data" error</a> will occur. Use end of data markers when necessary.</li>
<li><b><a class="mw-selflink selflink">DATA</a> fields can be placed after <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures, but line labels are not allowed.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Creating two DATA fields that can be <a href="READ" title="READ">READ</a> repeatedly using <a href="RESTORE" title="RESTORE">RESTORE</a> with the appropriate line label.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> Database2
<a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> A$, B$, C$, D$         'read 4 string values from second DATA field
PRINT A$ + B$ + C$ + D$     'note that quoted strings values are spaced
<a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> Database1
FOR i = 1 TO 18
  <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> number%                     'read first DATA field 18 times only
  PRINT number%;
NEXT
END
Database1:
<a class="mw-selflink selflink"><span style="color:#4593D8;">DATA</span></a> 1, 0, 0, 1, 1, 0, 1, 1, 1
<a class="mw-selflink selflink"><span style="color:#4593D8;">DATA</span></a> 2, 0, 0, 2, 2, 0, 2, 2, 2 :       ' DATA line comments require a colon
Database2:
<a class="mw-selflink selflink"><span style="color:#4593D8;">DATA</span></a> "Hello, ", "world! ", Goodbye, work!
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Hello world! Goodbyework!
1  0  0  1  1  0  1  1  1  2  0  0  2  2  0  2  2  2
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> How to <a href="RESTORE" title="RESTORE">RESTORE</a> and <a href="READ" title="READ">READ</a> DATA in a <a href="SUB" title="SUB">SUB</a> procedure in QB64. Line labels can be used for multiple DATA fields.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> num(10) 'shared array or must be passed as a parameter
ReadData 2 '&lt;&lt;&lt;&lt;&lt;&lt;&lt; change value to 1 to read other data
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> num(i);
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> ReadData (mode)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> mode = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> mydata1 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> mydata2
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
  <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> num(i)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
mydata1:
<a class="mw-selflink selflink"><span style="color:#4593D8;">DATA</span></a> 1,2,3,4,5,6,7,8,9,10
mydata2:
<a class="mw-selflink selflink"><span style="color:#4593D8;">DATA</span></a> 10,9,8,7,6,5,4,3,2,1
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 10  9  8  7  6  5  4  3  2  1 </pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RESTORE" title="RESTORE">RESTORE</a>. <a href="READ" title="READ">READ</a></li>
<li><a href="$EMBED" title="$EMBED">$EMBED</a>. <a href="EMBEDDED$" title="EMBEDDED$">_EMBEDDED$</a></li>
<li><a href="SUB" title="SUB">SUB</a>, <a href="FUNCTION" title="FUNCTION">FUNCTION</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061251
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.084 seconds
Preprocessor visited node count: 220/1000000
Post‐expand include size: 2218/2097152 bytes
Template argument size: 251/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   57.742      1 -total
 28.53%   16.472      1 Template:PageDescription
 24.80%   14.320     27 Template:Cl
  8.16%    4.711      2 Template:CodeStart
  7.46%    4.310      1 Template:PageExamples
  6.40%    3.695      1 Template:PageNavigation
  5.20%    3.001      1 Template:PageSyntax
  3.80%    2.193      2 Template:CodeEnd
  3.58%    2.069      1 Template:PageSeeAlso
  3.43%    1.983      2 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:287-0!canonical and timestamp 20240715061250 and revision id 8696.
 -->
</div>
</div>
</div>
</div>
</body>
</html>