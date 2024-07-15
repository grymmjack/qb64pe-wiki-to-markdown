<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RESTORE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RESTORE rootpage-RESTORE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RESTORE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>RESTORE</b> statement is used to reset the DATA pointer to the beginning of the data.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>RESTORE [datafield]</dd></dl></dd></dl>
<p>
</p>
<ul><li>The datafield line label or number enables a labeled data field to be <a href="READ" title="READ">READ</a> more than once as required.</li>
<li>Datafield label names are not required when working with ONE or a progression of data fields in the main body of code.</li>
<li>Label multiple data fields to restore them to use them again when necessary.</li>
<li>If RESTORE is used with unlabeled data fields or no datafield is designated then the first data field is read.</li>
<li>Use RESTORE to avoid an <a href="ERROR_Codes" title="ERROR Codes">"Out of Data" error</a> when reading a data field!</li>
<li>See the <a href="DATA" title="DATA">DATA</a> statement for <a href="STRING" title="STRING">STRING</a> data value specifications.</li>
<li><b>Do not place <a href="DATA" title="DATA">DATA</a> fields after <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures! QB64 will FAIL to <a class="mw-selflink selflink">RESTORE</a> properly!</b></li></ul>
<dl><dd>QBasic allowed programmers to add DATA fields anywhere because the IDE separated the main code from other procedures.</dd></dl>
<p>
<i>Example:</i> Restoring a labeled DATA field to avoid going past the end of DATA.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">DO
   <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a month number(1 to 12): ", monthnum%
   <a class="mw-selflink selflink"><span style="color:#4593D8;">RESTORE</span></a> Months
   FOR i = 1 TO monthnum%
      <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> month$, days%   'variables must match data field types
   NEXT
   <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "The month "; month$; " has"; days%; "days."
LOOP UNTIL monthnum% &lt; 1 OR monthnum% &gt; 12
 Months:
 <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> January, 31, February, 28, March, 31, April, 30, May, 31, June, 30
 <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> July, 31, August, 31, September, 30, October, 31, November, 30, December, 31
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Enter a month number(1 to 12): 6
The month June has 30 days.
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> String DATA values do not require quotes unless they have commas, end spaces or QBasic keywords in them.</dd></dl>
<p>
<i>Example:</i> Using RESTORE to know the number of elements in the DATA in order to dimension and store the items in a array.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
<a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> dummy$ 'we won't actually use this string for anything else than to know when there is no more DATA.
count = count + 1
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> dummy$ = "stop" 'when dummy$ = "stop" then we know that it is the last entry so it only does the above loop until then.
count = count - 1 'since the last string is "stop" and we don't want to store it in the array.
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "The number of relevant entries are:"; count
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> entry$(count) 'Now we know how many elements we need to make space for (DIM)
<a class="mw-selflink selflink"><span style="color:#4593D8;">RESTORE</span></a> 'We restore it so that it begins reading from the first DATA again.
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> c = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> count
<a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> entry$(c) 'read the DATA and store it into the array.
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
'we can now print the contents of the array:
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> c = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> count
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> entry$(c)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "entry1", "entry2", "entry3", "stop"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">The number of relevant entries are: 3
entry1
entry2
entry3
</pre>
</td></tr></tbody></table>
<p><i>Note:</i> Now we can add any number of entries without further compensation to the code.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DATA" title="DATA">DATA</a>, <a href="READ" title="READ">READ</a></li>
<li><a href="$EMBED" title="$EMBED">$EMBED</a>. <a href="EMBEDDED$" title="EMBEDDED$">_EMBEDDED$</a></li>
<li><a href="Line_numbers" title="Line numbers">line numbers</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061407
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 191/1000000
Post‐expand include size: 2050/2097152 bytes
Template argument size: 203/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.082      1 -total
 13.40%    2.692     23 Template:Cl
 12.19%    2.448      1 Template:PageSyntax
 10.99%    2.208      1 Template:PageNavigation
  9.47%    1.902      2 Template:CodeStart
  9.28%    1.864      2 Template:OutputEnd
  9.13%    1.833      1 Template:Small
  8.69%    1.745      2 Template:CodeEnd
  8.67%    1.741      1 Template:PageSeeAlso
  8.52%    1.712      2 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:250-0!canonical and timestamp 20240715061407 and revision id 8697.
 -->
</div>
</div>
</div>
</div>
</body>
</html>