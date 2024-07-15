<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CONSOLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CONSOLE rootpage-CONSOLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CONSOLE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CONSOLE</a> statement can be used to turn a console window ON/OFF.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_CONSOLE</a> {OFF|ON}</dd>
<dd>_DEST <a class="mw-selflink selflink">_CONSOLE</a></dd></dl>
<p>
</p>
<ul><li><a class="mw-selflink selflink">_CONSOLE</a> OFF or ON must be used after the <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> <a href="Metacommand" title="Metacommand">Metacommand</a> has established that a console window is desired.</li>
<li><a class="mw-selflink selflink">_CONSOLE</a> OFF turns the console window off once a console has been established using <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a>:ON or ONLY.</li>
<li><a class="mw-selflink selflink">_CONSOLE</a> ON should only be used after the console window has been turned OFF previously.</li>
<li><a href="DEST" title="DEST">_DEST</a> <a class="mw-selflink selflink">_CONSOLE</a> can be used to send screen output to the console window using QB64 commands such as <a href="PRINT" title="PRINT">PRINT</a>.</li>
<li><a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a> or <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a> can be used to hide or display the main program window.</li>
<li>The <a href="$SCREENHIDE" title="$SCREENHIDE">$SCREENHIDE</a> <a href="Metacommand" title="Metacommand">Metacommand</a> can hide the main program window throughout a program when only the console is used.</li>
<li><b>Note:</b> Text can be copied partially or totally from console screens in Windows by highlighting and using the title bar menu.</li></ul>
<dl><dd><dl><dd>To copy console text output, right click the title bar and select <i>Edit</i> for <i>Mark</i> to highlight and repeat to <i>Copy</i>.</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Hiding and displaying a console window. Use <a href="DELAY" title="DELAY">_DELAY</a> to place console in front of main program window.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$CONSOLE" title="$CONSOLE"><span style="color:#55FF55;">$CONSOLE</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CONSOLE</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a> <span style="color:#919191;">'close original console</span>
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">2</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CONSOLE</span></a> <a href="ON" title="ON"><span style="color:#4593D8;">ON</span></a> <span style="color:#919191;">'place console above program window</span>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_CONSOLE</span></a>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Enter your name: "</span>, nme$ <span style="color:#919191;">'get program input</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CONSOLE</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a> <span style="color:#919191;">'close console</span>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <span style="color:#F580B1;">0</span> <span style="color:#919191;">'destination program window</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> nme$
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="DEST" title="DEST">destination</a> must be changed with <a href="DEST" title="DEST">_DEST</a> <a class="mw-selflink selflink">_CONSOLE</a> to get <a href="INPUT" title="INPUT">INPUT</a> from the <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> screen.</dd></dl>
<p><i>Example 2:</i> <a href="CONSOLETITLE" title="CONSOLETITLE">_CONSOLETITLE</a> can be used to create a console title, but it must be redone every time the console window is restored once turned off:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$CONSOLE" title="$CONSOLE"><span style="color:#55FF55;">$CONSOLE</span></a>
<a href="CONSOLETITLE" title="CONSOLETITLE"><span style="color:#4593D8;">_CONSOLETITLE</span></a> <span style="color:#FFB100;">"firstone"</span>
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">10</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CONSOLE</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a>
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">10</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CONSOLE</span></a> <a href="ON" title="ON"><span style="color:#4593D8;">ON</span></a>
<a href="CONSOLETITLE" title="CONSOLETITLE"><span style="color:#4593D8;">_CONSOLETITLE</span></a> <span style="color:#FFB100;">"secondone"</span>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Some versions of Windows may display the program path or Administrator: prefix in console title bars.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a>, <a href="CONSOLETITLE" title="CONSOLETITLE">_CONSOLETITLE</a></li>
<li><a href="$SCREENHIDE" title="$SCREENHIDE">$SCREENHIDE</a>, <a href="$SCREENSHOW" title="$SCREENSHOW">$SCREENSHOW</a> <span style="color:#777777;">(QB64 <a href="Metacommand" title="Metacommand">Metacommands</a>)</span></li>
<li><a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a>, <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a></li>
<li><a href="DEST" title="DEST">_DEST</a>, <a href="ECHO" title="ECHO">_ECHO</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714145512
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 296/1000000
Post‐expand include size: 2678/2097152 bytes
Template argument size: 673/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 157/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.480      1 -total
 13.63%    3.200     21 Template:Cl
 12.52%    2.940     13 Template:Text
 10.80%    2.536      1 Template:PageSyntax
  9.43%    2.215      2 Template:Cm
  9.08%    2.131      1 Template:PageExamples
  9.01%    2.115      2 Template:CodeStart
  7.59%    1.781      1 Template:PageSeeAlso
  7.45%    1.749      2 Template:CodeEnd
  7.26%    1.705      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:97-0!canonical and timestamp 20240714145512 and revision id 8455.
 -->
</div>
</div>
</div>
</div>
</body>
</html>