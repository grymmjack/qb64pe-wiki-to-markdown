<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FREEFONT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FREEFONT rootpage-FREEFONT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FREEFONT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_FREEFONT</a> statement frees a font handle that was created by <a href="LOADFONT" title="LOADFONT">_LOADFONT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_FREEFONT</a> (<i>fontHandle&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Unloads fonts that are no longer in use or needed in order to free program memory and resources.</li>
<li>You cannot free a font which is in use. Change the font to a QB64 default font size before freeing the handle (see example below).</li>
<li>Predefined <b>QB64</b> font handle numbers can be used before freeing a font:
<ul><li><b>_FONT 8 </b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 1, 2, 7, 8 or 13</li>
<li><b>_FONT 14</b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 9 or 10</li>
<li><b>_FONT 16</b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 0 (<a href="WIDTH" title="WIDTH">WIDTH</a> 80, 25 text only), 11 or 12</li>
<li><b>_FONT 9, 15</b> and <b>17</b> are the double width versions of 8, 14 and 16 respectively in text <b>SCREEN 0</b>.</li></ul></li>
<li>If the font handle is invalid (equals -1 or 0), an <a href="ERROR_Codes" title="ERROR Codes">error</a> will occur. <b>Check handle values before using or freeing them.</b></li>
<li>You cannot free inbuilt/default QB64 fonts nor do they ever need freed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Previews and creates a file list of valid MONOSPACE TTF fonts by checking the <a href="LOADFONT" title="LOADFONT">_LOADFONT</a> handle values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">12</span>
path$ = <span style="color:#FFB100;">"C:\WINDOWS\Fonts\"</span> <span style="color:#919191;">'path to the font folder</span>
<a href="SHELL" title="SHELL"><span style="color:#4593D8;">SHELL</span></a> <a href="HIDE" title="HIDE"><span style="color:#4593D8;">_HIDE</span></a> <span style="color:#FFB100;">"DIR /b "</span> + path$ + <span style="color:#FFB100;">"\*.ttf &gt; TTFonts.INF"</span>
style$ = <span style="color:#FFB100;">"monospace"</span> <span style="color:#919191;">'set style to MONOSPACE</span>
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> <span style="color:#FFB100;">"TTFonts.INF"</span> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">FOR</span></a> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">INPUT</span></a> <a href="OPEN" title="OPEN"><span style="color:#4593D8;">AS</span></a> #1 <span style="color:#919191;">'list of TTF fonts only</span>
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> <span style="color:#FFB100;">"TTFMono.INF"</span> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">FOR</span></a> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">OUTPUT</span></a> <a href="OPEN" title="OPEN"><span style="color:#4593D8;">AS</span></a> #2 <span style="color:#919191;">'will hold list of valid MONOSPACE fonts</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO UNTIL</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(<span style="color:#F580B1;">1</span>): found = found + <span style="color:#F580B1;">1</span>
    <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT</span></a> #1, font$
    f&amp; = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(path$ + font$, <span style="color:#F580B1;">30</span>, style$)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> f&amp; &gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">'check for valid handle values &gt; 0</span>
        OK = OK + <span style="color:#F580B1;">1</span>
        <a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #2, font$
        <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> f&amp; <span style="color:#919191;">'will create error if handle is invalid!</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hello World!"</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> font$; f&amp;
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Press any key."</span>
        K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(<span style="color:#F580B1;">1</span>)
        <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <span style="color:#F580B1;">16</span> <span style="color:#919191;">'use QB64 default font to free tested font</span>
        <a class="mw-selflink selflink"><span style="color:#4593D8;">_FREEFONT</span></a> f&amp; <span style="color:#919191;">'returns an error if handle &lt;= 0!</span>
        <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> K$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Found"</span>; found; <span style="color:#FFB100;">"TTF files,"</span>; OK; <span style="color:#FFB100;">"can use Monospace,"</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Found 106 TTF files, 13 can use Monospace.
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> Using a _FREEFONT sub-procedure.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">fontpath$ = <a href="ENVIRON$" title="ENVIRON$"><span style="color:#4593D8;">ENVIRON$</span></a>(<span style="color:#FFB100;">"SYSTEMROOT"</span>) + <span style="color:#FFB100;">"\fonts\lucon.ttf"</span>
style$ = <span style="color:#FFB100;">"MONOSPACE, ITALIC, BOLD"</span>
fontsize% = <span style="color:#F580B1;">20</span>
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <span style="color:#F580B1;">16</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This is the QB64 default _FONT 16! To change, press any key!"</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> ClearFont <span style="color:#919191;">'call will not free anything if font&amp; = 0</span>
font&amp; = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(fontpath$, fontsize%, style$)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> font &gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> font&amp; <span style="color:#919191;">'NEVER try to load a font value less than 1!</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"A NEW _FONT style. To change to default, press any key!"</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> ClearFont <span style="color:#919191;">'call will free a valid font handle from memory</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
ClearFont:
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> font&amp; &gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <span style="color:#F580B1;">16</span> <span style="color:#919191;">'change used font to the QB64 8x16 default font</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_FREEFONT</span></a> font&amp;
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"The previous font was freed with _FREEFONT!"</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_FREEFONT was not used!"</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FONT" title="FONT">_FONT</a></li>
<li><a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062335
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.064 seconds
Real time usage: 0.104 seconds
Preprocessor visited node count: 960/1000000
Post‐expand include size: 7497/2097152 bytes
Template argument size: 2297/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 851/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   59.758      1 -total
 18.91%   11.303      1 Template:OutputStart
 10.04%    5.999     72 Template:Cl
  9.69%    5.788      1 Template:PageSyntax
  8.08%    4.829     46 Template:Text
  5.40%    3.227      2 Template:CodeEnd
  5.32%    3.178      2 Template:CodeStart
  4.37%    2.612      1 Template:PageNavigation
  4.18%    2.498      1 Template:OutputEnd
  4.09%    2.447      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:149-0!canonical and timestamp 20240715062335 and revision id 8336.
 -->
</div>
</div>
</div>
</div>
</body>
</html>