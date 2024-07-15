<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FULLSCREEN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FULLSCREEN rootpage-FULLSCREEN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FULLSCREEN</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_FULLSCREEN</a> statement attempts to make the program window fullscreen.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_FULLSCREEN</a> [<i>_STRETCH | _SQUAREPIXELS| _OFF</i>][, <i>_SMOOTH</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>_STRETCH</i> default first choice attempts to mimic QBasic's full screens if possible. <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)">_FULLSCREEN (function)</a> returns 1.</li>
<li><i>_SQUAREPIXELS</i> alternate choice enlarges the pixels into squares on some monitors. <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)">_FULLSCREEN</a> returns 2</li>
<li><i>_OFF</i> turns _FULLSCREEN off after full screen has been enabled. <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)">_FULLSCREEN (function)</a> returns 0.</li>
<li>Second optional parameter <i>_SMOOTH</i> applies antialiasing to the stretched screen.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>Set the <a href="SCREEN" title="SCREEN">SCREEN</a> mode and text <a href="WIDTH" title="WIDTH">WIDTH</a> when necessary first.</b> Otherwise there may be desktop view issues.</li>
<li>_FULLSCREEN with no parameters chooses <i>_STRETCH</i> or <i>_SQUAREPIXELS</i> (prioritizes _STRETCH to mimic QBasic if possible)</li>
<li><b>Check the fullscreen mode with the <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)">_FULLSCREEN</a> function in your programs when a method is required.</b></li>
<li>It is advisable to get <a href="INPUT" title="INPUT">input</a> from the user to confirm that fullscreen was completed or there were possible monitor incompatibilities.</li>
<li>If fullscreen is <b>not confirmed</b> with a <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)">_FULLSCREEN (function)</a> return <b>greater than 0</b>, then disable with <b>_FULLSCREEN _OFF</b>.</li>
<li><b>NOTE:</b> _FULLSCREEN can also be affected by custom <a href="FONT" title="FONT">_FONT</a> size settings and make program screens too large.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Setting the screen mode first prevents enlargement of the desktop before the program window is set:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">12</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)"><span style="color:#4593D8;">_FULLSCREEN</span></a> = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">_OFF</span></a> <span style="color:#919191;">'check that a full screen mode initialized</span>
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">100</span>, <span style="color:#F580B1;">100</span>)-(<span style="color:#F580B1;">500</span>, <span style="color:#F580B1;">400</span>), <span style="color:#F580B1;">13</span>, BF
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> How fonts and _FULLSCREEN affect the program's window size.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">0</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a href="LINE_INPUT" title="LINE INPUT"><span style="color:#4593D8;">LINE INPUT</span></a> <span style="color:#FFB100;">"Enter MODE 1) ENLARGE WINDOW  2) FULL _SQUAREPIXELS  3) FULL _STRETCH: "</span>, WMODE$
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> WMODE$ = <span style="color:#FFB100;">"1"</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"SIZE 1 TO 9: "</span>, ENLARGE%
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> ENLARGE%
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">4</span>, <span style="color:#F580B1;">5</span>: STYLE$ = <span style="color:#FFB100;">"MONOSPACE, BOLD"</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">6</span>, <span style="color:#F580B1;">7</span>, <span style="color:#F580B1;">8</span>, <span style="color:#F580B1;">9</span>: STYLE$ = <span style="color:#FFB100;">"MONOSPACE"</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>: STYLE$ = <span style="color:#FFB100;">"MONOSPACE"</span>
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> WMODE$
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#FFB100;">"1"</span>
            full = <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)"><span style="color:#4593D8;">_FULLSCREEN</span></a>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> full &gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">_OFF</span></a>
            f&amp; = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"c:\windows\fonts\lucon.ttf"</span>, <span style="color:#F580B1;">13</span> + ENLARGE%, STYLE$)
            <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> f&amp;
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#FFB100;">"2"</span>
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a class="mw-redirect" href="SQUAREPIXELS" title="SQUAREPIXELS"><span style="color:#4593D8;">_SQUAREPIXELS</span></a>
            full = <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)"><span style="color:#4593D8;">_FULLSCREEN</span></a>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> full = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> FCHECK
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#FFB100;">"3"</span>
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a class="mw-redirect" href="STRETCH" title="STRETCH"><span style="color:#4593D8;">_STRETCH</span></a>
            full = <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)"><span style="color:#4593D8;">_FULLSCREEN</span></a>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> full = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> FCHECK
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
    mode = <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)"><span style="color:#4593D8;">_FULLSCREEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_FULLSCREEN mode ="</span>; mode,
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"PRESS ESC TO END OR ENTER TO CONTINUE..."</span>
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: B$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>: <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">13</span>) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>)
    <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> ClearFont
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>)
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> ClearFont
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
FCHECK:
Z3 = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a> &lt; Z3 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> Z3 = Z3 - <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a> - Z3 &gt; <span style="color:#F580B1;">4</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
full = <a href="FULLSCREEN_(function)" title="FULLSCREEN (function)"><span style="color:#4593D8;">_FULLSCREEN</span></a>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> full = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">_OFF</span></a>: <a href="SOUND" title="SOUND"><span style="color:#4593D8;">SOUND</span></a> <span style="color:#F580B1;">100</span>, <span style="color:#F580B1;">.75</span>
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
ClearFont:
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> f&amp; &gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <span style="color:#F580B1;">16</span> <span style="color:#919191;">'select inbuilt 8x16 default font</span>
    <a href="FREEFONT" title="FREEFONT"><span style="color:#4593D8;">_FREEFONT</span></a> f&amp;
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Example 3:</i> Testing all fullscreen methods.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hello, world!"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hit 1 for windowed mode;"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"    2 for _STRETCH"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"    3 for _SQUAREPIXELS"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"    4 for _STRETCH, _SMOOTH"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"    5 for _SQUAREPIXELS, _SMOOTH"</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    k$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(k$)
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">1</span>
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">_OFF</span></a>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">2</span>
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a class="mw-redirect" href="STRETCH" title="STRETCH"><span style="color:#4593D8;">_STRETCH</span></a>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">3</span>
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a class="mw-redirect" href="SQUAREPIXELS" title="SQUAREPIXELS"><span style="color:#4593D8;">_SQUAREPIXELS</span></a>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">4</span>
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a class="mw-redirect" href="STRETCH" title="STRETCH"><span style="color:#4593D8;">_STRETCH</span></a> , <a href="SMOOTH_(function)" title="SMOOTH (function)"><span style="color:#4593D8;">_SMOOTH</span></a>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">5</span>
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLSCREEN</span></a> <a class="mw-redirect" href="SQUAREPIXELS" title="SQUAREPIXELS"><span style="color:#4593D8;">_SQUAREPIXELS</span></a> , <a href="SMOOTH_(function)" title="SMOOTH (function)"><span style="color:#4593D8;">_SMOOTH</span></a>
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="EXIT_(function)" title="EXIT (function)"><span style="color:#4593D8;">_EXIT</span></a>
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FULLSCREEN_(function)" title="FULLSCREEN (function)">_FULLSCREEN (function)</a></li>
<li><a href="SMOOTH_(function)" title="SMOOTH (function)">_SMOOTH (function)</a></li>
<li><a href="ALLOWFULLSCREEN" title="ALLOWFULLSCREEN">_ALLOWFULLSCREEN</a></li>
<li><a href="FONT" title="FONT">_FONT</a>, <a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li>
<li><a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a>, <a href="SCREENX" title="SCREENX">_SCREENX</a>, <a href="SCREENY" title="SCREENY">_SCREENY</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714104036
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.068 seconds
Real time usage: 0.087 seconds
Preprocessor visited node count: 1328/1000000
Post‐expand include size: 10081/2097152 bytes
Template argument size: 2774/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 453/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   46.627      1 -total
 15.37%    7.166    118 Template:Cl
 11.74%    5.476     56 Template:Text
 10.96%    5.112      1 Template:PageSyntax
  7.55%    3.522      3 Template:CodeStart
  6.67%    3.112      1 Template:PageSeeAlso
  5.71%    2.664      1 Template:PageNavigation
  5.17%    2.410      3 Template:CodeEnd
  5.08%    2.370      1 Template:PageExamples
  4.70%    2.191      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:152-0!canonical and timestamp 20240714104035 and revision id 8338.
 -->
</div>
</div>
</div>
</div>
</body>
</html>