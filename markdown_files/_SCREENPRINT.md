<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SCREENPRINT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SCREENPRINT rootpage-SCREENPRINT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SCREENPRINT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SCREENPRINT</a> statement simulates typing text into a Windows focused program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SCREENPRINT</a> <i>text$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li>
<li><i>text$</i> is the text to be typed into a focused program's text entry area, one character at a time.</li>
<li>Set the focus to a desktop program by using the <a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a> handle as the <a href="SOURCE" title="SOURCE">_SOURCE</a>. Use the image to map the desired area.</li>
<li><a href="SCREENCLICK" title="SCREENCLICK">_SCREENCLICK</a> can also be used to set the focus to a program's text entry area on the desktop.</li>
<li><b>Note: If the focus is not set correctly, the text may be printed to the QB64 IDE, if open, or not printed at all.</b></li>
<li>Ctrl + letter key shortcuts can be simulated using the appropriate <a href="ASCII" title="ASCII">ASCII</a> Control character codes 1 to 26 shown below:</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed"> CTRL + A = CHR$(1)   ☺  StartHeader (SOH)    CTRL + B = CHR$(2)   ☻  StartText         (STX)
 CTRL + C = CHR$(3)   ♥  EndText     (ETX)    CTRL + D = CHR$(4)   ♦  EndOfTransmit     (EOT)
 CTRL + E = CHR$(5)   ♣  Enquiry     (ENQ)    CTRL + F = CHR$(6)   ♠  Acknowledge       (ACK)
 CTRL + G = CHR$(7)   •  <a href="BEEP" title="BEEP">BEEP</a>        (BEL)    CTRL + H = CHR$(8)   ◘  <b>[Backspace]</b>       (BS)
 CTRL + I = CHR$(9)   ○  Horiz.Tab   <b>[Tab]</b>    CTRL + J = CHR$(10)  ◙  LineFeed(printer) (LF)
 CTRL + K = CHR$(11)  ♂  Vert. Tab   (VT)     CTRL + L = CHR$(12)  ♀  FormFeed(printer) (FF)
 CTRL + M = CHR$(13)  ♪  <b>[Enter]</b>     (CR)     CTRL + N = CHR$(14)  ♫  ShiftOut          (SO)
 CTRL + O = CHR$(15)  ☼  ShiftIn     (SI)     CTRL + P = CHR$(16)  ►  DataLinkEscape    (DLE)
 CTRL + Q = CHR$(17)  ◄  DevControl1 (DC1)    CTRL + R = CHR$(18)  ↕  DeviceControl2    (DC2)
 CTRL + S = CHR$(19)  ‼  DevControl3 (DC3)    CTRL + T = CHR$(20)  ¶  DeviceControl4    (DC4)
 CTRL + U = CHR$(21)  §  NegativeACK (NAK)    CTRL + V = CHR$(22)  ▬  Synchronous Idle  (SYN)
 CTRL + W = CHR$(23)  ↨  EndTXBlock  (ETB)    CTRL + X = CHR$(24)  ↑  Cancel            (CAN)
 CTRL + Y = CHR$(25)  ↓  EndMedium   (EM)     CTRL + Z = CHR$(26)  →  End Of File(SUB)  (EOF)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Printing text into a Windows text editor (Notepad) and copying to the clipboard. May not work on all systems.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFLNG" title="DEFLNG"><span style="color:#4593D8;">DEFLNG</span></a> A-Z
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "OPENing and MAXIMIZING Notepad in 5 seconds..."; : <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 5
<a href="SHELL" title="SHELL"><span style="color:#4593D8;">SHELL</span></a> <a href="DONTWAIT" title="DONTWAIT"><span style="color:#4593D8;">_DONTWAIT</span></a> "START /MAX NotePad.exe"  'opens Notepad file "untitled.txt"
'detect notepad open and maximized
'condition: 80% or more of the screen is white
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>                     'read the desktop screen image for maximized window
  s = <a href="SCREENIMAGE" title="SCREENIMAGE"><span style="color:#4593D8;">_SCREENIMAGE</span></a>
  <a href="SOURCE" title="SOURCE"><span style="color:#4593D8;">_SOURCE</span></a> s
  z = 0
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(s) - 1   'scan for large white area
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> x = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> _<a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">WIDTH</span></a>(s) - 1
       c = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(x, y)
       <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> c = <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(255, 255, 255) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> z = z + 1
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> z / (<a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(s) * _<a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">WIDTH</span></a>(s)) &gt; 0.8 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a> 'when 80% of screen is white
  <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> s   'free desktop image
  <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 1       'scans 1 loop per second
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> ".";
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "NOTEPAD detected as OPEN and MAXIMIZED"
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENPRINT</span></a> "HELLO WORLD"
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 2
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENPRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(8) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(8) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(8) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(8) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(8) 'backspace 5 characters
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 3
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENPRINT</span></a> "QB64!"
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 2
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENPRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(1) 'CTRL + A select all
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 2
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENPRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(3) 'CTRL + C copy to clipboard
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 2
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CLIPBOARD$_(function)" title="CLIPBOARD$ (function)"><span style="color:#4593D8;">CLIPBOARD$</span></a>
<a href="CLIPBOARD$" title="CLIPBOARD$"><span style="color:#4593D8;">_CLIPBOARD$</span></a> = "QB64 ROCKS!"
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 2
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENPRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(22) 'CTRL + V paste from clipboard
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> If the Windows shortcuts are set up properly, printing ASCII Control characters acts like the user selected the control + letter combinations to <i>Select all</i> (CHR$(1)), <i>Copy</i> (CHR$(3)) and <i>Paste</i> (CHR$(22)) the text with the Windows Clipboard. If the editor program's CTRL key combinations are different, use the matching letter <a href="ASCII" title="ASCII">ASCII</a> code from A = 1 to Z = 26 in the text editor.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1252" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a>, <a href="SCREENCLICK" title="SCREENCLICK">_SCREENCLICK</a></li>
<li><a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a>, <a href="SCREENX" title="SCREENX">_SCREENX</a>, <a href="SCREENY" title="SCREENY">_SCREENY</a></li>
<li><a href="ASCII" title="ASCII">ASCII</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062443
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.050 seconds
Real time usage: 0.078 seconds
Preprocessor visited node count: 438/1000000
Post‐expand include size: 3912/2097152 bytes
Template argument size: 725/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   36.829      1 -total
 16.15%    5.949      1 Template:CodeEnd
 11.24%    4.141     57 Template:Cl
  8.20%    3.020      1 Template:Small
  6.75%    2.486      1 Template:PageSeeAlso
  6.63%    2.442      1 Template:PageNavigation
  6.60%    2.429      1 Template:FixedStart
  6.43%    2.368      1 Template:PageExamples
  6.06%    2.233      1 Template:PageSyntax
  5.63%    2.073      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:317-0!canonical and timestamp 20240715062443 and revision id 8913.
 -->
</div>
</div>
</div>
</div>
</body>
</html>