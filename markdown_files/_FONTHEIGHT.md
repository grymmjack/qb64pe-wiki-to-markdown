<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FONTHEIGHT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FONTHEIGHT rootpage-FONTHEIGHT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FONTHEIGHT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_FONTHEIGHT</a> function returns the font height of a font handle created by <a href="LOADFONT" title="LOADFONT">_LOADFONT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixelHeight%</i> = <a class="mw-selflink selflink">_FONTHEIGHT</a>[(<i>fontHandle&amp;</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the height of the last font used if a handle is not designated.</li>
<li>If no font is set it returns the current screen mode's text block height.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Finding the <a href="FONT" title="FONT">font</a> or text block size of printed <a href="STRING" title="STRING">string</a> characters in graphic <a href="SCREEN" title="SCREEN">SCREEN</a> modes.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Enter Screen mode 1, 2 or 7 to 13 or 256, 32 for _NEWIMAGE: "</span>, scr$
    mode% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(scr$)
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> mode% &gt; <span style="color:#F580B1;">0</span>
<a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> mode%
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">7</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">13</span>: <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> mode%
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">256</span>, <span style="color:#F580B1;">32</span>: <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">800</span>, <span style="color:#F580B1;">600</span>, mode%)
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Invalid mode selected!"</span>: <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Enter first name of TTF font to use or hit enter for text block size: "</span>, TTFont$
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(TTFont$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Enter font height: "</span>, hi$
height&amp; = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(hi$)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> height&amp; &gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    fnt&amp; = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"C:\Windows\Fonts\"</span> + TTFont$ + <span style="color:#FFB100;">".ttf"</span>, height&amp;, style$)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> fnt&amp; &lt;= <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Invalid Font handle!"</span>: <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
    <a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> fnt&amp;
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<span style="color:#55FF55;">TextSize</span> wide&amp;, high&amp; <span style="color:#919191;">'get the font or current screen mode's text block pixel size</span>
<a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (<span style="color:#F580B1;">20</span>, <span style="color:#F580B1;">100</span>), <span style="color:#FFB100;">"Block size = "</span> + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">1</span>) + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(wide&amp;) + <span style="color:#FFB100;">" X"</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(high&amp;) + <span style="color:#FFB100;">" "</span> + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">2</span>)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">TextSize</span> (TextWidth&amp;, TextHeight&amp;)
    TextWidth&amp; = <a href="PRINTWIDTH" title="PRINTWIDTH"><span style="color:#4593D8;">_PRINTWIDTH</span></a>(<span style="color:#FFB100;">"W"</span>) <span style="color:#919191;">'measure width of one font or text character</span>
    TextHeight&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_FONTHEIGHT</span></a> <span style="color:#919191;">'can measure normal text block heights also</span>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1145" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a>, <a href="FONT" title="FONT">_FONT</a></li>
<li><a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a>, <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a> (Demo)</li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715045656
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.062 seconds
Real time usage: 0.083 seconds
Preprocessor visited node count: 575/1000000
Post‐expand include size: 4421/2097152 bytes
Template argument size: 1183/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 398/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   40.058      1 -total
 13.19%    5.282     41 Template:Cl
 13.04%    5.223     31 Template:Text
  9.23%    3.698      1 Template:PageSyntax
  7.56%    3.027      1 Template:CodeEnd
  7.36%    2.950      2 Template:Parameter
  6.89%    2.761      1 Template:CodeStart
  6.83%    2.736      1 Template:PageDescription
  6.68%    2.676      1 Template:PageNavigation
  6.63%    2.657      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:147-0!canonical and timestamp 20240715045656 and revision id 8893.
 -->
</div>
</div>
</div>
</div>
</body>
</html>