<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ALLOWFULLSCREEN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ALLOWFULLSCREEN rootpage-ALLOWFULLSCREEN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ALLOWFULLSCREEN</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ALLOWFULLSCREEN</a> statement allows setting the behavior of the ALT+ENTER combo.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_ALLOWFULLSCREEN</a> [{_STRETCH|_SQUAREPIXELS|OFF|_ALL}][, {_SMOOTH|OFF|_ALL}]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Calling the statement with no parameters enables all four possible full screen modes (and is the default state when a program is started): both <a class="mw-redirect" href="STRETCH" title="STRETCH">_STRETCH</a> (<a class="mw-redirect" href="SMOOTH" title="SMOOTH">_SMOOTH</a> and <a href="OFF" title="OFF">_OFF</a>) and <a class="mw-redirect" href="SQUAREPIXELS" title="SQUAREPIXELS">_SQUAREPIXELS</a> (<a class="mw-redirect" href="SMOOTH" title="SMOOTH">_SMOOTH</a> and <a href="OFF" title="OFF">_OFF</a>).
<ul><li>Using <a class="mw-selflink selflink">_ALLOWFULLSCREEN</a> <a class="mw-redirect" href="ALL" title="ALL">_ALL</a>, <a class="mw-redirect" href="ALL" title="ALL">_ALL</a> has the same effect.</li></ul></li>
<li><a class="mw-selflink selflink">_ALLOWFULLSCREEN</a> only affects the behavior of ALT+ENTER. The <a href="FULLSCREEN" title="FULLSCREEN">_FULLSCREEN</a> statement is not bound by <a class="mw-selflink selflink">_ALLOWFULLSCREEN</a>'s settings so all modes can be accessed programmatically.</li>
<li>To limit just the mode but allow both _SMOOTH + _OFF antialiasing modes, pass just the first parameter: <i>Example:</i> <a class="mw-selflink selflink">_ALLOWFULLSCREEN</a> _SQUAREPIXELS</li>
<li>To allow multiple modes with _SMOOTH or _OFF as default, pass just the second parameter. <i>Example:</i> <a class="mw-selflink selflink">_ALLOWFULLSCREEN</a> , _SMOOTH</li>
<li>Any possible permutation of the parameters is allowed.</li>
<li>With <a class="mw-selflink selflink">_ALLOWFULLSCREEN</a> _OFF you can trap Alt+Enter manually in your program and reassign it. See example 2 below.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.3 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Allowing only one fullscreen mode with square pixels and no antialiasing:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_ALLOWFULLSCREEN</span></a> <a class="mw-redirect" href="SQUAREPIXELS" title="SQUAREPIXELS"><span style="color:#4593D8;">_SQUAREPIXELS</span></a> , <a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> Disabling _FULLSCREEN with Alt+ENTER so the combo can be manually trapped:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">7</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"    - Press ALT+ENTER to test trapping the combo..."</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"    _ Press SPACEBAR to allow fullscreen again..."</span>
    k&amp; = <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> k&amp; = <span style="color:#F580B1;">13</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="KEYDOWN" title="KEYDOWN"><span style="color:#4593D8;">_KEYDOWN</span></a>(<span style="color:#F580B1;">100307</span>) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> <a href="KEYDOWN" title="KEYDOWN"><span style="color:#4593D8;">_KEYDOWN</span></a>(<span style="color:#F580B1;">100308</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            altEnter = altEnter + <span style="color:#F580B1;">1</span>
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> k&amp; = <span style="color:#F580B1;">32</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        fullscreenEnabled = <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> fullscreenEnabled
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">14</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> fullscreenEnabled <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a class="mw-selflink selflink"><span style="color:#4593D8;">_ALLOWFULLSCREEN</span></a> <a class="mw-redirect" href="ALL" title="ALL"><span style="color:#4593D8;">_ALL</span></a> , <a class="mw-redirect" href="ALL" title="ALL"><span style="color:#4593D8;">_ALL</span></a>
        altEnter = <span style="color:#F580B1;">0</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_ALLOWFULLSCREEN _ALL, _ALL"</span>
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">18</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"ALT+ENTER will trigger all four fullscreen modes now."</span>
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        <a class="mw-selflink selflink"><span style="color:#4593D8;">_ALLOWFULLSCREEN</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_ALLOWFULLSCREEN OFF"</span>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> altEnter <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">18</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"ALT+ENTER manually trapped"</span>; altEnter; <span style="color:#FFB100;">"times."</span>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FULLSCREEN" title="FULLSCREEN">_FULLSCREEN</a>, <a href="SMOOTH_(function)" title="SMOOTH (function)">_SMOOTH (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193301
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.052 seconds
Real time usage: 0.069 seconds
Preprocessor visited node count: 475/1000000
Post‐expand include size: 3929/2097152 bytes
Template argument size: 885/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 246/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   41.628      1 -total
 14.32%    5.960      2 Template:CodeStart
 13.91%    5.792     43 Template:Cl
  8.95%    3.726     18 Template:Text
  7.94%    3.305      1 Template:PageSyntax
  7.93%    3.301      1 Template:PageExamples
  7.41%    3.083      1 Template:PageSeeAlso
  6.07%    2.529      1 Template:PageAvailability
  5.95%    2.478      1 Template:PageDescription
  5.93%    2.469      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:39-0!canonical and timestamp 20240714193301 and revision id 8255.
 -->
</div>
</div>
</div>
</div>
</body>
</html>