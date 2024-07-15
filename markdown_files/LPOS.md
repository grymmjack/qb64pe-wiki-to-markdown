<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LPOS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LPOS rootpage-LPOS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LPOS</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LPOS</a> function returns the current LPT printer head position.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result%</i> = <a class="mw-selflink selflink">LPOS</a>(<i>index%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>index%</i> is the index of the printer, which can have the following values:
<ul><li>0 - LPT1:</li>
<li>1 - LPT1:</li>
<li>2 - LPT2:</li>
<li>3 - LPT3:</li></ul></li>
<li>The LPOS function does not necessarily give the physical position of the print head because it does not expand tab characters. In addition, some printers may buffer characters.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dd>Prompts the user for team names and the names of players on each team. It then prints the players and their teams on the printer.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="LPRINT" title="LPRINT"><span style="color:#4593D8;">LPRINT</span></a> "Team Members"; <a href="TAB" title="TAB"><span style="color:#4593D8;">TAB</span></a>(76); "TEAM" : <a href="LPRINT" title="LPRINT"><span style="color:#4593D8;">LPRINT</span></a>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "How many teams"; TEAMS
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "How many players per team";PPT
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> T = 1 TO TEAMS
    <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Team name: ", TEAM$
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> P = 1 TO PPT
        <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "   Enter player name: ", PLAYER$
        <a href="LPRINT" title="LPRINT"><span style="color:#4593D8;">LPRINT</span></a> PLAYER$;
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> P &lt; PPT <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">LPOS</span></a>(0) &gt; 55 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' Print a new line if print head past column 55.
                <a href="LPRINT" title="LPRINT"><span style="color:#4593D8;">LPRINT</span></a> : <a href="LPRINT" title="LPRINT"><span style="color:#4593D8;">LPRINT</span></a> <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(5);
            <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
                <a href="LPRINT" title="LPRINT"><span style="color:#4593D8;">LPRINT</span></a> ", ";         'Otherwise, print a comma.
            <a href="END" title="END"><span style="color:#4593D8;">END</span></a> IF
        <a href="END" title="END"><span style="color:#4593D8;">END</span></a> IF
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> P
<a href="LPRINT" title="LPRINT"><span style="color:#4593D8;">LPRINT</span></a> <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(80 - <a class="mw-selflink selflink"><span style="color:#4593D8;">LPOS</span></a>(0) - <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(TEAM$),"."); TEAM$
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> T
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LPRINT" title="LPRINT">LPRINT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714235445
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 242/1000000
Post‐expand include size: 2191/2097152 bytes
Template argument size: 299/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.400      1 -total
 13.89%    2.696     30 Template:Cl
 11.14%    2.161      1 Template:PageSyntax
 10.51%    2.038      1 Template:PageNavigation
 10.34%    2.007      1 Template:CodeStart
  9.54%    1.851      1 Template:PageSeeAlso
  9.19%    1.782      3 Template:Parameter
  8.81%    1.709      1 Template:PageExamples
  8.32%    1.614      1 Template:CodeEnd
  7.42%    1.440      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:555-0!canonical and timestamp 20240714235445 and revision id 658.
 -->
</div>
</div>
</div>
</div>
</body>
</html>