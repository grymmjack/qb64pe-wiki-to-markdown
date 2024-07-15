<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>OPEN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OPEN rootpage-OPEN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">OPEN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">OPEN</a> statement is used to open a file or <a href="OPEN_COM" title="OPEN COM">COM</a> serial communications port for program input or output.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">OPEN</a> <i>fileName$</i> [<b>FOR</b> <i>mode</i>] [{<a class="mw-redirect" href="ACCESS" title="ACCESS">ACCESS</a>|{<a href="LOCK" title="LOCK">LOCK</a>|SHARED}} [{READ|WRITE}] <a href="AS" title="AS">AS</a> [#]<i>fileNumber&amp;</i> [LEN = <i>recordLength</i>]</dd></dl>
<h3><span class="mw-headline" id="Legacy_GW-BASIC_syntax">Legacy GW-BASIC syntax</span></h3>
<dl><dd><a class="mw-selflink selflink">OPEN</a> <i>modeLetter$</i>, [#]<i>fileNumber&amp;</i>, <i>fileName$</i>[, <i>recordLength</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>fileName$</i> is a <a href="STRING" title="STRING">STRING</a> variable or literal file name (path optional) in quotes.</li>
<li>FOR mode can be: <a class="mw-redirect" href="APPEND" title="APPEND">APPEND</a> (write to end), <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> (read/write), <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)">INPUT</a> (read), <a class="mw-redirect" href="OUTPUT" title="OUTPUT">OUTPUT</a> (write new) or <a href="RANDOM" title="RANDOM">RANDOM</a> (read/write).</li>
<li>GW-BASIC's <i>modeLetter$</i> is a <a href="STRING" title="STRING">STRING</a> variable or the letter "A", "B", "I", "O" or "R" designating the OPEN modes above.</li>
<li><i>fileNumber&amp;</i> can be any <b>positive</b> <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="LONG" title="LONG">LONG</a> whole number value or an unused value determined by the <a href="FREEFILE" title="FREEFILE">FREEFILE</a> function.</li>
<li><a href="LEN" title="LEN">LEN</a> = or <i>recordLength</i> is optional to denote the RANDOM file record byte length (default = 128) or sequential (default = 512) load buffer.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>QB64</b> can open as many files as your computer memory can handle. QBasic could only open about 15 at a time.</li>
<li><b>QB64 will allocate 4 bytes of memory for every possible file number up to the highest number used in a program.</b></li>
<li><i>mode</i> defaults to RANDOM if the <i>mode</i> or FOR access statement is omitted. (see open modes described below)</li>
<li><b>Only the <i>fileName$</i>, <i>fileNumber&amp;</i> and LEN = <i>recordLength</i> values can use variable values in the QBasic syntax.</b></li>
<li>If <a href="LEN" title="LEN">LEN</a> = is ommitted, sequential file record sizes default to 512 and <a href="RANDOM" title="RANDOM">RANDOM</a> to 128 bytes in QBasic.</li>
<li><i>fileName$</i> can be up to 255 characters with no limit on file name extension length in <b>QB64</b>.</li>
<li>Once a file or port is opened, it can be used in any program procedure using the assigned file number.</li>
<li>The <b>"SCRN:"</b> device is supported in <b>version 1.000 and up</b> (see Example 3).</li>
<li><b>Devices such as "KYBD:", "CONS:", "COMn" and "LPTn:" are <a href="Keywords_currently_not_supported_by_QB64" title="Keywords currently not supported by QB64">not supported in QB64.</a></b>.</li></ul>
<dl><dd><b>Note:</b> OPEN "LPTn" is not supported by QB64, but may be supported directly by your operating system.</dd></dl>
<ul><li><a href="OPEN_COM" title="OPEN COM">OPEN COM</a> can also be used for serial port access in <b>QB64</b>.</li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li>Illegal <b>QB64</b> Windows filename characters are <b> " * / \ | ? : &lt; &gt; </b>. Multiple dots (periods) are allowed.</li>
<li>Possible OPEN <a href="ERROR_Codes" title="ERROR Codes">errors</a> include "Bad file name or number", "Bad File Mode", "File Not Found" or "Path Not Found".
<ul><li>An OPEN file not found error may occur if <a href="CHR$" title="CHR$">CHR$</a>(0) to (31) are used in a Windows file name.</li></ul></li>
<li><b>QB64</b> does not have DOS file name limitations.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Details">Details</span></h2>
<h3><span class="mw-headline" id="File_ACCESS_and_LOCK_Permissions">File ACCESS and LOCK Permissions</span></h3>
<ul><li><a class="mw-redirect" href="ACCESS" title="ACCESS">ACCESS</a> clause limits file access to READ, WRITE or READ WRITE on a network.</li>
<li><a href="LOCK_(access)" title="LOCK (access)">LOCK</a> clause can specify SHARED or a LOCK READ or LOCK WRITE file lock in an OPEN statement working on a network.</li>
<li>A separate <a href="LOCK" title="LOCK">LOCK</a> statement can lock or <a href="UNLOCK" title="UNLOCK">UNLOCK</a> file access on a network using a format that can lock specific records.</li>
<li>If another process already has access to a specified file, program access is denied for that file OPEN access. A "Permission Denied" error 70 will be returned. A network program must be able to handle a denial of access error.</li></ul>
<h3><span class="mw-headline" id="File_Access_Modes">File Access Modes</span></h3>
<ul><li>FOR mode can be:
<ul><li><b>OUTPUT</b>: Sequential mode creates a new file or erases an existing file for new program output. Use <a href="WRITE_(file_statement)" title="WRITE (file statement)">WRITE #</a> to write numerical or text data or <a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT #</a> for text. <b>OUTPUT clears files of all data</b> and clears the receive buffer on other devices such as <a href="OPEN_COM" title="OPEN COM">COM</a>.</li>
<li><b>APPEND</b>: Sequential mode creates a new file if it doesn't exist or appends program output to the end of an existing file. Use <a href="WRITE_(file_statement)" title="WRITE (file statement)">WRITE #</a> for numerical or text data or <a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT #</a> for text as in the OUTPUT mode. <b>APPEND does not remove previous data.</b></li>
<li><b>INPUT</b> : Sequential mode <b>only reads input</b> from an existing file. <b><a href="ERROR_Codes" title="ERROR Codes">File error</a> if file does not exist.</b> Use <a href="INPUT_(file_statement)" title="INPUT (file statement)">INPUT #</a> for comma separated numerical or text data and <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)">LINE INPUT #</a> or <a href="INPUT$" title="INPUT$">INPUT$</a> to only read text data. <b>Use <a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a> or <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a> to avoid errors.</b></li>
<li><b>BINARY</b>: Creates a new file when it doesn't exist or reads and writes to an existing binary file. Use <a href="GET" title="GET">GET #</a> to read or <a href="PUT" title="PUT">PUT #</a> to write byte positions simultaneously. <a href="LEN" title="LEN">LEN</a> = statements are ignored in this mode.</li>
<li><b>RANDOM</b>: Creates a new file when it doesn't exist or reads or writes to an existing random file record. Use <a href="GET" title="GET">GET #</a> or <a href="PUT" title="PUT">PUT #</a> to read or write to file records. A <a href="LEN" title="LEN">LEN</a> = statement can define the byte size of a record (no LEN statement defaults to 128 bytes)</li>
<li>Modes <b>INPUT</b>, <b>BINARY</b> and <b>RANDOM</b> allow a file to be concurrently opened in a different mode and number.</li></ul></li></ul>
<h3><span class="mw-headline" id="GW-BASIC_modes">GW-BASIC modes</span></h3>
<ul><li><i>Mode letter</i> is a variable or literal <a href="STRING" title="STRING">STRING</a> letter value as one of the following:
<ul><li>"A" = <b>APPEND</b>.</li>
<li>"B" = <b>BINARY</b>.</li>
<li>"I" = <b>INPUT</b>.</li>
<li>"O" = <b>OUTPUT</b>.</li>
<li>"R" = <b>RANDOM</b>.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Function that displays errors and the number of errors in QBasic filenames. Returns 0 when filename is OK.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> file$ = "Hello,~1.mp3"      'example call below
 <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 30: errors% = CheckName%(file$): <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "  Total Errors ="; errors%
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> CheckName% (Filename$)
  '<a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a>E: Function also displays filename errors so <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> on screen before call!
  <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> L <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, DP <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, XL <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
  L = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Filename$): DP = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(Filename$, "."): <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> DP <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> XL = L - DP 'extension
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> L = 0 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> L &gt; 12 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> DP &gt; 9 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> XL &gt; 3 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    CheckName% = -1: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Illegal format!"; : <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> L      'check each filename character"
     code% = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(Filename$, i%, 1)): <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 10      ' see ASCII codes
     <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> code%       'check for errors and highlight in red
        '<a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 34, 42 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 44, 47, 58 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 63, 91 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 93, 124: E% = E% + 1: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12 ' <b>QBasic errors</b>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 34, 42, 47, 58, 60, 62, 92, 124: E% = E% + 1: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12 ' <b>QB64 errors</b>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 46: dot% = dot% + 1: <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> dot% &gt; 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> E% = E% + 1: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12
     <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
     <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(code%);  'use <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> before <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> call to place print
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  CheckName% = E%
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Note: The QBasic character error list is commented out and the function will return invalid filenames under QB64.</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">                         <span style="color:#54FC54;">Hello</span><span style="color:red;">,</span><span style="color:#54FC54;">~1.mp3</span>  <span style="color:yellow;">Total Errors</span> = <span style="color:yellow;">1</span>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The screen output displays filename characters in green except for red comma QBasic error.</dd></dl>
<p>
<i>Example 2:</i> When <b>OPEN "SCRN:" FOR OUTPUT AS #f</b> is used, <b>PRINT #f</b> will print the text to the screen instead of to a file:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">f% = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a> 'should always be 1 at program start
<a class="mw-selflink selflink"><span style="color:#4593D8;">OPEN</span></a> "SCRN:" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="OUTPUT" title="OUTPUT"><span style="color:#4593D8;">OUTPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #f%
g% = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a> 'should always be 2 after 1
<a class="mw-selflink selflink"><span style="color:#4593D8;">OPEN</span></a> "temp.txt" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="OUTPUT" title="OUTPUT"><span style="color:#4593D8;">OUTPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #g%
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 2
    <a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #i, "Hello World, Screen and File version"
NEXT
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Linux or macOS file names can use a path destination such as ".\SCRN:" to use SCRN: as an actual file name.</dd></dl>
<p>
<i>Example 3:</i> Showcasing different file modes.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">OPEN</span></a> "test.tst" <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="OUTPUT" title="OUTPUT"><span style="color:#4593D8;">OUTPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #1, "If test.tst didn't exist:"
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #1, "A new file was created named test.tst and then deleted."
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #1, "If test.tst did exist:"
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #1, "It was overwritten with this and deleted."
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a class="mw-selflink selflink"><span style="color:#4593D8;">OPEN</span></a> "test.tst" <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(1)
<a href="INPUT_(file_statement)" title="INPUT (file statement)"><span style="color:#4593D8;">INPUT</span></a> #1, a$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a$
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> "test.tst"
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">If test.tst didn't exist:
A new file was created named test.tst and then deleted.
If test.tst did exist:
It was overwritten with this and deleted.
</pre>
</td></tr></tbody></table>
<dl><dd><b>Warning:</b> Make sure you don't have a file named test.tst before you run this or it will be overwritten.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT (file statement)</a>, <a href="INPUT_(file_statement)" title="INPUT (file statement)">INPUT (file statement)</a></li>
<li><a href="GET" title="GET">GET</a>, <a href="PUT" title="PUT">PUT</a>, <a href="WRITE_(file_statement)" title="WRITE (file statement)">WRITE (file statement)</a></li>
<li><a href="INPUT$" title="INPUT$">INPUT$</a>, <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)">LINE INPUT (file statement)</a></li>
<li><a href="CLOSE" title="CLOSE">CLOSE</a>, <a href="LOF" title="LOF">LOF</a>, <a href="EOF" title="EOF">EOF</a>, <a href="LOC" title="LOC">LOC</a></li>
<li><a href="SEEK" title="SEEK">SEEK</a>, <a href="SEEK_(function)" title="SEEK (function)">SEEK (function)</a></li>
<li><a href="OPEN_COM" title="OPEN COM">OPEN COM</a>, <a href="LEN" title="LEN">LEN</a>, <a href="RESET" title="RESET">RESET</a></li>
<li><a href="FIELD" title="FIELD">FIELD</a>, <a href="TYPE" title="TYPE">TYPE</a></li>
<li><a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a>, <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a></li>
<li><a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a>, <a href="OPENHOST" title="OPENHOST">_OPENHOST</a>, <a href="OPENCONNECTION" title="OPENCONNECTION">_OPENCONNECTION</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714101237
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.059 seconds
Real time usage: 0.073 seconds
Preprocessor visited node count: 858/1000000
Post‐expand include size: 6093/2097152 bytes
Template argument size: 1261/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 3/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   38.731      1 -total
 12.54%    4.859     86 Template:Cl
  7.10%    2.749     18 Template:Parameter
  6.73%    2.608      1 Template:PageSyntax
  6.40%    2.479      3 Template:CodeEnd
  6.21%    2.405      1 Template:PageParameters
  6.01%    2.327      1 Template:PageDescription
  5.93%    2.296      1 Template:PageExamples
  5.42%    2.099      3 Template:CodeStart
  4.88%    1.890      2 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:271-0!canonical and timestamp 20240714101237 and revision id 8156.
 -->
</div>
</div>
</div>
</div>
</body>
</html>