<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_glGetIntegerv - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-GlGetIntegerv rootpage-GlGetIntegerv skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_glGetIntegerv</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_glGetIntegerv</b> statement returns the value or values of a selected parameter.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_glGetIntegerv</a> GLenum <i>pname</i>, GLint <i>*params</i></dd></dl>
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
<li>The full description for this command can be found at <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgetintegerv" rel="nofollow">Microsoft Docs</a> and is also valid for QB64 usage.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GL" title="GL">SUB _GL</a></li>
<li><a href="GlAccum" title="GlAccum">_glAccum</a>, <a href="GlAlphaFunc" title="GlAlphaFunc">_glAlphaFunc</a>, <a href="GlBegin" title="GlBegin">_glBegin</a>, <a href="GlBlendFunc" title="GlBlendFunc">_glBlendFunc</a></li>
<li><a href="GlCallList" title="GlCallList">_glCallList</a>, <a href="GlClearAccum" title="GlClearAccum">_glClearAccum</a>, <a href="GlClearColor" title="GlClearColor">_glClearColor</a>, <a href="GlClearDepth" title="GlClearDepth">_glClearDepth</a></li>
<li><a href="GlClearIndex" title="GlClearIndex">_glClearIndex</a>, <a href="GlClearStencil" title="GlClearStencil">_glClearStencil</a>, <a href="GlClipPlane" title="GlClipPlane">_glClipPlane</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glcolor-functions" rel="nofollow">_glColor</a></li>
<li><a href="GlColorMask" title="GlColorMask">_glColorMask</a>, <a href="GlColorMaterial" title="GlColorMaterial">_glColorMaterial</a>, <a href="GlCullFace" title="GlCullFace">_glCullFace</a>, <a href="GlDepthFunc" title="GlDepthFunc">_glDepthFunc</a></li>
<li><a href="GlDepthMask" title="GlDepthMask">_glDepthMask</a>, <a href="GlDepthRange" title="GlDepthRange">_glDepthRange</a>, <a href="GlDrawBuffer" title="GlDrawBuffer">_glDrawBuffer</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gledgeflag-functions" rel="nofollow">_glEdgeFlag</a></li>
<li><a href="GlEnd" title="GlEnd">_glEnd</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glfog" rel="nofollow">_glFog</a>, <a href="GlFrontFace" title="GlFrontFace">_glFrontFace</a>, <a href="GlGetClipPlane" title="GlGetClipPlane">_glGetClipPlane</a></li>
<li><a href="GlGetError" title="GlGetError">_glGetError</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgetlight" rel="nofollow">_glGetLight</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgetmap" rel="nofollow">_glGetMap</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgetmaterial" rel="nofollow">_glGetMaterial</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgetpixelmap" rel="nofollow">_glGetPixelMap</a>, <a href="GlGetPolygonStipple" title="GlGetPolygonStipple">_glGetPolygonStipple</a>, <a href="GlGetString" title="GlGetString">_glGetString</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexenv" rel="nofollow">_glGetTexEnv</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexgen" rel="nofollow">_glGetTexGen</a>, <a href="GlGetTexImage" title="GlGetTexImage">_glGetTexImage</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexlevelparameter" rel="nofollow">_glGetTexLevelParameter</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexparameter" rel="nofollow">_glGetTexParameter</a></li>
<li><a href="GlHint" title="GlHint">_glHint</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glindex-functions" rel="nofollow">_glIndex</a>, <a href="GlIndexMask" title="GlIndexMask">_glIndexMask</a>, <a href="GlIsEnabled" title="GlIsEnabled">_glIsEnabled</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gllight-functions" rel="nofollow">_glLight</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gllightmodel-functions" rel="nofollow">_glLightModel</a>, <a href="GlLineStipple" title="GlLineStipple">_glLineStipple</a>, <a href="GlLineWidth" title="GlLineWidth">_glLineWidth</a></li>
<li><a href="GlListBase" title="GlListBase">_glListBase</a>, <a href="GlLogicOp" title="GlLogicOp">_glLogicOp</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glmap1" rel="nofollow">_glMap1</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glmap2" rel="nofollow">_glMap2</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glmapgrid-functions" rel="nofollow">_glMapGrid</a>, <a href="GlMatrixMode" title="GlMatrixMode">_glMatrixMode</a>, <a href="GlNewList" title="GlNewList">_glNewList</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glnormal-functions" rel="nofollow">_glNormal</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glpixelmap" rel="nofollow">_glPixelMap</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glpixelstore-functions" rel="nofollow">_glPixelStore</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glpixeltransfer" rel="nofollow">_glPixelTransfer</a>, <a href="GlPixelZoom" title="GlPixelZoom">_glPixelZoom</a></li>
<li><a href="GlPointSize" title="GlPointSize">_glPointSize</a>, <a href="GlPolygonMode" title="GlPolygonMode">_glPolygonMode</a>, <a href="GlPolygonStipple" title="GlPolygonStipple">_glPolygonStipple</a>, <a href="GlPushAttrib" title="GlPushAttrib">_glPushAttrib</a></li>
<li><a href="GlPushMatrix" title="GlPushMatrix">_glPushMatrix</a>, <a href="GlPushName" title="GlPushName">_glPushName</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glrasterpos-functions" rel="nofollow">_glRasterPos</a>, <a href="GlReadPixels" title="GlReadPixels">_glReadPixels</a></li>
<li><a href="GlScissor" title="GlScissor">_glScissor</a>, <a href="GlShadeModel" title="GlShadeModel">_glShadeModel</a>, <a href="GlStencilFunc" title="GlStencilFunc">_glStencilFunc</a>, <a href="GlStencilMask" title="GlStencilMask">_glStencilMask</a></li>
<li><a href="GlStencilOp" title="GlStencilOp">_glStencilOp</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexcoord-functions" rel="nofollow">_glTexCoord</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexenv-functions" rel="nofollow">_glTexEnv</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexgen-functions" rel="nofollow">_glTexGen</a></li>
<li><a href="GlTexImage1D" title="GlTexImage1D">_glTexImage1D</a>, <a href="GlTexImage2D" title="GlTexImage2D">_glTexImage2D</a>, <a href="GlViewport" title="GlViewport">_glViewport</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715033009
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 31/1000000
Post‐expand include size: 6899/2097152 bytes
Template argument size: 12/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.689      1 -total
 34.37%    6.767      1 Template:OpenGLTypesPlugin
 13.28%    2.615      2 Template:Parameter
 12.02%    2.366      1 Template:PageSyntax
 11.56%    2.277      1 Template:FixedStart
  9.94%    1.957      1 Template:PageDescription
  9.30%    1.830      1 Template:PageSeeAlso
  9.25%    1.821      1 Template:FixedEnd
  8.79%    1.730      1 Template:PageNavigation
  8.71%    1.714      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:925-0!canonical and timestamp 20240715033009 and revision id 6881.
 -->
</div>
</div>
</div>
</div>
</body>
</html>