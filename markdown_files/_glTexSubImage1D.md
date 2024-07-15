<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_glTexSubImage1D - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-GlTexSubImage1D rootpage-GlTexSubImage1D skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_glTexSubImage1D</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_glTexSubImage1D</b> statement specifies a portion of an existing one-dimensional texture image. You cannot define a new texture with <b>_glTexSubImage1D</b>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_glTexSubImage1D</a> GLenum <i>target</i>, GLint <i>level</i>, GLint <i>xoffset</i>, GLsizei <i>width</i>, GLenum <i>format</i>, GLenum <i>type</i>, const GLvoid <i>*pixels</i></dd></dl>
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
<li>The full description for this command can be found at <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexsubimage1d" rel="nofollow">Microsoft Docs</a> and is also valid for QB64 usage.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GL" title="GL">SUB _GL</a></li>
<li><a href="GlCopyTexImage1D" title="GlCopyTexImage1D">_glCopyTexImage1D</a>, <a href="GlCopyTexImage2D" title="GlCopyTexImage2D">_glCopyTexImage2D</a>, <a href="GlCopyTexSubImage1D" title="GlCopyTexSubImage1D">_glCopyTexSubImage1D</a>, <a href="GlCopyTexSubImage2D" title="GlCopyTexSubImage2D">_glCopyTexSubImage2D</a></li>
<li><a href="GlDrawPixels" title="GlDrawPixels">_glDrawPixels</a>, <a href="GlEnable" title="GlEnable">_glEnable</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glfog" rel="nofollow">_glFog</a>, <a href="GlGetTexImage" title="GlGetTexImage">_glGetTexImage</a></li>
<li><a href="GlIsEnabled" title="GlIsEnabled">_glIsEnabled</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glpixelstore-functions" rel="nofollow">_glPixelStore</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glpixeltransfer" rel="nofollow">_glPixelTransfer</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexenv-functions" rel="nofollow">_glTexEnv</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexgen-functions" rel="nofollow">_glTexGen</a>, <a href="GlTexImage1D" title="GlTexImage1D">_glTexImage1D</a>, <a href="GlTexImage2D" title="GlTexImage2D">_glTexImage2D</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexparameter-functions" rel="nofollow">_glTexParameter</a></li>
<li><a href="GlTexSubImage2D" title="GlTexSubImage2D">_glTexSubImage2D</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714212448
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.046 seconds
Preprocessor visited node count: 51/1000000
Post‐expand include size: 6947/2097152 bytes
Template argument size: 40/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.531      1 -total
 26.90%    6.062      1 Template:OpenGLTypesPlugin
 14.32%    3.227      1 Template:PageSyntax
 12.65%    2.850      1 Template:PageNavigation
 12.64%    2.849      7 Template:Parameter
 10.47%    2.358      1 Template:PageParameters
  8.87%    1.998      1 Template:PageSeeAlso
  8.81%    1.984      1 Template:PageDescription
  8.08%    1.820      1 Template:FixedEnd
  8.05%    1.815      1 Template:FixedStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:734-0!canonical and timestamp 20240714212448 and revision id 7083.
 -->
</div>
</div>
</div>
</div>
</body>
</html>