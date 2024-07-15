<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CINP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CINP rootpage-CINP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CINP</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CINP</a> function returns keyboard key press codes from a <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> window. Windows-only.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>keycode&amp;</i> = <a class="mw-selflink selflink">_CINP</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Return values are the same as the ones for <a href="INP" title="INP">INP</a> when used to read keyboard input. See table below.</li>
<li>Negative values returned indicate that a key was released or a lock function key has been turned off.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">'                            <b>Extended Keyboard Press Scancodes</b>
'
' <b>Esc  F1 F2 F3 F4 F5 F6 F7 F8 F9 F10  F11 F12   SysReq ScrL Pause</b>
'  1   59 60 61 62 63 64 65 66 67 68   87  88     0     70    29
' <b>`~  1! 2@ 3# 4$ 5% 6^ 7&amp; 8* 9( 0) -_ =+ BkSpc  Insert Home PgUp   NumL   /     *    -</b>
'  41 2  3  4  5  6  7  8  9  10 11 12 13  14     82    71    73     69    53    55   74
' <b>Tab  Q  W  E  R  T  Y  U  I  O  P  [{ ]} \|    Delete End  PgDn   7/Home 8/▲  9/PU  + </b>
'  15  16 17 18 19 20 21 22 23 24 25 26 27 43     83    79    81     71    72    73   78
' <b>CapL  A  S  D  F  G  H  J  K  L  ;: '"  Enter                     4/◄-   5    6/-►  E</b>
'  58   30 31 32 33 34 35 36 37 38 39 40   28                        75    76    77   <b>n</b>
' <b>Shift  Z  X  C  V  B  N  M  ,&lt; .&gt; /?    Shift         ▲           1/End  2/▼  3/PD  t</b>
'  42    44 45 46 47 48 49 50 51 52 53     54           72           79    80    81   <b>e</b>
' <b>Ctrl Win Alt    Spacebar    Alt Win Menu Ctrl     ◄-  ▼   -►      0/Insert    ./Del r</b>
'  29  <span style="color:purple;">91</span>  56        57       56  <span style="color:purple;">92   93</span>  29       75  80  77       82          83   28
'
</pre>
</td></tr></tbody></table>
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
    x = <a href="CONSOLEINPUT" title="CONSOLEINPUT"><span style="color:#4593D8;">_CONSOLEINPUT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">'read only keyboard input ( = 1)</span>
        c = <a class="mw-selflink selflink"><span style="color:#4593D8;">_CINP</span></a>
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
<li><a href="CONSOLEINPUT" title="CONSOLEINPUT">_CONSOLEINPUT</a></li>
<li><a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEY" title="MOUSEY">_MOUSEY</a>, <a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a>, <a href="MOUSEWHEEL" title="MOUSEWHEEL">_MOUSEWHEEL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193330
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 204/1000000
Post‐expand include size: 1973/2097152 bytes
Template argument size: 336/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 117/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.898      1 -total
  9.41%    2.062     17 Template:Cl
  8.13%    1.781      1 Template:PageSyntax
  7.38%    1.616      6 Template:Text
  7.35%    1.610      1 Template:Cm
  7.06%    1.546      1 Template:CodeStart
  6.85%    1.500      1 Template:PageSeeAlso
  6.85%    1.499      1 Template:FixedStart
  6.76%    1.480      1 Template:CodeEnd
  6.67%    1.461      1 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:84-0!canonical and timestamp 20240714193330 and revision id 8277.
 -->
</div>
</div>
</div>
</div>
</body>
</html>