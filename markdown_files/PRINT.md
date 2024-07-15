<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PRINT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PRINT rootpage-PRINT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PRINT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">PRINT</a> statement prints numeric or string expressions to the program screen. Typing shortcut <b>?</b>  will convert to PRINT.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><dl><dd><b>PRINT</b> [<i>expression</i>] [{;|,}] [<i>expression</i>...]</dd></dl></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>expression</i> is a numeric or string expression or list of expressions to be written to the screen. End quotes will not be displayed in strings.</li>
<li>The print statement can be followed by a <a href="Semicolon" title="Semicolon">semicolon</a> to stop the print cursor or a <a href="Comma" title="Comma">comma</a> to tab space the next print.</li></ul>
<p>
<i>Usage:</i>
</p>
<ul><li><a href="STRING" title="STRING">STRING</a> values will eliminate leading and trailing quotation marks when printed to the screen. Use <a href="CHR$" title="CHR$">CHR$</a>(34) to add quotes to the <a href="SCREEN" title="SCREEN">SCREEN</a>.</li>
<li>PRINT with no parameters moves the print cursor to the next print row at column 1.</li>
<li><i>expression</i> is a numeric or string expression to be printed.
<ul><li><a href="SPACE$" title="SPACE$">SPACE$</a>(<i>n%</i>) or <a href="SPC" title="SPC">SPC</a>(<i>n%</i>) - specifies that <i>n%</i> space characters will be printed.</li>
<li><a href="TAB" title="TAB">TAB</a>(<i>column%</i>) - specifies that the print cursor is to move to column number <i>column%</i>. If the print cursor is already beyond that column, it is moved to the designated column on the next row.</li></ul></li>
<li>A <i>separator</i> is used to separate multiple expressions and specifies how the print cursor is to be moved:
<ul><li><a href="Semicolon" title="Semicolon">Semicolon</a>(;) - specifies that the print cursor stops at the end of the printed <i>expression</i> and may append later <i>expressions</i> or prints. PRINT ; or PRINT ""; will stop cursor movement and append later prints. Ending <a href="Semicolon" title="Semicolon">semicolons</a> can also stop screen roll.</li>
<li><a href="Comma" title="Comma">Comma</a>(,) - specifies that the print cursor is to move to the next 14-column tab-stop. If the print cursor is at column 56 or greater, it is moved to the next row at column 1. When used after an <i>expression</i> it may Tab-stop append later prints.</li>
<li><a href="%2B" title="+">Plus</a>(+) uses <a href="Concatenation" title="Concatenation">concatenation</a> to add <a href="STRING" title="STRING">STRING</a> expressions ONLY with no spacing. <b>Cannot combine  numerical <i>expression</i>s!</b></li>
<li>If a <i>separator</i> is not used at the end of the expression list, the print cursor moves to the next row at column 1.</li></ul></li>
<li>When <b>printing numerical</b> <i>expressions</i> values, the following rules are used:
<ul><li>If the value is positive, the number is prefixed with a space character, otherwise, the number is prefixed with a negative sign (-).</li>
<li>If the value is an integer (whole number), no decimal point or fractional part will be printed.</li>
<li>If the value is not an <a href="INTEGER" title="INTEGER">integer</a>(whole number) and has zero for a coefficient, no leading zero is printed. EX: -0.123 prints "-.123 "</li>
<li>If the expression is in <a href="Scientific_notation" title="Scientific notation">scientific notation</a>, the number is also printed in scientific notation.</li>
<li>The number is <a class="mw-selflink selflink">printed</a> with a space after it unless <a href="STR$" title="STR$">STR$</a>(number) is used to convert it to string text.</li>
<li>Numerical values MUST be added to a PRINT statement string using <a href="Comma" title="Comma">commas</a> or <a href="Semicolon" title="Semicolon">semicolons</a> on each side of the value or by using <a href="STR$" title="STR$">STR$</a> to convert the value to a string to use <a href="Concatenation" title="Concatenation">concatenation</a> (+ string addition).</li></ul></li>
<li><a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a> can set up a viewport area for PRINTs. Text printed on the bottom view port row will scroll the text upward.</li>
<li>Text to be printed can be a <a href="STRING" title="STRING">STRING</a> variable or a literal value inside of quotation marks.</li>
<li>Use <a href="Semicolon" title="Semicolon">semicolon</a> ends on bottom 2 rows of the SCREEN mode used or the PRINT will roll the screen up.</li>
<li><b>Quotes cannot be inside of a literal STRING! Use <a href="CHR$" title="CHR$">CHR$</a>(34) <a href="Concatenation" title="Concatenation">concatenation</a> to insert <a href="Quotation_mark" title="Quotation mark">quotation marks</a> into a literal string.</b></li>
<li>To better format number and text data placement use <a href="PRINT_USING" title="PRINT USING">PRINT USING</a>.</li>
<li>Instead of typing PRINT you can just type a <a href="Question_mark" title="Question mark">question mark</a> (?). It will change to PRINT when enter is pressed in the IDE.</li>
<li>Use the <a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a> statement before a print to deal with the text background in <b>QB64</b>:</li></ul>
<dl><dd><ul><li><b>1</b> _KEEPBACKGROUND: Text background transparent. Only the text is displayed over anything behind it.</li>
<li><b>2</b> _ONLYBACKGROUND: Text background is only displayed. Text is transparent to anything behind it.</li>
<li><b>3</b> _FILLBACKGROUND: Text and background block anything behind them. Default setting.</li>
<li>Use the <a href="PRINTMODE_(function)" title="PRINTMODE (function)">_PRINTMODE (function)</a> to find the current _PRINTMODE setting number.</li></ul></dd></dl>
<ul><li><a href="WRITE" title="WRITE">WRITE</a> can be used to print a list of comma separated data values to the screen with <a href="Comma" title="Comma">commas</a> between each value.</li>
<li>Use <a href="DEST" title="DEST">_DEST</a> <a href="CONSOLE" title="CONSOLE">_CONSOLE</a> before PRINT statements to be used in a <a href="$CONSOLE" title="$CONSOLE">console</a> window.</li>
<li>Use <a href="CONTROLCHR" title="CONTROLCHR">_CONTROLCHR</a> <b>OFF</b> to PRINT the unprintable lower <a href="ASCII" title="ASCII">ASCII</a> control characters in QB64.</li></ul>
<p>
<i>Example 1:</i> Using semicolons, comma tabs or concatenation to insert <a href="ASCII" title="ASCII">ASCII</a> characters and numbers in a PRINT:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> CHR$(34); "Hello world!"; CHR$(34) ' adding quotation marks
<a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> 123 'demonstrates the positive leading space
a$ = "Hello country!": a = 321: b = -321
<a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> a$, a ' demonstrates comma in statement
<a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> a$; a ' demonstrates semicolon in statement
<a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> a$ + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(b) ' concatenation of string numerical values only
? "Hello city!" ' a ? changes to PRINT after moving cursor from the code line in IDE
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">"Hello world!"
 123
Hello country!      321
Hello country! 321
Hello country!-321
Hello city!
</pre>
</td></tr></tbody></table>
<dl><dd>First PRINT prints the text between two quotation marks, then it prints the value 123, notice that there are no quotation marks when printing the value, quotation marks mean that it will be treated like a literal string of text. a$ is set to "Hello country" and 'a' is set to the value 321, the dollar sign is used when a variable holds the text string. The contents of a$ is then printed and the "," means that the value of 'a' is printed separated by a tab and ";" means that there is no separation from the other text except for the leading positive value space.</dd></dl>
<p>
<i>Example 2:</i> Changing colors in a line of text using semicolons with colon separators between PRINTs on the same code line.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 12: <a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> "Start red "; : <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 10: <a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> "and end green."
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 11: <a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> "Start aqua ";
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14: <a class="mw-selflink selflink"><span style="color:#4593D8;">PRINT</span></a> "and end blue."
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="color:#FF1515;">Start red</span> <span style="color:#15FF15;">and end green.</span>
<span style="color:#15FFFF;">Start aqua</span> <span style="color:#0000FF;">and end blue.</span> </pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a>, <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a>, <a href="PRINT_USING" title="PRINT USING">PRINT USING</a></li>
<li><a href="SPC" title="SPC">SPC</a>, <a href="TAB" title="TAB">TAB</a>, <a href="SPACE$" title="SPACE$">SPACE$</a>, <a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="CSRLIN" title="CSRLIN">CSRLIN</a>, <a href="POS" title="POS">POS</a>, <a href="SCREEN_(function)" title="SCREEN (function)">SCREEN (function)</a></li>
<li><a href="COLOR" title="COLOR">COLOR</a>, <a href="LOCATE" title="LOCATE">LOCATE</a>, <a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a></li>
<li><a href="INPUT" title="INPUT">INPUT</a>, <a href="STR$" title="STR$">STR$</a>, <a href="CHR$" title="CHR$">CHR$</a></li>
<li><a href="ASCII" title="ASCII">ASCII</a>, <a href="CONTROLCHR" title="CONTROLCHR">_CONTROLCHR</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714091532
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.056 seconds
Real time usage: 0.097 seconds
Preprocessor visited node count: 190/1000000
Post‐expand include size: 1819/2097152 bytes
Template argument size: 271/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   58.842      1 -total
 18.14%   10.671      1 Template:PageSyntax
 11.75%    6.914      4 Template:Text
 11.68%    6.871      1 Template:PageParameters
 10.56%    6.215      2 Template:CodeStart
  9.89%    5.822      9 Template:Parameter
  8.10%    4.769     14 Template:Cl
  5.28%    3.107      1 Template:PageSeeAlso
  4.88%    2.869      2 Template:OutputStart
  4.87%    2.864      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:74-0!canonical and timestamp 20240714091532 and revision id 8853.
 -->
</div>
</div>
</div>
</div>
</body>
</html>