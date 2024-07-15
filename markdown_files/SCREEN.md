<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SCREEN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SCREEN rootpage-SCREEN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SCREEN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">SCREEN</a> statement sets the video display mode and size of the program window's workspace.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">SCREEN</a> {<i>mode%</i>|<i>imagehandle&amp;</i>} [, , active_page, visual_page]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The SCREEN <i>mode</i> <a href="INTEGER" title="INTEGER">INTEGER</a> values available today are 0 to 2 and 7 to 13 listed below.</li>
<li><b>QB64</b> can use a <a href="LONG" title="LONG">LONG</a> <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> page or <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> file <i>image handle</i> value instead.</li>
<li>The empty comma disables color when any value is used. <b>DO NOT USE!</b> Include the comma ONLY when using page flipping.</li>
<li>If the SCREEN mode supports pages, the <i>active page</i> is the page to be worked on while <i>visual page</i> is the one displayed.</li></ul>
<p>
<i>Usage:</i>
</p>
<ul><li>No SCREEN statement in a program defaults to <a class="mw-selflink selflink">SCREEN</a> 0 text ONLY mode.</li>
<li>A SCREEN statement that changes screen modes also clears the screen like <a href="CLS" title="CLS">CLS</a>. Nothing on the screen is retained.</li>
<li>Some screen mode text sizes are adjustable with <a href="WIDTH" title="WIDTH">WIDTH</a> and all <b>QB64</b> screens support <a href="PCOPY" title="PCOPY">PCOPY</a> and page flipping.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">                       <b>LEGACY SCREEN MODES AT A GLANCE</b>
 <b>Screen      Text           Graphics          Colors      Video    Text      Default</b>
  <b>Mode   Rows   Columns   Width   Height  Attrib.   BPP   Pages    Block    QB64 Font</b>
   0   25/43/50  80/40    No graphics     16/16 DAC  4     0-7     -----    _FONT 16
   1      25      40      320     200     16/4 BG    4     none    8 X 8    _FONT 8
   2      25      80      640     200      2/mono    1     none    8 X 8    _FONT 8
   .................................................................................
   7      25      40      320     200     16/16 DAC  4     0-7     8 X 8    _FONT 8
   8      25      80      640     200     16/16      4     0-3     8 X 8    _FONT 8
   9      25      80      640     350     16/64 DAC  4     0-1     8 X 14   _FONT 14
  10      25      80      640     350     4/2 GScale 2     none    8 X 14   _FONT 14
  11     30/60    80      640     480      2/mono    1     none    8 X 16   _FONT 16
  12     30/60    80      640     480     16/262K    4     none    8 X 16   _FONT 16
  13      25      40      320     200     256/65K    8     none    8 X 8    _FONT 8
              <b>QB64 allows video paging and <a href="PCOPY" title="PCOPY">PCOPY</a> in ALL screen modes!</b>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="QB64_Custom_Screen_Modes">QB64 Custom Screen Modes</span></h2>
<dl><dd><a class="mw-selflink selflink">SCREEN</a> <i>imagehandle&amp;</i> [, , <i>active_page</i>, <i>visual_page</i>]</dd></dl>
<dl><dd><a class="mw-selflink selflink">SCREEN</a> <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>(<i>wide&amp;</i>, <i>high&amp;</i>[, {<i>mode</i>|<i>256</i>|<i>32</i>}]) [, , <i>active_page</i>, <i>visual_page</i>]</dd></dl>
<dl><dd><a class="mw-selflink selflink">SCREEN</a> <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>(<i>file$</i>[, {<i>mode</i>|<i>256</i>|<i>32</i>}]) [, , <i>active_page</i>, <i>visual_page</i>]</dd></dl>
<p>
</p>
<ul><li>Custom screen modes can be created using a <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> or <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> function <i>imagehandle</i> return value.</li>
<li><b>QB64</b> screen modes 0 to 2 and 7 to 13 can be emulated with the same color depth and text block size and different dimensions.</li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> screens can be any set size. A screen mode can be emulated or 256 or 32 bit colors can be designated.</li>
<li>The <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> screen size will be the size of the image loaded. Can designate a <i>mode</i> or 256 or 32 bit colors.</li>
<li><b>QB64</b> allows page flipping or a <a href="PCOPY" title="PCOPY">PCOPY</a> in ANY SCREEN mode. <a href="DISPLAY" title="DISPLAY">_DISPLAY</a> can also be used to reduce flickering in animations.</li>
<li>All SCREEN modes are Windows in QB64. Use <a href="FULLSCREEN" title="FULLSCREEN">_FULLSCREEN</a> to set the window area to full screen.</li>
<li><a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a> can position a window or the _MIDDLE option can center it on the desktop.</li></ul>
<p style="text-align: center">(<a href="#toc">Return to Table of Contents</a>)</p>
<p>
</p>
<h2><span class="mw-headline" id="Legacy_Screen_Modes">Legacy Screen Modes</span></h2>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 0</b> (default mode) is a <b>text only</b> screen mode. 64 (VGA) colors with hi-intensity(blinking) colors 16 to 31. (<a href="DAC" title="DAC">DAC</a> attrib 6, 8 to 15). 8 Background colors intensities only(0 - 7). No graphics are possible! Normally runs in a window. ALT-Enter switches from a window to fullscreen. To automatically run in <b>QBasic</b> fullscreen, use another Screen mode before using <a class="mw-selflink selflink">SCREEN</a> 0.  Can use <a href="PCOPY" title="PCOPY">PCOPY</a> with video pages 0 to 7. Text is 25, 43 or 50 rows by 40 or 80 columns. Default is 25 by 80. See <a href="WIDTH" title="WIDTH">WIDTH</a>.</li></ul>
<dl><dd><b>Note:</b> Use <a href="OUT" title="OUT">OUT</a> or <a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a> to create higher intensity color backgrounds than <a href="COLOR" title="COLOR">COLOR</a> , 7.</dd></dl>
<dl><dd><dl><dd><dl><dd><b>All other available <a class="mw-selflink selflink">SCREEN</a> modes can use text and graphics and are fullscreen in QBasic ONLY.</b></dd></dl></dd></dl></dd></dl>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 1</b> has 4 background color attributes. 0 = black, 1 = blue, 2 = green, 3 = grey. White foreground only. Text is 25 by 40. White graphics is 320 by 200.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 2</b> is <b>monochrome</b> with black background and white foreground. Text is 25 by 80. White graphics 640 by 200.          NO <a href="COLOR" title="COLOR">COLOR</a> keyword allowed.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 3 to 6 are no longer supported</b> on most computers! Using them will cause a video <a href="ERROR_Codes" title="ERROR Codes">error</a>!</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 7</b> has 16 color attributes (<a href="DAC" title="DAC">DAC</a> attrib. 8 to 15) with background colors. Text 25 rows by 40 columns. Graphics 320 columns by 200 rows. Video  pages 0 to 7 for flipping or <a href="PCOPY" title="PCOPY">PCOPY</a>.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 8</b> has 16 color attributes with background. Text is 25 by 80. Graphics is 640 by 200. Video pages 0 to 3.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 9</b> has 64 DAC color hues for (<a href="DAC" title="DAC">DAC</a> attrib. 6, 8 to 15) with background colors. Text is 25 by 80. Graphics is 640 by 350. Video pages 0 and 1 for flipping or <a href="PCOPY" title="PCOPY">PCOPY</a>.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 10</b> has 4 gray scale color attributes with black background. 1 = normal white, 2 = blinking white and 3 = bright white. Text is 25 by 80. Graphics is 640 by 350.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 11</b> is <b>monochrome</b> with black background and white foreground. Text is 30 or 60 by 80 columns(see <a href="WIDTH" title="WIDTH">WIDTH</a>). White graphics is 640 by 480. NO <a href="COLOR" title="COLOR">COLOR</a> keyword allowed.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 12</b> has 16 color attributes, black background. 256K possible color hues. Text is 30 or 60 by 80 columns(see <a href="WIDTH" title="WIDTH">WIDTH</a>). Graphics 640 by 480.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> 13</b> has 256 color attributes, black background. 256K possible color hues. Text is 25 by 40. Graphics is 320 by 200.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></b>(wide&amp;, deep&amp;, mode%) can imitate any size screen mode or use 32 bit or 256 color modes in <b>QB64</b>.</li></ul>
<ul><li><b><a class="mw-selflink selflink">SCREEN</a> <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></b>(imagehandle&amp;, colors) can load a program screen of an image file handle in <b>QB64</b> using 256 or 32 bit.</li></ul>
<p style="text-align: center">(<a href="#toc">Return to Table of Contents</a>)</p>
<p>
</p>
<h2><span class="mw-headline" id="Text_and_Graphics">Text and Graphics</span></h2>
<dl><dd><b>Text Coordinates:</b></dd></dl>
<ul><li>Are a minimum of 1 and the values given above are the maximums. <a href="LOCATE" title="LOCATE">LOCATE</a> 1, 1 is the top left <a class="mw-selflink selflink">SCREEN</a> text position.</li>
<li>Text characters occupy a certain sized pixel box adjusted by <a href="WIDTH" title="WIDTH">WIDTH</a> in some screen modes.</li>
<li>Text <a href="PRINT" title="PRINT">PRINT</a> cursor positions can be read by <a href="CSRLIN" title="CSRLIN">CSRLIN</a> and <a href="POS" title="POS">POS(0)</a> to <a href="LOCATE" title="LOCATE">LOCATE</a> text <a href="PRINT" title="PRINT">PRINTs</a>.</li>
<li><a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a> can be used to designate a text view port area.</li>
<li>In <b>QB64</b> the <a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH</a> and <a href="HEIGHT" title="HEIGHT">_HEIGHT</a> functions will return the text dimensions in SCREEN 0 only.</li></ul>
<p>
</p>
<dl><dd><b>Graphic Coordinates:</b></dd></dl>
<ul><li>The minimum on screen graphics pixel coordinates are 0 for columns and rows in the top left corner.</li>
<li>Maximum pixel coordinates are one less than the maximum dimensions above because the pixel count starts at 0.</li>
<li>Graphic objects such as <a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a>, <a href="LINE" title="LINE">LINE</a>, <a href="CIRCLE" title="CIRCLE">CIRCLE</a> and <a href="DRAW" title="DRAW">DRAW</a> can be placed partially off of the screen.</li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> and <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a> screen image operations MUST be located completely on the screen in QBasic!</li>
<li><a href="VIEW" title="VIEW">VIEW</a> can be used to designate a graphic view port area of the screen.</li>
<li><a href="WINDOW" title="WINDOW">WINDOW</a> can be used to set the graphics SCREEN coordinates to almost any size needed. Use the SCREEN option for normal row coordinate values. Row coordinates are Cartesian(decrease in value going down the screen) otherwise.</li>
<li>In <b>QB64</b> the <a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH</a> and <a href="HEIGHT" title="HEIGHT">_HEIGHT</a> functions will return the graphic pixel dimensions in SCREENs other than 0.</li></ul>
<p>
</p>
<dl><dd><b>QB64 Screen Statements and Functions:</b></dd></dl>
<ul><li>For file image screens that adopt the image dimensions and image color settings use: <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li>To create custom sized screen modes or pages and 256 or 32 bit colors use: <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></li>
<li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a> can stretch or reduce the size of images to fit the SCREEN size.</li>
<li><a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a> can use <a href="CLIP" title="CLIP">_CLIP</a> to set objects partially off screen. <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> can read objects off screen as a color in QB64 ONLY.</li>
<li>A <a href="DISPLAY" title="DISPLAY">_DISPLAY</a> statement can be used to only display an image after changes instead of using page flipping or <a href="PCOPY" title="PCOPY">PCOPY</a>.</li>
<li>The current desktop screen resolution can be found using the <a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a> handle value with <a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH</a> and <a href="HEIGHT" title="HEIGHT">_HEIGHT</a>.</li>
<li><b>NOTE: Default 32 bit backgrounds are clear black or <a href="RGBA" title="RGBA">_RGBA</a>(0, 0, 0, 0)! Use <a href="CLS" title="CLS">CLS</a> to make the black opaque!</b></li></ul>
<p style="text-align: center">(<a href="#toc">Return to Table of Contents</a>)</p>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dd><i>Example 1:</i> Shows an example of each legacy screen mode available to QBasic and QB64.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">SCREEN</span></a> 0
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This is <a class="mw-selflink selflink"><span style="color:#4593D8;">SCREEN</span></a> 0 - only text is allowed!"
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> S = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 13
   <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> S &lt; 3 <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> S &gt; 6 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
     <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
     <a class="mw-selflink selflink"><span style="color:#4593D8;">SCREEN</span></a> S
     <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This is <a class="mw-selflink selflink"><span style="color:#4593D8;">SCREEN</span></a>"; S; " - can use text and graphics!"
       <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> S = 2 <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> S = 11 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Monochrome - no <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> statements!"
       <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> S = 10 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
         <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This <a class="mw-selflink selflink"><span style="color:#4593D8;">SCREEN</span></a> has only 4 colors. Black and 3 white: 2 blinks.
         <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (100,100), 50, 2
       <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> : <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (100,100), 100, S
       <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
   <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">This is SCREEN 0 - only text is allowed!
</pre>
</td></tr></tbody></table>
<dl><dd>Displays each <a class="mw-selflink selflink">SCREEN</a> mode one at a time with a <a href="CIRCLE" title="CIRCLE">CIRCLE</a> (except for <a class="mw-selflink selflink">SCREEN</a> 0)</dd></dl>
<p style="text-align: center">(<a href="#toc">Return to Table of Contents</a>)</p>
<h3><span class="mw-headline" id="More_Examples">More Examples</span></h3>
<ul><li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="Program_ScreenShots" title="Program ScreenShots">Program ScreenShots</a></li>
<li><a href="ThirtyTwoBit_SUB" title="ThirtyTwoBit SUB">ThirtyTwoBit SUB</a></li>
<li><a href="SelectScreen" title="SelectScreen">SelectScreen</a></li>
<li><a href="ScreenMode" title="ScreenMode">ScreenMode</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="COLOR" title="COLOR">COLOR</a>, <a href="CLS" title="CLS">CLS</a>, <a href="WIDTH" title="WIDTH">WIDTH</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="SAVEIMAGE" title="SAVEIMAGE">_SAVEIMAGE</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li>
<li><a href="LOADFONT" title="LOADFONT">_LOADFONT</a>, <a href="FONT" title="FONT">_FONT</a></li>
<li><a href="DISPLAY" title="DISPLAY">_DISPLAY</a>, <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a>, <a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a></li>
<li><a href="SCREENHIDE" title="SCREENHIDE">_SCREENHIDE</a>, <a href="SCREENSHOW" title="SCREENSHOW">_SCREENSHOW</a>, <a href="SCREENICON" title="SCREENICON">_SCREENICON</a></li>
<li><a href="PALETTE" title="PALETTE">PALETTE</a>, <a href="OUT" title="OUT">OUT</a>, <a href="PCOPY" title="PCOPY">PCOPY</a>,</li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a>, <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a></li>
<li><a href="VIEW" title="VIEW">VIEW</a>, <a href="WINDOW" title="WINDOW">WINDOW</a>, <a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a></li>
<li><a href="SCREEN_(function)" title="SCREEN (function)">SCREEN (function)</a>, <a href="POINT" title="POINT">POINT</a></li>
<li><a href="Screen_Memory" title="Screen Memory">Screen Memory</a>, <a href="Screen_Saver_Programs" title="Screen Saver Programs">Screen Saver Programs</a></li>
<li><a href="CONSOLE" title="CONSOLE">_CONSOLE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714200340
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.069 seconds
Real time usage: 0.086 seconds
Preprocessor visited node count: 467/1000000
Post‐expand include size: 2489/2097152 bytes
Template argument size: 304/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   36.003      1 -total
 11.82%    4.257      1 Template:OutputEnd
  9.59%    3.452     34 Template:Cl
  9.17%    3.300      1 Template:PageSyntax
  8.57%    3.086      1 Template:CodeEnd
  8.26%    2.974      1 Template:OutputStart
  6.77%    2.438      1 Template:PageParameters
  6.76%    2.435      1 Template:PageSeeAlso
  6.67%    2.400      1 Template:FixedStart
  6.02%    2.168      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:502-0!canonical and timestamp 20240714200340 and revision id 8691.
 -->
</div>
</div>
</div>
</div>
</body>
</html>