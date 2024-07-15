<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SHELL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SHELL rootpage-SHELL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SHELL</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">SHELL</a> statement allows a program to run external programs or command line statements in Windows, macOS and Linux.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">SHELL</a> [<i>DOSCommand$</i>]</dd>
<dd><a class="mw-selflink selflink">SHELL</a> [<b>_DONTWAIT</b>] [<b>_HIDE</b>] [<i>DOSCommand$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If the <i>DOSCommand$</i> <a href="STRING" title="STRING">STRING</a> parameter isn't used, the "command console" is opened and execution is halted until the user closes it manually.</li>
<li>If <a href="DONTWAIT" title="DONTWAIT">_DONTWAIT</a> is used, the <b>QB64</b> program doesn't wait for the SHELLed program/command to end.</li>
<li>When the <a href="HIDE" title="HIDE">_HIDE</a> action is used, the <a href="CONSOLE" title="CONSOLE">console</a> window is hidden and screen info can be "redirected" (using redirection characters like &gt;) to a file (recommended).</li>
<li>Commands are external commands, according to the user's operating system, passed as <a href="STRING" title="STRING">strings</a> enclosed in quotes or string variables.</li>
<li>Commands can be a mixture of <a href="STRING" title="STRING">strings</a> and string variables added together using the + <a href="Concatenation" title="Concatenation">concatenation</a> operator.</li>
<li>Command text can be in upper or lower case. Use single spacing between items and options.</li>
<li><b>QB64</b> automatically uses CMD /C when using <a class="mw-selflink selflink">SHELL</a>, but it is allowed in a command string. <span style="color:red;">Note: CMD alone may lock up program.</span>
<ul><li><b>Note: Some commands may not work without adding CMD /C to the start of the command line.</b></li></ul></li>
<li><b>QB64</b> program screens will not get distorted, minimized or freeze the program like QBasic fullscreen modes would.</li>
<li><b>QB64</b> can use long path folder names and file names and <a class="mw-selflink selflink">SHELL</a> command lines can be longer than 124 characters.</li>
<li>In Windows, use additional <a href="CHR$" title="CHR$">CHR$</a>(34) quotation marks around folder or file names that contain spaces.</li>
<li>For other operating systems, both the quotation mark character and the apostrophe can be used to enclose a file name that contains spaces.</li>
<li><b>NOTE: Use <a href="CHDIR" title="CHDIR">CHDIR</a> instead of CD as SHELL commands cannot affect the current program path.</b></li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li><b>QBasic BAS files could be run like compiled programs without returning to the IDE when <a href="SYSTEM" title="SYSTEM">SYSTEM</a> was used to <a href="END" title="END">end</a> them.</b></li>
<li>A user would invoke it with <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">SHELL "QB.EXE /L /RUN program.BAS"</span></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> When working with file or folder names with spaces, add quotation marks around the path and/or file name with <a href="CHR$" title="CHR$">CHR$</a>(34).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">SHELL</span></a> <a href="HIDE" title="HIDE"><span style="color:#4593D8;">_HIDE</span></a> "dir " + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(34) + "free cell.ico" + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(34) + " /b &gt; temp.dir"
<a class="mw-selflink selflink"><span style="color:#4593D8;">SHELL</span></a> "start Notepad temp.dir" ' display temp file contents in Notepad window
</pre>
</td></tr></tbody></table>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">Free Cell.ico
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Opening a Windows program (Notepad) to read or print a Basic created text file.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a file name to read in Notepad: ", filename$
<a class="mw-selflink selflink"><span style="color:#4593D8;">SHELL</span></a> "CMD /C start /max notepad " + filename$  ' display in Notepad full screen in XP or NT
'<a class="mw-selflink selflink"><span style="color:#4593D8;">SHELL</span></a> "start /min notepad /p " + filename$ ' taskbar print using QB64 CMD /C not necessary
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Notepad is an easy program to open in Windows as no path is needed. Windows NT computers, including XP, use CMD /C where older versions of DOS don't require any command reference. The top command opens Notepad in a normal window for a user to view the file. They can use Notepad to print it. The second command places Notepad file in the taskbar and prints it automatically. The filename variable is added by the program using proper spacing.</dd></dl>
<dl><dd><dl><dd><ul><li><b>Start</b> is used to allow a Basic program to run without waiting for Notepad to be closed.</li>
<li><b>/min</b> places the window into the taskbar. <b>/max</b> is fullscreen and no option is a normal window.</li>
<li>Notepad's <b>/p</b> option prints the file contents, even with USB printers.</li></ul></dd></dl></dd></dl>
<p>
<i>Example 3:</i> Function that returns the program's current working path.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> currentpath$ = Path$ ' function call saves a path for later program use
 PRINT currentpath$
 <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> Path$
   <a class="mw-selflink selflink"><span style="color:#4593D8;">SHELL</span></a> <a href="HIDE" title="HIDE"><span style="color:#4593D8;">_HIDE</span></a> "CD &gt; D0S-DATA.INF"   'code to hide window in <b>QB64</b>
   <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "D0S-DATA.INF" FOR <a class="mw-redirect" href="APPEND" title="APPEND"><span style="color:#4593D8;">APPEND</span></a> AS #1  'this may create the file
        L% = <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(1)          'verify that file and data exist
   <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
   <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> L% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>                       'read file if it has data
     <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "D0S-DATA.INF" FOR <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> AS #1
     <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT</span></a> #1, line$           'read only line in file
     Path$ = line$ + "\"            'add slash to path so only a filename needs added later
     <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
   <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> : Path = ""                 'returns zero length string if path not found
   END IF
   <a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> "D0S-DATA.INF"              'deleting the file is optional
 <a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <b>SHELL "CD"</b> statement requests the current working path. This info is normally printed to the screen, but the <b>&gt;</b> pipe character sends the information to the DOS-DATA.INF file instead(<b>QB64</b> can use <a href="HIDE" title="HIDE">_HIDE</a> to not display the DOS window). The function uses the <a href="OPEN" title="OPEN">OPEN</a> FOR <a class="mw-redirect" href="APPEND" title="APPEND">APPEND</a> mode to check for the file and the data(<a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)">INPUT</a> would create an error if file does not exist). The current path is listed on one line of the file. The file is opened and <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)">LINE INPUT</a> returns one line of the file text. The function adds a "\" so that the Path$ returned can be used in another file statement by just adding a file name. Save the Path$ to another variable for later use when the program has moved to another directory.</dd>
<dd>In <b>QB64</b> you can simply use the <a href="CWD$" title="CWD$">_CWD$</a> statement for the same purpose of the example above.</dd></dl>
<p>
<i>Example 4:</i> Determining if a drive or path exists. Cannot use with a file name specification.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="LINE_INPUT" title="LINE INPUT"><span style="color:#4593D8;">LINE INPUT</span></a> "Enter a drive or path (no file name): ", DirPath$
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> PathExist%(DirPath$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> PRINT "Drive Path exists!" <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> PRINT "Drive Path does not exist!"
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> PathExist% (Path$)
PathExist% = 0
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Path$) = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a> 'no entry
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(<a href="ENVIRON$" title="ENVIRON$"><span style="color:#4593D8;">ENVIRON$</span></a>("OS")) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> CMD$ = "CMD /C " <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> CMD$ = "COMMAND /C "
<a class="mw-selflink selflink"><span style="color:#4593D8;">SHELL</span></a> <a href="HIDE" title="HIDE"><span style="color:#4593D8;">_HIDE</span></a> CMD$ + "If Exist " + Path$ + "
ul echo yes &gt; D0S-DATA.INF"
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "D0S-DATA.INF" <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="APPEND" title="APPEND"><span style="color:#4593D8;">APPEND</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> PathExist% = -1             'yes will be in file if path exists
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> "D0S-DATA.INF"               'delete data file optional
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation: IF Exist</i> checks for the drive path. <i>\Nul</i> allows an emply folder at end of path. <i>Echo</i> prints <b>yes</b> in the file if it exists.</dd>
<dd>In <b>QB64</b> you can simply use the <a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a> statement for the same purpose of the example above.</dd></dl>
<p>
<i>Snippet 1:</i> When looking for <b>printers</b> this command gives you a file list with the default printer marked as <b>TRUE</b>:
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext"><a class="mw-selflink selflink"><span style="color:blue;">SHELL</span></a> <a href="HIDE" title="HIDE"><span style="color:blue;">_HIDE</span></a> "CMD /C" + "wmic printer get name,default &gt; default.txt"
</pre>
</td></tr></tbody></table>
<p><b>Created file's text:</b>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">Default  Name
  FALSE    Microsoft XPS Document Writer
  TRUE     HP Photosmart C7200 series
  FALSE    HP Officejet Pro 8600
  FALSE    Fax
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a> could be used to find the printer names as <a href="STRING" title="STRING">STRING</a> variables.</dd></dl>
<p>
<i>Snippet 2:</i> Here is the code to set the default printer to the "HP Officejet Pro 8600":
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">SHELL _HIDE "CMD /C" + "wmic printer where name='HP Officejet Pro 8600' call setdefaultprinter"
</pre>
</td></tr></tbody></table>
<dl><dd>After executing this program, and then running the first snippet again, we see the following <b>contents of the text file:</b></dd></dl>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">Default  Name
  FALSE    Microsoft XPS Document Writer
  FALSE    HP Photosmart C7200 series
  TRUE     HP Officejet Pro 8600
  FALSE    Fax
</pre>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="More_examples">More examples</span></h3>
<ul><li><a href="FILELIST$_(function)" title="FILELIST$ (function)">FILELIST$ (function)</a></li>
<li><a href="Windows_Libraries#File_Exist" title="Windows Libraries">FileExist Library Function</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1282" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="SHELL_(function)" title="SHELL (function)">SHELL (function)</a>, <a href="SHELLHIDE" title="SHELLHIDE">_SHELLHIDE</a></li>
<li><a href="FILES" title="FILES">FILES</a>, <a href="CHDIR" title="CHDIR">CHDIR</a>, <a href="MKDIR" title="MKDIR">MKDIR</a></li>
<li><a href="CWD$" title="CWD$">_CWD$</a>, <a href="STARTDIR$" title="STARTDIR$">_STARTDIR$</a></li>
<li><a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a>, <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a></li>
<li><a href="RMDIR" title="RMDIR">RMDIR</a>, <a href="NAME" title="NAME">NAME</a>, <a href="KILL" title="KILL">KILL</a>, <a href="RUN" title="RUN">RUN</a></li>
<li><a href="HIDE" title="HIDE">_HIDE</a>, <a href="DONTWAIT" title="DONTWAIT">_DONTWAIT</a></li>
<li><a href="CONSOLE" title="CONSOLE">_CONSOLE</a>, <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a></li>
<li><a href="$SCREENHIDE" title="$SCREENHIDE">$SCREENHIDE</a>, <a href="$SCREENSHOW" title="$SCREENSHOW">$SCREENSHOW</a></li>
<li><a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a>, <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a></li>
<li><a href="FILELIST$" title="FILELIST$">FILELIST$</a>, <a href="PDS(7.1)_Procedures#DIR$" title="PDS(7.1) Procedures">DIR$</a></li>
<li><a href="Windows_Libraries#File_Dialog_Boxes" title="Windows Libraries">Windows Open and Save Dialog Boxes</a></li>
<li><a href="C_Libraries#Console_Window" title="C Libraries">C Console Library</a></li>
<li><a href="Windows_Printer_Settings" title="Windows Printer Settings">Windows Printer Settings</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192545
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.064 seconds
Real time usage: 0.079 seconds
Preprocessor visited node count: 646/1000000
Post‐expand include size: 4687/2097152 bytes
Template argument size: 713/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   39.677      1 -total
  9.33%    3.701     51 Template:Cl
  7.28%    2.889      1 Template:PageSyntax
  6.79%    2.694      2 Template:Parameter
  6.08%    2.412      1 Template:PageDescription
  5.94%    2.356      1 Template:Text
  5.37%    2.129      4 Template:CodeEnd
  5.16%    2.047      2 Template:Cb
  5.15%    2.045      1 Template:PageNavigation
  5.09%    2.020      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:140-0!canonical and timestamp 20240714192545 and revision id 8924.
 -->
</div>
</div>
</div>
</div>
</body>
</html>