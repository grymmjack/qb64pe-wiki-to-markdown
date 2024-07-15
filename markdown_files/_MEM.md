<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEM - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEM rootpage-MEM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEM</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEM</a> variable type can be used when working with memory blocks. It has no variable <a href="Variable_Types" title="Variable Types">type</a> suffix.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DIM" title="DIM">DIM</a> m <a href="AS" title="AS">AS</a> <a class="mw-selflink selflink">_MEM</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<p><i>Variable TYPE:</i>
</p>
<ul><li>Memory DOT values are actually part of the built in memory variable <a href="Variable_Types" title="Variable Types">type</a> in QB64. The following <a href="TYPE" title="TYPE">TYPE</a> is built in:</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">TYPE memory_type
  OFFSET AS _OFFSET       'start location of block(changes with byte position)
  SIZE AS _OFFSET         'size of block remaining at offset(changes with position)
  TYPE AS _OFFSET         'type description of variable used(never changes)
  ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)
  IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used
  SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used
END TYPE
<span style="color:red;">The above <a href="TYPE" title="TYPE">TYPE</a> is for clarification purposes only. It <b>doesn't need</b> to be pasted ina program to use _MEM.</span>
<span style="color:red;"><b>IMPORTANT NOTE:</b> <i>As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.</i></span>
</pre>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="Usage">Usage</span></h3>
<ul><li>The _MEM type contains the following <b>read-only</b> elements where <i>name</i> is the _MEM variable name:</li></ul>
<dl><dd><dl><dd><i>name</i><b>.OFFSET</b> is the current start position in the memory block AS <a href="OFFSET" title="OFFSET">_OFFSET</a>. Add bytes to change position.</dd>
<dd><i>name</i><b>.SIZE</b> is the remaining size of the block at current position in bytes AS <a href="OFFSET" title="OFFSET">_OFFSET</a></dd>
<dd><i>name</i><b>.TYPE</b> is the type (represented as bits combined to form a value) AS <a href="OFFSET" title="OFFSET">_OFFSET</a>:</dd></dl></dd></dl>
<p>
</p>
<h2><span id=".TYPE_values_.28version_1.000_and_up_incl._all_QB64-PE_releases.29"></span><span class="mw-headline" id=".TYPE_values_(version_1.000_and_up_incl._all_QB64-PE_releases)">.TYPE values (version 1.000 and up incl. all QB64-PE releases)</span></h2>
<dl><dd><dl><dd><dl><dd><ul><li>[bit 0] 1* byte types (_BYTE)</li>
<li>[bit 1] 2* byte types (INTEGER)</li>
<li>[bit 2] 4* byte types (LONG or SINGLE)</li>
<li>[bit 3] 8* byte types (DOUBLE or _INTEGER64)</li>
<li>[bit 4] 16* byte types (reserved for future use)</li>
<li>[bit 5] 32* byte types (_FLOAT)</li>
<li>[bit 6] 64* byte types (reserved for future use)</li>
<li>[bit 7] 128 = integer types (_BYTE, INTEGER, LONG, _INTEGER64) (added to *)</li>
<li>[bit 8] 256 = floating point types (SINGLE, DOUBLE, _FLOAT) (added to *)</li>
<li>[bit 9] 512 = STRING types (fixed length or variable length)</li>
<li>[bit 10] 1024 = _UNSIGNED types (added to *+128)</li>
<li>[bit 11] 2048 = pixel data usually from _MEMIMAGE (added to 1+128+1024 for 256 color screens, or 2+128+1024 for text screens, or 4+128+1024 for 32-bit color screens)</li>
<li>[bit 12] 4096 = _MEM TYPE structure (NOT added to 32768)</li>
<li>[bit 13] 8192 = _OFFSET type (added to 4+128+[1024] or 8+128+[1024] or future_size+128+[1024])</li>
<li>[bit 14] 16384 = data created/defined by _MEMNEW(size) or _MEMNEW(offset,size)</li>
<li>[bit 15] 32768 = a custom, user defined type (ie. created with TYPE name ... END TYPE)</li>
<li>[bit 16] 65536 = an array of data (added to other type values defining the array's data type)</li></ul></dd></dl></dd></dl></dd></dl>
<p><i>Note: If a future integer, float or other type doesn't have a size that is 1,2,4,8,16,32,64,128 or 256 it won't have a size-bit set.</i>
</p>
<h3><span id="Versions_prior_to_1.000_.28never_use_with_QB64-PE_releases.29"></span><span class="mw-headline" id="Versions_prior_to_1.000_(never_use_with_QB64-PE_releases)">Versions prior to 1.000 (never use with QB64-PE releases)</span></h3>
<dl><dd><dl><dd><dl><dd><ul><li>1 = Integer types such as <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> or <a href="OFFSET" title="OFFSET">_OFFSET</a></li>
<li>2 = <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> variable types. Value must be added to the variable type value.(2 cannot be used by itself)</li>
<li>3 = ALL <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="INTEGER" title="INTEGER">INTEGER</a> type values.(add 1 + 2)</li>
<li>4 = Floating point types such as <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a></li>
<li>8 = <a href="STRING" title="STRING">STRING</a></li>
<li>0 = unknown(eg. created with <a href="MEMNEW" title="MEMNEW">_MEMNEW</a>) or <a href="TYPE" title="TYPE">user-defined-types</a></li></ul></dd></dl></dd></dl></dd></dl>
<ul><li><b>Note: <a href="OFFSET" title="OFFSET">_OFFSET</a> values cannot be cast to other variable <a href="Variable_Types" title="Variable Types">types</a> reliably. _MEM is a reserved custom variable <a href="Variable_Types" title="Variable Types">type</a>.</b></li>
<li><b><a href="MEM_(function)" title="MEM (function)">_MEM</a> cannot reference variable length <a href="STRING" title="STRING">STRING</a> variable values. String values must be designated as a fixed-<a href="LEN" title="LEN">length</a> string.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Demonstration of .IMAGE to determine an image's dimensions, .TYPE to verify the type and <a href="MEMEXISTS" title="MEMEXISTS">_MEMEXISTS</a> to check image has not been freed
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><span style="color:#919191;">'The $UNSTABLE command may not be necessary if HTTP integration has been fully accepted into QB64PE.</span>
<span style="color:#919191;">'Feel free to remark it out if the IDE flags the following line with an ERROR message.</span>
<span style="color:#919191;">'And kindly report the issue on our forums or Discord so that we can update this page to keep it as 100% relevant, as possible.</span>
<a href="$UNSTABLE" title="$UNSTABLE"><span style="color:#55FF55;">$UNSTABLE</span></a>:HTTP
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">500</span>, <span style="color:#F580B1;">500</span>, <span style="color:#F580B1;">32</span>)
Image$ = <span style="color:#55FF55;">Download$</span>(<span style="color:#FFB100;">"https://qb64phoenix.com/qb64wiki/resources/assets/peWikiLogo.png"</span>, statusCode&amp;) <span style="color:#919191;">'Let's try and download the QB64PE Logo from the web</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> statusCode&amp; = <span style="color:#F580B1;">200</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">'                                      200 says a proper connection was made to the web page in question</span>
    i = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(Image$, <span style="color:#F580B1;">32</span>, <span style="color:#FFB100;">"memory"</span>) <span style="color:#919191;">'                       and then we load it for use as a registered imange</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"HTTP ERROR"</span>; statusCode <span style="color:#919191;">'                             can't get a proper connection to our webpage, so we don't have an image to work with.</span>
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a> <span style="color:#919191;">'                                                        end and go report the issue on the forums, if you'd be so kind, dear user.</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)-(<span style="color:#F580B1;">500</span>, <span style="color:#F580B1;">500</span>), i <span style="color:#919191;">'                                 put the image on the screen so we can view it</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEM</span></a>: m = <a href="MEMIMAGE" title="MEMIMAGE"><span style="color:#4593D8;">_MEMIMAGE</span></a>(i) <span style="color:#919191;">'                                make a memblock and point it towards our image</span>
<span style="color:#919191;">'                                                           **** try uncommenting the following line and see what happens ****</span>
<span style="color:#919191;">'_MEMFREE m</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> m.TYPE <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">2048</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"this is/was an image"</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="MEMEXISTS" title="MEMEXISTS"><span style="color:#4593D8;">_MEMEXISTS</span></a>(m) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">'                                      check if memory m is still available</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> t <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">7</span>; <span style="color:#FFB100;">"bytes per pixel"</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"image handle "</span>; m.IMAGE
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"image width"</span>; <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(m.IMAGE)
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"image height"</span>; <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(m.IMAGE)
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <span style="color:#919191;">'                                                       if we removed the remark from the _MEMFREE above, we'll see the following message</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Memory already freed!"</span>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<span style="color:#919191;">' Content of the HTTP response is returned.</span>
<span style="color:#919191;">' The statusCode is also assigned.</span>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">Download$</span> (url <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, statusCode <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> h <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, content <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, s <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
    h = <a href="OPENCLIENT" title="OPENCLIENT"><span style="color:#4593D8;">_OPENCLIENT</span></a>(<span style="color:#FFB100;">"HTTP:"</span> + url)
    statusCode = <a href="STATUSCODE" title="STATUSCODE"><span style="color:#4593D8;">_STATUSCODE</span></a>(h)
    <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(h)
        <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">60</span>
        <a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #h, , s
        content = content + s
    <a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
    <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #h
    <span style="color:#55FF55;">Download$</span> = content
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Converts the current <a href="DEST" title="DEST">destination</a> <a href="SCREEN" title="SCREEN">SCREEN</a> 13 image memory altered by <a href="PSET" title="PSET">PSET</a> to a <a href="STRING" title="STRING">STRING</a> value. SCREEN 13 only.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">13</span>
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<span style="color:#FFB100;">"H"</span>) <span style="color:#919191;">'put the ASCII value of "H" into the top left corner of screen, which is the first byte of screen image memory</span>
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (<span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">0</span>), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<span style="color:#FFB100;">"E"</span>) <span style="color:#919191;">'put the ASCII value of "E" into the 2nd byte of screen image memory</span>
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (<span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">0</span>), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<span style="color:#FFB100;">"L"</span>) <span style="color:#919191;">'put the ASCII value of "L" into the 3nd byte of screen image memory</span>
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (<span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">0</span>), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<span style="color:#FFB100;">"L"</span>) <span style="color:#919191;">'put the ASCII value of "L" into the 4th byte of screen image memory</span>
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (<span style="color:#F580B1;">4</span>, <span style="color:#F580B1;">0</span>), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<span style="color:#FFB100;">"O"</span>) <span style="color:#919191;">'put the ASCII value of "O" into the 5th byte of screen image memory                                                                                                                                                                                                            'put the ASCII value of "E" into the 2nd byte of screen image memory</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEM</span></a> <span style="color:#919191;">'                         define m as a mem block</span>
m = <a href="MEMIMAGE" title="MEMIMAGE"><span style="color:#4593D8;">_MEMIMAGE</span></a>(<span style="color:#F580B1;">0</span>) <span style="color:#919191;">'                      point m to where our screen exists in memory</span>
x1$ = <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(m, m.OFFSET, <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * <span style="color:#F580B1;">5</span>) <span style="color:#919191;">'m is the mem block that we're wanting to get information from</span>
<span style="color:#919191;">'                                       m.OFFSET is the mem block m starting position</span>
<span style="color:#919191;">'                                       STRING * 5 is the size and type of information that we want to get from that position in memory.</span>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">1</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(x1$) <span style="color:#919191;">'                        prints 5 bytes as we deliberately fetched STRING * 5 bytes with our _MEMGET above.</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x1$ <span style="color:#919191;">'                             prints the contents of that 5-byte string which we got above -- which is "HELLO" as CHR$() string character values</span>
<a href="MEMFREE" title="MEMFREE"><span style="color:#4593D8;">_MEMFREE</span></a> m
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 5
HELLO
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Using _MEM to convert _OFFSET to _INTEGER64.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEM</span></a>
m = <a href="MEM_(function)" title="MEM (function)"><span style="color:#4593D8;">_MEM</span></a>(x)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> m.OFFSET
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#55FF55;">ConvertOffset</span>(m.OFFSET)
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">ConvertOffset&amp;&amp;</span> (value <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="OFFSET_(function)" title="OFFSET (function)"><span style="color:#4593D8;">_OFFSET</span></a>)
    <a href="$CHECKING" title="$CHECKING"><span style="color:#55FF55;">$CHECKING</span></a>:<a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEM</span></a> <span style="color:#919191;">'Define a memblock</span>
    m = <a href="MEM_(function)" title="MEM (function)"><span style="color:#4593D8;">_MEM</span></a>(value) <span style="color:#919191;">'Point it to use value</span>
    <a href="$IF" title="$IF"><span style="color:#55FF55;">$IF</span></a> <span style="color:#F580B1;">64BIT</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> temp <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER64" title="INTEGER64"><span style="color:#4593D8;">_INTEGER64</span></a> <span style="color:#919191;">'On 64 bit OSes, an OFFSET is 8 bytes in size.</span>
    <a class="mw-redirect" href="$ELSE" title="$ELSE"><span style="color:#55FF55;">$ELSE</span></a>
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> temp <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> <span style="color:#919191;">'      However, on 32 bit OSes, an OFFSET is only 4 bytes.</span>
    <a class="mw-redirect" href="$END_IF" title="$END IF"><span style="color:#55FF55;">$END IF</span></a> 
    <a href="MEMGET" title="MEMGET"><span style="color:#4593D8;">_MEMGET</span></a> m, m.OFFSET, temp <span style="color:#919191;">'Once we've sized our variable correctly, let's get it</span>
    <span style="color:#55FF55;">ConvertOffset&amp;&amp;</span> = temp <span style="color:#919191;">'   And then assign that long value to ConvertOffset&amp;&amp;</span>
    <a href="MEMFREE" title="MEMFREE"><span style="color:#4593D8;">_MEMFREE</span></a> m <span style="color:#919191;">'               Free the memblock</span>
    <a href="$CHECKING" title="$CHECKING"><span style="color:#55FF55;">$CHECKING</span></a>:<a href="ON" title="ON"><span style="color:#4593D8;">ON</span></a>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Explanation:</i> The above will print two numbers which should match.  These numbers will vary, as they're representations of where X is stored in memory, and that position is going to vary every time the program is run.  What it should illustrate, however, is a way to convert _OFFSET to _INTEGER64 values, which can sometimes be useful when trying to run calculations involving mem.SIZE, mem.TYPE, or mem.ELEMENTSIZE.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM_(function)" title="MEM (function)">_MEM (function)</a>, <a href="MEMELEMENT" title="MEMELEMENT">_MEMELEMENT</a></li>
<li><a href="MEMNEW" title="MEMNEW">_MEMNEW</a>, <a href="MEMCOPY" title="MEMCOPY">_MEMCOPY</a>, <a href="MEMFREE" title="MEMFREE">_MEMFREE</a></li>
<li><a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMPUT" title="MEMPUT">_MEMPUT</a>, <a href="MEMFILL" title="MEMFILL">_MEMFILL</a></li>
<li><a href="MEMIMAGE" title="MEMIMAGE">_MEMIMAGE</a>, <a href="MEMSOUND" title="MEMSOUND">_MEMSOUND</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192744
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.073 seconds
Real time usage: 0.096 seconds
Preprocessor visited node count: 1590/1000000
Post‐expand include size: 11828/2097152 bytes
Template argument size: 3896/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 3174/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   56.696      1 -total
 17.30%    9.811      1 Template:FixedStart
 11.06%    6.272     86 Template:Text
 10.72%    6.078    103 Template:Cl
  6.84%    3.876      1 Template:PageExamples
  5.37%    3.047      3 Template:CodeStart
  5.25%    2.976      7 Template:Cm
  3.83%    2.173      1 Template:OutputStart
  3.74%    2.122      3 Template:CodeEnd
  3.66%    2.074      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:175-0!canonical and timestamp 20240714192744 and revision id 8528.
 -->
</div>
</div>
</div>
</div>
</body>
</html>