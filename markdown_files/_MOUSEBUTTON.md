<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MOUSEBUTTON - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOUSEBUTTON rootpage-MOUSEBUTTON skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MOUSEBUTTON</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MOUSEBUTTON</a> function returns the button status of a specified mouse button when read after <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>buttonStatus%%</i> = <a class="mw-selflink selflink">_MOUSEBUTTON</a>(<i>buttoNumber</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><a href="INTEGER" title="INTEGER">INTEGER</a> <i>buttoNumber</i> designates the mouse button to read (See <a href="DEVICES" title="DEVICES">_DEVICES</a> for more than 3).
<ul><li>1 = Left mouse button</li>
<li>2 = Right mouse button</li>
<li>3 = Center or scroll button</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns -1 if the corresponding <i>buttoNumber</i> is pressed or zero when released.</li>
<li>Read <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> first to return the current button up or down status. (See Example 2)</li>
<li>Button clicks and mouse movements will be remembered and should be cleared after an <a href="INPUT" title="INPUT">INPUT</a> statement or other interruption.</li>
<li>To clear unread mouse input, use a <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> loop that loops until it returns 0.</li>
<li>Use <a href="DEVICE$" title="DEVICE$">_DEVICE$</a> to find the "[MOUSE]" <a href="DEVICES" title="DEVICES">_DEVICES</a> number to find the number of buttons available using <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>.</li>
<li><b>Note:</b> The center mouse button can also be read as <a href="BUTTON" title="BUTTON">_BUTTON</a>(2) on <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a>(2) when a mouse is present.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Finding the number of mouse buttons available in QB64. This could also be used for other controller devices.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> d = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a>  'number of input devices found
  dev$ = <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(d)
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(dev$, "[MOUSE]") <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> buttons = <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(d): <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> buttons; "mouse buttons available"
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> How to monitor when a button is down or wait until a mouse button is not held down.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hold down the left mouse button until you want to quit!"
DO
    i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a> ' read #1
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Left button down!": <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> '                                                      need to wait
    i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a> '  read #2                         until the mouse
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1) '                       button is released
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "DONE!"
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Checking for a click or a double-click by the user.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>  'main program loop
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>                'check mouse status
    buttondown = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1)
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> buttondown                 'check for button release
    i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
    buttondown = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1)
    Click = 1
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Click = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>                   'if button was pressed and released
    t = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a> + .3
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a> &lt; t      'check for a second press within .3 seconds
      i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> Click = 2: <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Click = 2 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Double click" <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Click"
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  Click = 0: buttondown = 0            'reset where needed
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> To find the current button status read <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> repeatedly. The <a href="TIMER_(function)" title="TIMER (function)">TIMER</a> loop looks for a second click.</dd></dl>
<p>
<i>Example 4:</i> Verifying that a user clicked and released a mouse button on a program button.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (250, 250)-(300, 300), 14, BF
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  Mouser mx, my, mb
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> mb <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> mx &gt;= 250 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> my &gt;= 250 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> mx &lt;= 300 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> my &lt;= 300 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'button down
      <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> mb 'wait for button release
        Mouser mx, my, mb
      <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
      'verify mouse still in box area
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> mx &gt;= 250 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> my &gt;= 250 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> mx &lt;= 300 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> my &lt;= 300 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Click verified on yellow box!"
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> Mouser (x, y, b)
mi = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
b = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1)
x = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
y = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The mouse SUB has no internal <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> loop so that no button presses, releases or moves are missed.</dd>
<dd>If the above read procedure goes to another one, it may be advisable to skip over unread input in a <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> only loop.</dd></dl>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext"><a href="SUB" title="SUB"><span style="color:blue;">SUB</span></a> Catchup
<a href="DO...LOOP" title="DO...LOOP"><span style="color:blue;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:blue;">WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:blue;">_MOUSEINPUT</span></a>: <a href="LOOP" title="LOOP"><span style="color:blue;">LOOP </span></a>
<a href="END_SUB" title="END SUB"><span style="color:blue;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd>The above procedure can be used to catch up after <a href="INPUT" title="INPUT">INPUT</a>, <a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a> or <a href="INPUT$" title="INPUT$">INPUT$</a> delays when mouse input may accumulate.</dd></dl>
<p>
<i>Example 5:</i> Combining mouse button or keyboard selections in a menu or test:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> 'main program loop in demo only
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "A" 'position A, B &amp; C in same position on every question
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 12, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "B"
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 14, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "C" 'demo only
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 10 'get user answer loop
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> 'read mouse
    K$ = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>) 'read keypresses also
    x% = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
    y% = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
    Lclick = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1)
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x%, y%, Lclick 'only used to find mouse coordinates
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x% = 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y% = 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Lclick <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'position clicked
      DO
        i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
        x% = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
        y% = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
      <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1)
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x% = 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y% = 10 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> K$ = "A" 'position released
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x% = 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y% = 12 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Lclick <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'position clicked
      DO
        i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
        x% = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
        y% = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
      <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1)
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x% = 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y% = 12 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> K$ = "B" 'position released
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x% = 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y% = 14 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Lclick <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'position clicked
      DO
        i = <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
        x% = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
        y% = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
      <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1)
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x% = 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y% = 14 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> K$ = "C" 'position released
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> K$ = "A" <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> K$ = "B" <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> K$ = "C" '<a href="GOTO" title="GOTO"><span style="color:#4593D8;">GOTO</span></a> next question
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(K$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'DEMO ONLY
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 22, 35: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "  Answer = "; K$ 'display user answer at location
    <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 2 'allow time for user to view answer
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 22, 35: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "SELECT AGAIN"
    K$ = "" 'reset K$
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> 'DEMO only loop use red X box to quit
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> User can cancel letter selection by moving pointer off letter before releasing the left mouse button.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEY" title="MOUSEY">_MOUSEY</a>, <a href="MOUSEWHEEL" title="MOUSEWHEEL">_MOUSEWHEEL</a></li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>, <a href="MOUSEMOVE" title="MOUSEMOVE">_MOUSEMOVE</a></li>
<li><a href="MOUSESHOW" title="MOUSESHOW">_MOUSESHOW</a>, <a href="MOUSEHIDE" title="MOUSEHIDE">_MOUSEHIDE</a></li>
<li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a></li>
<li><a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="BUTTONCHANGE" title="BUTTONCHANGE">_BUTTONCHANGE</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714154041
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.084 seconds
Real time usage: 0.103 seconds
Preprocessor visited node count: 1259/1000000
Post‐expand include size: 10391/2097152 bytes
Template argument size: 2230/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   54.501      1 -total
 17.27%    9.411    165 Template:Cl
  6.54%    3.564      1 Template:TextStart
  6.17%    3.360      1 Template:Small
  5.29%    2.883      6 Template:Cb
  5.28%    2.876      1 Template:TextEnd
  5.18%    2.821      1 Template:PageParameters
  4.91%    2.678      1 Template:PageSyntax
  4.73%    2.577      5 Template:CodeEnd
  4.71%    2.569      5 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:188-0!canonical and timestamp 20240714154041 and revision id 8047.
 -->
</div>
</div>
</div>
</div>
</body>
</html>