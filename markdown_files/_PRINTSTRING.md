<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PRINTSTRING - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PRINTSTRING rootpage-PRINTSTRING skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PRINTSTRING</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_PRINTSTRING</a> statement prints text <a href="STRING" title="STRING">strings</a> using graphic column and row coordinate positions.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_PRINTSTRING</a>(<i>column</i>, <i>row</i>), <i>textExpression$</i>[, <i>imageHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>column</i> and <i>row</i> are <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="LONG" title="LONG">LONG</a> starting PIXEL (graphic) column and row coordinates to set text or custom fonts.</li>
<li><i>textExpression$</i> is any literal or variable <a href="STRING" title="STRING">string</a> value of text to be displayed.</li>
<li><i>imageHandle&amp;</i> is the optional image or destination to use. Zero designates current <a href="SCREEN" title="SCREEN">SCREEN</a> page.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The starting coordinate sets the top left corner of the text to be printed. Use <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a> to calculate that text or <a href="FONT" title="FONT">font</a> position</li>
<li>The <a href="FONT" title="FONT">_FONT</a> size can affect the <a href="SCREEN" title="SCREEN">screen</a> and row heights.
<ul><li>Custom fonts are not required. <a class="mw-selflink selflink">_PRINTSTRING</a> can print all <a href="ASCII" title="ASCII">ASCII</a> characters.</li></ul></li>
<li><a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a> can be used to determine how wide a text print will be so that the screen width is not exceeded.</li>
<li>If the <i>imageHandle&amp;</i> is omitted, the current image, page or screen destination is used.</li>
<li>Can use the current font alpha blending with a designated image background. See the <a href="RGBA" title="RGBA">_RGBA</a> function example.</li>
<li>Use the <a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a> statement before printing to set how the background is rendered.
<ul><li>Use the <a href="PRINTMODE_(function)" title="PRINTMODE (function)">_PRINTMODE (function)</a> to find the current _PRINTMODE setting.</li></ul></li>
<li>In SCREEN 0 (text only), <a class="mw-selflink selflink">_PRINTSTRING</a> works as one-line replacement for <b>LOCATE x, y: PRINT text$</b>, without changing the current cursor position.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li>In versions of QB64 prior to 1.000 _PRINTSTRING can only be used in graphic, 256 color or 32 bit screen modes, not SCREEN 0.<i></i></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Printing those unprintable <a href="ASCII" title="ASCII">ASCII</a> control characters is no longer a problem!
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 256)
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> code = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 31
  chrstr$ = chrstr$ + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(code) + <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(1)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>("C:\Windows\Fonts\Cour.ttf", 20, "MONOSPACE") 'select monospace font
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTSTRING</span></a> (0, 16), chrstr$
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">  ☺ ☻ ♥ ♦ ♣ ♠ • ◘ ○ ◙ ♂ ♀ ♪ ♫ ☼ ► ◄ ↕ ‼ ¶ § ▬ ↨ ↑ ↓ → ← ∟ ↔ ▲ ▼
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Making any <b>QB64 program window</b> larger using a SUB that easily converts PRINT to <a class="mw-selflink selflink">_PRINTSTRING</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">Scr13&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(320, 200, 13)  'this is the old SCREEN 13 image page to set the image
Big13&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 256) 'use 4 X 3 aspect ratio that QBasic used when full screen
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> Big13&amp;
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> Scr13&amp;
image1&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("Howie.BMP", 256)
image2&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("Howie2.BMP", 256)
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (10, 20), image1&amp;, Scr13&amp;
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (160, 20), image2&amp;, Scr13&amp;
<a href="COPYPALETTE" title="COPYPALETTE"><span style="color:#4593D8;">_COPYPALETTE</span></a> image1&amp;, Scr13&amp;
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 151: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 2, 4: PRINTS "Screen 13 Height Reduction to 83%"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 22, 22: PRINTS <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(24) + " 4 X 3 Proportion"  'use <a href="Concatenation" title="Concatenation"><span style="color:#4593D8;">concatenation</span></a>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 24, 21: PRINTS <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) + " Stretched at 100%" 'instead of a <a href="Semicolon" title="Semicolon"><span style="color:#4593D8;">semicolon</span></a>!
<a href="COPYPALETTE" title="COPYPALETTE"><span style="color:#4593D8;">_COPYPALETTE</span></a> Scr13&amp;, Big13&amp;  'required when imported image colors are used
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , Scr13&amp;, Big13&amp;   'stretches the screen to double the size
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> PRINTS (Text$)
row% = (<a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a> - 1) * <a href="FONTHEIGHT" title="FONTHEIGHT"><span style="color:#4593D8;">_FONTHEIGHT</span></a>      'finds current screen page text or font row height
col% = (<a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(0) - 1) * <a href="PRINTWIDTH" title="PRINTWIDTH"><span style="color:#4593D8;">_PRINTWIDTH</span></a>("W") 'finds current page text or font column width
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTSTRING</span></a> (col%, row%), Text$
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The procedure above creates a larger version of a SCREEN 13 window by stretching it with <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a>. It cannot stretch PRINTed text so <a class="mw-selflink selflink">_PRINTSTRING</a> must be used instead. <a href="LOCATE" title="LOCATE">LOCATE</a> sets the PRINT cursor position for <a href="CSRLIN" title="CSRLIN">CSRLIN</a> and <a href="POS" title="POS">POS</a>(0) to read. The SUB then converts the coordinates to graphical ones. Then <b>change</b> <a href="PRINT" title="PRINT">PRINT</a> to PRINTS using the IDE <b>Search Menu</b>.</dd></dl>
<p>
<i>Example 3:</i> Rotating a text string around a graphic object.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> row <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, cnt <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, cstart <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>, cend <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> xrot <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, yrot <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, scale <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
' <a href="FULLSCREEN" title="FULLSCREEN"><span style="color:#4593D8;">_FULLSCREEN</span></a>                       'full screen optional
cstart = 0: cend = 8 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1)
xrot = 6: yrot = 60: scale = 4
row = 1
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (320, 240), 15, 9: <a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(0, 0), 9
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = cstart <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> cend <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> .04
    x = 300 + (scale * 40 - (row * xrot)) * <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(i)
    y = 200 + (scale * 40 - (row * yrot)) * <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(i)
    cnt = cnt + 1
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 7: <a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTSTRING</span></a> (x, y), "HELLO WORLD!", 0  'display
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> cnt = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(text$) * 8 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> cnt = 0: <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0: <a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTSTRING</span></a> (x, y), "HELLO WORLD!", 0  'erase
    <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.02
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) 'escape key exit
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a>, <a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a></li>
<li><a href="CONTROLCHR" title="CONTROLCHR">_CONTROLCHR</a></li>
<li><a href="FONT" title="FONT">_FONT</a>, <a href="LOADFONT" title="LOADFONT">_LOADFONT</a>, <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>, <a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a>, <a href="SCREENPRINT" title="SCREENPRINT">_SCREENPRINT</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211459
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.052 seconds
Real time usage: 0.066 seconds
Preprocessor visited node count: 672/1000000
Post‐expand include size: 5799/2097152 bytes
Template argument size: 1140/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   37.870      1 -total
 14.55%    5.511     84 Template:Cl
  9.00%    3.408      2 Template:Small
  5.69%    2.156      1 Template:PageSeeAlso
  5.45%    2.062      1 Template:PageParameters
  5.41%    2.049      1 Template:OutputEnd
  5.34%    2.021      1 Template:PageAvailability
  5.21%    1.972      1 Template:PageSyntax
  5.15%    1.949      1 Template:OutputStart
  5.07%    1.920      9 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:254-0!canonical and timestamp 20240714211459 and revision id 7931.
 -->
</div>
</div>
</div>
</div>
</body>
</html>