<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SPACE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SPACE rootpage-SPACE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SPACE$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">SPACE$</a> function returns a <a href="STRING" title="STRING">STRING</a> consisting of a number of space characters.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <b>SPACE$(<i>count&amp;</i>)</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>count&amp;</i> is the number of space characters to repeat. Cannot use negative values!</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Semicolons can be used to combine spaces with text <a href="STRING" title="STRING">STRING</a> or numerical values.</li>
<li><a href="Concatenation" title="Concatenation">Concatenation</a> using + can be used to combine <a href="STRING" title="STRING">STRING</a> text values only.</li>
<li>Spaces are often used to erase previous text PRINTs from the screen.</li>
<li>The function result can also be used to <a href="GET" title="GET">GET</a> and <a href="PUT" title="PUT">PUT</a> a number of bytes as zero characters: bytes$ = SPACE$(numbytes)</li>
<li>Spaces can also be made using <a href="SPC" title="SPC">SPC</a>, <a href="CHR$" title="CHR$">CHR$</a>(32) or <a href="STRING$" title="STRING$">STRING$</a>(n%, 32).</li></ul>
<p>
<i>Differences between QB64 and QB 4.5:</i>
</p>
<ul><li><b>QB64</b> can use <a href="LONG" title="LONG">LONG</a> values for count up to 2,147,483,647 while <b>QB 4.5</b> could only use <a href="INTEGER" title="INTEGER">INTEGER</a> values up to 32,767.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> How to space text in a <a href="PRINT" title="PRINT">PRINT</a> statement using SPACE$ with string <a href="Concatenation" title="Concatenation">concatenation</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> count% = 0 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">TO</span></a> 3
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "abc" + <a class="mw-selflink selflink"><span style="color:#4593D8;">SPACE$</span></a>( count% ) + "def"
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">NEXT</span></a> count%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">abcdef
abc def
abc  def
abc   def
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> In <a href="SCREEN" title="SCREEN">SCREEN</a> 0 SPACE$ can be used to change the background color to make an American flag.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> USA flag centered on screen with thin horizontal red &amp; white stripes
' blue corner field with randomly twinkling stars
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 25, 1
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press any key to stop twinkling";
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> , 4
z = 15
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> x = 5 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 19          '13 red &amp; white stripes (x =5 to 21 for 15 stripes)
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> z = 15 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> z = 4 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> z = 15
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> , z
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> x, 15
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">SPACE$</span></a>(55)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> x = 5 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 11          'blue field in upper left quadrant (x = 5 to 13 to hold all 50 stars)
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15, 1            'sits above 4th white stripe
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> x, 15
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">SPACE$</span></a>(23)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
DO
    stop$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> x = 5 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> 2  '39 stars staggered across blue field (50 stars if x = 5 to 12)
        w = 16
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 6      '5 rows of 6 stars
            r = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 6)
            <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> r = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> z = 31 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> z = 15
            <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> stop$ = "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> z <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15
            <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> x, w
            w = w + 4
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "*";
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
        w = 18
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 5      '5 rows of 5 stars
            r = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 6)
            <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> r = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> z = 31 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> z = 15
            <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> stop$ = "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> z <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15
            <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> x + 1, w
            w = w + 4
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "*";
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
    w = 16
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 6          '1 row of 6 stars
            r = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 6)
            <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> r = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> z = 31 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> z = 15
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> stop$ = "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> z <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> x, w
        w = w + 4
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "*";
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
    t = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> t + .2 &gt;= <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> stop$ = ""
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 7, 0
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> In <a href="SCREEN" title="SCREEN">SCREEN</a> 0, the background color is only placed with the the printed text and spaces. <a href="CLS" title="CLS">CLS</a> can color the entire screen.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PRINT" title="PRINT">PRINT</a>, <a href="PRINT_USING" title="PRINT USING">PRINT USING</a></li>
<li><a href="STRING$" title="STRING$">STRING$</a>, <a href="CLS" title="CLS">CLS</a></li>
<li><a href="SPC" title="SPC">SPC</a>, <a href="TAB" title="TAB">TAB</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034220
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.058 seconds
Real time usage: 0.072 seconds
Preprocessor visited node count: 639/1000000
Post‐expand include size: 5284/2097152 bytes
Template argument size: 842/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   42.887      1 -total
 15.64%    6.710     85 Template:Cl
  8.88%    3.807      1 Template:PageSyntax
  6.49%    2.785      1 Template:Small
  6.45%    2.765      2 Template:Parameter
  5.68%    2.437      2 Template:CodeStart
  5.61%    2.405      1 Template:PageDescription
  5.56%    2.385      1 Template:PageParameters
  5.46%    2.341      1 Template:PageExamples
  5.37%    2.305      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:565-0!canonical and timestamp 20240715034220 and revision id 8065.
 -->
</div>
</div>
</div>
</div>
</body>
</html>