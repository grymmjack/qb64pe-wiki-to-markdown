<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MOUSEMOVE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOUSEMOVE rootpage-MOUSEMOVE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MOUSEMOVE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MOUSEMOVE</a> statement moves the mouse pointer to a new position on the screen as determined by the column and row coordinates.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_MOUSEMOVE</a> <i>column%</i>, <i>row%</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>column%</i> is the horizontal pixel coordinate to place the mouse pointer and can be any value from 0 to <a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH</a>(0) - 1.</li>
<li><i>row%</i> is the vertical pixel position to place the mouse pointer and can be any value from 0 to <a href="HEIGHT" title="HEIGHT">_HEIGHT</a>(0) - 1</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Maximum coordinate values are based on a program's current <a href="SCREEN" title="SCREEN">SCREEN</a> mode resolution or the pixel size set by <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>.</li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a> 0 uses text block coordinates. <b>Coordinates off the screen area will create an "Illegal Function Call" <a href="ERROR_Codes" title="ERROR Codes">ERROR</a></b></li>
<li>Can be used to position the pointer to a default dialog button or move the cursor away from a button so it is not clicked twice.</li>
<li>Does not require <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> to be used, but all moves will be remembered and can be read by mouse functions.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Versions prior to 1.000</b> (Version 1.000 had this function disabled for compatibility reasons.)</li>
<li><b>Version 1.1 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> How to move the mouse cursor using remembered mouse movements. Press any key to quit.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a> 'start reading mouse events before INPUT to hold in memory
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Move the mouse pointer and make a few clicks, then press Enter!", dummy$
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEMOVE</span></a> 1, 1
DO: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 30
    count = count + 1
    i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
    x = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>: y = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
    b = <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> count, x, y, b
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEMOVE</span></a> x, y
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> i = 0 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &gt; ""
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Done!"
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> function will hold previous and _MOUSEMOVE events so press any key when you want to quit.</dd></dl>
<dl><dd><b>Note: <a href="INPUT" title="INPUT">INPUT</a>, <a href="INPUT$" title="INPUT$">INPUT$</a> and <a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a> will allow continued reading of mouse events while awaiting program user input!</b></dd>
<dd>It is recommended that a <a class="mw-redirect" href="WHILE" title="WHILE">WHILE</a> <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>: <a class="mw-redirect" href="WEND" title="WEND">WEND</a> loop be used immediately after to clear stored mouse events.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1141" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEY" title="MOUSEY">_MOUSEY</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062411
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 162/1000000
Post‐expand include size: 1709/2097152 bytes
Template argument size: 266/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.943      1 -total
 12.11%    3.020      1 Template:PageNavigation
 10.21%    2.548     17 Template:Cl
  9.62%    2.400      1 Template:PageSeeAlso
  9.27%    2.311      1 Template:PageSyntax
  9.05%    2.258      1 Template:PageDescription
  7.92%    1.975      4 Template:Parameter
  6.94%    1.731      1 Template:CodeStart
  6.91%    1.724      1 Template:PageParameters
  6.83%    1.704      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:191-0!canonical and timestamp 20240715062411 and revision id 8890.
 -->
</div>
</div>
</div>
</div>
</body>
</html>