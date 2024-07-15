<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ACCEPTFILEDROP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ACCEPTFILEDROP rootpage-ACCEPTFILEDROP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ACCEPTFILEDROP</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ACCEPTFILEDROP</a> statement prepares a program window to receive files dropped from Windows Explorer in a drag/drop operation.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_ACCEPTFILEDROP</a> [{ON|OFF}]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Calling the statement with no parameters turns drag/dropping ON.</li>
<li>To know when files have been dropped into your program's window, check that <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES">_TOTALDROPPEDFILES</a> is greater than 0.</li>
<li>Use <a href="DROPPEDFILE" title="DROPPEDFILE">_DROPPEDFILE</a> to read the list, either sequentially or by index.</li>
<li>If using <a href="DROPPEDFILE" title="DROPPEDFILE">_DROPPEDFILE</a> with an index, you must call <a href="FINISHDROP" title="FINISHDROP">_FINISHDROP</a> after you finish working with the list.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.3 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Accepting files dragged from a folder and processing the list received sequentially.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">128</span>, <span style="color:#F580B1;">25</span>, <span style="color:#F580B1;">0</span>)
<a class="mw-selflink selflink"><span style="color:#4593D8;">_ACCEPTFILEDROP</span></a> <span style="color:#919191;">'enables drag/drop functionality</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Drag files from a folder and drop them in this window..."</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES"><span style="color:#4593D8;">_TOTALDROPPEDFILES</span></a> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES"><span style="color:#4593D8;">_TOTALDROPPEDFILES</span></a>
            a$ = <a href="DROPPEDFILE" title="DROPPEDFILE"><span style="color:#4593D8;">_DROPPEDFILE</span></a> <span style="color:#919191;">'reads the list sequentially; when the result is empty ("") it means the list is over</span>
            <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">15</span>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i,
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="FILEEXISTS" title="FILEEXISTS"><span style="color:#4593D8;">_FILEEXISTS</span></a>(a$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
                <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">2</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"file"</span>,
            <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
                <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="DIREXISTS" title="DIREXISTS"><span style="color:#4593D8;">_DIREXISTS</span></a>(a$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
                    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">3</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"folder"</span>,
                <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
                    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">4</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"not found"</span>, <span style="color:#919191;">'highly unlikely, but who knows?</span>
                <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
            <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
            <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">15</span>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a$
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES">_TOTALDROPPEDFILES</a>, <a href="DROPPEDFILE" title="DROPPEDFILE">_DROPPEDFILE</a>, <a href="FINISHDROP" title="FINISHDROP">_FINISHDROP</a></li>
<li><a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a>, <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062542
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.042 seconds
Real time usage: 0.054 seconds
Preprocessor visited node count: 416/1000000
Post‐expand include size: 3471/2097152 bytes
Template argument size: 811/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 232/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   34.174      1 -total
 16.61%    5.678      1 Template:PageSyntax
 13.48%    4.606     36 Template:Cl
  9.89%    3.381     17 Template:Text
  7.32%    2.503      1 Template:PageDescription
  7.09%    2.424      1 Template:CodeStart
  7.07%    2.417      1 Template:PageAvailability
  6.97%    2.381      1 Template:PageExamples
  6.77%    2.313      1 Template:CodeEnd
  5.45%    1.864      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:36-0!canonical and timestamp 20240715062542 and revision id 8253.
 -->
</div>
</div>
</div>
</div>
</body>
</html>