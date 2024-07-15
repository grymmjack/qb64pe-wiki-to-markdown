<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PMAP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PMAP rootpage-PMAP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PMAP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>PMAP</b> statement returns the physical or <a href="WINDOW" title="WINDOW">WINDOW</a> view port coordinates.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>PMAP (<i>coordinate</i>, <i>function_number%</i>)</dd></dl></dd></dl>
<p>
</p>
<ul><li>The <i>coordinate</i> is the coordinate point to be mapped.</li>
<li>The <i>function</i> can have one of four values:</li></ul>
<dl><dd><dl><dd>0 = Maps view port coordinate to physical x screen coordinate</dd>
<dd>1 = Maps view port coordinate to physical y screen coordinate</dd>
<dd>2 = Maps physical screen coordinate to view port x coordinate</dd>
<dd>3 = Maps physical screen coordinate to view port y coordinate</dd></dl></dd></dl>
<ul><li>The four PMAP functions allow the user to find equal point locations between the view coordinates created with the <a href="WINDOW" title="WINDOW">WINDOW</a> statement and the physical screen coordinates of the viewport as defined by the <a href="VIEW" title="VIEW">VIEW</a> statement.</li>
<li>Mouse co-ordinates returned by <a href="MOUSEX" title="MOUSEX">_MOUSEX</a> and <a href="MOUSEY" title="MOUSEY">_MOUSEY</a> are the physical screen co-ordinates.</li></ul>
<p>
<i>Example:</i> Use PMAP to convert coordinate values from view to screen coordinates and from screen coordinates to view coordinates.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
 'Coordinates of upper-left corner of the window is defined in following statement are (90,100)
<a href="WINDOW" title="WINDOW"><span style="color:#4593D8;">WINDOW</span></a> <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> (90, 100)-(200, 200) 'coordinates of lower-right 'corner are 200, 200.
X = <a class="mw-selflink selflink"><span style="color:#4593D8;">PMAP</span></a>(90, 0)          ' X = 0
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> X
Y = <a class="mw-selflink selflink"><span style="color:#4593D8;">PMAP</span></a>(100, 1)         ' Y = 0
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Y
'These statements return the screen coordinates equal to the view coordinates 200, 200.
X = <a class="mw-selflink selflink"><span style="color:#4593D8;">PMAP</span></a>(200, 0)         ' X = 639
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> X
Y = <a class="mw-selflink selflink"><span style="color:#4593D8;">PMAP</span></a>(200, 1)         ' Y = 479
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Y
'These statements return the view coordinates equal to the screen coordinates 0, 0
X = <a class="mw-selflink selflink"><span style="color:#4593D8;">PMAP</span></a>(0, 0)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> X
Y = <a class="mw-selflink selflink"><span style="color:#4593D8;">PMAP</span></a>(0, 0)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Y
'These statements return the view coordinates equal to the screen coordinates 639, 479.
X = <a class="mw-selflink selflink"><span style="color:#4593D8;">PMAP</span></a>(639, 2)         ' X = 200
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> X
Y = <a class="mw-selflink selflink"><span style="color:#4593D8;">PMAP</span></a>(479, 3)         ' Y = 200
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Y
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>                    ' pause before clearing view port
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> 1                    ' clear grahic view port
<a href="WINDOW" title="WINDOW"><span style="color:#4593D8;">WINDOW</span></a>                   ' end graphic view port
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> If physical screen coordinates are (0, 0) in the upper-left corner and (639, 479) in the lower-right corner, then the statements return the screen coordinate's equal to the view coordinates 90, 100.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="WINDOW" title="WINDOW">WINDOW</a>, <a href="VIEW" title="VIEW">VIEW</a></li>
<li><a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061357
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 175/1000000
Post‐expand include size: 1730/2097152 bytes
Template argument size: 214/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.433      1 -total
 19.55%    3.994     23 Template:Cl
 15.46%    3.159      1 Template:PageSyntax
 14.05%    2.871      1 Template:CodeEnd
 13.42%    2.743      1 Template:CodeStart
 12.91%    2.638      1 Template:PageSeeAlso
 12.68%    2.592      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:485-0!canonical and timestamp 20240715061357 and revision id 7357.
 -->
</div>
</div>
</div>
</div>
</body>
</html>