<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_HIDE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-HIDE rootpage-HIDE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_HIDE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_HIDE</a> action is used to hide the console window opened by a <a href="SHELL" title="SHELL">SHELL</a> statement.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="SHELL" title="SHELL">SHELL</a> [<b>_HIDE</b>] <i>StringCommandLine$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Allows any command line window to be hidden from view without affecting the program.</li>
<li><a class="mw-selflink selflink">_HIDE</a> must be used when sending ("piping") screen information to a file.</li>
<li><b>Note:</b> Some commands may not work without adding CMD /C to the start of the command line.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Subprogram that displays long and short filenames using the DIR /X option in SCREEN 12:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">12</span>
<span style="color:#55FF55;">LFN</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">LFN</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(<a href="ENVIRON$" title="ENVIRON$"><span style="color:#4593D8;">ENVIRON$</span></a>(<span style="color:#FFB100;">"OS"</span>)) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_SUB" title="EXIT SUB"><span style="color:#4593D8;">EXIT SUB</span></a> <span style="color:#919191;">' /X not available Win 9X and ME</span>
    <a href="SHELL" title="SHELL"><span style="color:#4593D8;">SHELL</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_HIDE</span></a> <span style="color:#FFB100;">"cmd /c dir /x &gt; DOS-DATA.INF"</span> <span style="color:#919191;">' load display data to a file</span>
    <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> <span style="color:#FFB100;">"DOS-DATA.INF"</span> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">FOR</span></a> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">INPUT</span></a> <a href="OPEN" title="OPEN"><span style="color:#4593D8;">AS</span></a> #1
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(<span style="color:#F580B1;">1</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        Header$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">10</span>) + <span style="color:#FFB100;">"Short"</span> + <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">16</span>) + <span style="color:#FFB100;">"Long"</span> + <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">20</span>) + <span style="color:#FFB100;">"Last Modified"</span>
        tmp$ = <span style="color:#FFB100;">"\   \  \          \      &amp;"</span> <span style="color:#919191;">' print using template format</span>
        <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">4</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Header$
        <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO UNTIL</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(<span style="color:#F580B1;">1</span>)
            <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT</span></a> #1, line$
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(line$) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(line$, <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span>) &lt;&gt; <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">1</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">' ignore other file data</span>
                cnt% = cnt% + <span style="color:#F580B1;">1</span>
                last$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(line$, <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">17</span>): DIR$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(line$, <span style="color:#F580B1;">23</span>, <span style="color:#F580B1;">3</span>)
                <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(line$, <span style="color:#F580B1;">37</span>, <span style="color:#F580B1;">1</span>) &lt;&gt; <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">1</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">' found line with short and long name</span>
                    SHFN$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(line$, <span style="color:#F580B1;">37</span>, <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(<span style="color:#F580B1;">37</span>, line$, <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">1</span>)) - <span style="color:#F580B1;">1</span>)
                    LGFN$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(line$, <span style="color:#F580B1;">50</span>)
                <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>: SHFN$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(line$, <span style="color:#F580B1;">50</span>): LGFN$ = <span style="color:#FFB100;">""</span> <span style="color:#919191;">' found short name only</span>
                <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
                <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> cnt% <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">24</span> = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">' pause every 24 files</span>
                    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">28</span>, <span style="color:#F580B1;">27</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Press a key for more files!"</span>
                    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span>: <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
                    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">4</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Header$
                <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
                <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">11</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> (cnt% <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">24</span>) + <span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">4</span>
                <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> tmp$; DIR$; SHFN$; LGFN$
                <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> (cnt% <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">24</span>) + <span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">58</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> last$
            <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">10</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a> + <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">27</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Total folders and files ="</span>; cnt%
    <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> The above routine can also be used to place the file name info into string arrays by using the count variable cnt% to determine the index. Long file names are normally returned by <b>QB64</b>. To keep older QBasic programs compatible, you may want to only use the short names when displaying the files on the screen.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHELL" title="SHELL">SHELL</a>, <a href="DONTWAIT" title="DONTWAIT">_DONTWAIT</a></li>
<li><a href="FILELIST$_(function)" title="FILELIST$ (function)">FILELIST$ (function)</a> (<a href="FILES" title="FILES">FILES</a> function, member-contributed)</li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192728
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.049 seconds
Real time usage: 0.058 seconds
Preprocessor visited node count: 1073/1000000
Post‐expand include size: 7728/2097152 bytes
Template argument size: 2044/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 363/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.856      1 -total
 14.97%    4.919     76 Template:Cl
 13.35%    4.387     66 Template:Text
  9.55%    3.139      1 Template:PageSeeAlso
  6.72%    2.207      1 Template:CodeEnd
  5.92%    1.945      1 Template:PageExamples
  5.90%    1.937      1 Template:PageSyntax
  5.53%    1.818      1 Template:PageNavigation
  5.47%    1.796      1 Template:Parameter
  4.97%    1.632      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:139-0!canonical and timestamp 20240714192728 and revision id 8349.
 -->
</div>
</div>
</div>
</div>
</body>
</html>