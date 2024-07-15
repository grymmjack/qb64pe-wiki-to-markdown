<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>INPUT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INPUT rootpage-INPUT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">INPUT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">INPUT</a> statement requests a <a href="STRING" title="STRING">STRING</a> or numerical keyboard entry from the user.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">INPUT</a> [;] "[Question or statement text]"{,|;} <i>variable</i>[, ...]</dd>
<dd><a class="mw-selflink selflink">INPUT</a> ; <i>variable</i>[, ...]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>A <a href="Semicolon" title="Semicolon">semicolon</a> after the <a class="mw-selflink selflink">INPUT</a> keyword keeps the entry on the same row after enter is pressed  and prevents the screen contents from rolling up.</li>
<li>The optional prompt "Question or statement text" must be a literal predefined <a href="STRING" title="STRING">string</a>. <b>The prompt cannot use a variable.</b></li>
<li><a href="Quotation_mark" title="Quotation mark">Quotation marks</a> are required except when a semicolon follows <a class="mw-selflink selflink">INPUT</a>. A question mark will appear before the cursor.</li>
<li>A <a href="Semicolon" title="Semicolon">semicolon</a> immediately after the text statement will display a question mark with a space after it. Use a <a href="Comma" title="Comma">comma</a> for input statements.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>QB64</b> does not return <i>Redo from start</i> errors like QBasic did, as user input is limited to the scope of the variable <a href="Data_types" title="Data types">type</a> used.</li>
<li>Text entries (with a <a href="STRING" title="STRING">STRING</a> variable can receive any characters, including numerical. <b>QB64 will ignore commas in single variable text entries.</b></li>
<li>The <a href="Data_types" title="Data types">type</a> of the <i>variable</i> used to store user input determines the valid numerical range for value entries in QB64, with non-numerical characters limited to D, E, <a href="%26H" title="&amp;H">&amp;H</a>, <a href="%26O" title="&amp;O">&amp;O</a> or <a href="%26B" title="&amp;B">&amp;B</a>.
<ul><li>For example, if you use an <a href="INTEGER" title="INTEGER">INTEGER</a> variable, as in <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">INPUT "Initial value: ", myValue%</span>, the valid range is -32768 to 32767.</li>
<li><a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, and <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> entries will ignore decimal points entered and will use all numbers.</li></ul></li>
<li>INPUT can be used to get more than one <i>variable</i> value from the user. Do so by separating input variables with commas in the code.
<ul><li>The program must inform the user that more than one variable is requested, in order to enter each value separated with a comma at runtime.</li>
<li><a href="STRING" title="STRING">String</a> and numerical variables can both be used in multiple entry requests separated by commas.</li>
<li><b>QB64</b>  allows comma separated entries to be skipped by the user without generating an error.</li></ul></li>
<li><b>Use <a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a> for text input entries that may contain commas such as address or name entries.</b></li>
<li>The user must press enter for the INPUT procedure to end.</li>
<li><a class="mw-selflink selflink">INPUT</a> accepts the <a href="Scientific_notation" title="Scientific notation">scientific notation</a> letters D or E in <a href="SINGLE" title="SINGLE">SINGLE</a> or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> numerical values.</li>
<li>Numerical values starting with <a href="%26H" title="&amp;H">&amp;H</a>, <a href="%26O" title="&amp;O">&amp;O</a> and <a href="%26B" title="&amp;B">&amp;B</a> can also be entered.</li>
<li>The statement halts a program until enter is pressed, which may not be desired in programs using mouse input (see <a href="INKEY$" title="INKEY$">INKEY$</a> loops).</li>
<li>Use <a href="DEST" title="DEST">_DEST</a> <a href="CONSOLE" title="CONSOLE">_CONSOLE</a> before INPUT statements to receive input from a <a href="$CONSOLE" title="$CONSOLE">console</a> window.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Using a variable in an input text message using PRINT. INPUT prompts cannot use variables.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">INPUT</span></a> "Enter your name: ", name$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> name$ + " please enter your age: ";: <a class="mw-selflink selflink"><span style="color:#4593D8;">INPUT</span></a> "", age% 'empty string with comma
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> name$ + " how much do you weigh"; : <a class="mw-selflink selflink"><span style="color:#4593D8;">INPUT</span></a> weight%   'no text adds ?
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Use an empty string with a comma to eliminate the question mark that would appear without the string.</dd></dl>
<p>
<i>Example 2:</i> How QB64 avoids a <i>Redo from start</i> multiple entry error. Use commas between values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  <a class="mw-selflink selflink"><span style="color:#4593D8;">INPUT</span></a> "What is your name, age, and sex(M/F)"; name$, age%, sex$
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> age%        'loop until age is not 0
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> age% &gt;= 21 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "You can drink beer!" <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "You cannot drink beer yet!"
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">What is your name, age, and sex(M/F)? Tom,24,M
You can drink beer!
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Try to enter text for the age value and it will not work. E or D should be allowed as decimal point numerical entries.</dd></dl>
<p>
<i>Example 3:</i> Preventing screen roll after an input entry on the bottom 2 screen rows.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 29, 2 '          place cursor at beginning of prompt line
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Enter a name to search for... "; 'print prompt on screen with input to follow
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15: <a class="mw-selflink selflink"><span style="color:#4593D8;">INPUT</span></a> <span style="color:red;">;</span> "", name$ '       get search name from user
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 29, 2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="SPC" title="SPC"><span style="color:#4593D8;">SPC</span></a>(78); '       erase previous prompt
n$ = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(name$) '                 convert search name to upper case
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14'                        change foreground color to yellow
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 29, 2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Searching..."; 'print message
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="color:#FFFF00;">Enter a name to search for...</span> █
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <span style="color:red;">red</span> <a href="Semicolon" title="Semicolon">semicolon</a> after INPUT acts like a semicolon after a <a href="PRINT" title="PRINT">PRINT</a>, which keeps the print cursor on the same row.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INPUT$" title="INPUT$">INPUT$</a>, <a href="INKEY$" title="INKEY$">INKEY$</a></li>
<li><a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a>, <a href="LOCATE" title="LOCATE">LOCATE</a></li>
<li><a href="INPUT_(file_statement)" title="INPUT (file statement)">INPUT #</a>, <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)">LINE INPUT #</a> <span style="color:#777777;">(file input)</span></li>
<li><a href="KEYHIT" title="KEYHIT">_KEYHIT</a>, <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a></li>
<li><a href="Scancodes" title="Scancodes">Scancodes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714160111
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.050 seconds
Real time usage: 0.067 seconds
Preprocessor visited node count: 288/1000000
Post‐expand include size: 2862/2097152 bytes
Template argument size: 364/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   38.618      1 -total
  8.12%    3.134      1 Template:PageSeeAlso
  7.69%    2.970     29 Template:Cl
  7.67%    2.964      4 Template:Text
  7.45%    2.876      1 Template:InlineCode
  7.23%    2.791      1 Template:InlineCodeEnd
  7.20%    2.780      1 Template:PageSyntax
  5.64%    2.176      4 Template:Parameter
  5.61%    2.168      1 Template:PageDescription
  5.37%    2.072      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:475-0!canonical and timestamp 20240714160111 and revision id 7886.
 -->
</div>
</div>
</div>
</div>
</body>
</html>