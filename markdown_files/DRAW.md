<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DRAW - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DRAW rootpage-DRAW skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DRAW</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">DRAW</a> statement uses a <a href="STRING" title="STRING">STRING</a> expression to draw lines on the screen.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">DRAW</a> <i>drawString$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>drawString$</i> can be <a class="mw-selflink selflink">DRAW</a> instructions in quotation marks or a <a href="STRING" title="STRING">STRING</a> variable using <a class="mw-selflink selflink">DRAW</a> instructions.</li>
<li><a class="mw-selflink selflink">DRAW</a> starting coordinates can be set using <a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a>, <a href="CIRCLE" title="CIRCLE">CIRCLE</a> or <a href="LINE" title="LINE">LINE</a> ending positions.</li>
<li>Other graphic objects can be located at or relative to the last DRAW position using <a href="STEP" title="STEP">STEP</a>.</li>
<li><a class="mw-selflink selflink">DRAW</a> can inherit colors from other graphic statements such as <a href="PSET" title="PSET">PSET</a>, <a href="LINE" title="LINE">LINE</a> and <a href="CIRCLE" title="CIRCLE">CIRCLE</a>.</li>
<li>Draw strings use letters followed by the number of pixels to move, an angle, coordinate or a color value.</li>
<li>Draw strings are flexible with spacing. <b>Spacing is not required.</b> <a class="mw-selflink selflink">DRAW</a> will look for a number value after a valid letter.</li>
<li>DRAW statements are not case sensitive.
<ul><li>"<b>B</b>" (blind) before a line move designates that the line move will be hidden. Use to offset from a "P" or <a href="PAINT" title="PAINT">PAINT</a> border.</li>
<li>"<b>C</b> n" designates the color attribute or <a href="RGB" title="RGB">_RGB</a> <a href="STR$" title="STR$">string</a> numerical color value to be used in the draw statement immediately after.</li>
<li>"<b>M</b> x, y" can move to another coordinate area of the screen. When a + or - sign is used before a coordinate, it is a relative coordinate move similar to using the <a href="STEP" title="STEP">STEP</a> graphics keyword. DRAW "M+=" + <a href="VARPTR$" title="VARPTR$">VARPTR$</a>(variable%)</li>
<li>"<b>N</b>" before a line move designates that the graphic cursor will return to the starting position after the line is drawn.</li>
<li>"<b>P</b> f [, b]" is used to <a href="PAINT" title="PAINT">paint</a> enclosed objects. f denotes the fill color and b the border color, if needed.</li>
<li>"<b>S</b> n" changes the pixel move size of the lines. Default is 4 (1 pixel) minimum. "S8" would double the pixel line moves.</li>
<li>"<b>X</b>" + <a href="VARPTR$" title="VARPTR$">VARPTR$</a>(value) can draw another substring.</li></ul></li></ul>
<ul><li>Certain letter designations create line moves on the SCREEN. Each move is followed by the number of pixels:
<ul><li>"<b>D</b> n" draws a line vertically DOWN n pixels.</li>
<li>"<b>E</b> n" draws a diagonal / line going UP and RIGHT n pixels each direction.</li>
<li>"<b>F</b> n" draws a diagonal \ line going DOWN and RIGHT n pixels each direction.</li>
<li>"<b>G</b> n" draws a diagonal / LINE going DOWN and LEFT n pixels each direction.</li>
<li>"<b>H</b> n" draws a diagonal \ LINE going UP and LEFT n pixels each direction.</li>
<li>"<b>L</b> n" draws a line horizontally LEFT n pixels.</li>
<li>"<b>R</b> n" draws a line horizontally RIGHT n pixels.</li>
<li>"<b>U</b> n" draws a line vertically UP n pixels.</li></ul></li></ul>
<ul><li>Angles are used to rotate all subsequent draw moves.
<ul><li>"<b>A</b> n" can use values of 1 to 3 to rotate up to 3 90 degree(270) angles.</li>
<li><b>TA</b> n" can use any n angle from -360 to 0 to 360 to rotate a DRAW (Turn Angle). "TA0" resets to normal.</li>
<li>When <a href="VARPTR$" title="VARPTR$">VARPTR$</a> is used, DRAW functions such as <b>TA</b> angles use an equal sign: "TA=" + VARPTR$(angle%)</li></ul></li>
<li>The graphic cursor is set to the center of the program window on program start for <a href="STEP" title="STEP">STEP</a> relative coordinates.</li>
<li><b>DRAW can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Placing an octagon shape DRAW across the the screen using PSET.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> SCREEN 12
 octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
 <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
 FOR i% = 1 TO 11
   <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (i% * 50, 100), 15
   <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> .5         ' delay for demo
   <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> octagon$     ' DRAW the octagon using variable
   <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> .5         ' delay for demo
 NEXT i%
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> Once a DRAW string variable is created, it can be used to draw a shape throughout the program at any time.
<i>Example 2:</i> Creating an analog clock's hour markers using "TA=" + <a href="VARPTR$" title="VARPTR$">VARPTR$</a>(angle).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> SCREEN 12
 FOR angle = 0 TO 360 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> 30             ' 360/12 hour circles = 30 degrees apart
   PSET (175, 250), 6 ' stay at center point of clock
   <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "TA=" + <a href="VARPTR$" title="VARPTR$"><span style="color:#4593D8;">VARPTR$</span></a>(angle) + "BU100" ' move invisibly to set next circle's center point
   <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(0, 0), 5, 12 ' circle placed at end of blind line
   <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "P9, 12" ' paint inside of circle
   <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 1     ' slowed for demo only
 NEXT
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> To place 12 circles in a circle each move is 30 degrees. PSET sets the center of the circular path every loop. TA moves counter-clockwise with positive degree angles. Once TA sets the angle a blind Up move is at that angle. The hour circles use the end point of the blind line as centers using the STEP relative coordinates of 0. After the circles are drawn, a draw "P" string paints the circle centers. DRAW paint strings use the last coordinate position also.
<i>Example 3:</i> Creating a moving second hand for the clock above (SCREEN 12). (See <a href="TIME$" title="TIME$">TIME$</a> example 1)
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> DO: sec$ = <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>, 2) ' get actual seconds from TIME$ function
   degree$ = <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(<a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(sec$) * -6) ' 60 second moves. TA uses negative angles for clockwise moves
   <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (175, 250), 9 ' stay at clock center
   DRAW "TA" + degree$ + "U90" ' up becomes TA directional line
   DO: LOOP UNTIL RIGHT$(TIME$, 2) &lt;&gt; sec$ ' wait for a new second value
   IF INKEY$ &lt;&gt; "" THEN <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a> ' any key exit
   PSET (175, 250), 0 ' set at clock center to erase line
   DRAW "TA" + degree$ + "U90" ' erases old second hand line using color 0 from PSET
 LOOP
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> The degrees to move from the original UP line move is calculated by dividing 360/60 seconds in a full rotation. That value of 6 is made negative to use TA correctly and multiplied by the <a href="VAL" title="VAL">VALue</a> of seconds from the TIME$ function. The degree angle is converted by <a href="STR$" title="STR$">STR$</a> to a string and added to the DRAW string using the <a href="STRING" title="STRING">STRING</a> <b>concatenation +</b> operator. Do not use semicolons to create DRAW strings. Once the second hand is placed on the screen, a loop waits for the second value to change. It then erases the hand and it repeats the process again.
<i>Example 4:</i> Creating digital displays using DRAW format strings to create the LED segments. (See <a href="SELECT_CASE" title="SELECT CASE">SELECT EVERYCASE</a> example 5)
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
DO
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a number 0 to 9: ", num
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> num
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 2, 3, 5 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 20), 12
      <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "E2R30F2G2L30H2BR5P12,12" 'top horiz
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> num
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 4 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 6, 8, 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 20), 12
      <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "F2D30G2H2U30E2BD5P12,12" 'left top vert
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> num
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 2, 6, 8: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 54), 12
      <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "F2D30G2H2U30E2BD5P12, 12" 'left bot vert
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> num
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 2 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 6, 8, 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 54), 12
      <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "E2R30F2G2L30H2BR5P12, 12" 'middle horiz
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> num
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 4, 7 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (54, 20), 12
      <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "F2D30G2H2U30E2BD5P12,12" 'top right vert
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> num
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 1, 3 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (54, 54), 12
      <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "F2D30G2H2U30E2BD5P12,12" 'bottom right vert
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> num
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 2, 3, 5, 6, 8: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 88), 12
      <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "E2R30F2G2L30H2BR5P12,12" 'bottom horiz
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> num &gt; 9
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The DRAW strings can be used more than once with different <a href="PSET" title="PSET">PSET</a> positions to create more digits.</dd></dl>
<p>
<i>Example 5:</i> Using 32 bit or <a href="RGB" title="RGB">_RGB</a> color <a href="STR$" title="STR$">string</a> values when using the DRAW C text statement
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 800, 12)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="ALPHA" title="ALPHA"><span style="color:#4593D8;">_ALPHA</span></a>(10), <a href="RED" title="RED"><span style="color:#4593D8;">_RED</span></a>(10), <a href="GREEN" title="GREEN"><span style="color:#4593D8;">_GREEN</span></a>(10), <a href="BLUE" title="BLUE"><span style="color:#4593D8;">_BLUE</span></a>(10)
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 800, 32) 'comment out this line to use the non-32 bit screen mode 12
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="ALPHA" title="ALPHA"><span style="color:#4593D8;">_ALPHA</span></a>(10), <a href="RED" title="RED"><span style="color:#4593D8;">_RED</span></a>(10), <a href="GREEN" title="GREEN"><span style="color:#4593D8;">_GREEN</span></a>(10), <a href="BLUE" title="BLUE"><span style="color:#4593D8;">_BLUE</span></a>(10)
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (400, 400), 0 ' move to 320, 240... draw will start where pset leaves off
c = 14
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> k <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
k = <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(80, 255, 80)
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> repeat = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 16
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> p = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 359
    c = c + 1: d = c / 14
    <a class="mw-selflink selflink"><span style="color:#4593D8;">DRAW</span></a> "c" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(k) + " ta" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(p) + " bu " + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(d) + "l7 u7 r7 d7 bd " + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(d)
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> p
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> repeat
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> DRAW strings will ignore spaces between letters and numbers so string trimming is not necessary.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LINE" title="LINE">LINE</a>, <a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a>, <a href="CIRCLE" title="CIRCLE">CIRCLE</a></li>
<li><a href="PAINT" title="PAINT">PAINT</a>, <a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="COLOR" title="COLOR">COLOR</a>, <a href="PLAY" title="PLAY">PLAY</a></li>
<li><a href="TIME$" title="TIME$">TIME$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061258
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.074 seconds
Real time usage: 0.097 seconds
Preprocessor visited node count: 724/1000000
Post‐expand include size: 6111/2097152 bytes
Template argument size: 1083/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   53.306      1 -total
 21.39%   11.403      1 Template:PageDescription
 17.87%    9.526     97 Template:Cl
  7.29%    3.885      1 Template:PageExamples
  6.78%    3.616      5 Template:CodeStart
  5.50%    2.931      1 Template:Small
  5.48%    2.921      1 Template:PageSyntax
  5.31%    2.832      1 Template:PageSeeAlso
  4.78%    2.547      5 Template:CodeEnd
  4.57%    2.437      2 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:438-0!canonical and timestamp 20240715061258 and revision id 7867.
 -->
</div>
</div>
</div>
</div>
</body>
</html>