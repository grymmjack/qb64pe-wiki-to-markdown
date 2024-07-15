<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>INPUT$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INPUT rootpage-INPUT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">INPUT$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">INPUT$</a> function is used to receive data from the user's keyboard, an open file or an open port.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">INPUT$</a>(<i>numberOfBytes%</i>[, fileOrPortNumber])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Keyboard input is limited to the <a href="INTEGER" title="INTEGER">INTEGER</a> <i>numberOfBytes%</i> (characters) designated by program.</li>
<li>The keyboard is the default device when a file or port number is omitted. The <i>numberOfBytes%</i> is number of key presses to read.</li>
<li>INPUT$ will wait until the number of bytes are read from the keyboard or port. One byte per loop is recommended with ports.</li>
<li><a href="RANDOM" title="RANDOM">RANDOM</a> opened file bytes can be up to the <a href="LEN" title="LEN">LEN</a> = recordLength statement, or 128 if no statement is used.</li>
<li>fileOrPortNumber is the number that was used in the <a href="OPEN" title="OPEN">OPEN</a> AS statement.</li>
<li>Returns <a href="STRING" title="STRING">STRING</a> values including spaces or even extended <a href="ASCII" title="ASCII">ASCII</a> characters.</li>
<li>Backspace key results in the <a href="CHR$" title="CHR$">CHR$</a>(8) character being added to an entry.</li>
<li>Use <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , , 1</span> to view the cursor entry. Turn the cursor off using <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , , 0</span>.</li>
<li>Use <a href="DEST" title="DEST">_DEST</a> <a href="CONSOLE" title="CONSOLE">_CONSOLE</a> before INPUT$ is used  to receive input from a <a href="$CONSOLE" title="$CONSOLE">console</a> window.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li><i>numberOfBytes%</i> could not exceed 32767 in <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> files or a QBasic error would occur.</li>
<li>Ctrl + Break would not interrupt the QBasic program until there was a full INPUT$ key entry. In <b>QB64</b> Ctrl + Break will immediately exit a running program.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> A keyboard limited length entry can be made with a fixed blinking cursor. Entry must be completed before it can be shown.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 10, 1         'display fixed cursor at location
year$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">INPUT$</span></a>(4)        'waits until all 4 digits are entered
PRINT year$              'display the text entry
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Reading bytes from a text file for an 80 wide screen mode.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 5, 5, 1                    'locate and display cursor
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "Diary.txt" FOR <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> AS #1  'open existing text file
text$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">INPUT$</span></a>(70, 1)
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 5, 6, 0: PRINT text$       'print text and turn cursor off
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Getting the entire text file data as one string value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "Diary.txt FOR <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> AS #1  'open an existing file up to 32767 bytes
IF <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(1) &lt;= 32767 THEN Text$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">INPUT$</span></a>(LOF(1), 1)
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The IF statement gets the entire contents when the file size is less than 32768. The program can then work with the string by using <a href="MID$_(function)" title="MID$ (function)">MID$</a> or <a href="INSTR" title="INSTR">INSTR</a>. Note: A text file string will also have <b>CrLf</b> line break end characters <a href="CHR$" title="CHR$">CHR$</a>(13) + <a href="CHR$" title="CHR$">CHR$</a>(10).</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INPUT" title="INPUT">INPUT</a>, <a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a> <span style="color:#777777;">(keyboard input)</span></li>
<li><a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)">INPUT (file mode)</a>, <a href="INPUT_(file_statement)" title="INPUT (file statement)">INPUT #</a>, <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)">LINE INPUT #</a> <span style="color:#777777;">(file input)</span></li>
<li><a href="OPEN" title="OPEN">OPEN</a>, <a href="LOC" title="LOC">LOC</a> <span style="color:#777777;">(file)</span></li>
<li><a href="LOCATE" title="LOCATE">LOCATE</a> <span style="color:#777777;">(cursor on/off)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192448
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.057 seconds
Real time usage: 0.124 seconds
Preprocessor visited node count: 212/1000000
Post‐expand include size: 2204/2097152 bytes
Template argument size: 274/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   98.165      1 -total
 13.96%   13.705      1 Template:PageDescription
 13.72%   13.468      5 Template:Parameter
 12.24%   12.020     14 Template:Cl
 11.77%   11.551      2 Template:InlineCode
  8.76%    8.601      1 Template:PageExamples
  7.65%    7.513      1 Template:PageSeeAlso
  7.28%    7.149      4 Template:Text
  6.00%    5.887      2 Template:InlineCodeEnd
  4.55%    4.462      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:477-0!canonical and timestamp 20240714192448 and revision id 8136.
 -->
</div>
</div>
</div>
</div>
</body>
</html>