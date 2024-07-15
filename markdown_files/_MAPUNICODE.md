<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MAPUNICODE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MAPUNICODE rootpage-MAPUNICODE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MAPUNICODE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MAPUNICODE</a> statement maps a <a href="Unicode" title="Unicode">Unicode</a> value to an <a href="ASCII" title="ASCII">ASCII</a> character code value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_MAPUNICODE</a> <i>unicode&amp;</i> <b>TO</b> <i>asciiCode%</i></dd></dl>
<p>
</p>
<ul><li>The <a href="LONG" title="LONG">LONG</a> <i>unicode&amp;</i> value is a <a href="HEX$" title="HEX$">hexadecimal</a> or decimal code value from a <a href="Unicode" title="Unicode">Unicode</a> <a href="Code_Pages" title="Code Pages">Code Page</a>.</li>
<li>The <i>asciiCode%</i> <a href="INTEGER" title="INTEGER">INTEGER</a> parameter is any <a href="ASCII" title="ASCII">ASCII</a> or Extended code value from 0 to 255.</li>
<li>Use the Unicode Page Table values listed here: <a class="extiw" href="https://en.wikipedia.org/wiki/Category:DOS_code_pages" title="wikipedia:Category:DOS code pages">DOS Code Pages</a> or <a class="external text" href="http://unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/" rel="nofollow">Windows Mapping</a></li>
<li>Once the codes are mapped, key entries will display the unicode character in the <b>monospace </b> <a href="FONT" title="FONT">font</a> selected.</li>
<li>The <a href="MAPUNICODE_(function)" title="MAPUNICODE (function)">_MAPUNICODE</a> function can be used to verify or read the present <a href="Unicode" title="Unicode">Unicode</a> UTF32 code point settings.</li>
<li><b><a class="mw-selflink selflink">_MAPUNICODE</a> can place the Unicode characters TO any <a href="ASCII" title="ASCII">ASCII</a> code space you desire (0 to 255)</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Converting the extended <a href="ASCII" title="ASCII">ASCII</a> characters to other characters using DATA from the Unicode <a href="Code_Pages" title="Code Pages">Code Pages</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 0
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>("C:\windows\fonts\cour.ttf", 20, "MONOSPACE")
<a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> Microsoft_pc_cpMIK
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> ASCIIcode = 128 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 255
  <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> unicode
  <a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPUNICODE</span></a> Unicode <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> ASCIIcode
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 128 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 255
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(i) + " ";
  cnt = cnt + 1
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> cnt <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 16 = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
Microsoft_pc_cpMIK:
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 9492,9524,9516,9500,9472,9532,9571,9553,9562,9566,9577,9574,9568,9552,9580,9488
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 9617,9618,9619,9474,9508,8470,167,9559,9565,9496,9484,9608,9604,9612,9616,9600
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 945,223,915,960,931,963,181,964,934,920,937,948,8734,966,949,8745
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 8801,177,8805,8804,8992,8993,247,8776,176,8729,183,8730,8319,178,9632,160
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The Unicode data field is created by adding DATA before each line listed for the appropriate <a href="Code_Pages" title="Code Pages">Code Page</a>.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1169" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="MAPUNICODE_(function)" title="MAPUNICODE (function)">_MAPUNICODE (function)</a></li>
<li><a href="ASCII" title="ASCII">ASCII</a>, <a href="Unicode" title="Unicode">Unicode</a>, <a href="FONT" title="FONT">_FONT</a></li>
<li><a href="KEYHIT" title="KEYHIT">_KEYHIT</a>, <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a></li>
<li><a href="ASC" title="ASC">ASC</a>, <a href="INKEY$" title="INKEY$">INKEY$</a>, <a href="CHR$" title="CHR$">CHR$</a></li>
<li><a href="Code_Pages" title="Code Pages">Code Pages</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062356
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.046 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 230/1000000
Post‐expand include size: 2071/2097152 bytes
Template argument size: 297/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.381      1 -total
 17.23%    4.889     28 Template:Cl
 13.58%    3.855      1 Template:PageSyntax
 12.90%    3.662      1 Template:CodeEnd
  9.80%    2.780      4 Template:Parameter
  9.05%    2.569      1 Template:CodeStart
  8.94%    2.537      1 Template:PageSeeAlso
  8.81%    2.499      1 Template:PageNavigation
  8.34%    2.368      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:172-0!canonical and timestamp 20240715062356 and revision id 8989.
 -->
</div>
</div>
</div>
</div>
</body>
</html>