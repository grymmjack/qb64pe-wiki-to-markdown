<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>BEEP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BEEP rootpage-BEEP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">BEEP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">BEEP</a> statement produces a beep sound through the sound card.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">BEEP</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">BEEP</a> can be placed anywhere to alert the user that there is something to do or an error has occurred.</li>
<li><b>QB64</b> produces the actual "beep" sound through the PC's sound card, to emulate QBasic's beeping through the <a class="extiw" href="https://en.wikipedia.org/wiki/PC_speaker" title="wikipedia:PC speaker">PC speaker</a>.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>Older programs may attempt to produce a BEEP by printing <a href="CHR$" title="CHR$">CHR$</a>(7) to the screen. This is no longer supported in QB64 after <b>version 1.000</b>.
<ul><li>You may have to replace instances of PRINT CHR$(7) in older programs to the <a class="mw-selflink selflink">BEEP</a> statement to maintain the legacy functionality.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SOUND" title="SOUND">SOUND</a>, <a href="PLAY" title="PLAY">PLAY</a></li>
<li><a href="SNDPLAY" title="SNDPLAY">_SNDPLAY</a> <span style="color:#777777;">(play sound files)</span></li>
<li><a href="SNDRAW" title="SNDRAW">_SNDRAW</a> <span style="color:#777777;">(play frequency waves)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061227
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.019 seconds
Real time usage: 0.025 seconds
Preprocessor visited node count: 34/1000000
Post‐expand include size: 657/2097152 bytes
Template argument size: 40/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   12.661      1 -total
 21.95%    2.779      1 Template:PageSyntax
 19.35%    2.450      2 Template:Text
 18.24%    2.310      1 Template:PageNavigation
 18.18%    2.302      1 Template:PageSeeAlso
 17.26%    2.186      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:399-0!canonical and timestamp 20240715061227 and revision id 8979.
 -->
</div>
</div>
</div>
</div>
</body>
</html>