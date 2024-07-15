<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ENVIRON$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ENVIRON rootpage-ENVIRON skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ENVIRON$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">ENVIRON$</a> function returns a <a href="STRING" title="STRING">STRING</a> environmental value from <b>Windows'</b> environmental settings list.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>setting$</i> = <a class="mw-selflink selflink">ENVIRON$</a>({<i>listIndex%</i>|<i>systemID$</i>})</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function can use an <a href="INTEGER" title="INTEGER">INTEGER</a> <i>listIndex%</i> value or <a href="STRING" title="STRING">STRING</a> <i>systemID$</i> parameter.</li>
<li><i>listIndex%</i> refers to the number order of the environmental list. Returns are not in any particular numerical order.</li>
<li><i>systemID$</i> is the specific <a href="STRING" title="STRING">STRING</a> parameter requested. Returns only the specified environmental <a href="STRING" title="STRING">STRING</a> setting:
<ul><li>"BLASTER" = current Sound Blaster settings if installed.</li>
<li>"COMPUTERNAME" or "USERDOMAIN" = OEM PC serial number or the computer name assigned by owner.</li>
<li>"HOMEDRIVE" or "SystemDrive" = Windows root drive, normally C: on single partition drives.</li>
<li>"HOMEPATH" = current user's Administrator or the single user's "OWNER" folder path.</li>
<li>"OS" = Windows Operating System version. Often WindowsNT in modern computers.</li>
<li>"PATH" = full path setting that Windows uses to look for file extensions in PATHEXT below.</li>
<li>"PATHEXT = Windows extensions used:  COM, EXE, BAT, CMD, VBS, VBE, JS, JSE, WSF, WSH, MSC</li>
<li>"PROCESSOR_ARCHITECTURE" = x86 for 32 or 64 bit.</li>
<li>"PROGRAMFILES" = path to <i>Program files</i> folder, normally "C:\PROGRAM FILES"</li>
<li>"PROMPT" = normally "$P$G" on Windows NT.</li>
<li>"SYSTEMROOT" or "windir" = path to the Windows folder including the drive letter like "C:\WINDOWS"</li>
<li>"TEMP" or "TMP" = path to TEMP folder. "C:\TEMP" or the user specific temp folder on later versions.</li>
<li>"USERNAME" = current Administrator name or "OWNER".</li></ul></li></ul>
<dl><dd><i>Note:</i> There are other possible system settings that are not listed or never used on older versions. Run <i>Example 1</i> below for a complete list in your system.</dd></dl>
<ul><li><i>Note:</i> <b>QB64</b> may not return the same environment list as QBasic or SET did in DOS.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Viewing the list of environmental parameter settings using a counter loop like SET does in DOS.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  i = i + 1
  setting$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">ENVIRON$</span></a>(i) ' get a setting from the list
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> setting$
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> i <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 20 = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press a key": <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> setting$ = ""
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">ALLUSERSPROFILE=C:\ProgramData
COMPUTERNAME=TED-LAPTOP
ComSpec=C:\WINDOWS\system32\cmd.exe
HOMEDRIVE=C:
HOMEPATH=\Users\Ted
LOCALAPPDATA=C:\Users\Ted\AppData\Local
OS=Windows_NT
Path=C:\PROGRAMDATA\ORACLE\JAVA\JAVAPATH;C:\WINDOWS\SYSTEM32;C:\WINDOWS;
C:\WINDOWS\SYSTEM32\WBEM;C:\WINDOWS\SYSTEM32\WINDOWSPOWERSHELL\V1.0\;C:\
WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32
\WindowsPowerShell\v1.0\
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
PROCESSOR_ARCHITECTURE=x86
PROCESSOR_IDENTIFIER=x86 Family 6 Model 14 Stepping 8, GenuineIntel
ProgramFiles=C:\Program Files
PROMPT=$P$G
PSModulePath=C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules\
SystemRoot=C:\WINDOWS
TEMP=C:\Users\TED\AppData\Local\Temp
TMP=C:\Users\TED\AppData\Local\Temp
USERDOMAIN=TED-LAPTOP
USERNAME=Ted
USERPROFILE=C:\Users\Ted
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Windows environmental settings are listed alphabetically, 20 at a time. <b>QB64 may not read all of them or may return an empty string.</b> The settings above were returned with SET in DOS. PROMPT returned nothing where SET returned $P$G.</dd></dl>
<p>
<i>Example 2:</i> Creating a shortcut on a user's desktop for QB64.EXE using the program's icon. Must be run in program's folder to work!
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">'=== Enter the EXE file and ICON or BMP image for the shortcut.
Program$ = "QB64.EXE"  '&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; Enter the <b>exact</b> program name for shortcut
ICON$ = "QB64ICON.BMP" '&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; Enter icon or bitmap to use from program's folder
DeskTopShortcut Program$, ICON$
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>             '====== END DEMO CODE ======
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> DeskTopShortcut (Program$, ICON$)
f = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a>
<a href="SHELL" title="SHELL"><span style="color:#4593D8;">SHELL</span></a> <a href="HIDE" title="HIDE"><span style="color:#4593D8;">_HIDE</span></a> "CD &gt; PRGMDIR.INF"  'get the current program path
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "PRGMDIR.INF" <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #f
<a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT</span></a> #f, PATH$
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #f
<a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> "PRGMDIR.INF"
PATH$ = PATH$ + "\": FILE$ = PATH + Program$
PRINT PATH$                         'DEMO print
A$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">ENVIRON$</span></a>("HOMEDRIVE")          '=== Get Current User setting from Environment.
B$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">ENVIRON$</span></a>("HOMEPATH")
C$ = A$ + B$                        'shortcut to user's desktop if found
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> C$ = "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> C$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">ENVIRON$</span></a>("ALLUSERSPROFILE") 'try desktop for all users
PRINT C$                            'DEMO print
URLFILE$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(Program$, 1, <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(Program$, ".")) + "URL" 'change EXE to URL
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> C$ &gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
     SHORTCUT$ = C$ + "\Desktop\" + URLFILE$ 'create filename for the desktop
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> SHORTCUT$ = PATH$ + URLFILE$   'if all else fails put in program folder
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
PRINT SHORTCUT                      'DEMO print
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> SHORTCUT$ <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="APPEND" title="APPEND"><span style="color:#4593D8;">APPEND</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #f
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(f) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #f: <a href="EXIT_SUB" title="EXIT SUB"><span style="color:#4593D8;">EXIT SUB</span></a>   '=== if filesize is NOT Zero don't overwrite!
Q$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(34)                       '=== Write URL Shortcut file info.
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #f, "[InternetShortcut]"                    'URL type
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #f, "URL=" + Q$ + "file://" + FILE$ + Q$    'URL program file
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #f, "WorkingDirectory=" + Q$ + PATH$ + Q$   'Working path
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #f, "IconIndex = " + Q$ + "0" + Q$          '0 is first index
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #f, "IconFile = " + Q$ + PATH$ + ICON$ + Q$ 'Icon path in working folder
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #f
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The SUB program finds the current program's path and user's desktop path. It then creates the shortcut on the desktop with a program icon. The custom icon should be in the program's folder. If an environmental path is not found, the shortcut is placed in the program's folder. The SUB can be added to any program.</dd>
<dd><span style="color:#777777;"><b>NOTE:</b> A temorary file named PRGMDIR.INF is created and deleted in the example above.</span></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ENVIRON" title="ENVIRON">ENVIRON</a> (statement)</li>
<li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICE$" title="DEVICE$">_DEVICE$</a></li>
<li><a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="OS$" title="OS$">_OS$</a></li>
<li><a href="Windows_Environment" title="Windows Environment">Windows Environment</a></li>
<li><a href="Windows_Libraries#Windows_User" title="Windows Libraries">Windows User Paths Library</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061302
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.052 seconds
Real time usage: 0.088 seconds
Preprocessor visited node count: 424/1000000
Post‐expand include size: 3903/2097152 bytes
Template argument size: 838/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   56.404      1 -total
 10.87%    6.130     51 Template:Cl
 10.86%    6.128      1 Template:PageNavigation
  9.50%    5.359      1 Template:OutputEnd
  9.17%    5.171      1 Template:PageSeeAlso
  8.32%    4.694      1 Template:PageExamples
  8.15%    4.596      1 Template:Small
  7.61%    4.294      1 Template:Text
  6.69%    3.774      2 Template:CodeStart
  4.75%    2.682      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:463-0!canonical and timestamp 20240715061302 and revision id 8125.
 -->
</div>
</div>
</div>
</div>
</body>
</html>