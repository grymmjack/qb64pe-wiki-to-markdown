<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CONTROLCHR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CONTROLCHR rootpage-CONTROLCHR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CONTROLCHR</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CONTROLCHR</a> statement can be used to turn OFF control character attributes and allow them to be printed.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_CONTROLCHR</a> {OFF|ON}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <a href="OFF" title="OFF">OFF</a> clause allows control characters 0 to 31 to be printed and not format printing as normal text characters.</li></ul>
<dl><dd><dl><dd>For example: <b><span style="color:green;">PRINT CHR$(13)</span></b> 'will not move the cursor to the next line and <b><span style="color:green;">PRINT CHR$(9)</span></b> 'will not tab.</dd></dl></dd></dl>
<ul><li>The default <a href="ON" title="ON">ON</a> statement allows <a href="ASCII#Control_Characters" title="ASCII">Control Characters</a> to be used as control commands where some will not print or will format prints.</li>
<li><b>Note:</b> File prints may be affected also when using Carriage Return or Line Feed/Form Feed formatting.</li>
<li>The QB64 IDE may allow Alt + number pad character entries, but they must be inside of <a href="STRING" title="STRING">STRING</a> values. Otherwise the IDE may not recognize them.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Printing the 255 <a href="ASCII" title="ASCII">ASCII</a> characters in <a href="SCREEN" title="SCREEN">SCREEN</a> 0 with 32 colors.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
<a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">WIDTH</span></a> <span style="color:#F580B1;">40</span>, <span style="color:#F580B1;">25</span>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CONTROLCHR</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a>
i = <span style="color:#F580B1;">0</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(i);
    i = i + <span style="color:#F580B1;">1</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> (i <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">&amp;HF</span>) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP WHILE</span></a> i
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">20</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> i <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">&amp;HF</span> <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> (i <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">&amp;H80</span>) \ <span style="color:#F580B1;">&amp;H8</span>, (i <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">&amp;H70</span>) \ <span style="color:#F580B1;">&amp;H10</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(i);
    i = i + <span style="color:#F580B1;">1</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> (i <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">&amp;HF</span>) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">1</span> + i \ <span style="color:#F580B1;">&amp;H10</span>, <span style="color:#F580B1;">20</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP WHILE</span></a> i
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1260" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="CONTROLCHR_(function)" title="CONTROLCHR (function)">_CONTROLCHR (function)</a></li>
<li><a href="CHR$" title="CHR$">CHR$</a>, <a href="ASC_(function)" title="ASC (function)">ASC (function)</a></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a>, <a href="KEYHIT" title="KEYHIT">_KEYHIT</a></li>
<li><a href="ASCII" title="ASCII">ASCII</a></li>
<li><a href="ASCII#Control_Characters" title="ASCII">Control Characters</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035635
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 385/1000000
Post‐expand include size: 3035/2097152 bytes
Template argument size: 505/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.807      1 -total
 20.22%    3.803     21 Template:Text
 12.61%    2.371     31 Template:Cl
  9.64%    1.814      1 Template:PageSyntax
  7.89%    1.484      1 Template:PageDescription
  7.41%    1.394      1 Template:CodeEnd
  7.27%    1.368      1 Template:CodeStart
  7.17%    1.349      1 Template:PageSeeAlso
  7.12%    1.339      1 Template:PageExamples
  7.03%    1.322      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:101-0!canonical and timestamp 20240715035635 and revision id 8916.
 -->
</div>
</div>
</div>
</div>
</body>
</html>