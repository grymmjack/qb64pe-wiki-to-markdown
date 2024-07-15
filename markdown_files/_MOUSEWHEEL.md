<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MOUSEWHEEL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOUSEWHEEL rootpage-MOUSEWHEEL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MOUSEWHEEL</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MOUSEWHEEL</a> function returns a positive or negative <a href="INTEGER" title="INTEGER">INTEGER</a> value indicating mouse scroll events since the last read of <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>scrollAmount%</i> = <a class="mw-selflink selflink">_MOUSEWHEEL</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns -1 when scrolling up and 1 when scrolling down with 0 indicating no movement since last read.</li>
<li>After an event has been read, the value resets to 0 automatically so cumulative position values must be added.</li>
<li>If no movement on the wheel has occurred since the last <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> read, <a class="mw-selflink selflink">_MOUSEWHEEL</a> returns 0.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v0.851"><img alt="v0.851" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v0.851</b>
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
<ul><li>Available for <i>macOS</i> since <b>QB64-PE v3.13.0</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Reading the cumulative mouse wheel "clicks".</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">50</span>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
        Scroll = Scroll + <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEWHEEL</span></a>
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">10</span>, <span style="color:#F580B1;">20</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Scroll
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">13</span>) <span style="color:#919191;">' press Enter to quit</span>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>A simple text scrolling routine using the mouse wheel value to read a text array.</dd>
<dd>You will need a text file that is large enough for this example.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Array$(<span style="color:#F580B1;">100</span>)
<a href="LINE_INPUT" title="LINE INPUT"><span style="color:#4593D8;">LINE INPUT</span></a> <span style="color:#FFB100;">"Enter a file name with 100 or more lines of text: "</span>, file$
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> file$ <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">FOR</span></a> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">INPUT</span></a> <a href="OPEN" title="OPEN"><span style="color:#4593D8;">AS</span></a> #1
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO UNTIL</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(<span style="color:#F580B1;">1</span>)
    inputcount = inputcount + <span style="color:#F580B1;">1</span>
    <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT</span></a> #1, Array$(inputcount)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> inputcount = <span style="color:#F580B1;">100</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> n = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">21</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Array$(n): <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> row &gt;= <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> row = row + <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEWHEEL</span></a> <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> row = <span style="color:#F580B1;">0</span> <span style="color:#919191;">'prevent under scrolling</span>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> row &gt; inputcount - <span style="color:#F580B1;">20</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> row = inputcount - <span style="color:#F580B1;">20</span> <span style="color:#919191;">'prevent over scrolling</span>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> prevrow &lt;&gt; row <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">'look for a change in row value</span>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> row &gt; <span style="color:#F580B1;">0</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> row &lt;= inputcount - <span style="color:#F580B1;">20</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
                <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">1</span>
                <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> n = row <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> row + <span style="color:#F580B1;">20</span>
                    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Array$(n)
                <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
            <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        prevrow = row <span style="color:#919191;">'store previous row value</span>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &gt; <span style="color:#FFB100;">""</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1302" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEY" title="MOUSEY">_MOUSEY</a>, <a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a></li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>, <a href="MOUSEMOVE" title="MOUSEMOVE">_MOUSEMOVE</a></li>
<li><a href="MOUSESHOW" title="MOUSESHOW">_MOUSESHOW</a>, <a href="MOUSEHIDE" title="MOUSEHIDE">_MOUSEHIDE</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714123110
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.071 seconds
Real time usage: 0.104 seconds
Preprocessor visited node count: 625/1000000
Post‐expand include size: 4959/2097152 bytes
Template argument size: 1107/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2543/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   80.209      1 -total
  6.97%    5.588      1 Template:PageAvailability
  6.20%    4.977     26 Template:Text
  4.87%    3.905      1 Template:PageExamples
  4.47%    3.589     54 Template:Cl
  4.23%    3.395      1 Template:Small
  2.84%    2.278      1 Template:PageSyntax
  2.38%    1.908      2 Template:CodeStart
  2.26%    1.812      2 Template:CodeEnd
  2.22%    1.782      1 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:196-0!canonical and timestamp 20240714123110 and revision id 8927.
 -->
</div>
</div>
</div>
</div>
</body>
</html>