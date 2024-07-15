<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DO...LOOP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DO_LOOP rootpage-DO_LOOP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DO...LOOP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>DO...LOOP</b> statements are used in programs to repeat code or return to the start of a procedure.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<p><i>Syntax 1:</i>
</p>
<dl><dd><b><a class="mw-redirect" href="DO" title="DO">DO</a></b> [{<a class="mw-redirect" href="WHILE" title="WHILE">WHILE</a>|<a href="UNTIL" title="UNTIL">UNTIL</a>} condition]
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><b><a href="LOOP" title="LOOP">LOOP</a></b></dd></dl>
<p>
<i>Syntax 2:</i>
</p>
<dl><dd><b><a class="mw-redirect" href="DO" title="DO">DO</a></b>
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><b><a href="LOOP" title="LOOP">LOOP</a></b> [{<a class="mw-redirect" href="WHILE" title="WHILE">WHILE</a>|<a href="UNTIL" title="UNTIL">UNTIL</a>} condition]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>DO UNTIL or DO WHILE used with LOOP</b>: The condition is evaluated before running the loop code.</li></ul>
<dl><dd><dl><dd><a href="UNTIL" title="UNTIL">UNTIL</a> checks if the condition is false each time before running code.</dd>
<dd><a class="mw-redirect" href="WHILE" title="WHILE">WHILE</a> checks if the condition is true each time before running code.</dd></dl></dd></dl>
<ul><li><b>DO used with LOOP UNTIL or LOOP WHILE</b>: The code block will run at least once:</li></ul>
<dl><dd><dl><dd><a href="UNTIL" title="UNTIL">UNTIL</a> checks if the condition is false before running loop code again.</dd>
<dd><a class="mw-redirect" href="WHILE" title="WHILE">WHILE</a> checks if the condition is true before running loop code again.</dd></dl></dd></dl>
<ul><li>NOTE: You cannot use a condition after both the DO and LOOP statements at the same time.</li>
<li>Use <b><a href="EXIT" title="EXIT">EXIT</a> DO</b> to exit a loop block even before the condition is met.
<ul><li>If you don't specify a condition, you must exit the loop block manually using <b><a href="EXIT" title="EXIT">EXIT</a> DO</b>.</li></ul></li>
<li>If a loop never meets an exit condition requirement, it will never stop.</li></ul>
<p>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">         Table 3: The relational operations for condition checking.
 In this table, <b>A</b> and <b>B</b> are the <a href="Expression" title="Expression">Expressions</a> to compare. Both must represent
 the same general type, i.e. they must result into either numerical values
 or <a href="STRING" title="STRING">STRING</a> values. If a test succeeds, then <b>true</b> (-1) is returned, <b>false</b> (0)
     if it fails, which both can be used in further <a href="Boolean" title="Boolean">Boolean</a> evaluations.
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                          <b><a href="Relational_Operations" title="Relational Operations">Relational Operations</a></b>                          │
 ├────────────┬───────────────────────────────────────────┬────────────────┤
 │ <b>Operation</b>  │                <b>Description</b>                │ <b>Example usage</b>  │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Equal" title="Equal">=</a> B    │ Tests if A is <b>equal</b> to B.                 │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Equal" title="Equal">=</a> B <a href="THEN" title="THEN">THEN</a>  │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Not_Equal" title="Not Equal">&lt;&gt;</a> B   │ Tests if A is <b>not equal</b> to B.             │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Not_Equal" title="Not Equal">&lt;&gt;</a> B <a href="THEN" title="THEN">THEN</a> │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Less_Than" title="Less Than">&lt;</a> B    │ Tests if A is <b>less than</b> B.                │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Less_Than" title="Less Than">&lt;</a> B <a href="THEN" title="THEN">THEN</a>  │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Greater_Than" title="Greater Than">&gt;</a> B    │ Tests if A is <b>greater than</b> B.             │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Greater_Than" title="Greater Than">&gt;</a> B <a href="THEN" title="THEN">THEN</a>  │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Less_Than_Or_Equal" title="Less Than Or Equal">&lt;=</a> B   │ Tests if A is <b>less than or equal</b> to B.    │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Less_Than_Or_Equal" title="Less Than Or Equal">&lt;=</a> B <a href="THEN" title="THEN">THEN</a> │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Greater_Than_Or_Equal" title="Greater Than Or Equal">&gt;=</a> B   │ Tests if A is <b>greater than or equal</b> to B. │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Greater_Than_Or_Equal" title="Greater Than Or Equal">&gt;=</a> B <a href="THEN" title="THEN">THEN</a> │
 └────────────┴───────────────────────────────────────────┴────────────────┘
   The operations should be very obvious for numerical values. For strings
   be aware that all checks are done <b>case sensitive</b> (i.e. "Foo" &lt;&gt; "foo").
   The <b>equal</b>/<b>not equal</b> check is pretty much straight forward, but for the
   <b>less</b>/<b>greater</b> checks the <a href="ASCII" title="ASCII">ASCII</a> value of the first different character is
                          used for decision making:
   <b>E.g.</b> "abc" is <b>less</b> than "abd", because in the first difference (the 3rd
        character) the "c" has a lower <a href="ASCII" title="ASCII">ASCII</a> value than the "d".
   This behavior may give you some subtle results, if you are not aware of
                   the <a href="ASCII" title="ASCII">ASCII</a> values and the written case:
   <b>E.g.</b> "abc" is <b>greater</b> than "abD", because the small letters have higher
        <a href="ASCII" title="ASCII">ASCII</a> values than the capital letters, hence "c" &gt; "D". You may use
        <a href="LCASE$" title="LCASE$">LCASE$</a> or <a href="UCASE$" title="UCASE$">UCASE$</a> to make sure both strings have the same case.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Using WHILE to clear the keyboard buffer.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
DO WHILE <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; "": LOOP ' checks evaluation before running loop code
DO: LOOP WHILE INKEY$ &lt;&gt; "" ' checks evaluation after one run of loop code
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Using UNTIL to clear the keyboard buffer.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
DO UNTIL <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = "": LOOP ' checks evaluation before running loop code
DO: LOOP UNTIL <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = "" ' checks evaluation after one run of loop code
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Using a one time DO loop to exit ANY of several FOR LOOPs, without using <a href="GOTO" title="GOTO">GOTO</a>.
</p>
<dl><dd>SUB reads header contents of a <a href="BSAVE" title="BSAVE">BSAVE</a> file that may include embedded RGB color settings before the image.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a BSAVE file name to read the file for screen mode:"', filenm$
CheckScreen filenm$
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> CheckScreen (Filename$)        'find Screen mode (12 or 13) and image dimensions
   DIM Bsv AS <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 1
   DIM Header AS STRING * 6
   Scr = 0: MaxColors = 0
   <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> Filename$ FOR <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> AS #1
   <a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #1, , Bsv           '1 check for small 2 character
   GET #1, , Header        '2 - 7 rest of file header
   IF Bsv &lt;&gt; <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(253) THEN   ' small 2 character denotes a <a href="BSAVE" title="BSAVE"><span style="color:#4593D8;">BSAVE</span></a> file
      COLOR 12: LOCATE 15, 33: PRINT "Not a BSAVE file!": SLEEP 3: <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> SUB
   END IF
   GET #1, , widN           '8 no color info bmp sizes
   GET #1, , depN           '9   "        "      "
DO
  IF widN &gt; 63 OR depN &gt; 63 THEN <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>  ' width and depth already found
  FOR i = 10 TO 55       'check for Screen 12 embedded colors
    GET #1, , RGB
    tot12&amp; = tot12&amp; + RGB
    'PRINT i; RGB; : SOUND 300, 1         'test sound slows loop in QB
    IF RGB &gt; 63 OR RGB &lt; 0 THEN <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
    IF i = 55 AND tot12&amp; = 0 THEN <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  NEXT
  GET #1, , wid12          '56
  GET #1, , dep12          '57
  IF wid12 &gt; 63 OR dep12 &gt; 63 THEN <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  FOR i = 58 TO 775      'check for Screen 13 embedded colors
    GET #1, , RGB
    tot13&amp; = tot13&amp; + RGB
    'PRINT i; RGB; : SOUND 300, 1          'test
    IF RGB &gt; 63 OR RGB &lt; 0 THEN <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
    IF i = 775 AND tot13&amp; = 0 THEN <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  NEXT
  GET #1, , wid13          '776
  GET #1, , dep13          '777
LOOP <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> 1 = 1    'TRUE statement exits one-time LOOP
CLOSE #1
COLOR 14: LOCATE 10, 25
<a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> i
  <a class="mw-redirect" href="CASE_IS" title="CASE IS"><span style="color:#4593D8;">CASE IS</span></a> &lt; 56:
   IF widN &gt; 640 THEN
       Scr = 13: MaxColors = 0
       PRINT "Default Screen 13:"; widN \ 8; "X"; depN
   ELSE
    LOCATE 10, 15
    PRINT "Screen 12 ("; widN; "X"; depN; ") OR 13 ("; widN \ 8; "X"; depN; ")"
    DO: SOUND 600, 4
       COLOR 13: LOCATE 12, 23  'ask if no data found. Prevents ERROR opening in wrong mode
       <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a Screen mode 12 or 13 : ", Scrn$
       Scr = VAL(Scrn$)
    LOOP UNTIL Scr = 12 OR Scr = 13
   END IF
   IF Scr = 12 THEN MaxColors = 0: PWidth = widN: PDepth = depN
   IF Scr = 13 THEN MaxColors = 0: PWidth = widN \ 8: PDepth = depN
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 56 TO 775
     PRINT "Custom Screen 12:"; wid12; "X"; dep12
     Scr = 12: MaxColors = 16: PWidth = wid12: PDepth = dep12
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 776: PRINT "Custom Screen 13:"; wid13 \ 8; "X"; dep13
     Scr = 13: MaxColors = 256: PWidth = wid13 \ 8: PDepth = dep13
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The SUB procedure reads a file that was <a href="BSAVE" title="BSAVE">BSAVEd</a> previously. If the RGB colors are stored before the image, the values can only be between 0 and 63. Higher values indicate that the image width and height are located there and that there are no stored color values to be read. SUB later displays the dimensions of the file image that <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> placed in the file array. The loop is set to only run once by creating <b>a TRUE <a href="UNTIL" title="UNTIL">UNTIL</a> statement</b> such as 1 = 1. When a screen mode cannot be determined, the user must select one.</dd></dl>
<dl><dd>Dimensions and location of width and height information indicates the screen mode as <a href="SCREEN" title="SCREEN">SCREEN</a> 13 if it has 768 RGB values and dimensions of 320 X 200 max. If the file only holds 64 settings and/or is larger than 320 X 200, it uses SCREEN 12 or 9. The procedure <a href="EXIT" title="EXIT">EXITs</a> the DO LOOP early when the image size is found with or without custom color settings.</dd></dl>
<dl><dd>Divide SCREEN 13 <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> widths by 8.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="EXIT_DO" title="EXIT DO">EXIT DO</a></li>
<li><a href="WHILE...WEND" title="WHILE...WEND">WHILE...WEND</a></li>
<li><a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031552
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 241/1000000
Post‐expand include size: 6983/2097152 bytes
Template argument size: 359/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.794      1 -total
 28.45%    7.055      1 Template:RelationalOperationsPlugin
  9.88%    2.450     29 Template:Cl
  8.36%    2.073      1 Template:PageSyntax
  8.33%    2.064      1 Template:Small
  7.01%    1.737      1 Template:PageDescription
  6.97%    1.727      1 Template:PageNavigation
  6.28%    1.556      1 Template:FixedStart
  6.15%    1.525      1 Template:PageSeeAlso
  5.84%    1.448      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:459-0!canonical and timestamp 20240715031551 and revision id 7865.
 -->
</div>
</div>
</div>
</div>
</body>
</html>