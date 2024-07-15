<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$CONSOLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_CONSOLE rootpage-_CONSOLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$CONSOLE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$CONSOLE</a> <a href="Metacommand" title="Metacommand">Metacommand</a> creates a console window that can be used throughout a QB64 program module.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$CONSOLE</a>[:ONLY]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a href="CONSOLE" title="CONSOLE">_CONSOLE</a> <b>ON</b> or <b>OFF</b> may be used to show or hide the console window at run time.</li>
<li>The <b>:ONLY</b> option can be used when only a console window is desired without a program window.</li>
<li><a href="DEST" title="DEST">_DEST</a> <a href="CONSOLE" title="CONSOLE">_CONSOLE</a> may be used to send screen output to the console window.</li>
<li><a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a> and <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a> can be used to hide or show the main program window.</li>
<li><a href="DELAY" title="DELAY">_DELAY</a> or <a href="SLEEP" title="SLEEP">SLEEP</a> can be used to allow the console window to be set in front of the main program window.</li>
<li><b>QB64 <a href="Metacommand" title="Metacommand">Metacommands</a> are not commented out with ' or REM, unlike QuickBASIC metacommands</b></li>
<li>Change the title of the <a class="mw-selflink selflink">$CONSOLE</a> windows created using <a href="CONSOLETITLE" title="CONSOLETITLE">_CONSOLETITLE</a></li>
<li><b>Note:</b> Text can be copied partially or totally from console screens in Windows by highlighting and using the title bar menu.</li></ul>
<dl><dd><dl><dd>To copy console text output, right click the title bar and select <i>Edit</i> for <i>Mark</i> to highlight and repeat to <i>Copy</i></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Hiding and displaying a console window. Use <a href="DELAY" title="DELAY">_DELAY</a> to place console in front of main program window.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#55FF55;">$CONSOLE</span></a>
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">4</span>
<a href="CONSOLE" title="CONSOLE"><span style="color:#4593D8;">_CONSOLE</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a>
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">4</span>
<a href="CONSOLE" title="CONSOLE"><span style="color:#4593D8;">_CONSOLE</span></a> <a href="ON" title="ON"><span style="color:#4593D8;">ON</span></a>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <a href="CONSOLE" title="CONSOLE"><span style="color:#4593D8;">_CONSOLE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Close this console window or click main window and press a key!"</span>
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> How to use a Console window to copy screen output using the <i>Edit</i> menu by right clicking the console title bar.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#55FF55;">$CONSOLE</span></a>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <a href="CONSOLE" title="CONSOLE"><span style="color:#4593D8;">_CONSOLE</span></a>
c&amp;&amp; = <span style="color:#F580B1;">-1</span>: d&amp; = <span style="color:#F580B1;">-1</span>: e% = <span style="color:#F580B1;">-1</span>: f%% = <span style="color:#F580B1;">-1</span>
hx$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(f%%)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Max hex _BYTE = "</span>; hx$; <span style="color:#FFB100;">" with"</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(hx$); <span style="color:#FFB100;">"digits ="</span>; <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<span style="color:#FFB100;">"&amp;H"</span> + hx$)
hx$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(e%)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Max hex INTEGER = "</span>; hx$; <span style="color:#FFB100;">" with"</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(hx$); <span style="color:#FFB100;">"digits ="</span>; <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<span style="color:#FFB100;">"&amp;H"</span> + hx$)
hx$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(d&amp;)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Max hex LONG = "</span>; hx$; <span style="color:#FFB100;">" with"</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(hx$); <span style="color:#FFB100;">"digits ="</span>; <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<span style="color:#FFB100;">"&amp;H"</span> + hx$)
hx$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(c&amp;&amp;)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Max hex _INTEGER64 = "</span>; hx$; <span style="color:#FFB100;">" with"</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(hx$); <span style="color:#FFB100;">"digits ="</span>; <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<span style="color:#FFB100;">"&amp;H"</span> + hx$)
hx$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<span style="color:#F580B1;">9223372036854775807</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Max _INTEGER64 value = "</span>; hx$; <span style="color:#FFB100;">" with"</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(hx$); <span style="color:#FFB100;">"digits"</span>
hx$ = <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<span style="color:#F580B1;">-9223372036854775808</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Min _INTEGER64 value = "</span>; hx$; <span style="color:#FFB100;">" with"</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(hx$); <span style="color:#FFB100;">"digits"</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Max hex _BYTE = FF with 2 digits = 255
Max hex INTEGER = FFFF with 4 digits = 65535
Max hex LONG = FFFFFFFF with 8 digits = 4294967295
Max hex _INTEGER64 = FFFFFFFFFFFFFFFF with 16 digits =-1
Max _INTEGER64 value = 7FFFFFFFFFFFFFFF with 16 digits
Min _INTEGER64 value = 8000000000000000 with 16 digits
</pre>
</td></tr></tbody></table>
<dl><dd><i>Console:</i> Right click and select <i>Edit</i> &gt; <i>Select All</i> (mouse highlight after) then hit Enter or select <i>Edit</i> &gt; <i>Copy</i> to the clipboard.</dd></dl>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">Max hex _BYTE = FF with 2 digits = 255
Max hex INTEGER = FFFF with 4 digits = 65535
Max hex LONG = FFFFFFFF with 8 digits = 4294967295
Max hex _INTEGER64 = FFFFFFFFFFFFFFFF with 16 digits =-1
</pre>
</td></tr></tbody></table>
<dl><dd><i>Copied text:</i> The above text was copied after <i>Select All</i> was selected and the smaller area was re-highlighted with the mouse.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CLIPBOARD$_(function)" title="CLIPBOARD$ (function)">_CLIPBOARD$ (function)</a>, <a href="CLIPBOARD$" title="CLIPBOARD$">_CLIPBOARD$</a> (statement)</li>
<li><a href="CONSOLE" title="CONSOLE">_CONSOLE</a>, <a href="ECHO" title="ECHO">_ECHO</a></li>
<li><a href="$SCREENHIDE" title="$SCREENHIDE">$SCREENHIDE</a>, <a href="$SCREENSHOW" title="$SCREENSHOW">$SCREENSHOW</a> (QB64 <a href="Metacommand" title="Metacommand">Metacommands</a>)</li>
<li><a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a>, <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a></li>
<li><a href="C_Libraries#Console_Window" title="C Libraries">C Console Library</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035337
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.054 seconds
Real time usage: 0.072 seconds
Preprocessor visited node count: 564/1000000
Post‐expand include size: 4569/2097152 bytes
Template argument size: 1376/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 307/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   44.417      1 -total
 10.59%    4.704      1 Template:PageSyntax
  9.11%    4.047     33 Template:Cl
  8.10%    3.600      2 Template:Cm
  7.61%    3.381     31 Template:Text
  6.98%    3.099      2 Template:CodeStart
  6.19%    2.748      1 Template:PageExamples
  6.18%    2.747      1 Template:OutputStart
  5.90%    2.622      1 Template:PageDescription
  5.48%    2.433      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:95-0!canonical and timestamp 20240715035337 and revision id 8456.
 -->
</div>
</div>
</div>
</div>
</body>
</html>