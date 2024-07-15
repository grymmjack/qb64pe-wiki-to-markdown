<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>TYPE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TYPE rootpage-TYPE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">TYPE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>TYPE</b> definitions are used to create variables that can hold more than one variable type of a fixed byte length.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>TYPE</b> typename</dd>
<dd>.</dd>
<dd>. variable(s) <a href="AS" title="AS">AS</a> type</dd>
<dd>.</dd>
<dd><b>END TYPE</b></dd></dl>
<p>
</p>
<ul><li>Typename is an undefined type name holder as it can hold any variable types.</li>
<li>TYPE definitions should be placed in the main module before the start of the program code execution.</li>
<li>TYPE definitions CAN be placed in <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures using QB64 only!</li>
<li>TYPE definitions cannot contain Array variables! Arrays can be <a href="DIM" title="DIM">DIMensioned</a> as a TYPE definition.</li>
<li>TYPE definitions cannot be inside of another TYPE definition, but variables can be defined AS another type.(See Example 3)</li>
<li>TYPE definitions must be ended with <a class="mw-redirect" href="END_TYPE" title="END TYPE">END TYPE</a>.</li>
<li>A TYPE variable MUST be assigned to the type after it is defined. Array variables are allowed.</li>
<li>Type variables must be defined in every SUB or FUNCTION unless the type variable is <a href="DIM" title="DIM">DIMensioned</a> as <a href="SHARED" title="SHARED">SHARED</a>.</li>
<li>Type variables use DOT variable names to read or write specific values. They do not use type suffixes as they can hold ANY variable type values! The name before the dot is the one you defined after the type definition and the name after is the variable name used inside of the TYPE. The name of the dimensioned type variable alone can be used to <a href="PUT" title="PUT">PUT</a> # or <a href="GET" title="GET">GET</a> # all of the data at once!</li>
<li>Once the TYPE variable is created you can find the record or byte size by using <a href="LEN" title="LEN">LEN</a>(typevariable).</li>
<li>TYPE definitions can also be placed in <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> .BI text files such as <a href="QB.BI" title="QB.BI">QB.BI</a> is used by <a href="INTERRUPT" title="INTERRUPT">INTERRUPT</a> and <a href="INTERRUPTX" title="INTERRUPTX">INTERRUPTX</a>.</li>
<li><b><a href="BIT" title="BIT">_BIT</a> is not currently supported in User Defined <a class="mw-selflink selflink">TYPEs</a></b>.</li>
<li><b>NOTE: Many QBasic keyword variable names CAN be used with a <a href="STRING" title="STRING">STRING</a> suffix($) ONLY! You CANNOT use them without the suffix, use a numerical suffix or use <a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a>, <a href="DEFINE" title="DEFINE">_DEFINE</a>, <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> or <a class="mw-selflink selflink">TYPE</a> variable <a href="AS" title="AS">AS</a> statements!</b></li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">         Table 1: The variable types supported by the QB64 language.
┌───────────────────────────────────────────────────────────────────────────┐
│                              <b>Numerical types</b>                              │
├──────────────────────┬───────────┬────────────────────────────┬───────────┤
│      <b>Type Name</b>       │   <b>Type</b>    │       <b>Minimum value</b>        │  <b>Size in</b>  │
│                      │  <b>suffix</b>   │       <b>Maximum value</b>        │   <b>Bytes</b>   │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│         <a href="BIT" title="BIT">_BIT</a>         │     `     │                         -1 │    1/8    │
│                      │           │                          0 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│       <a href="BIT" title="BIT">_BIT * n</a>       │    `n     │                       -128 │    n/8    │
│                      │           │                        127 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│    <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="BIT" title="BIT">_BIT</a>    │    ~`     │                          0 │    1/8    │
│                      │           │                          1 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│        <a href="BYTE" title="BYTE">_BYTE</a>         │    %%     │                       -128 │     1     │
│                      │           │                        127 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│   <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="BYTE" title="BYTE">_BYTE</a>    │    ~%%    │                          0 │     1     │
│                      │           │                        255 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│       <a href="INTEGER" title="INTEGER">INTEGER</a>        │     %     │                    -32,768 │     2     │
│                      │           │                     32,767 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│  <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="INTEGER" title="INTEGER">INTEGER</a>   │    ~%     │                          0 │     2     │
│                      │           │                     65,535 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│         <a href="LONG" title="LONG">LONG</a>         │     &amp;     │             -2,147,483,648 │     4     │
│                      │           │              2,147,483,647 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│    <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a>    │    ~&amp;     │                          0 │     4     │
│                      │           │              4,294,967,295 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│      <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>      │    &amp;&amp;     │ -9,223,372,036,854,775,808 │     8     │
│                      │           │  9,223,372,036,854,775,807 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> │    ~&amp;&amp;    │                          0 │     8     │
│                      │           │ 18,446,744,073,709,551,615 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│        <a href="SINGLE" title="SINGLE">SINGLE</a>        │     !     │              -2.802597E-45 │     4     │
│                      │ (or none) │              +3.402823E+38 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│        <a href="DOUBLE" title="DOUBLE">DOUBLE</a>        │     #     │    -4.490656458412465E-324 │     8     │
│                      │           │    +1.797693134862310E+308 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│        <a href="FLOAT" title="FLOAT">_FLOAT</a>        │    ##     │                -1.18E-4932 │    32     │
│                      │           │                +1.18E+4932 │ (10 used) │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│       <a href="OFFSET" title="OFFSET">_OFFSET</a>        │    %&amp;     │ -9,223,372,036,854,775,808 │  use <a href="LEN" title="LEN">LEN</a>  │
│                      │           │  9,223,372,036,854,775,807 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│  <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="OFFSET" title="OFFSET">_OFFSET</a>   │    ~%&amp;    │                          0 │  use <a href="LEN" title="LEN">LEN</a>  │
│                      │           │ 18,446,744,073,709,551,615 │           │
├──────────────────────┼───────────┼────────────────────────────┴───────────┤
│         <a href="MEM" title="MEM">_MEM</a>         │   none    │ <b>An internal <a class="mw-selflink selflink">TYPE</a> like memory variable.</b> │
└──────────────────────┴───────────┴────────────────────────────────────────┘
  For the floating-point numeric types <a href="SINGLE" title="SINGLE">SINGLE</a> (default when not assigned),
 <a href="DOUBLE" title="DOUBLE">DOUBLE</a> and <a href="FLOAT" title="FLOAT">_FLOAT</a>, the minimum values represent the smallest values closest
  to zero, while the maximum values represent the largest values closest to
    pos./neg. infinity. <a href="OFFSET" title="OFFSET">_OFFSET</a> dot values are used as a part of the <a href="MEM" title="MEM">_MEM</a>
       variable type in QB64 to return or set the position in memory.
┌───────────────────────────────────────────────────────────────────────────┐
│                                <b>Text types</b>                                 │
├──────────────────────┬───────────┬────────────────────────────┬───────────┤
│      <b>Type Name</b>       │   <b>Type</b>    │       <b>Minimum value</b>        │  <b>Size in</b>  │
│                      │  <b>suffix</b>   │       <b>Maximum value</b>        │   <b>Bytes</b>   │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│        <a href="STRING" title="STRING">STRING</a>        │     $     │                          0 │  use <a href="LEN" title="LEN">LEN</a>  │
│                      │           │              2,147,483,647 │           │
├──────────────────────┼───────────┼────────────────────────────┼───────────┤
│      <a href="STRING" title="STRING">STRING * n</a>      │    $n     │                          1 │     n     │
│                      │           │              2,147,483,647 │           │
└──────────────────────┴───────────┴────────────────────────────┴───────────┘
  While a regular variable length <a href="STRING" title="STRING">STRING</a> may have a minimum length of <b>zero</b>
   (empty string), the fixed length string type <a href="STRING" title="STRING">STRING * n</a>, where <b>n</b> is an
 integer length value, must have a minimum length of at least <b>one</b> character.
</pre>
</td></tr></tbody></table>
<p>
<i>Example 1:</i> Creating a mouse <a href="INTERRUPT" title="INTERRUPT">INTERRUPT</a> TYPE definition. Each <a href="INTEGER" title="INTEGER">INTEGER</a> value is 2 bytes.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-selflink selflink"><span style="color:#4593D8;">TYPE</span></a> RegType
   AX <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' mouse function to use
   BX <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' mouse button
   CX <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' mouse graphic column position
   DX <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' mouse graphic row position
   BP <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' not used by mouse, but required *
   SI <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' not used by mouse, but required *
   DI <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' not used by mouse, but required *
   Flags <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a> ' not used by mouse but required *
   DS <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' used by <a href="INTERRUPTX" title="INTERRUPTX"><span style="color:#4593D8;">INTERRUPTX</span></a> only
   ES <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>    ' used by <a href="INTERRUPTX" title="INTERRUPTX"><span style="color:#4593D8;">INTERRUPTX</span></a> only
 <a class="mw-selflink selflink"><span style="color:#4593D8;">END TYPE</span></a>
 <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> InRegs <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> RegType, OutRegs <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> RegType ' create dot variables
 InRegs.AX = 3 ' sets the mouse function to read the mouse buttons and position.
 <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> <a href="INTERRUPT" title="INTERRUPT"><span style="color:#4593D8;">INTERRUPT</span></a>(&amp;H33, InRegs, OutRegs)
 column% = OutRegs.CX ' returns the current mouse column position
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> InRegs and OutRegs become the DOT variable prefix name for the TYPE definition's variables.</dd></dl>
<dl><dd><dl><dd><dl><dd><dl><dd>Each TYPE variable is designated as the DOT variable's suffix.</dd></dl></dd></dl></dd></dl></dd></dl>
<p><b>* Note: Omitting variables in the RegType definition can change other program variable values!</b>
<i>Example 2:</i> Creating an addressbook database for a <a href="RANDOM" title="RANDOM">RANDOM</a> file.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> TYPE ContactInfo
   First AS STRING * 10
   Last AS STRING * 15
   Address1 AS STRING * 30
   Address2 AS STRING * 30
   City AS STRING * 15
   State AS STRING * 2
   Zip AS LONG   ' (4 bytes)
   Phone AS STRING * 12
 END TYPE
 DIM Contact AS ContactInfo 'create contact record variable for <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> file
 RecordLEN% = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Contact) ' 118 bytes
  'define values
 Contact.First = "Ted" ' the fixed string length value will contain 7 extra spaces
 Contact.Zip = 15236 ' <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> value that can be used to search certain zip code numbers.
 <a href="PUT" title="PUT"><span style="color:#4593D8;">PUT #</span></a>1, 5,Contact  'place contact info into fifth record position
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Use the assigned type variable to find the RANDOM record length which is 118 bytes.
<dl><dd><dl><dd><dl><dd>The DOT variable names consist of Contact as the prefix:</dd></dl></dd></dl></dd></dl></dd></dl>
<p>
<i>Example 3:</i> Defining a TYPE variable as another variable type from a previous TYPE definition in QB64.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">TYPE</span></a> bar
  b <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 10
END TYPE
TYPE foo
  a <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
  c <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> bar          'define variable as a bar type
END TYPE
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> foobar <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> foo   'create a variable to use the foo type
foobar.a = 15.5
foobar.c.b = "this is me"
PRINT foobar.a, foobar.c.b
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 4:</i> A bitmap header information TYPE <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> File.
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">' ********
'Bitmap.BI can be included at start of program
 TYPE BMPHeaderType        ' Description                  Bytes      <b>QB64</b>
   ID AS STRING * 2        ' File ID is "BM"                2
   Size AS LONG            ' Size of the data file          4
   Res1 AS INTEGER         ' Reserved 1 should be 0         2
   Res2 AS INTEGER         ' Reserved 2 should be 0         2
   Offset AS LONG          ' Start position of pixel data   4
   Hsize AS LONG           ' Information header size        4
   PWidth AS LONG          ' Image width                    4       <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:blue;">_WIDTH (function)</span></a>
   PDepth AS LONG          ' Image height                   4       <a href="HEIGHT" title="HEIGHT"><span style="color:blue;">_HEIGHT</span></a>
   Planes AS INTEGER       ' Number of planes               2
   BPP AS INTEGER          ' Bits per pixel(palette)        2       <a href="PIXELSIZE" title="PIXELSIZE"><span style="color:blue;">_PIXELSIZE</span></a>
   Compress AS LONG        ' Compression                    4
   ImageBytes AS LONG      ' Width * Height = ImageSIZE     4
   Xres AS LONG            ' Width in PELS per metre        4
   Yres AS LONG            ' Depth in PELS per metre        4
   NumColors AS LONG       ' Number of Colors               4
   SigColors AS LONG       ' Significant Colors             4
 END TYPE                  '          Total Header bytes = 54
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">'<a href="$INCLUDE" title="$INCLUDE"><span style="color:#4593D8;">$INCLUDE</span></a>: 'Bitmap.BI'  'use only when including a BI file
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> BMPHead AS BMPHeaderType
<a href="GET" title="GET"><span style="color:#4593D8;">GET #</span></a>1, , BMPHead  'get the entire bitmap header information
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Use one <a href="GET" title="GET">GET</a> to read all of the header information from the start of the bitmap file opened AS <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a>. It reads all 54 bytes as <a href="STRING" title="STRING">STRING</a>, <a href="INTEGER" title="INTEGER">INTEGER</a> and <a href="LONG" title="LONG">LONG</a> type DOT variable values.</dd></dl>
<dl><dd>NOTE: BPP returns 4(16 colors), 8(256 colors) or 24(16 million colors) bits per pixel in QBasic. 24 bit can only be in greyscale.</dd></dl>
<dl><dd>Then use the DOT variable name values like this <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a> after you load the bitmap image to the screen:</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="GET_(graphics_statement)" title="GET (graphics statement)"><span style="color:#4593D8;">GET</span></a> (0, 0)-(BMPHead.PWidth - 1, BMPHead.PDepth - 1), Image(48) 'indexed for 4 BPP colors
</pre>
</td></tr></tbody></table>
<dl><dd>The bitmap image is now stored in an <a href="Arrays" title="Arrays">array</a> to <a href="BSAVE" title="BSAVE">BSAVE</a> to a file. The RGB color information follows the file header as <a href="ASCII" title="ASCII">ASCII</a> character values read using <a href="ASC_(function)" title="ASC (function)">ASC</a>. The color values could be indexed at the start of the Array with the image being offset to: index = NumberOfColors * 3. As determined by the <a href="SCREEN" title="SCREEN">SCREEN</a> mode used. In SCREEN 13(256 colors) the index would be 768.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a></li>
<li><a href="LONG" title="LONG">LONG</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>, <a href="FLOAT" title="FLOAT">_FLOAT</a></li>
<li><a href="STRING" title="STRING">STRING</a>, <a href="BYTE" title="BYTE">_BYTE</a>, <a href="BIT" title="BIT">_BIT</a>, <a href="OFFSET" title="OFFSET">_OFFSET</a></li>
<li><a href="GET" title="GET">GET #</a>, <a href="PUT" title="PUT">PUT #</a>, <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a></li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a>, <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="LEN" title="LEN">LEN</a>, <a href="LOF" title="LOF">LOF</a>, <a href="EOF" title="EOF">EOF</a></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a>, <a href="Creating_Icon_Bitmaps#Icon_to_Bitmap_Conversion_Function" title="Creating Icon Bitmaps">Icon to Bitmap Conversion Function</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034235
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.051 seconds
Real time usage: 0.064 seconds
Preprocessor visited node count: 395/1000000
Post‐expand include size: 14186/2097152 bytes
Template argument size: 523/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.427      1 -total
 24.91%    8.078      1 Template:DataTypePlugin
 11.27%    3.655     48 Template:Cl
  8.93%    2.897      1 Template:PageSyntax
  7.07%    2.293      3 Template:Cb
  6.82%    2.212      5 Template:CodeEnd
  6.79%    2.202      1 Template:FixedStart
  6.65%    2.157      1 Template:TextStart
  6.24%    2.024      1 Template:TextEnd
  6.11%    1.980      1 Template:FixedEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:274-0!canonical and timestamp 20240715034235 and revision id 8738.
 -->
</div>
</div>
</div>
</div>
</body>
</html>