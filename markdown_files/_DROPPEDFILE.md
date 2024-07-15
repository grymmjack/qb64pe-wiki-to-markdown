<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DROPPEDFILE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DROPPEDFILE rootpage-DROPPEDFILE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DROPPEDFILE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DROPPEDFILE</a> function returns the list of items (files or folders) dropped in a program's window after <a href="ACCEPTFILEDROP" title="ACCEPTFILEDROP">_ACCEPTFILEDROP</a> is enabled.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<p><i>Syntax 1</i>
</p>
<dl><dd><i>nextItem$</i> = <a class="mw-selflink selflink">_DROPPEDFILE</a></dd></dl>
<p><i>Syntax 2</i>
</p>
<dl><dd><i>nextItem$</i> = <a class="mw-selflink selflink">_DROPPEDFILE</a>(<i>index&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>After <a href="ACCEPTFILEDROP" title="ACCEPTFILEDROP">_ACCEPTFILEDROP</a> is enabled, once <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES">_TOTALDROPPEDFILES</a> is greater than 0 the list of dropped items will be available for retrieval with <a class="mw-selflink selflink">_DROPPEDFILE</a></li>
<li>When using <a class="mw-selflink selflink">_DROPPEDFILE</a> to read the list sequentially (without specifying an <i>index&amp;</i>), an empty string ("") indicates the list is over and then <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES">_TOTALDROPPEDFILES</a> gets reset to 0.</li>
<li>When using <a class="mw-selflink selflink">_DROPPEDFILE</a> with an index (which goes from 1 to <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES">_TOTALDROPPEDFILES</a>), you must call <a href="FINISHDROP" title="FINISHDROP">_FINISHDROP</a> after you finish working with the list.</li>
<li>Because it returns a string, <a class="mw-selflink selflink">_DROPPEDFILE</a> also accepts being followed by a string suffix (<a class="mw-selflink selflink">_DROPPEDFILE</a><b>$</b>)</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.3 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Accepting files dragged from a folder and processing the list received by specifying an index.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">128</span>, <span style="color:#F580B1;">25</span>, <span style="color:#F580B1;">0</span>)
<a href="ACCEPTFILEDROP" title="ACCEPTFILEDROP"><span style="color:#4593D8;">_ACCEPTFILEDROP</span></a> <span style="color:#919191;">'enables drag/drop functionality</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Drag files from a folder and drop them in this window..."</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES"><span style="color:#4593D8;">_TOTALDROPPEDFILES</span></a> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES"><span style="color:#4593D8;">_TOTALDROPPEDFILES</span></a>
            a$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_DROPPEDFILE</span></a>(i)
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
        <a href="FINISHDROP" title="FINISHDROP"><span style="color:#4593D8;">_FINISHDROP</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ACCEPTFILEDROP" title="ACCEPTFILEDROP">_ACCEPTFILEDROP</a>, <a href="TOTALDROPPEDFILES" title="TOTALDROPPEDFILES">_TOTALDROPPEDFILES</a>, <a href="FINISHDROP" title="FINISHDROP">_FINISHDROP</a></li>
<li><a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a>, <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062545
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.051 seconds
Real time usage: 0.065 seconds
Preprocessor visited node count: 425/1000000
Post‐expand include size: 3500/2097152 bytes
Template argument size: 816/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 147/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   37.667      1 -total
 11.79%    4.442     37 Template:Cl
  9.63%    3.628      1 Template:PageDescription
  9.45%    3.561     16 Template:Text
  8.97%    3.377      1 Template:PageSyntax
  8.56%    3.223      1 Template:PageAvailability
  7.07%    2.663      1 Template:CodeStart
  6.56%    2.471      3 Template:Parameter
  6.44%    2.424      1 Template:PageExamples
  6.40%    2.411      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:128-0!canonical and timestamp 20240715062545 and revision id 8317.
 -->
</div>
</div>
</div>
</div>
</body>
</html>