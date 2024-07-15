<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CLIPBOARD$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CLIPBOARD rootpage-CLIPBOARD skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CLIPBOARD$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_CLIPBOARD$</b> statement copies the <a href="STRING" title="STRING">STRING</a> value into the system clipboard.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_CLIPBOARD$</a> = <i>string_expression$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>string_expression$</i> is the string value to be sent to the clipboard.</li>
<li>The string value will replace everything previously in the clipboard.</li>
<li>Assemble long text into one string variable value before using this statement.</li>
<li>Add CHR$(13) + CHR$(10) CRLF characters to move to a new clipboard line.</li>
<li>When copying text files, end line CRLF characters 13 and 10 do not have to be added.</li>
<li>Numerical values can be converted to strings using <a href="STR$" title="STR$">STR$</a>, <a href="MK$" title="MK$">_MK$</a>, <a href="MKI$" title="MKI$">MKI$</a>, <a href="MKL$" title="MKL$">MKL$</a>, <a href="MKS$" title="MKS$">MKS$</a>, <a href="MKD$" title="MKD$">MKD$</a>, <a href="BIN$" title="BIN$">_BIN$</a>, <a href="HEX$" title="HEX$">HEX$</a> or <a href="OCT$" title="OCT$">OCT$</a>.</li>
<li>The clipboard can be used to copy, paste and communicate between running programs.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Set 2 lines of text in the clipboard using a carriage return to end text lines</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> CrLf <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * <span style="color:#F580B1;">2</span> <span style="color:#919191;">'define as 2 byte STRING</span>
CrLf = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">13</span>) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">10</span>) <span style="color:#919191;">'carriage return &amp; line feed</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CLIPBOARD$</span></a> = <span style="color:#FFB100;">"This is line 1"</span> + CrLf + <span style="color:#FFB100;">"This is line 2"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CLIPBOARD$_(function)" title="CLIPBOARD$ (function)"><span style="color:#4593D8;">_CLIPBOARD$</span></a> <span style="color:#919191;">'display what is in the clipboard</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">This is line 1
This is line 2
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1238" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="CLIPBOARD$_(function)" title="CLIPBOARD$ (function)">_CLIPBOARD$ (function)</a></li>
<li><a href="CLIPBOARDIMAGE_(function)" title="CLIPBOARDIMAGE (function)">_CLIPBOARDIMAGE (function)</a>, <a href="CLIPBOARDIMAGE" title="CLIPBOARDIMAGE">_CLIPBOARDIMAGE</a> (statement)</li>
<li><a href="CHR$" title="CHR$">CHR$</a>, <a href="ASCII" title="ASCII">ASCII</a> (code table)</li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211312
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.033 seconds
Preprocessor visited node count: 161/1000000
Post‐expand include size: 1659/2097152 bytes
Template argument size: 370/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 117/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.264      1 -total
  9.71%    2.064      1 Template:PageSyntax
  8.65%    1.840      8 Template:Text
  8.40%    1.787      2 Template:Parameter
  8.21%    1.745      8 Template:Cl
  7.39%    1.572      1 Template:CodeEnd
  7.39%    1.571      1 Template:PageSeeAlso
  7.34%    1.561      1 Template:PageDescription
  7.24%    1.540      1 Template:PageExamples
  7.14%    1.518      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:26-0!canonical and timestamp 20240714211312 and revision id 8918.
 -->
</div>
</div>
</div>
</div>
</body>
</html>