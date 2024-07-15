<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CONST - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CONST rootpage-CONST skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CONST</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">CONST</a> statement globally defines one or more named numeric or string values which will not change while the program is running.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CONST</a> <i>constantName</i> = <i>value</i>[, ...]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>constantName</i> is the constant name or list of names assigned by the programmer.</li>
<li><i>value</i> is the value to initialize the global constant which cannot change once defined.
<ul><li>If <i>constantName</i> specifies a numeric type, <i>value</i> must be a numeric expression containing literals and other constants.</li>
<li>If <i>constantName</i> specifies a string type, the <i>value</i> must be a literal value.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>constantName</i> does not have to include a type suffix. The datatype is automatically infered by the compiler using the <i>value</i>.</li>
<li>Constant values cannot reference a variable, <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> return values when defined.
<ul><li>The exception to the above are color functions <a href="RGB32" title="RGB32">_RGB32</a> and <a href="RGBA32" title="RGBA32">_RGBA32</a>, which can be used in a CONST statement. See <i>Example 2</i> below.</li></ul></li>
<li>Constants cannot be reassigned values. They retain the same value throughout all of the program procedures.</li>
<li>Constants defined in module-level code have <a href="SHARED" title="SHARED">shared</a> scope, so they can also be used in <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures.</li>
<li>Constants defined in <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures are local to those procedures.</li>
<li><a href="CLEAR" title="CLEAR">CLEAR</a> will not affect or change constant values.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Display the circumference and area of circles:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">' Declare a numeric constant approximately equal to the ratio of a circle's
' circumference to its diameter:
<a class="mw-selflink selflink"><span style="color:#4593D8;">CONST</span></a> PI = 3.141593
' Declare some string constants:
<a class="mw-selflink selflink"><span style="color:#4593D8;">CONST</span></a> circumferenceText = "The circumference of the circle is"
<a class="mw-selflink selflink"><span style="color:#4593D8;">CONST</span></a> areaText = "The area of the circle is"
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
    <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter the radius of a circle or zero to quit"; radius
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> radius = 0 <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">THEN</span></a> <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> circumferenceText; 2 * PI * radius
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> areaText; PI * radius * radius ' radius squared
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Enter the radius of a circle or zero to quit? <i>10</i>
The circumference of the circle is 62.83186
The area of the circle is 314.1593
Enter the radius of a circle or zero to quit? <i>123.456</i>
The circumference of the circle is 775.697
The area of the circle is 47882.23
Enter the radius of a circle or zero to quit? <i>0</i>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> PI cannot change as it is a mathematical constant so it is fitting to define it as a constant. Trying to change PI will result in a calculation error.</dd></dl>
<p>
<i>Example 2</i>: Using _RGB32 to set a constant's value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">CONST</span></a> Red = _RGB32(255,0,0)
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> Red
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hello World"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DIM" title="DIM">DIM</a>, <a href="SHARED" title="SHARED">SHARED</a></li>
<li><a href="STATIC" title="STATIC">STATIC</a>, <a href="COMMON" title="COMMON">COMMON</a></li>
<li><a href="PI" title="PI">_PI</a>, <a href="RGB32" title="RGB32">_RGB32</a>, <a href="RGBA32" title="RGBA32">_RGBA32</a></li>
<li><a class="external text" href="http://doc.pcsoft.fr/en-US/?6510001" rel="nofollow">Windows 32 API constant values</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031538
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 176/1000000
Post‐expand include size: 1722/2097152 bytes
Template argument size: 239/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.052      1 -total
  9.47%    2.088     15 Template:Cl
  9.12%    2.012      1 Template:PageSyntax
  8.84%    1.950     10 Template:Parameter
  7.58%    1.671      1 Template:PageParameters
  7.41%    1.635      2 Template:CodeStart
  7.22%    1.592      1 Template:PageSeeAlso
  7.10%    1.565      1 Template:PageNavigation
  7.06%    1.557      1 Template:PageDescription
  6.96%    1.534      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:419-0!canonical and timestamp 20240715031538 and revision id 7244.
 -->
</div>
</div>
</div>
</div>
</body>
</html>