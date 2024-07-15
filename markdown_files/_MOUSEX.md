<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MOUSEX - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOUSEX rootpage-MOUSEX skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MOUSEX</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MOUSEX</a> function returns the current horizontal (column) mouse cursor position when read after <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixelColumn%</i> = <a class="mw-selflink selflink">_MOUSEX</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a href="SCREEN" title="SCREEN">SCREEN</a> 0 returns the <a href="INTEGER" title="INTEGER">INTEGER</a> horizontal text column position (from build 20170817/62 onward); older versions return a <a href="SINGLE" title="SINGLE">SINGLE</a> horizontal text column position. Use <a href="INTEGER" title="INTEGER">INTEGER</a> variables to avoid floating decimal returns.</li>
<li>Graphic screen modes 1, 2 and 7 to 13 and <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> 32 bit return the <a href="INTEGER" title="INTEGER">INTEGER</a> pixel columns.</li>
<li>To calculate text columns in graphic modes, divide the return by 8 or the <a href="FONTWIDTH" title="FONTWIDTH">_FONTWIDTH</a> of <a href="FONT" title="FONT">_FONT</a> characters.</li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> must be used to detect any changes in the mouse position and is <b>required</b> for any coordinate returns.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>In <a href="SCREEN" title="SCREEN">SCREEN</a> 0, QBasic's <a href="CALL_ABSOLUTE" title="CALL ABSOLUTE">ABSOLUTE</a> returned graphic coordinates. QB64 mouse functions return the text coordinates.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> A simple mouse drawing board using <a class="mw-selflink selflink">_MOUSEX</a> and <a href="MOUSEY" title="MOUSEY">_MOUSEY</a> coordinate values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (99, 9)-(601, 401), 7, BF
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (101, 11)-(599, 399), 8, BF
tm$ = " Column = ###  Row = ###  Button1 = ##  Button2 = ##  Button3 = ##"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 29, 20: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "LeftButton = draw - RightButton = Erase";
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: K$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
    X = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEX</span></a>: Y = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X &gt; 100 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> X &lt; 600 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> PX &gt; 100 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> PX &lt; 600 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Y &gt; 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Y &lt; 400 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> PY &gt; 10 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> PY &lt; 400 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (PX, PY)-(X, Y), 15
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(2) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (101, 11)-(599, 399), 8, BF
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    PX = X: PY = Y
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 28, 10: <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> tm$; X; Y; <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1); <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(2); <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(3)
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> K$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MOUSEY" title="MOUSEY">_MOUSEY</a></li>
<li><a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a>, <a href="MOUSEWHEEL" title="MOUSEWHEEL">_MOUSEWHEEL</a></li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>, <a href="MOUSEMOVE" title="MOUSEMOVE">_MOUSEMOVE</a></li>
<li><a href="MOUSESHOW" title="MOUSESHOW">_MOUSESHOW</a>, <a href="MOUSEHIDE" title="MOUSEHIDE">_MOUSEHIDE</a></li>
<li><a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a>, <a href="MOUSEMOVEMENTY" title="MOUSEMOVEMENTY">_MOUSEMOVEMENTY</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062416
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.055 seconds
Preprocessor visited node count: 340/1000000
Post‐expand include size: 2902/2097152 bytes
Template argument size: 526/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.214      1 -total
 14.86%    3.599     42 Template:Cl
 13.79%    3.340      1 Template:PageSyntax
  9.02%    2.185      1 Template:Parameter
  8.84%    2.141      1 Template:PageDescription
  8.82%    2.136      1 Template:CodeEnd
  8.69%    2.104      1 Template:PageNavigation
  8.58%    2.078      1 Template:CodeStart
  8.28%    2.004      1 Template:PageSeeAlso
  8.22%    1.991      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:197-0!canonical and timestamp 20240715062416 and revision id 7624.
 -->
</div>
</div>
</div>
</div>
</body>
</html>