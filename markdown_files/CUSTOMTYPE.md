<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DECLARE LIBRARY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DECLARE_LIBRARY rootpage-DECLARE_LIBRARY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DECLARE LIBRARY</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>DECLARE LIBRARY</b> declaration allows for the utilization of external library <a href="SUB" title="SUB">SUB</a> and <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>DECLARE [DYNAMIC|CUSTOMTYPE|STATIC] LIBRARY</b> [<i>"Library_name"</i>][, <i>"Library_name2"</i>][, ...]
<dl><dd>{<a href="SUB" title="SUB">SUB</a>|<a href="FUNCTION" title="FUNCTION">FUNCTION</a>} <i>Procedure_name</i> [<b>ALIAS</b> <i>Library_procedure</i>] (<a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> <i>Parameter</i>[{suffix| <a href="AS" title="AS">AS</a> <a href="Variable_Types" title="Variable Types">type</a>[, <i>Parameter2</i>...][, ...)</dd>
<dd>.</dd>
<dd>. ' Other SUBs or FUNCTIONs as required</dd>
<dd>.</dd></dl></dd>
<dd><b>END DECLARE</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The declaration can be used with:
<ul><li>C/C++ sub-procedures files (<i>.h</i> and <i>.hpp</i>)</li>
<li>Dynamically linked libraries and shared object files (<i>.dll</i>, <i>.so</i> and <i>.dylib</i>)</li>
<li>Static libraries (<i>.a</i>)</li>
<li>Object files (<i>.o</i>)</li></ul></li>
<li><i>Library file names</i> can be listed to combine more than one supported file name or path into one DECLARE LIBRARY block (<b>except for dynamically linked libraries and shared object files</b>). Do not include any file extension (<i>.h</i>, <i>.dll</i>, <i>.a</i> etc.).</li>
<li>The dynamically linked library or shared object file can be in a relative/absolute path specified along with the library name, in the operating system's directory (e.g., C:\Windows\System32), or in the QB64 directory (alongside your program's executable).</li>
<li>Specify <i>""</i> as the library file name to inform QB64 that the function exists in a library that is already linked and that it must define the C function before calling it, as well as allowing QB64 code to call it.</li>
<li>It's a good idea to try declaring Operating System API libraries without a library file name first, as most common Operating System headers are already included in QB64 source.</li>
<li>When using a procedure from a dynamically linked library or shared object (<i>.dll</i>, <i>.so</i> and <i>.dylib</i> files) use <b>DECLARE DYNAMIC LIBRARY</b>.</li>
<li>When using a procedure from a static library (<i>.a</i> files) use <b>DECLARE STATIC LIBRARY</b>.</li>
<li><i>Procedure_name</i> can be any desired procedure name designated by using <a href="ALIAS" title="ALIAS">ALIAS</a> with the <i>Library_procedure</i> name following. Enclose <i>Library_procedure</i> in <i>""</i> when using a C++ function with the scope operator (e.g., "std::clamp").</li>
<li><i>Parameters</i> used by the library procedure can be passed by value (<a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a>) when needed, except for <a href="STRING" title="STRING">STRING</a> values.</li>
<li>QB64 <a href="STRING" title="STRING">STRINGs</a> are passed to external libraries as pointers to first character. Many external library procedures expect strings to be NULL terminated. Terminate <a href="STRING" title="STRING">STRINGs</a> using <a href="CHR$" title="CHR$">CHR$</a>(0) wherever it is needed.</li>
<li>Declarations can be made inside of <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures. Declarations do not need to be at program start.</li>
<li>C/C++ procedures can use a header file name and the file code must be included with program code.</li>
<li>C/C++ header files cannot be used with <b>DECLARE DYNAMIC LIBRARY</b>. Existence of any <i>.h</i> or <i>.hpp</i> file of the same name as the dynamically linked library or shared object file will cause DECLARE DYNAMIC LIBRARY to fail.</li>
<li>The <a href="OFFSET" title="OFFSET">_OFFSET</a> in memory can be used in <b>CUSTOMTYPE</b>, <b>STATIC</b> and <b>DYNAMIC LIBRARY</b> declarations.</li>
<li><b>DECLARE DYNAMIC LIBRARY</b> let's you specify any <a href="SUB" title="SUB">SUB</a>/<a href="FUNCTION" title="FUNCTION">FUNCTION</a> calling format you wish, but if the size of the parameters does not match, the size expected within the library, your code will probably cause a GPF (General Protection Fault). It is important to understand that pointers (if required) will be 32-bits in size (the equivalent of a <a href="LONG" title="LONG">LONG</a>) when creating a 32-bit program (even under 64-bit Windows).</li>
<li><b>STATIC</b> is the same as <b>DYNAMIC</b> except that it prioritizes linking to static libraries (<i>.a</i> and <i>.o</i> files) over dynamically linked libraries and shared object files, if both exist.</li>
<li><b>CUSTOMTYPE</b> is already implied when using <b>DECLARE DYNAMIC LIBRARY</b>. This type of library just allows the same flexibility to apply when referencing STATIC libraries that are used to refer to dynamic libraries.</li>
<li><a href="SUB" title="SUB">SUB</a> procedures using <b>DECLARE CUSTOMTYPE LIBRARY</b> API procedures <b>may error</b>. Try <b>DYNAMIC</b> with the dynamically linked library or shared object file name.</li>
<li>It is up to the user to document and determine the suitability of all libraries and procedures they choose to use. QB64 cannot guarantee that any procedure will work and cannot guarantee any troubleshooting help.</li>
<li>QB64 version 1.000 and up produce standalone executables. External dynamically linked libraries or shared object files must be distributed with your program.</li>
<li>What libraries are or aren't automatically used in the linking process is not formally defined, nor is it guaranteed to stay that way in future versions of QB64.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>Library_name</i> is needed if a library is not already loaded by QB64. Do not include the file extension. Begin the <i>Library_name</i> with <b>./</b> or <b>.\</b> to make it relative to the path where your source file is saved, so you can keep all your project files together.</li>
<li><i>Procedure_name</i> is any program procedure name you want to designate by using <a href="ALIAS" title="ALIAS">ALIAS</a> with the <i>Library_procedure</i> name.</li>
<li><i>Library procedure</i> is the actual procedure name used inside of the library or header file.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v0.923"><img alt="v0.923" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v0.923</b>
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
<ul><li>Available for <i>Linux</i> and <i>macOS</i> since <b>QB64 v0.940</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Using GLUT library procedure as a program SUB procedure to set the mouse pointer style.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_NORMAL = <span style="color:#F580B1;">1</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_HAND = <span style="color:#F580B1;">2</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_HELP = <span style="color:#F580B1;">4</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_CYCLE = <span style="color:#F580B1;">7</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_TEXT = <span style="color:#F580B1;">8</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_CROSSHAIR = <span style="color:#F580B1;">3</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_UP_DOWN = <span style="color:#F580B1;">10</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_LEFT_RIGHT = <span style="color:#F580B1;">11</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_LEFT_RIGHT_CORNER = <span style="color:#F580B1;">16</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_RIGHT_LEFT_CORNER = <span style="color:#F580B1;">17</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_MOVE = <span style="color:#F580B1;">5</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> CURSOR_NONE = <span style="color:#F580B1;">23</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">DECLARE LIBRARY</span></a>
    <a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">glutSetCursor</span> (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> style&amp;)
<a class="mw-redirect" href="END_DECLARE" title="END DECLARE"><span style="color:#4593D8;">END DECLARE</span></a>
<span style="color:#55FF55;">glutSetCursor</span> CURSOR_CROSSHAIR
</pre>
</td></tr></tbody></table>
<p>
</p>
<dl><dt>Example 2</dt>
<dd>Using <a href="ALIAS" title="ALIAS">ALIAS</a> to create a program SUB or FUNCTION<b>.</b></dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">DECLARE LIBRARY</span></a>
    <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">GetMilliseconds~&amp;&amp;</span> <a href="ALIAS" title="ALIAS"><span style="color:#4593D8;">ALIAS</span></a> GetTicks
<a class="mw-redirect" href="END_DECLARE" title="END DECLARE"><span style="color:#4593D8;">END DECLARE</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , <span style="color:#F580B1;">1</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Seconds since program start:"</span>; <span style="color:#55FF55;">GetMilliseconds</span> \ <span style="color:#F580B1;">1000</span>;
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a> = <span style="color:#F580B1;">27</span>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> When a library procedure is used to represent another procedure name use <a href="ALIAS" title="ALIAS">ALIAS</a> instead. Saves creating a SUB!</dd></dl>
<p>
</p>
<dl><dt>Example 3</dt>
<dd>Don't know if a C function is defined by C++ or QB64? Try using empty quotes.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">DECLARE LIBRARY</span></a> <span style="color:#FFB100;">""</span>
    <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">addone&amp;</span> (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> value&amp;)
<a class="mw-redirect" href="END_DECLARE" title="END DECLARE"><span style="color:#4593D8;">END DECLARE</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The C function 'addone' exists in a library QB64 already links to, but it hasn't been defined as a C function or a QB64 function. By using "" we are telling QB64 the function exists in a library which is already linked to and that it must define the C function before calling it, as well as allowing QB64 code to call it. Trying the above code without the "" will fail.</dd></dl>
<p>
</p>
<dl><dt>Example 4</dt>
<dd>This example plays MIDI files using the <i>playmidi32.dll</i> documented here: <a class="external text" href="http://libertybasicuniversity.com/lbnews/nl110/midi3.htm" rel="nofollow">Liberty Basic University</a>. Download the following DLL file to your main QB64 directory: <a class="external text" href="https://www.qb64.org/resources/Playmidi32.dll" rel="nofollow">PlayMidi32.dll</a></dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DECLARE" title="DECLARE"><span style="color:#4593D8;">DECLARE</span></a> <a href="DYNAMIC" title="DYNAMIC"><span style="color:#4593D8;">DYNAMIC</span></a> <a class="mw-redirect" href="LIBRARY" title="LIBRARY"><span style="color:#4593D8;">LIBRARY</span></a> <span style="color:#FFB100;">"playmidi32"</span>
    <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">PlayMIDI&amp;</span> (filename <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>)
<a class="mw-redirect" href="END_DECLARE" title="END DECLARE"><span style="color:#4593D8;">END DECLARE</span></a>
result = <span style="color:#55FF55;">PlayMIDI</span>(<span style="color:#FFB100;">".\samples\qb64\original\ps2battl.mid"</span> + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">0</span>))
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> result
</pre>
</td></tr></tbody></table>
<p>
</p>
<dl><dt>Example 5</dt>
<dd>Using a CUSTOMTYPE LIBRARY to return the <a href="Unicode" title="Unicode">Unicode</a> version of the current running program's name.</dd></dl>
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
f = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>(<span style="color:#FFB100;">"cyberbit.ttf"</span>, <span style="color:#F580B1;">24</span>, <span style="color:#FFB100;">"UNICODE"</span>)
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
<ul><li><a href="SUB" title="SUB">SUB</a>, <a href="FUNCTION" title="FUNCTION">FUNCTION</a></li>
<li><a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a>, <a href="ALIAS" title="ALIAS">ALIAS</a></li>
<li><a href="OFFSET_(function)" title="OFFSET (function)">_OFFSET (function)</a>, <a href="OFFSET" title="OFFSET">_OFFSET</a> <span style="color:#777777;">(variable type)</span></li>
<li><a href="C_Libraries" title="C Libraries">C Libraries</a>, <a href="DLL_Libraries" title="DLL Libraries">DLL Libraries</a>, <a href="Windows_Libraries" title="Windows Libraries">Windows Libraries</a></li>
<li><a href="Port_Access_Libraries" title="Port Access Libraries">Port Access Libraries</a></li>
<li><a href="SQL_Client" title="SQL Client">SQL Client</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714180424
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.077 seconds
Real time usage: 0.092 seconds
Preprocessor visited node count: 1282/1000000
Post‐expand include size: 9616/2097152 bytes
Template argument size: 2442/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2639/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   53.422      1 -total
  9.53%    5.092     96 Template:Cl
  7.35%    3.925     72 Template:Text
  5.20%    2.778      1 Template:PageSyntax
  3.54%    1.892      1 Template:Small
  3.49%    1.862      1 Template:PageExamples
  3.48%    1.861      5 Template:CodeStart
  3.26%    1.739      1 Template:PageDescription
  3.20%    1.708      5 Template:Parameter
  3.16%    1.688      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:107-0!canonical and timestamp 20240714180424 and revision id 8832.
 -->
</div>
</div>
</div>
</div>
</body>
</html>