<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_glTexCoord4sv - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-GlTexCoord4sv rootpage-GlTexCoord4sv skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_glTexCoord4sv</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_glTexCoord4sv</b> statement sets the current texture coordinates.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_glTexCoord4sv</a> const GLshort <i>*v</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>OpenGL is using its own set of variable types to describe its command parameters.</li>
<li>Use the following table to find the respective QB64 <a href="Variable_Types" title="Variable Types">Variable Types</a>.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">   Table 2: Relations between the OpenGL variable types vs. C/C++ and QB64.
 ┌──────────────┬────────────────┬──────────────────────────────────────────┐
 │    <b>OpenGL</b>    │     <b>C/C++</b>      │     <b>QB64</b>                                 │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLenum       │ unsigned int   │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a>                           │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLboolean    │ unsigned char  │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="BYTE" title="BYTE">_BYTE</a>                          │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLbitfield   │ unsigned int   │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a>                           │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLbyte       │ signed char    │ <a href="BYTE" title="BYTE">_BYTE</a>                                    │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLshort      │ short          │ <a href="INTEGER" title="INTEGER">INTEGER</a>                                  │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLint        │ int            │ <a href="LONG" title="LONG">LONG</a>                                     │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLsizei      │ int            │ <a href="LONG" title="LONG">LONG</a>                                     │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLubyte      │ unsigned char  │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="BYTE" title="BYTE">_BYTE</a>                          │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLushort     │ unsigned short │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="INTEGER" title="INTEGER">INTEGER</a>                        │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLuint       │ unsigned int   │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a>                           │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLfloat      │ float          │ <a href="SINGLE" title="SINGLE">SINGLE</a>                                   │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLclampf     │ float          │ <a href="SINGLE" title="SINGLE">SINGLE</a>                                   │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLdouble     │ double         │ <a href="DOUBLE" title="DOUBLE">DOUBLE</a>                                   │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLclampd     │ double         │ <a href="DOUBLE" title="DOUBLE">DOUBLE</a>                                   │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLvoid   <b>(1)</b> │ void           │ <a href="OFFSET" title="OFFSET">_OFFSET</a>(any fixed lenght string or <a href="BYTE" title="BYTE">_BYTE</a> │
 │              │                │         array element)                   │
 └──────────────┴────────────────┴──────────────────────────────────────────┘
 <b>Note:</b> If a parameter has an asterisk (*) in front, then it's a pointer to
       the designated OpenGL variable type, rather than a value of that type.
       Those must be passed using the <a href="OFFSET" title="OFFSET">_OFFSET</a>(...) notation.
 <b>E.g.</b>  GLuint *anyParam is actually the offset of a <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> (~&amp;)
       variable or array, which must be passed as <a href="OFFSET" title="OFFSET">_OFFSET</a>(anyVar~&amp;) or
       <a href="OFFSET" title="OFFSET">_OFFSET</a>(anyArr~&amp;()) respectively.
  <b>(1)</b>  This type is regularly only used for pointers (with asterisk (*)) to
       any byte sized memory data, hence <a href="BYTE" title="BYTE">_BYTE</a> or fixed length strings.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>OpenGL's documentation is available in several places, so we won't reproduce it here for another time.</li>
<li>The full description for this command can be found at <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexcoord4sv" rel="nofollow">Microsoft Docs</a> and is also valid for QB64 usage.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GL" title="GL">SUB _GL</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glvertex-functions" rel="nofollow">_glVertex</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714213546
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.038 seconds
Preprocessor visited node count: 27/1000000
Post‐expand include size: 6885/2097152 bytes
Template argument size: 2/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.536      1 -total
 32.95%    7.756      1 Template:OpenGLTypesPlugin
 11.66%    2.745      1 Template:PageSyntax
 10.59%    2.492      1 Template:Parameter
 10.43%    2.456      1 Template:PageParameters
 10.38%    2.444      1 Template:PageDescription
 10.18%    2.395      1 Template:PageNavigation
  9.99%    2.350      1 Template:PageSeeAlso
  9.90%    2.331      1 Template:FixedStart
  9.74%    2.293      1 Template:FixedEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1102-0!canonical and timestamp 20240714213546 and revision id 7065.
 -->
</div>
</div>
</div>
</div>
</body>
</html>