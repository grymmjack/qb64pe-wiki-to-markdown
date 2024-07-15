<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_WINDOWHANDLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WINDOWHANDLE rootpage-WINDOWHANDLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_WINDOWHANDLE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_WINDOWHANDLE</a> function returns the window handle assigned to the current program by the OS. Windows-only.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>hwnd&amp;&amp;</i> = <a class="mw-selflink selflink">_WINDOWHANDLE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The result is an <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> number assigned by Windows to your running program.</li>
<li>Use it to make <a href="Windows_Libraries" title="Windows Libraries">API calls</a> that require a window handle to be passed.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Build 20170924/68</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Showing the system-default message box in Windows.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">'Message Box Constant values as defined by Microsoft (MBType)
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_OK&amp; = 0                'OK button only
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_OKCANCEL&amp; = 1          'OK &amp; Cancel
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_ABORTRETRYIGNORE&amp; = 2  'Abort, Retry &amp; Ignore
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_YESNOCANCEL&amp; = 3       'Yes, No &amp; Cancel
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_YESNO&amp; = 4             'Yes &amp; No
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_RETRYCANCEL&amp; = 5       'Retry &amp; Cancel
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_CANCELTRYCONTINUE&amp; = 6 'Cancel, Try Again &amp; Continue
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_ICONSTOP&amp; = 16         'Error stop sign icon
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_ICONQUESTION&amp; = 32     'Question-mark icon
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_ICONEXCLAMATION&amp; = 48  'Exclamation-point icon
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_ICONINFORMATION&amp; = 64  'Letter i in a circle icon
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_DEFBUTTON1&amp; = 0        '1st button default(left)
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_DEFBUTTON2&amp; = 256      '2nd button default
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_DEFBUTTON3&amp; = 512      '3rd button default(right)
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_APPLMODAL&amp; = 0         'Message box applies to application only
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_SYSTEMMODAL&amp; = 4096    'Message box on top of all other windows
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MB_SETFOCUS&amp; = 65536      'Set message box as focus
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDOK&amp; = 1                 'OK button pressed
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDCANCEL&amp; = 2             'Cancel button pressed
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDABORT&amp; = 3              'Abort button pressed
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDRETRY&amp; = 4              'Retry button pressed
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDIGNORE&amp; = 5             'Ignore button pressed
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDYES&amp; = 6                'Yes button pressed
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDNO&amp; = 7                 'No button pressed
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDTRYAGAIN&amp; = 10          'Try again button pressed
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> IDCONTINUE&amp; = 1           'Continue button pressed
'----------------------------------------------------------------------------------------
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE DYNAMIC LIBRARY</span></a> "user32"
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> MessageBoxA&amp; (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> hwnd <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Message <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, Title <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> MBType <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">END DECLARE</span></a>
DO
  msg&amp; = 0: icon&amp; = 0: DB&amp; = 0
  <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter Message Box type(0 to 6 other Quits): ", BOX&amp;
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> BOX&amp; &lt; 0 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> BOX&amp; &gt; 6 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter Icon&amp;(0=none, 1=stop, 2=?, 3=!, 4=info): ", Icon&amp;
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> BOX&amp; <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> "Enter Default Button(1st, 2nd or 3rd): ", DB&amp;
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> DB&amp; <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> DB&amp; = DB&amp; - 1     'adjust value to 0, 1, or 2
  msg&amp; = MsgBox&amp;("Box Title", "Box text message", BOX&amp;, Icon&amp;, DB&amp;, 4096) 'on top of all windows
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Button ="; msg&amp;
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> MsgBox&amp; (Title$, Message$, BoxType&amp;, Icon&amp;, DBtn&amp;, Mode&amp;)
<a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> Icon&amp;
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 1: Icon&amp; = MB_ICONSTOP&amp;          'warning X-sign icon
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 2: Icon&amp; = MB_ICONQUESTION&amp;      'question-mark icon
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 3: Icon&amp; = MB_ICONEXCLAMATION&amp;   'exclamation-point icon
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 4: Icon&amp; = MB_ICONINFORMATION&amp;   'lowercase letter i in circle
  <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>: Icon&amp; = 0 'no icon
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> BoxType&amp; &gt; 0 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> DBtn&amp; &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'set default button as 2nd(256) or 3rd(512)
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> BoxType&amp;
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 2, 3, 6
     <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> DBtn&amp; = 2 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> Icon&amp; = Icon&amp; + MB_DEFBUTTON3&amp; <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> Icon&amp; = Icon&amp; + MB_DEFBUTTON2&amp; '3 button
    <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>: Icon&amp; = Icon&amp; + MB_DEFBUTTON2&amp; '2nd button default
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
Focus&amp; = MB_SetFocus&amp;
MsgBox&amp; = MessageBoxA&amp;(<a class="mw-selflink selflink"><span style="color:#4593D8;">_WINDOWHANDLE</span></a>, Message$, Title$, BoxType&amp; + Icon&amp; + Mode&amp; + Focus&amp;) 'focus on button
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Notice how the call to the external dynamic library function MessageBoxA&amp; passes _WINDOWHANDLE to the API and how the message box shown is created as a child of your program's window, not allowing the main window to be manipulated while the message box is open.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="WINDOWHASFOCUS" title="WINDOWHASFOCUS">_WINDOWHASFOCUS</a></li>
<li><a href="SCREENEXISTS" title="SCREENEXISTS">_SCREENEXISTS</a></li>
<li><a href="Windows_Libraries" title="Windows Libraries">Windows Libraries</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062518
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.043 seconds
Real time usage: 0.056 seconds
Preprocessor visited node count: 553/1000000
Post‐expand include size: 4661/2097152 bytes
Template argument size: 891/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.422      1 -total
 16.39%    4.985      1 Template:PageAvailability
 14.68%    4.465     75 Template:Cl
  9.55%    2.904      1 Template:PageSyntax
  7.23%    2.199      1 Template:CodeEnd
  7.02%    2.136      1 Template:PageExamples
  6.98%    2.124      1 Template:CodeStart
  6.65%    2.024      1 Template:Parameter
  6.25%    1.903      1 Template:PageNavigation
  6.20%    1.887      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:365-0!canonical and timestamp 20240715062518 and revision id 8492.
 -->
</div>
</div>
</div>
</div>
</body>
</html>