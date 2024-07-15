<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_LOADFONT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LOADFONT rootpage-LOADFONT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_LOADFONT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_LOADFONT</a> function loads a FreeType supported font file in a specific size and style and returns a <a href="LONG" title="LONG">LONG</a> font handle.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>handle&amp;</i> = <a class="mw-selflink selflink">_LOADFONT</a>(<i>fontFileName$</i>, <i>size&amp;</i>[, "{MONOSPACE|, BOLD|, ITALIC|, UNDERLINE|, UNICODE|, DONTBLEND|, MEMORY|, AUTOMONO}"][, <i>fontIndex&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The assigned <a href="LONG" title="LONG">LONG</a> font <i>handle&amp;</i> variable return value designates a font style to be used somewhere in a program. Valid handle values are greater than 0 (<b><i>handle&amp;</i> &gt; 0</b>).</li>
<li><i>fontFileName$</i> is the filename of a font. It can include the path to the font file. <b>TTF, TTC, OTF, FNT, FON, PCF and BDF</b> font file formats are supported. Best practice is to include font files with a program.</li>
<li>If no path is specified for <i>fontFileName$</i> and the font file isn't in the same folder as the resulting binary, QB64 attempts to load from the default <i>%SystemRoot%\Fonts</i> path. Similar known locations are searched in other operating systems.</li>
<li><i>size&amp;</i> is the <a href="INTEGER" title="INTEGER">INTEGER</a> height of the font. If the size is too large or small an <a href="ERROR_Codes" title="ERROR Codes">error</a> will occur.</li>
<li>Optional comma separated <i>style</i> parameter(s) used are literal <a href="STRING" title="STRING">STRINGs</a> (in quotes) or can be contained in variable(s).
<ul><li><b>"MONOSPACE"</b> loads a font with all characters occupying the same width. Results may be too spaced out for fonts that aren't designed for monospace use.</li>
<li><b>"BOLD", "ITALIC"</b> or <b>"UNDERLINE"</b> create bold, italic or underlined fonts when available in font.
<ul><li>(valid for QB64 versions prior to 1.000).</li>
<li>For <b>QB64 1.000 or later</b>, you must specify the proper file name according to the desired attributes. For example, Courier New is in font <b>cour.ttf</b> while Courier New Bold is in font <b>courbd.ttf</b>, as shipped with Windows.</li></ul></li>
<li><b>"UNICODE"</b> loads Unicode fonts such as <i>cyberbit.ttf</i> which is included in the QB64 downloads.</li>
<li><b>"DONTBLEND"</b> turns off <a href="ALPHA" title="ALPHA">_ALPHA</a> blending of fonts. This can also be done with the <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> statement.</li>
<li><b>"MEMORY"</b> will treat <i>fontFileName$</i> as a memory buffer containing the font file instead of a file name.</li>
<li><b>"AUTOMONO"</b> will automatically detect monospace fonts and set the <b>"MONOSPACE"</b> flag if <i>fontFileName$</i> is monospaced.</li></ul></li></ul>
<dl><dd><ul><li>You can pass different font styles using different predefined <a href="STRING" title="STRING">STRING</a> variable lists. You <b>can</b> include an empty style string.</li></ul></dd></dl>
<ul><li><i>fontIndex&amp;</i> is the index of a font in a font collection (usually <b>.ttc</b> files). When this is negative the first font from the collection is loaded.</li>
<li><b>Always check that font handle values are greater than 0 (</b><i>handle&amp;</i> &gt; 0<b>) before using them or <a href="ERROR_Codes" title="ERROR Codes">illegal function errors</a> may occur.</b></li>
<li><b>NOTE: SCREEN 0 can only use ONE font on a screen page. Thus a style like underline would affect the entire page.</b></li>
<li>Font sizes can be found using the <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a> function. Font <i>size</i>s can also affect <a href="SCREEN" title="SCREEN">SCREEN</a> sizes.</li>
<li><a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a> can only measure monospaced fonts. <b>"MONOSPACE" can be used to load a variable width font as a monospace font.</b></li>
<li><a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a> can measure the width of a string of text in <b>graphics modes only</b>. Use one character to get the font's width.</li></ul>
<p>
</p>
<ul><li>Multiple fonts will require multiple font variable handles unless used and freed consecutively.</li>
<li>Font handles with values greater than 0 that are <b>no longer used</b> should be freed using <a href="FREEFONT" title="FREEFONT">_FREEFONT</a>.</li>
<li><b>Predefined QB64</b> font handle numbers can be substituted before freeing a font handle:
<ul><li><b>_FONT 8 </b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 1, 2, 7, 8 or 13</li>
<li><b>_FONT 14</b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 9 or 10</li>
<li><b>_FONT 16</b> - default font for <a href="SCREEN" title="SCREEN">SCREEN</a> 0 (<a href="WIDTH" title="WIDTH">WIDTH</a> 80, 25 text only), 11 or 12</li>
<li><b>_FONT 9, 15</b> and <b>17</b> are the double width versions of 8, 14 and 16 respectively in text <b>SCREEN 0 only</b>.</li></ul></li>
<li>Once the font is changed to a predefined value, the font handle value can be freed using <a href="FREEFONT" title="FREEFONT">_FREEFONT</a> for another font type.</li>
<li>Font handle values of -1 (load failure) <b>do not</b> need to be freed. <b>An <a href="ERROR_Codes" title="ERROR Codes">error</a> will occur if you try to free invalid handles.</b></li></ul>
<p>
</p>
<ul><li>Windows users should find <b>TTF</b> font files in the C:\WINDOWS\FONTS folder, but don't depend on unusual ones being there.</li>
<li><b>Check the font file name. The name in the "viewer" is not necessarily the file's name. Use the name in properties (right click a font listed and choose Properties in the contextual menu)</b></li>
<li>If a program is on a different drive than Windows, <a href="ENVIRON$" title="ENVIRON$">ENVIRON$</a>("SYSTEMROOT") will return the path to the "WINDOWS" folder. Normally "C:\WINDOWS". Then add the "\FONTS\" folder and the font <b>.TTF</b> filename to the path <a href="STRING" title="STRING">STRING</a>.</li></ul>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v1.3"><img alt="v1.3" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v1.3</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="all"><img alt="all" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>all</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Apix.png"><img alt="Apix.png" decoding="async" height="48" src="/qb64wiki/images/5/5f/Apix.png" width="48"/></a></div></div>
<div class="gallerytext">
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Win.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/29/Win.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
</ul>
<ul><li>The capability to load from <i>memory</i> and loading a font from a <i>font collection</i> was introduced in <b>QB64-PE</b> <i>v3.7.0</i>.</li>
<li>The capability to auto-detect monospaced fonts was introduced in <b>QB64-PE</b> <i>v3.13.1</i>.</li></ul>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>You need to know that if you are in a text mode (such as SCREEN 0 - the default) then you will only be able to use mono-spaced (fixed width) fonts.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">rootpath$ = <a href="ENVIRON$" title="ENVIRON$"><span style="color:#4593D8;">ENVIRON$</span></a>(<span style="color:#FFB100;">"SYSTEMROOT"</span>) <span style="color:#919191;">'normally "C:\WINDOWS"</span>
fontfile$ = rootpath$ + <span style="color:#FFB100;">"\Fonts\cour.ttf"</span> <span style="color:#919191;">'TTF file in Windows</span>
style$ = <span style="color:#FFB100;">"monospace"</span> <span style="color:#919191;">'font style is not case sensitive</span>
f&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_LOADFONT</span></a>(fontfile$, <span style="color:#F580B1;">30</span>, style$)
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> f&amp;
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hello!"</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Hello!
</pre>
</td></tr></tbody></table>
<p><i>Note:</i> 30 means each row of text (including vertical spacing) will be exactly 30 pixels high. This may make some program screens larger. If you don't want a style listed just use style$ = "" if using a <a href="STRING" title="STRING">STRING</a> variable for different calls.
</p>
<dl><dt>Example 2</dt>
<dd>In a 32-bit graphics mode you can alpha blend onto the background.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">i&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">800</span>, <span style="color:#F580B1;">600</span>, <span style="color:#F580B1;">32</span>)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> i&amp;
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">&amp;HC0FFFF00</span>, <span style="color:#F580B1;">&amp;H200000FF</span>
f&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"C:\Windows\Fonts\times.ttf"</span>, <span style="color:#F580B1;">25</span>) <span style="color:#919191;">'normal style</span>
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> f&amp;
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hello!"</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Hello!
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> You can load a fixed width font file without using the "monospace" option and it will be treated as variable width. This can be useful because LOCATE treats the horizontal position as an offset in pixels for variable width fonts.</dd></dl>
<dl><dt>Example 3</dt>
<dd>Loading a <a href="Unicode" title="Unicode">Unicode</a> font, <i>cyberbit.ttf</i>, which was downloaded with QB64.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">12</span>
<a href="DECLARE" title="DECLARE"><span style="color:#4593D8;">DECLARE</span></a> <a class="mw-redirect" href="CUSTOMTYPE" title="CUSTOMTYPE"><span style="color:#4593D8;">CUSTOMTYPE</span></a> <a class="mw-redirect" href="LIBRARY" title="LIBRARY"><span style="color:#4593D8;">LIBRARY</span></a> <span style="color:#919191;">'Directory Information using KERNEL32 provided by Dav</span>
    <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">GetModuleFileNameA&amp;</span> (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> hModule <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, lpFileName <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> nSize <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">GetModuleFileNameW&amp;</span> (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> hModule <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, lpFileName <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> nSize <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
<a class="mw-redirect" href="END_DECLARE" title="END DECLARE"><span style="color:#4593D8;">END DECLARE</span></a>
<span style="color:#919191;">'=== SHOW CURRENT PROGRAM</span>
FileName$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">512</span>)
Result = <span style="color:#55FF55;">GetModuleFileNameA</span>(<span style="color:#F580B1;">0</span>, FileName$, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(FileName$))
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Result <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"CURRENT PROGRAM (ASCII): "</span>; <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(FileName$, Result)
<span style="color:#919191;">'load a unicode font</span>
f = <a class="mw-selflink selflink"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"cyberbit.ttf"</span>, <span style="color:#F580B1;">24</span>, <span style="color:#FFB100;">"UNICODE"</span>)
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> f
Result = <span style="color:#55FF55;">GetModuleFileNameW</span>(<span style="color:#F580B1;">0</span>, FileName$, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(FileName$) \ <span style="color:#F580B1;">2</span>)
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">1</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#55FF55;">QuickCP437toUTF32$</span>(<span style="color:#FFB100;">"CURRENT PROGRAM (UTF): "</span>) + <span style="color:#55FF55;">QuickUTF16toUTF32$</span>(<a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(FileName$, Result * <span style="color:#F580B1;">2</span>))
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <span style="color:#F580B1;">16</span> <span style="color:#919191;">'restore CP437 font</span>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">QuickCP437toUTF32$</span> (a$)
    b$ = <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(<a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$) * <span style="color:#F580B1;">4</span>, <span style="color:#F580B1;">0</span>)
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$)
        <a href="ASC" title="ASC"><span style="color:#4593D8;">ASC</span></a>(b$, i * <span style="color:#F580B1;">4</span> - <span style="color:#F580B1;">3</span>) = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(a$, i)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <span style="color:#55FF55;">QuickCP437toUTF32$</span> = b$
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">QuickUTF16toUTF32$</span> (a$)
    b$ = <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(<a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$) * <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">0</span>)
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$) \ <span style="color:#F580B1;">2</span>
        <a href="ASC" title="ASC"><span style="color:#4593D8;">ASC</span></a>(b$, i * <span style="color:#F580B1;">4</span> - <span style="color:#F580B1;">3</span>) = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(a$, i * <span style="color:#F580B1;">2</span> - <span style="color:#F580B1;">1</span>)
        <a href="ASC" title="ASC"><span style="color:#4593D8;">ASC</span></a>(b$, i * <span style="color:#F580B1;">4</span> - <span style="color:#F580B1;">2</span>) = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(a$, i * <span style="color:#F580B1;">2</span>)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <span style="color:#55FF55;">QuickUTF16toUTF32$</span> = b$
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FONT" title="FONT">_FONT</a>, <a href="FONT_(function)" title="FONT (function)">_FONT (function)</a></li>
<li><a href="FREEFONT" title="FREEFONT">_FREEFONT</a></li>
<li><a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a>, <a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a></li>
<li><a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a>, <a href="PRINTMODE_(function)" title="PRINTMODE (function)">_PRINTMODE (function)</a></li>
<li><a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>, <a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a> <span style="color:#777777;">(Demo)</span></li>
<li><a href="Windows_Libraries#Font_Dialog_Box" title="Windows Libraries">Windows Font Dialog Box</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714130610
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.096 seconds
Real time usage: 0.123 seconds
Preprocessor visited node count: 1061/1000000
Post‐expand include size: 7756/2097152 bytes
Template argument size: 2142/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2723/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   82.067      1 -total
 11.63%    9.540     68 Template:Cl
  6.88%    5.649     62 Template:Text
  4.00%    3.284      1 Template:PageSyntax
  3.81%    3.129      1 Template:PageSeeAlso
  3.22%    2.639     13 Template:Parameter
  2.96%    2.428      1 Template:PageExamples
  2.63%    2.158      3 Template:CodeStart
  2.46%    2.018      1 Template:PageNavigation
  2.42%    1.985      1 Template:PageAvailability
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:169-0!canonical and timestamp 20240714130610 and revision id 8869.
 -->
</div>
</div>
</div>
</div>
</body>
</html>