<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>TAB - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TAB rootpage-TAB skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">TAB</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">TAB</a> function is used in <a href="PRINT" title="PRINT">PRINT</a> and <a href="LPRINT" title="LPRINT">LPRINT</a> statements to move to a specified column position.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">TAB</a>(<i>column%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Space characters are printed until the print cursor reaches the designated <i>column%</i>, overwriting existing characters.</li>
<li>If a subsequent TAB <i>column%</i> is less than the current position, TAB moves the next print to that column on the next row.</li>
<li><a href="ASCII" title="ASCII">ASCII</a> <a href="CHR$" title="CHR$">CHR$</a>(9) can be substituted for sequencial 9 space column moves.</li>
<li><a href="Comma" title="Comma">Comma</a> PRINT spacing is up to 15 column places (IE: TAB(15)) to a maximum column of 57.</li>
<li>When printing to a file, a carriage return(<a href="CHR$" title="CHR$">CHR$</a>(13)) and linefeed(<a href="CHR$" title="CHR$">CHR$</a>(10)) character are output when it moves to the next row.</li>
<li><b>Note:</b> QBasic did not allow a TAB to be <a href="Concatenation" title="Concatenation">added</a> to a string value. In <a href="PRINT" title="PRINT">PRINT</a> statements the <a href="%2B" title="+">plus</a> would be changed to a <a href="Semicolon" title="Semicolon">semicolon</a>.</li></ul>
<dl><dd>In QB64, TAB <a href="Concatenation" title="Concatenation">concatenation</a> is allowed instead of <a href="Semicolon" title="Semicolon">semicolons</a>. Example: <span style="color:green;">PRINT "text" + TAB(9) + "here"</span></dd></dl>
<p>
<i>Example:</i> Comparing TAB to <a href="Comma" title="Comma">comma</a> print spacing which moves the next text print 15 columns.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">TAB</span></a>(15); "T" 'TAB spacing
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> , "T" 'comma spacing
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">TAB</span></a>(15); "T"<span style="color:red;">;</span> <a class="mw-selflink selflink"><span style="color:#4593D8;">TAB</span></a>(20); "A"; <a class="mw-selflink selflink"><span style="color:#4593D8;">TAB</span></a>(15); "B" 'semicolons add nothing to position
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">TAB</span></a>(15); "T"<span style="color:red;">,</span> <a class="mw-selflink selflink"><span style="color:#4593D8;">TAB</span></a>(20); "A"; <a class="mw-selflink selflink"><span style="color:#4593D8;">TAB</span></a>(15); "B" 'comma moves column position beyond 20
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">              T
              T
              T    A
              B
              T
                   A
              B</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> TAB moves the PRINT down to the next row when the current column position is more than the TAB position.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PRINT" title="PRINT">PRINT</a>, <a href="LPRINT" title="LPRINT">LPRINT</a></li>
<li><a href="SPC" title="SPC">SPC</a>, <a href="SPACE$" title="SPACE$">SPACE$</a></li>
<li><a href="STRING$" title="STRING$">STRING$</a></li>
<li><a href="CHR$" title="CHR$">CHR$</a>, <a href="ASCII" title="ASCII">ASCII</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035552
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.049 seconds
Preprocessor visited node count: 128/1000000
Post‐expand include size: 1369/2097152 bytes
Template argument size: 139/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   29.584      1 -total
 10.51%    3.109      1 Template:PageSyntax
  9.69%    2.868     11 Template:Cl
  9.68%    2.864      2 Template:Parameter
  9.39%    2.777      3 Template:Text
  8.54%    2.528      1 Template:CodeEnd
  8.29%    2.452      1 Template:OutputEnd
  8.01%    2.371      1 Template:OutputStart
  7.71%    2.281      1 Template:PageDescription
  7.40%    2.190      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:487-0!canonical and timestamp 20240715035552 and revision id 7977.
 -->
</div>
</div>
</div>
</div>
</body>
</html>