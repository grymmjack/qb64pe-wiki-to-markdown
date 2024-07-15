<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CONSOLEINPUT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CONSOLEINPUT rootpage-CONSOLEINPUT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CONSOLEINPUT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CONSOLEINPUT</a> function is used to monitor any new mouse or keyboard input coming from a $CONSOLE window. It must be called in order for <a href="CINP" title="CINP">_CINP</a> to return valid values. Windows-only.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>infoExists%%</i> = <a class="mw-selflink selflink">_CONSOLEINPUT</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns 1 if new keyboard information is available, 2 if mouse information is available, otherwise it returns 0.</li>
<li>Must be called before reading any of the other mouse functions and before reading <a href="CINP" title="CINP">_CINP</a>.</li>
<li>To clear all previous input data, read <a class="mw-selflink selflink">_CONSOLEINPUT</a> in a loop until it returns 0.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Reading individual key strokes from a console window (Windows).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$CONSOLE" title="$CONSOLE"><span style="color:#55FF55;">$CONSOLE</span></a>:<a href="ONLY" title="ONLY"><span style="color:#4593D8;">ONLY</span></a>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <a href="CONSOLE" title="CONSOLE"><span style="color:#4593D8;">_CONSOLE</span></a>: <a href="SOURCE" title="SOURCE"><span style="color:#4593D8;">_SOURCE</span></a> <a href="CONSOLE" title="CONSOLE"><span style="color:#4593D8;">_CONSOLE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Press any key, and I'll give you the scan code for it.  &lt;ESC&gt; quits the demo."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    x = <a class="mw-selflink selflink"><span style="color:#4593D8;">_CONSOLEINPUT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">'read only keyboard input ( = 1)</span>
        c = <a href="CINP" title="CINP"><span style="color:#4593D8;">_CINP</span></a>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> c;
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> c = <span style="color:#F580B1;">1</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a>, <a href="CONSOLE" title="CONSOLE">_CONSOLE</a></li>
<li><a href="CINP" title="CINP">_CINP</a>, <a href="Keyboard_scancodes#INP_Scan_Codes" title="Keyboard scancodes">Scan Codes</a></li>
<li><a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEY" title="MOUSEY">_MOUSEY</a>, <a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a>, <a href="MOUSEWHEEL" title="MOUSEWHEEL">_MOUSEWHEEL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062604
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.043 seconds
Real time usage: 0.058 seconds
Preprocessor visited node count: 185/1000000
Post‐expand include size: 1827/2097152 bytes
Template argument size: 319/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 117/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   35.532      1 -total
 12.63%    4.487      1 Template:PageSeeAlso
 12.17%    4.323     17 Template:Cl
  9.02%    3.206      1 Template:PageSyntax
  7.83%    2.782      1 Template:Parameter
  7.76%    2.758      1 Template:CodeEnd
  7.67%    2.725      4 Template:Text
  7.33%    2.604      1 Template:PageNavigation
  7.05%    2.505      1 Template:CodeStart
  7.00%    2.488      1 Template:Cm
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:98-0!canonical and timestamp 20240715062604 and revision id 8291.
 -->
</div>
</div>
</div>
</div>
</body>
</html>