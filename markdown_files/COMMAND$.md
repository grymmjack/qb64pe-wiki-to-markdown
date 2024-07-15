<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>COMMAND$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-COMMAND rootpage-COMMAND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">COMMAND$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>COMMAND$</b> function returns the command line argument(s) passed when a program is run.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>commandLine$</i> = <a class="mw-selflink selflink">COMMAND$</a>[(count%)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <a href="STRING" title="STRING">STRING</a> return value is anything typed after a program's executable file name in command line (or using the <a href="RUN" title="RUN">RUN</a> statement).</li>
<li>Unlike QuickBASIC, <b>QB64</b> does not return all <a href="UCASE$" title="UCASE$">uppercase</a> values so keep that in mind when checking parameters.</li>
<li>In <b>QB64</b>, COMMAND$ works as an array to return specific elements passed to the command line. COMMAND$(2) would return the second parameter passed at the command line. Arguments can contain spaces if they are passed inside quotation marks. This can be used to properly retrieve file names and arguments which contain spaces.</li>
<li>Use the <a href="COMMANDCOUNT" title="COMMANDCOUNT">_COMMANDCOUNT</a> function to find the number of parameters passed to a program via the command line. See <i>Example 2</i> below.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Compile both programs. ProgramA <a href="RUN" title="RUN">RUNs</a> ProgramB with a parameter passed following the filename:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 12, 36: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "ProgramA"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 23, 25: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press any key to run ProgramB"
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
<a href="RUN" title="RUN"><span style="color:#4593D8;">RUN</span></a> "ProgramB FS"  'pass FS parameter to ProgramB in QB64 or QB4.5
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>ProgramB</i> checks for fullscreen parameter pass in QB64 and goes full screen.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 17, 36: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "ProgramB"
parameter$ = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">COMMAND$</span></a>) 'UCASE$ is needed in QB64 only, as QB4.5 will always return upper case
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 33: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Parameter = " + parameter$
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(parameter$, 2) = "FS" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="FULLSCREEN" title="FULLSCREEN"><span style="color:#4593D8;">_FULLSCREEN</span></a> 'parameter changes to full screen
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">                                    ProgramB
                                 Parameter = FS.EXE
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Program gets the number of parameters passed to the program, and then prints those parameters to the screen one at a time.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">count = <a href="COMMANDCOUNT" title="COMMANDCOUNT"><span style="color:#4593D8;">_COMMANDCOUNT</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> c = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> count
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">COMMAND$</span></a>(c) 'or process commands sent
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">-1
a data file
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation: If we start </i>ThisProgram.exe<i> with the command line <b>ThisProgram -l "a data file"</b>, COMMAND$ will return a single string of "-1 a data file" which might be hard to process and interpret properly, but COMMAND$(1) would return "-l" and COMMAND$(2) would return the quoted "a data file" option as separate entries for easier parsing and processing.</i></dd></dl>
<p>
<i>Example 3:</i> As part of the command array syntax, you can also just read the array to see how many commands were sent (or simply check <a href="COMMANDCOUNT" title="COMMANDCOUNT">_COMMANDCOUNT</a>):
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">DO
    count = count + 1
    cmd$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">COMMAND$</span></a>(count)
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> cmd$ = "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a> 'read until an empty return
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> cmd$ 'or process commands sent
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
count = count - 1 'save the number of parameters sent to this program when run
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1271" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="SHELL" title="SHELL">SHELL</a>, <a href="RUN" title="RUN">RUN</a></li>
<li><a href="UCASE$" title="UCASE$">UCASE$</a>, <a href="LCASE$" title="LCASE$">LCASE$</a></li>
<li><a href="COMMANDCOUNT" title="COMMANDCOUNT">_COMMANDCOUNT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211032
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.069 seconds
Preprocessor visited node count: 251/1000000
Post‐expand include size: 2589/2097152 bytes
Template argument size: 359/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   43.939      1 -total
 15.06%    6.618      2 Template:OutputStart
 13.19%    5.794      1 Template:PageDescription
 12.87%    5.653      2 Template:OutputEnd
 11.52%    5.061      1 Template:PageSeeAlso
  7.70%    3.383     30 Template:Cl
  6.07%    2.669      1 Template:PageNavigation
  6.03%    2.651      1 Template:PageSyntax
  5.43%    2.384      1 Template:PageExamples
  4.81%    2.112      1 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:417-0!canonical and timestamp 20240714211032 and revision id 8921.
 -->
</div>
</div>
</div>
</div>
</body>
</html>