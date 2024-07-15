<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CIRCLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CIRCLE rootpage-CIRCLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CIRCLE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">CIRCLE</a> statement is used in graphic <a href="SCREEN" title="SCREEN">SCREEN</a> modes to create circles, arcs or ellipses.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CIRCLE</a> [[[STEP]<b>(</b><i>column</i><b>,</b> <i>row</i><b>),</b> <i>radius%</i><b>,</b> [<i>drawColor%</i>][, <i>startRadian!</i>, <i>stopRadian!</i>] [, <i>aspect!</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Can use <a href="STEP" title="STEP">STEP</a> for relative coordinate moves from the previous graphic coordinates.</li>
<li>Coordinates designate the center position of the circle. Can be partially drawn offscreen.</li>
<li><i>radius%</i> is an <a href="INTEGER" title="INTEGER">INTEGER</a> value for half of the total circle diameter.</li>
<li><i>drawColor%</i> is any available color attribute in the <a href="SCREEN" title="SCREEN">SCREEN</a> mode used.</li>
<li><i>startRadian!</i> and <i>stopRadian!</i> can be any <a href="SINGLE" title="SINGLE">SINGLE</a> value from 0 to 2 * π to create partial circles or ellipses.</li>
<li><i>aspect!</i> <a href="SINGLE" title="SINGLE">SINGLE</a> values of 0 to 1 affect the vertical height and values over 1 affect the horizontal width of an ellipse. Aspect = 1 is a normal circle.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>When using <i>aspect!</i> the <i>startRadian!</i> and <i>stopRadian!</i> commas must be included even if not used.</li>
<li>Radians move in a counter clockwise direction from 0 to 2 * π. Zero and 2 * π are the same circle radian at 3 o'clock.</li>
<li>Negative radian values can be used to draw lines from the end of an arc or partial ellipse to the circle center.</li>
<li>Commas after the <i>drawColor%</i> parameter are not required when creating a normal circle. <i>drawColor%</i> can also be omitted to use the last color used in a draw statement.</li>
<li>The graphic cursor is set to the center of the program window on program start for <a href="STEP" title="STEP">STEP</a> relative coordinates.</li>
<li><b>CIRCLE can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Finding when the mouse is inside of a circular area:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
r&amp; = 200 'radius    change circle size and position here
cx&amp; = 320 'center x horizontal
cy&amp; = 240 'center y vertical
DO
  i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
  x&amp; = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
  y&amp; = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
  xy&amp; = ((x&amp; - cx&amp;) ^ 2) + ((y&amp; - cy&amp;) ^ 2) 'Pythagorean theorem
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> r&amp; ^ 2 &gt;= xy&amp; <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (cx&amp;, cy&amp;), r&amp;, 10 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (cx&amp;, cy&amp;), r&amp;, 12
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) 'escape key exit
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The square of the circle radius will be greater than or equal to the sum of the square of the mouse coordinates minus the center position when the pointer is inside of the circle. In this example the circle color will change from red to green.</dd></dl>
<p>
<i>Example 2:</i> Program illustrates how the CIRCLE command using a negative radian value can be used to create the hands of a clock.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> PI = 3.141593 'The mathematical value of PI to six places. You can also use QB64's native _PI.
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> clock(60)             'A dimensioned array to hold 60 radian points
clockcount% = 15          'A counter to keep track of the radians
'* Start at radian 2*PI and continue clockwise to radian 0
'* Since radian 2*PI points directly right, we need to start clockcount%
'* at 15 (for 15 seconds).  The <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a>/<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> loop counts backwards in increments
'* of 60 giving us the 60 second clock points.  These points are then stored
'* in the dimensioned array clock() to be used later.
'*
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> radian = 2 * PI <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -(2 * PI) / 60
    clock(clockcount%) = radian
    clockcount% = clockcount% + 1
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> clockcount% = 61 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> clockcount% = 1
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> radian
'* Change to a graphics screen and draw the clock face
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 7
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14, 0
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Ritchie's Clock"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 9, 0
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Uses <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> to"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "draw hands!"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 8, 0
<a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 110, 8 'circle with radius of 110 and dark gray
<a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 102, 8 'circle with radius of 102 and dark gray
<a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> (265, 100), 8, 8 'fill between the two dark gray circles with gray
<a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 110, 7 'circle with radius of 110 and light gray
'*
'* Get the current time from the QuickBASIC built in variable <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>
'* Since <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a> is a string, we need to extract the hours, minutes and
'* seconds from it using <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>, <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a> and <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>. Then, each of these
'* extractions need to be converted to a numeric value using VAL and
'* stored in their respective variables.
'*
seconds% = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2))) 'extract seconds from <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> seconds% = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> seconds% = 60 'array counts 1 to 60 not 0 to 59
previoussecond% = seconds% 'hold current second for later use
minutes% = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 4, 2))) 'extract minutes from <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> minutes% = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> minutes% = 60 'array counts 1 to 60 not 0 to 59
previousminute% = minutes% 'hold current minute for later use
hours% = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2))) 'extract hour from <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> hours% &gt;= 12 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> hours% = hours% - 12 'convert from military time
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> hours% = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> hours% = 12 'count from 1 to 12 not 0 to 11
previoushour% = hours% 'hold current hour for later use
'*
'* Start of main program loop
'*
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> seconds% &lt;&gt; previoussecond% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'has a second elapsed?
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 22, 17 'print the time on the screen at
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>; 'position 22, 17
        '* Since a second has elapsed we need to erase the old second hand
        '* position and draw the new position
        <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 100, 0, -clock(previoussecond%), clock(previoussecond%)
        <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 100, 15, -clock(seconds%), clock(seconds%)
        previoussecond% = seconds% 'hold current second for later use
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> minutes% &lt;&gt; previousminute% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'has a minute elapsed?
            '* Since a minute has elapsed we need to erase the old hour hand position
            <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 90, 0, -clock(previousminute%), clock(previousminute%)
            previousminute% = minutes% 'hold current minute for later use
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        '*
        '* Draw the current minute hand position
        '*
        <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 90, 14, -clock(minutes%), clock(minutes%)
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> hours% &lt;&gt; previoushour% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'has an hour elapsed?
            '* Since an hour has elapsed we need to erase the old hour hand position
            <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 75, 0, -clock(previoushour% * 5), clock(previoushour% * 5)
            previoushour% = hours% 'hold current hour for later use
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        '*
        '* Draw the current hour hand position
        '*
        <a class="mw-selflink selflink"><span style="color:#4593D8;">CIRCLE</span></a> (160, 100), 75, 12, -clock(hours% * 5), clock(hours% * 5)
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    seconds% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2)) 'extract time again and do all over
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> seconds% = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> seconds% = 60
    minutes% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 4, 2))
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> minutes% = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> minutes% = 60
    hours% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2))
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> hours% &gt;= 12 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> hours% = hours% - 12
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> hours% = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> hours% = 12
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; "" 'stop program if user presses a key
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="STEP" title="STEP">STEP</a>, <a href="DRAW" title="DRAW">DRAW</a></li>
<li><a href="LINE" title="LINE">LINE</a>, <a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="SCREEN_(function)" title="SCREEN (function)">SCREEN (function)</a></li>
<li><a href="Alternative_circle_routine" title="Alternative circle routine">Alternative circle routine</a> <span style="color:#777777;">(member-contributed program)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715012502
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.069 seconds
Real time usage: 0.091 seconds
Preprocessor visited node count: 833/1000000
Post‐expand include size: 6506/2097152 bytes
Template argument size: 1260/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   43.024      1 -total
 13.77%    5.924    104 Template:Cl
 11.62%    4.999      1 Template:PageSyntax
  7.74%    3.328      1 Template:PageParameters
  6.87%    2.954      1 Template:Text
  6.38%    2.744     17 Template:Parameter
  6.18%    2.660      1 Template:Small
  5.86%    2.521      1 Template:PageDescription
  5.55%    2.390      1 Template:PageExamples
  5.41%    2.326      2 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:410-0!canonical and timestamp 20240715012502 and revision id 8114.
 -->
</div>
</div>
</div>
</div>
</body>
</html>