<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FONT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FONT rootpage-FONT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FONT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_FONT</a> statement sets the current <a href="LOADFONT" title="LOADFONT">_LOADFONT</a> function font handle to be used by <a href="PRINT" title="PRINT">PRINT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_FONT</a> <i>fontHandle&amp;</i>[, <i>imageHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>fontHandle&amp;</i> is the handle retrieved from <a href="LOADFONT" title="LOADFONT">_LOADFONT</a> function, the <a href="FONT_(function)" title="FONT (function)">_FONT</a> function, or a predefined handle.</li>
<li>If the image handle is omitted the current image <a href="DEST" title="DEST">_DESTination</a> is used. Zero can designate the current program <a href="SCREEN" title="SCREEN">SCREEN</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Predefined <b>QB64</b> font handle numbers can be used before freeing a font:
<ul><li><b>_FONT 8 </b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 1, 2, 7, 8 or 13</li>
<li><b>_FONT 14</b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 9 or 10</li>
<li><b>_FONT 16</b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 0 (<a href="WIDTH" title="WIDTH">WIDTH</a> 80, 25 text only), 11 or 12</li>
<li><b>_FONT 9, 15</b> and <b>17</b> are the double width versions of 8, 14 and 16 respectively in text <b>SCREEN 0 only</b>.</li></ul></li>
<li><a href="Unicode" title="Unicode">Unicode</a> characters can be assigned to a monospace font that contains those unicode characters using the <a href="MAPUNICODE" title="MAPUNICODE">_MAPUNICODE</a> TO <a href="ASCII" title="ASCII">ASCII</a> mapping statement. The optional <b>IME cyberbit.ttf</b> font included with QB64 can also be used.</li>
<li>Can alpha blend a font with a background screen created by <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> in 32 bit color.</li>
<li><b>Check for valid handle values greater than 0 before using or freeing font handles.</b></li>
<li>Free <b>unused</b> font handles with <a href="FREEFONT" title="FREEFONT">_FREEFONT</a>. Freeing invalid handles will create an <a href="ERROR_Codes" title="ERROR Codes">"illegal function call"</a> error.</li>
<li><b>NOTE: SCREEN 0 can only use one font type and style per viewed SCREEN page. Font size may also affect the window size.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Previewing a font in SCREEN 0. A different true type font can be substituted below.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">fontpath$ = <a href="ENVIRON$" title="ENVIRON$"><span style="color:#4593D8;">ENVIRON$</span></a>(<span style="color:#FFB100;">"SYSTEMROOT"</span>) + <span style="color:#FFB100;">"\fonts\lucon.ttf"</span> <span style="color:#919191;">'Find Windows Folder Path.</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
        style$ = <span style="color:#FFB100;">"MONOSPACE"</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
        <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Enter A FONT Size 8 TO 25: "</span>, fontsize%
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> fontsize% &gt; <span style="color:#F580B1;">7</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> fontsize% &lt; <span style="color:#F580B1;">26</span>
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
        <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Enter (0) for REGULAR OR (1) for ITALIC FONT: "</span>, italic%
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> italic% = <span style="color:#F580B1;">0</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> italic% = <span style="color:#F580B1;">1</span>
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
        <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Enter (0) for REGULAR OR (1) for BOLD FONT: "</span>, bold%
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> italic% = <span style="color:#F580B1;">0</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> italic% = <span style="color:#F580B1;">1</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> italic% = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> style$ = style$ + <span style="color:#FFB100;">", ITALIC"</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> bold% = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> style$ = style$ + <span style="color:#FFB100;">", BOLD"</span>
    <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> ClearFont
    font&amp; = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(fontpath$, fontsize%, style$)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_FONT</span></a> font&amp;
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This is your LUCON font! Want to try another STYLE?(Y/N): "</span>;
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: K$ = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>): <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> K$ = <span style="color:#FFB100;">"Y"</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> K$ = <span style="color:#FFB100;">"N"</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> K$ = <span style="color:#FFB100;">"N"</span>
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> ClearFont
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This is the QB64 default _FONT 16!"</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
ClearFont:
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> font&amp; &gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_FONT</span></a> <span style="color:#F580B1;">16</span> <span style="color:#919191;">'select inbuilt 8x16 default font</span>
    <a href="FREEFONT" title="FREEFONT"><span style="color:#4593D8;">_FREEFONT</span></a> font&amp;
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<p><b>NOTE:</b> <a href="ENVIRON$" title="ENVIRON$">ENVIRON$</a>("SYSTEMROOT") returns a string value of: "C:\WINDOWS". Add the "\FONTS\" folder and the <b>.TTF</b> font file name.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FONT_(function)" title="FONT (function)">_FONT (function)</a></li>
<li><a href="LOADFONT" title="LOADFONT">_LOADFONT</a>, <a href="FREEFONT" title="FREEFONT">_FREEFONT</a></li>
<li><a href="Unicode" title="Unicode">Unicode</a>, <a href="MAPUNICODE" title="MAPUNICODE">_MAPUNICODE</a></li>
<li><a href="Windows_Libraries#Font_Dialog_Box" title="Windows Libraries">Windows Font Dialog Box</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714170233
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.041 seconds
Real time usage: 0.051 seconds
Preprocessor visited node count: 557/1000000
Post‐expand include size: 4381/2097152 bytes
Template argument size: 1192/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 346/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.998      1 -total
 14.09%    3.662     43 Template:Cl
  9.38%    2.437     25 Template:Text
  8.82%    2.292      1 Template:PageSyntax
  7.77%    2.020      1 Template:CodeEnd
  7.72%    2.006      1 Template:CodeStart
  7.58%    1.970      1 Template:PageExamples
  7.01%    1.821      3 Template:Parameter
  6.25%    1.626      1 Template:PageParameters
  5.97%    1.553      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:145-0!canonical and timestamp 20240714170233 and revision id 8334.
 -->
</div>
</div>
</div>
</div>
</body>
</html>