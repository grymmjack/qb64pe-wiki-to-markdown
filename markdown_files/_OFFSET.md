<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_OFFSET - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OFFSET rootpage-OFFSET skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_OFFSET</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_OFFSET</a> variable type stores the location of a value in memory. The byte size varies as required by the system.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DIM" title="DIM">DIM</a> variable <a href="AS" title="AS">AS</a> <b>_OFFSET</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>_OFFSET types can be created as signed or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> at the programmer's discretion.</li>
<li>The type suffix for _OFFSET is <b>%&amp;</b> which designates the integer value's flexible size.</li>
<li>Offset values are only useful when used in conjunction with <a href="MEM" title="MEM">_MEM</a> or <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a> procedures.</li>
<li>OFFSET values are used as a part of the <a href="MEM" title="MEM">_MEM</a> variable <a href="Variable_Types" title="Variable Types">type</a> in QB64. Variable.OFFSET returns or sets the current position in memory.</li>
<li>API <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">LIBRARY</a> parameter or <a href="TYPE" title="TYPE">type</a> names may include <b>lp, ptr</b> or <b>p</b> which designates them as a pointer type.</li>
<li><b>Warning: _OFFSET values cannot be cast to other variable type values reliably.</b></li>
<li><b>Warning: Variable length <a href="STRING" title="STRING">STRING</a> values can move about in memory at any time.</b> If you get the _OFFSET of a variable length sting on one code line and use it on the next it may not be there anymore.<b> To be safe, move variable length strings into fixed length strings first.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> The SHBrowseForFolder function receives information about the folder selected by the user in Windows XP and 7.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE CUSTOMTYPE LIBRARY</span></a>
    <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> FindWindow&amp; (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> ClassName AS <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a>, WindowName$)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE</span></a>
<a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "Super Window"
hwnd&amp; = FindWindow(0, "Super Window" + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0))
<a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> BROWSEINFO  'typedef struct _browseinfo '<a class="external text" href="http://msdn.microsoft.com/en-us/library/bb773205%28v=vs.85%29.aspx" rel="nofollow">Microsoft MSDN</a>
  hwndOwner <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> '              '  HWND
  pidlRoot <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a> '            '  PCIDLIST_ABSOLUTE
  pszDisplayName <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a> '      '  LPTSTR
  lpszTitle <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a> '           '  LPCTSTR
  ulFlags <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>        '  UINT
  lpfn <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a> '                '  BFFCALLBACK
  lParam <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a> '              '  LPARAM
  iImage <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> '                 '  int
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a>  'BROWSEINFO, *PBROWSEINFO, *LPBROWSEINFO;
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE DYNAMIC LIBRARY</span></a> "shell32"
  <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> SHBrowseForFolder%&amp; (x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> BROWSEINFO) '<a class="external text" href="http://msdn.microsoft.com/en-us/library/bb762115%28v=vs.85%29.aspx" rel="nofollow">Microsoft MSDN</a>
  <a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> SHGetPathFromIDList (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> lpItem <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a>, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> szDir <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a>) '<a class="external text" href="http://msdn.microsoft.com/en-us/library/bb762194%28VS.85%29.aspx" rel="nofollow">Microsoft MSDN</a>
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">END DECLARE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> b <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> BROWSEINFO
b.hwndOwner = hwnd
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> s <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 1024
b.pszDisplayName = <a href="OFFSET_(function)" title="OFFSET (function)"><span style="color:#4593D8;">_OFFSET</span></a>(s$)
a$ = "Choose a folder!!!" + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0)
b.lpszTitle = <a href="OFFSET_(function)" title="OFFSET (function)"><span style="color:#4593D8;">_OFFSET</span></a>(a$)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> o <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_OFFSET</span></a>
o = SHBrowseForFolder(b)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> o <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(s$, <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(s$, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0)) - 1)
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> s2 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 1024
    SHGetPathFromIDList o, <a href="OFFSET_(function)" title="OFFSET (function)"><span style="color:#4593D8;">_OFFSET</span></a>(s2$)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(s2$, <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(s2$, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0)) - 1)
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Cancel?"
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="WINDOWHANDLE" title="WINDOWHANDLE">_WINDOWHANDLE</a></li>
<li><a href="Using_OFFSET" title="Using OFFSET">Using _OFFSET</a></li>
<li><a href="OFFSET_(function)" title="OFFSET (function)">_OFFSET (function)</a>, <a href="MEM" title="MEM">_MEM</a></li>
<li><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a></li>
<li><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034427
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.038 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 495/1000000
Post‐expand include size: 4260/2097152 bytes
Template argument size: 742/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.878      1 -total
 19.40%    4.827     67 Template:Cl
  9.76%    2.428      1 Template:PageSyntax
  8.79%    2.186      1 Template:PageDescription
  8.75%    2.177      1 Template:CodeEnd
  8.33%    2.073      1 Template:CodeStart
  8.03%    1.997      1 Template:Small
  7.93%    1.974      1 Template:PageExamples
  7.26%    1.806      1 Template:PageSeeAlso
  7.06%    1.756      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:204-0!canonical and timestamp 20240715034427 and revision id 8800.
 -->
</div>
</div>
</div>
</div>
</body>
</html>