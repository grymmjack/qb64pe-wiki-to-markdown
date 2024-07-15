<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FILES$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FILES rootpage-FILES skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FILES$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_FILES$</a> function returns a file or directory name that matches the specified pattern.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>e$</i> = <a class="mw-selflink selflink">_FILES$</a>[(<i>filespec$</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>filespec$</i> is an optional string expression that specifies a file name or path; may include wildcard characters.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If you omit <i>filespec$</i> when you first call <a class="mw-selflink selflink">_FILES$</a>, QB64-PE generates the error message, "Illegal Function Call."</li>
<li>If <i>filespec$</i> is an empty string, then it is assumed to be "<b>*</b>" internally.</li>
<li><a class="mw-selflink selflink">_FILES$</a> returns the first file or directory name that matches the <i>filespec$</i> you specify. To retrieve additional file or directory names that match the <i>filespec$</i> pattern, call <a class="mw-selflink selflink">_FILES$</a> again with no argument. When no file or directory names match, <a class="mw-selflink selflink">_FILES$</a> returns an empty string.</li>
<li>You do not have to retrieve all the file names that match a given <i>filespec$</i> before calling <a class="mw-selflink selflink">_FILES$</a> again with a new <i>filespec$</i>.</li>
<li><a class="mw-selflink selflink">_FILES$</a> is not case sensitive in Windows. However, it is case sensitive in Linux and macOS.</li>
<li>Because file and directory names are retrieved in no particular order, you may want to store file names in a dynamic array and sort the array.</li>
<li>Directory names returned, ends with a backslash on Windows and a forward-slash on Linux and macOS.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="none"><img alt="none" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>none</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.11.0"><img alt="v3.11.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.11.0</b>
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
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Prints the names of all ".bas" files in the parent directory.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$CONSOLE" title="$CONSOLE"><span style="color:#55FF55;">$CONSOLE</span></a>:<a href="ONLY" title="ONLY"><span style="color:#4593D8;">ONLY</span></a>
<a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> f <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>: f = <a class="mw-selflink selflink"><span style="color:#4593D8;">_FILES$</span></a>(<span style="color:#FFB100;">"../*.bas"</span>)
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(f) &gt; <span style="color:#F580B1;">0</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> f
    f = <a class="mw-selflink selflink"><span style="color:#4593D8;">_FILES$</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Recursively prints the directory tree.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$CONSOLE" title="$CONSOLE"><span style="color:#55FF55;">$CONSOLE</span></a>:<a href="ONLY" title="ONLY"><span style="color:#4593D8;">ONLY</span></a>
<a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> directory <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>: directory = <a href="COMMAND$" title="COMMAND$"><span style="color:#4593D8;">COMMAND$</span></a>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="DIREXISTS" title="DIREXISTS"><span style="color:#4593D8;">_DIREXISTS</span></a>(directory) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> directory = <a href="CWD$" title="CWD$"><span style="color:#4593D8;">_CWD$</span></a>
<a href="$IF" title="$IF"><span style="color:#55FF55;">$IF</span></a> <span style="color:#55FF55;">WINDOWS</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(directory, <span style="color:#F580B1;">1</span>) &lt;&gt; <span style="color:#FFB100;">"\"</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> directory = directory + <span style="color:#FFB100;">"\"</span>
<a class="mw-redirect" href="$ELSE" title="$ELSE"><span style="color:#55FF55;">$ELSE</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(directory, <span style="color:#F580B1;">1</span>) &lt;&gt; <span style="color:#FFB100;">"/"</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> directory = directory + <span style="color:#FFB100;">"/"</span>
<a class="mw-redirect" href="$END_IF" title="$END IF"><span style="color:#55FF55;">$END IF</span></a> 
<span style="color:#55FF55;">PrintDirectory</span> <span style="color:#F580B1;">3</span>, directory
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">PrintDirectory</span> (L <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, directory <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>)
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> entry(<span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">0</span>) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> CL <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: CL = L
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> CL &gt; <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> CL = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> e <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>: e = <a class="mw-selflink selflink"><span style="color:#4593D8;">_FILES$</span></a>(directory)
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
        entry(n) = e
        n = n + <span style="color:#F580B1;">1</span>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> n &gt; <a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(entry) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> <a href="PRESERVE" title="PRESERVE"><span style="color:#4593D8;">_PRESERVE</span></a> entry(<span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> n) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
        e = <a class="mw-selflink selflink"><span style="color:#4593D8;">_FILES$</span></a>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP WHILE</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(e) &gt; <span style="color:#F580B1;">0</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> CL &gt; <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , CL - <span style="color:#F580B1;">2</span> <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , CL
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> directory
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
    <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> i &lt; n
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , CL: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> entry(i)
        <a href="$IF" title="$IF"><span style="color:#55FF55;">$IF</span></a> <span style="color:#55FF55;">WINDOWS</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> entry(i) &lt;&gt; <span style="color:#FFB100;">".\"</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> entry(i) &lt;&gt; <span style="color:#FFB100;">"..\"</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(entry(i), <span style="color:#F580B1;">1</span>) = <span style="color:#FFB100;">"\"</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#55FF55;">PrintDirectory</span> CL + <span style="color:#F580B1;">2</span>, directory + entry(i)
        <a class="mw-redirect" href="$ELSE" title="$ELSE"><span style="color:#55FF55;">$ELSE</span></a>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> entry(i) &lt;&gt; <span style="color:#FFB100;">"./"</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> entry(i) &lt;&gt; <span style="color:#FFB100;">"../"</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(entry(i), <span style="color:#F580B1;">1</span>) = <span style="color:#FFB100;">"/"</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#55FF55;">PrintDirectory</span> CL + <span style="color:#F580B1;">2</span>, directory + entry(i)
        <a class="mw-redirect" href="$END_IF" title="$END IF"><span style="color:#55FF55;">$END IF</span></a> 
        i = i + <span style="color:#F580B1;">1</span>
    <a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2727" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="FILES" title="FILES">FILES</a></li>
<li><a href="CWD$" title="CWD$">_CWD$</a>, <a href="STARTDIR$" title="STARTDIR$">_STARTDIR$</a></li>
<li><a href="DIR$" title="DIR$">_DIR$</a></li>
<li><a href="FULLPATH$" title="FULLPATH$">_FULLPATH$</a></li>
<li><a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a>, <a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714174225
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.127 seconds
Real time usage: 0.167 seconds
Preprocessor visited node count: 1052/1000000
Post‐expand include size: 7732/2097152 bytes
Template argument size: 1759/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2417/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  123.126      1 -total
  6.85%    8.437      1 Template:PageAvailability
  4.16%    5.126     92 Template:Cl
  2.99%    3.678     10 Template:Cm
  2.88%    3.552     33 Template:Text
  1.84%    2.263      1 Template:PageExamples
  1.78%    2.197      1 Template:PageSeeAlso
  1.64%    2.024      9 Template:Parameter
  1.64%    2.022      2 Template:CodeStart
  1.61%    1.987      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1223-0!canonical and timestamp 20240714174225 and revision id 8968.
 -->
</div>
</div>
</div>
</div>
</body>
</html>