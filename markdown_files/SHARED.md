<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SHARED - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SHARED rootpage-SHARED skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SHARED</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>SHARED</b> statement allows variables to be passed automatically to any <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedure.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>DIM SHARED Qt AS STRING * 1</dd></dl></dd></dl>
<p>
</p>
<ul><li><a href="DIM" title="DIM">DIMensioned</a> variables are shared with all procedures in the program module.</li>
<li>When used with <a href="DIM" title="DIM">DIM</a> in the main module, it eliminates the need to pass a parameter variable to a <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a>.</li>
<li>Use <a href="COMMON_SHARED" title="COMMON SHARED">COMMON SHARED</a> to share a list of variable values with sub-procedures or other modules. See also: <a href="COMMON" title="COMMON">COMMON</a></li>
<li>SHARED (<b>without <a href="DIM" title="DIM">DIM</a></b>) can share a list of variables inside of <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures with the main module only.</li></ul>
<dl><dd><b>Note: SHARED variables in sub-procedures will not be passed to other sub-procedures, only the main module.</b></dd></dl>
<p>
<i>Example 1:</i> Defining variable types with <a href="AS" title="AS">AS</a> or type suffixes.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">SHARED</span></a> Qt AS <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 1, price AS <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, ID AS <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">SHARED</span></a> Q$, prices#, IDs%
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> The DIR$ function returns a filename or a list when more than one exist. The file spec can use a path and/or wildcards.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 2
  <a href="LINE_INPUT" title="LINE INPUT"><span style="color:#4593D8;">LINE INPUT</span></a> "Enter a file spec: ", spec$
  file$ = DIR$(spec$)        'use a file spec ONCE to find the last file name listed
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> DIRCount%, file$,    'function can return the file count using SHARED variable
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
    file$ = DIR$("")         'use an empty string parameter to return a list of files!
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> file$,
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(file$) = 0  'file list ends with an empty string
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> DIR$ (spec$)
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> TmpFile$ = "DIR$INF0.INF", ListMAX% = 500  'change maximum to suit your needs
<a class="mw-selflink selflink"><span style="color:#4593D8;">SHARED</span></a> DIRCount%                                 'returns file count if desired
<a href="STATIC" title="STATIC"><span style="color:#4593D8;">STATIC</span></a> Ready%, Index%, DirList$()
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> Ready% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> DirList$(ListMax%): Ready% = -1  'DIM array first use
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> spec$ &gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>                               'get file names when a spec is given
  <a href="SHELL" title="SHELL"><span style="color:#4593D8;">SHELL</span></a> <a href="HIDE" title="HIDE"><span style="color:#4593D8;">_HIDE</span></a> "DIR " + spec$ + " /b &gt; " + TmpFile$
  Index% = 0: DirList$(Index%) = "": ff% = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a>
  <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> TmpFile$ <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="APPEND" title="APPEND"><span style="color:#4593D8;">APPEND</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #ff%
  size&amp; = <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(ff%)
  <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #ff%
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> size&amp; = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> TmpFile$: <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
  <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> TmpFile$ <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #ff%
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(ff%) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Index% &lt; ListMAX%
    Index% = Index% + 1
    <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT</span></a> #ff%, DirList$(Index%)
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
  DIRCount% = Index%                       'SHARED variable can return the file count
  <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #ff%
  <a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> TmpFile$
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Index% &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> Index% = Index% - 1 'no spec sends next file name
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
DIR$ = DirList$(Index%)
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The SHARED variable value <i>DIRcount%</i> can tell the main program how many files were found using a wildcard spec.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a></li>
<li><a href="COMMON" title="COMMON">COMMON</a>, <a href="COMMON_SHARED" title="COMMON SHARED">COMMON SHARED</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714101102
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.051 seconds
Real time usage: 0.089 seconds
Preprocessor visited node count: 442/1000000
Post‐expand include size: 3883/2097152 bytes
Template argument size: 661/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   60.334      1 -total
 30.55%   18.433      1 Template:Small
 13.10%    7.902     60 Template:Cl
 12.25%    7.389      1 Template:PageNavigation
 10.77%    6.497      1 Template:PageSyntax
 10.00%    6.033      1 Template:PageSeeAlso
  7.16%    4.322      2 Template:CodeEnd
  6.56%    3.957      2 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:295-0!canonical and timestamp 20240714101102 and revision id 7955.
 -->
</div>
</div>
</div>
</div>
</body>
</html>