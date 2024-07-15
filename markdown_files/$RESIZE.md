<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$RESIZE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_RESIZE rootpage-_RESIZE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$RESIZE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$RESIZE</a> <a href="Metacommand" title="Metacommand">metacommand</a> determines if a program window can be resized by the user.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$RESIZE</a>:{ON|OFF|STRETCH|SMOOTH}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>$RESIZE:ON is used to allow the program window to be resized by a program user. Otherwise it cannot be changed.</li>
<li>$RESIZE:OFF (<b>default</b>) is used when the program's window size cannot be changed by the user.</li>
<li>$RESIZE:STRETCH the screen will be stretched to fit the new window size with a 1 to 1 ratio of width and height.</li>
<li>$RESIZE:SMOOTH the screen will be stretched also, but with linear filtering applied to the pixels.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v1.0"><img alt="v1.0" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v1.0</b>
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
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Resizing a program screen when the user changes it without clearing the entire screen image:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">$RESIZE</span></a>:ON
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(160, 140, 32)
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.1
<a href="SCREENMOVE" title="SCREENMOVE"><span style="color:#4593D8;">_SCREENMOVE</span></a> 20, 20
<a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
' CLEAR _RESIZE FLAG BY READING IT ONCE
temp&amp; = <a href="RESIZE_(function)" title="RESIZE (function)"><span style="color:#4593D8;">_RESIZE</span></a>
DO
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 60
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> CheckResize(<a href="SOURCE" title="SOURCE"><span style="color:#4593D8;">_SOURCE</span></a>) = -1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
            <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(0) - 1, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(0) - 1), <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 100 + 5, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 255, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 255, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 255)
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 200
            <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(0) - 1, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(0) - 1), <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 255, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 255, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 255)
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    k&amp; = <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> k&amp; = 27 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> k&amp; = 32
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
' *************************************************************************************************
' *                                                                                               *
' *  CheckResize: This FUNCTION checks if the user resized the window, and if so, recreates the   *
' *               ORIGINAL SCREEN image to the new window size.                                   *
' *                                                                                               *
' *               Developer Note: You must use $RESIZE:ON, $RESIZE:SMOOTH, or $RESIZE:SMOOTH at   *
' *                               the beginning of your project for this to work.                 *
' *                               This FUNCTION only works in QB64 version 1.000 and up.          *
' *                                                                                               *
' *************************************************************************************************
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> CheckResize (CurrentScreen <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    ' *** Define local variable for temporary screen
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> TempScreen <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
    CheckResize = 0
    ' *** Check to see if the user resized the window. If so, change the SCREEN image to the correct size.
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="RESIZE_(function)" title="RESIZE (function)"><span style="color:#4593D8;">_RESIZE</span></a> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        ' *** First, create a copy of the current <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> image.
        TempScreen = <a href="COPYIMAGE" title="COPYIMAGE"><span style="color:#4593D8;">_COPYIMAGE</span></a>(CurrentScreen, 32)
        ' *** Set the <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> to the copied image, releasing the current SCREEN image.
        <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> TempScreen
        ' *** Remove (FREE) the original <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> image.
        <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> CurrentScreen
        ' *** Create a new "original" <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> image.
        CurrentScreen = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<a href="RESIZEWIDTH" title="RESIZEWIDTH"><span style="color:#4593D8;">_RESIZEWIDTH</span></a>, <a href="RESIZEHEIGHT" title="RESIZEHEIGHT"><span style="color:#4593D8;">_RESIZEHEIGHT</span></a>, 32)
        ' *** Set the <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> to the new "original" image, releasing the copied <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> image.
        <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> CurrentScreen
        '  <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> PREVIOUS <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> ON THE NEW ONE
        <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 0), TempScreen, CurrentScreen
        <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
        ' *** Remove (FREE) the copied <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> image.
        <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> TempScreen
        ' *** Tell the caller there was a resize
        CheckResize = -1
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RESIZE" title="RESIZE">_RESIZE</a>, <a href="RESIZE_(function)" title="RESIZE (function)">_RESIZE (function)</a></li>
<li><a href="RESIZEWIDTH" title="RESIZEWIDTH">_RESIZEWIDTH</a>, <a href="RESIZEHEIGHT" title="RESIZEHEIGHT">_RESIZEHEIGHT</a> <span style="color:#777777;">(functions return the requested dimensions)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061216
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.130 seconds
Real time usage: 0.200 seconds
Preprocessor visited node count: 574/1000000
Post‐expand include size: 4970/2097152 bytes
Template argument size: 1006/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2359/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  174.353      1 -total
  5.72%    9.981      1 Template:PageSyntax
  4.66%    8.129      1 Template:PageAvailability
  4.01%    6.991     76 Template:Cl
  3.58%    6.244      1 Template:PageDescription
  2.59%    4.511      1 Template:PageExamples
  1.82%    3.166      1 Template:CodeStart
  1.68%    2.937      1 Template:CodeEnd
  1.60%    2.797      1 Template:Small
  1.31%    2.285      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:221-0!canonical and timestamp 20240715061216 and revision id 8028.
 -->
</div>
</div>
</div>
</div>
</body>
</html>