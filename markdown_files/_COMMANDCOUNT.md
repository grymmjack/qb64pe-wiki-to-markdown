<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_COMMANDCOUNT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-COMMANDCOUNT rootpage-COMMANDCOUNT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_COMMANDCOUNT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_COMMANDCOUNT</a> function returns the number or arguments passed from the command line to the <a href="COMMAND$" title="COMMAND$">COMMAND$</a> function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result&amp;</i> = <a class="mw-selflink selflink">_COMMANDCOUNT</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function returns the number of arguments passed from the command line to a program when it's executed.</li>
<li>Arguments are spaced as separate numerical or text values. Spaced text inside of quotes is considered as one argument.</li>
<li>In C, this function would generally be regarded as 'argc' when the main program is defined as the following: <b>int main(int argc, char *argv[])</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> The code below gets the number of parameters passed to our program from the command line with _COMMANDCOUNT:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">limit = <a class="mw-selflink selflink"><span style="color:#4593D8;">_COMMANDCOUNT</span></a>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> limit
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="COMMAND$" title="COMMAND$"><span style="color:#4593D8;">COMMAND$</span></a>(i)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> If we start <i>ThisProgram.exe</i> from the command window with <b>ThisProgram -l "loadfile.txt" -s "savefile.txt"</b>, the _COMMANDCOUNT would be 4, "-l", "loadfile.txt", "-s", "savefile.txt" command arguments passed to the program, which we could then read separately with COMMAND$(n).</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="COMMAND$" title="COMMAND$">COMMAND$</a></li>
<li><a href="SHELL" title="SHELL">SHELL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062259
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.038 seconds
Preprocessor visited node count: 74/1000000
Post‐expand include size: 1014/2097152 bytes
Template argument size: 85/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   26.115      1 -total
 10.50%    2.742      1 Template:PageSyntax
 10.31%    2.692      6 Template:Cl
 10.14%    2.647      1 Template:Parameter
  9.86%    2.574      1 Template:PageExamples
  9.85%    2.573      1 Template:CodeStart
  9.67%    2.526      1 Template:PageDescription
  8.85%    2.312      1 Template:Text
  8.74%    2.282      1 Template:CodeEnd
  8.65%    2.260      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:92-0!canonical and timestamp 20240715062259 and revision id 8287.
 -->
</div>
</div>
</div>
</div>
</body>
</html>