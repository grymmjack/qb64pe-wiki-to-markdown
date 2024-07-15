<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>MOD - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOD rootpage-MOD skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">MOD</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">MOD</a> operator gives the remainder after division of one number by another (sometimes called modulus).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>remainder</i> = <i>numerator</i> <a class="mw-selflink selflink">MOD</a> <i>divisor</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Returns the integer division remainder as a whole <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a> or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> value.</li>
<li><i>numerator</i> is the <a href="INTEGER" title="INTEGER">INTEGER</a> value to divide.</li>
<li><i>divisor</i> is the <a href="INTEGER" title="INTEGER">INTEGER</a> value to divide by.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Floating decimal point <i>numerator</i> and <i>divisor</i> values are <a href="CINT" title="CINT">CINT</a> rounded (e.g. <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">19 MOD 6.7</span> returns 5 just like <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">19 MOD 7</span> would).</li>
<li>MOD returns 0 if a number is evenly divisible by integer division ( <a href="%5C" title="\">\</a> ) or the number divided is 0.</li>
<li><b><i>divisor</i> (second value) must not be between 0 and .5</b>. This will create a <a href="ERROR_Codes" title="ERROR Codes">"Division by zero" error</a> due to <a href="CINT" title="CINT">CINT</a> rounding the value to 0.</li>
<li>The result has the same sign as the numerator (e.g. <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">-1 MOD 7</span> returns -1, not 6).</li>
<li>Division and multiplication operations are performed before addition and subtraction in QBasic's order of operations.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">  I% = 100 <a href="%5C" title="\"><span style="color:#4593D8;">\</span></a> 9
  R% = 100 <a class="mw-selflink selflink"><span style="color:#4593D8;">MOD</span></a> 9
  PRINT "Integer division ="; I%, "Remainder ="; R%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">  Integer division = 11        Remainder = 1
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> Integer division 100 \ 9 returns 11. 11 <a href="*" title="*">*</a> 9 = 99. So the remainder must be 1 as 100 - 99 = 1. Normal decimal point division would return 11.11111.
<i>Example 2:</i> Comparing normal, integer and remainder division.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">tmp1$ = " Normal:         ####.# / #### = ##.###   "
tmp2$ = " Integer:        ####.# \ #### = ###      "
tmp3$ = " Remainder:    ####.# MOD #### = ####     "
FOR i = 1 TO 6
   SELECT CASE i
     CASE 1: numerator = 1: divisor = 5
     CASE 2: numerator = 13: divisor = 10
     CASE 3: numerator = 990: divisor = 100
     CASE 4: numerator = 1100: divisor = 100
     CASE 5: numerator = 4501: divisor = 1000
     CASE 6: numerator = 50.6: divisor = 10
   END SELECT
LOCATE 5, 20: PRINT USING tmp1$; numerator; divisor; numerator / divisor
LOCATE 7, 20: PRINT USING tmp2$; numerator; divisor; numerator \ divisor
LOCATE 9, 20: PRINT USING tmp3$; numerator; divisor; numerator MOD divisor
DO: SLEEP: LOOP UNTIL INKEY$ &lt;&gt; ""
NEXT
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Integer division and MOD can be used to convert values to different base numbering systems from base 2 to 36 as <a href="STRING" title="STRING">strings</a>:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
DO
  <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a base number system 2 to 36: ", b%
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> b% &lt; 2 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> b% &gt; 36 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Enter a positive value to convert: ";
  num$ = ""
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: K$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
    num$ = num$ + K$
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a>, <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(0): <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> K$;
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> K$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(13)
  n&amp; = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(num$)
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> n&amp; = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  Bnum$ = BASEN$(n&amp;, b%)
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Bnum$ ', <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>("<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>" + Bnum$) 'tests hexadecimal base 16 only
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> BASEN$ (number&amp;, basenum%)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> basenum% &lt; 2 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> basenum% &gt; 36 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> number&amp; = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
num&amp; = number&amp; 'protect value of number!
DO
  remain% = <a href="ABS" title="ABS"><span style="color:#4593D8;">ABS</span></a>(num&amp;) <a class="mw-selflink selflink"><span style="color:#4593D8;">MOD</span></a> basenum% ' remainder is used to create actual digit 0 to Z
  num&amp; = num&amp; \ basenum% ' move up one exponent of base% with integer division
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> remain% &gt; 9 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    b$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(65 + (remain% - 10)) 'limited to base 36
  <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>: b$ = <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(remain%)) ' make remainder a string number
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  BN$ = b$ + BN$ ' add remainder character to base number string
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> num&amp; = 0
BASEN$ = BN$
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Base numbering systems over base 10(0 - 9) use alphabetical letters to represent digits greater than 9 like <a href="%26H" title="&amp;H">Hexadecimal</a>(0 - F).</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1196" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="/" title="/">/ (normal division operator)</a></li>
<li><a href="%5C" title="\">\ (integer division operator)</a></li>
<li><a href="INT" title="INT">INT</a>, <a href="CINT" title="CINT">CINT</a>, <a href="FIX" title="FIX">FIX</a>, <a href="ROUND" title="ROUND">_ROUND</a>, <a href="CEIL" title="CEIL">_CEIL</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061345
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.042 seconds
Real time usage: 0.060 seconds
Preprocessor visited node count: 384/1000000
Post‐expand include size: 3875/2097152 bytes
Template argument size: 501/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   39.081      1 -total
 18.51%    7.234      1 Template:PageSyntax
  8.98%    3.509      1 Template:PageDescription
  8.23%    3.217     45 Template:Cl
  7.19%    2.808      3 Template:InlineCode
  5.83%    2.280      6 Template:Parameter
  5.37%    2.099      3 Template:InlineCodeEnd
  5.09%    1.991      1 Template:PageParameters
  4.86%    1.898      1 Template:PageExamples
  4.77%    1.865      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:581-0!canonical and timestamp 20240715061345 and revision id 8902.
 -->
</div>
</div>
</div>
</div>
</body>
</html>