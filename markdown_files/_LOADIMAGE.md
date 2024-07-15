<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_LOADIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LOADIMAGE rootpage-LOADIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_LOADIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_LOADIMAGE</b> function loads an image into memory and returns valid <a href="LONG" title="LONG">LONG</a> image handle values that are less than -1.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>handle&amp;</i> = <a class="mw-selflink selflink">_LOADIMAGE</a>(<i>fileName$</i>[, [<i>mode&amp;</i>][, <i>requirements$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>filename$</i> is literal or variable <a href="STRING" title="STRING">STRING</a> file name value.</li>
<li>Optional <i>mode&amp;</i> <a href="LONG" title="LONG">LONG</a> values can be:
<ul><li>32 = 32-bit image.</li>
<li>33 = 32-bit hardware image.</li>
<li>256 = 8-bit (256 color) image using the QB64-PE master palette.</li>
<li>257 = 8-bit (256 color) image using an adaptive palette.</li></ul></li>
<li>Optional <i>requirements$</i> <a href="STRING" title="STRING">STRING</a> values can be a combination of (<b>version 3.6.0 and up</b>):
<ul><li><b>HARDWARE</b>: Loads the image as a 32-bit hardware image. This can be used instead of mode <b>33</b> (above).</li>
<li><b>ADAPTIVE</b>: Loads the image as an 8-bit (256 color) image using an adaptive palette. This can be used instead of mode <b>257</b> (above).</li>
<li><b>MEMORY</b>: This will treat filename$ as a memory buffer containing the image file instead of a file name.</li>
<li><b>SXBR2</b>: Applies the Super-xBR 2x pixel scaler on the image.</li>
<li><b>MMPX2</b>: Applies the MMPX Style-Preserving 2x pixel scaler on the image.</li>
<li><b>HQ2XA</b>: Applies the High Quality Cartoon 2x pixel scaler on the image.</li>
<li><b>HQ2XB</b>: Applies the High Quality Complex 2x pixel scaler on the image.</li>
<li><b>HQ3XA</b>: Applies the High Quality Cartoon 3x pixel scaler on the image.</li>
<li><b>HQ3XB</b>: Applies the High Quality Complex 3x pixel scaler on the image.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Image file formats <b>JPG, PNG, TGA, BMP, PSD, GIF, HDR, PIC, PNM, PCX, SVG and QOI</b> are supported. A path can also be given.</li>
<li>The <i>mode&amp;</i> parameter can be 32, 33,256 or 257. Omit to use the current graphic screen settings.</li>
<li>Mode 33 images are <b>hardware</b> accelerated and are created using <a class="mw-selflink selflink">_LOADIMAGE</a> or <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a> (<b>version 1.000 and up</b>).</li>
<li>Mode 256 images are loaded using the QB64-PE master VGA palette. This is the same palette that is used for 256 color screens like <a href="SCREEN" title="SCREEN">SCREEN</a> 13.</li>
<li>Mode 257 images are loaded using an adaptive palette making these images look better than mode 256 when used with 32-bit color screens (<b>version 3.1.0 and up</b>).</li>
<li>Loaded images can be read invisibly using <a href="POINT" title="POINT">POINT</a>. Image coordinates start at 0 up to the <a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH</a> - 1 and <a href="HEIGHT" title="HEIGHT">_HEIGHT</a> - 1.</li>
<li>Images can be made into a program <a href="SCREEN" title="SCREEN">SCREEN</a> or page adopting the size and palette settings or placed using <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a>.</li>
<li>Returns -1 as an invalid handle if it can't load the image. Valid <a href="LONG" title="LONG">LONG</a> handle returns are less than -1 (<i>handle&amp;</i> &lt; -1).</li>
<li>Valid images only need to be loaded once. The handle can be used repeatedly until freed.</li>
<li><b>Images are not deallocated when the <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> they are created in ends. Free them with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a>.</b></li>
<li>Use the various pixel scalers to scale and load extremely low resolution (retro) graphics without blurring.</li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li>Some picture file images may not load when a <i>mode&amp;</i> value is designated. Try loading it without a <i>mode&amp;</i> designation.</li>
<li><b>It is important to free unused or discarded images with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a> to prevent CPU memory overflow errors.</b></li>
<li><b>In text-only <a href="SCREEN" title="SCREEN">SCREEN</a> 0, <i>mode&amp;</i> 32 must be specified.</b> When loading an <a href="ICON" title="ICON">_ICON</a> image use 32 for the <i>mode&amp;</i> too.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v0.800"><img alt="v0.800" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v0.800</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="all"><img alt="all" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>all</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Apix.png"><img alt="Apix.png" decoding="async" height="48" src="/qb64wiki/images/5/5f/Apix.png" width="48"/></a></div></div>
<div class="gallerytext">
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Win.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/29/Win.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
</ul>
<ul><li>Mode 33 was added in <b>QB64 v1.0</b>, which makes it also available in <b>all QB64-PE</b> versions.</li>
<li>Mode 257 was added in <b>QB64-PE v3.1.0</b>, hence it's <b>not available</b> in the original <b>QB64</b> versions.</li>
<li>In <b>QB64-PE v3.6.0</b> this function got a new optional parameter <i>requirements$</i> and the ability to load image files from memory.</li>
<li>SVG and QOI support was added in <b>QB64-PE v3.9.0</b>.</li>
<li>Pixel scaler support was added in <b>QB64-PE v3.9.0</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>To display an image in 32-bit color using its resolution as a program screen.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">i&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_LOADIMAGE</span></a>("mypic.jpg", 32)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> i&amp;
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd><a href="DRAW" title="DRAW">DRAWing</a> and rotating an image 360 degrees using Turn Angle. <a href="POINT" title="POINT">POINT</a> is used to read the invisible image source.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 32)
img&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_LOADIMAGE</span></a>("QB64.PNG")                           'use any 24/32 bit image
wide% = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(img&amp;): deep% = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(img&amp;)
TLC$ = "BL" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(wide% \ 2) + "BU" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(deep% \ 2)  'start draw at top left corner
RET$ = "BD BL" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(wide%)                            'return to left side of image
<a href="SOURCE" title="SOURCE"><span style="color:#4593D8;">_SOURCE</span></a> img&amp;
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> 0
DO
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> angle% = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 360 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> 15
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "BM400, 300" + "TA=" + <a href="VARPTR$" title="VARPTR$"><span style="color:#4593D8;">VARPTR$</span></a>(angle%) + TLC$
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> deep% - 1
      <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> x = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> wide% - 1
        <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "C" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(<a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(x, y)) + "R1"            'color and DRAW each pixel
      <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
      <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> RET$
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>                         'NOTE: CPU usage will be HIGH!
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &gt; ""
</pre>
</td></tr></tbody></table>
<dl><dt>Example 3</dt>
<dd>Load and scale an image from memory and display it on the screen.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Bee&amp; <span style="color:#919191;">'                                               the image file</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> cx%, cy% <span style="color:#919191;">'                                           center x,y coordinate for image</span>
<a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> Data_tbee0_png_2314
Bee&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<span style="color:#55FF55;">LoadResource</span>, <span style="color:#F580B1;">32</span>, <span style="color:#FFB100;">"memory, hq3xa"</span>) <span style="color:#919191;">'   load image file from memory and scale it using a pixel scaler</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>) <span style="color:#919191;">'                         enter a graphics screen</span>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">127</span>, <span style="color:#F580B1;">127</span>, <span style="color:#F580B1;">127</span>) <span style="color:#919191;">'                            clear the screen with gray</span>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">15</span> <span style="color:#919191;">'                                           position text cursor</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"An image loaded into memory and placed on the screen."</span>
cx% = (<span style="color:#F580B1;">640</span> - <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(Bee&amp;)) \ <span style="color:#F580B1;">2</span> <span style="color:#919191;">'                         calculate x center position</span>
cy% = (<span style="color:#F580B1;">480</span> - <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(Bee&amp;)) \ <span style="color:#F580B1;">2</span> <span style="color:#919191;">'                        calculate y center position</span>
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (cx%, cy%), Bee&amp; <span style="color:#919191;">'                             place image onto center of screen</span>
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> <span style="color:#919191;">'                                                  wait for key stroke</span>
<a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> Bee&amp; <span style="color:#919191;">'                                        remove image from memory</span>
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a> <span style="color:#919191;">'                                                 return to OS</span>
Data_tbee0_png_2314:
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">2314</span>,<span style="color:#F580B1;">2988</span>,<span style="color:#F580B1;">-1</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> eJx1VmdUU9kWDiihKDGEariKEKzUoV4FHWMgCYj0iVIVKeIocgNKiSCIkQuEZGBQRARxgCdNLNRQFYgE
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> pGMARYOSCCqiSAkgUia8f28t3zrfPvtb31lnn732+bF3oqM9SV4OK4dAIORtyFbOYg+vmwxSvFt+tF0/
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> QJ4+SrJCrK2vew0FaWJFFiK7hSIQKM66SdzUQakjEDLFNlZ414jhr3wPO6XjAPJ7V4D6yajg4eHaeQx/
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">7iqd7Pt2sNckOvBk8pNWtXNM5hOOmguzyMk3YSFCVqEeaS25T0YyLjYpFk23flFcKIp3biLzZgI1jjUe</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> yriNaumc9Oye7DTKab9l/cprfEaYtZZ121hdEn1arRTCGXKa0NIEYDP1f0nLr0Qx+aVINfylyEl101GU
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> w9uirxhQ0dLryI+G/ZemdqAEO1Al7V1d1hcu6C/zPjBovyt8IQIc/DpY4Qlp2/JEw12huF5G4dIR3owi
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> CUu1ynOSlUDYLR7AMuNAyRAlDJOowCSObfNDwjM1trp4sFhhnrhQq0Ot/qKLPPCCWpe3uXr4aOp5PXxZ
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">5UZfnM1b9kUlb0FK2MMQWOdqYZ7Isu6wlYBN</span>/bynlfj3TFXDgHfSm23+<span style="color:#F580B1;">7JeR2PC6boF3</span>+E5L7jR7TXL7
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> /IAAPxW5PBCNKoIqstpJwbM+<span style="color:#F580B1;">2lhGLx9CD33Z1PtHOCLb9Of7</span>+XjKpCvisINvav3sf3KKfPbEjLw8of10
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> EIW26HjrVr7F65I01NCI4MtLpwbqHhGHEEdySBRecVDePneX29LobvntaWzFezUsm15QnWmYUS+TCh7o
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> nsJfHtBnX+KdohNKRI5rnShUnchaLF3MerchFUSmqU7PURTjkfp4kDV6+fhvJtDWMCrC8HpeaYi0u05V
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> kx5wkGkdwuPHY+BaC6en3fJAqfKbXkrNhgAI8ZgpnLI4bhg1tQ8QRqy+xxK/VTftRZXrwfS8MbtDD28E
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> WxczDVaOVireEMV5f/WhE3R21aIjXycPCm1/UMTJw8qAvTtKltu2YmYZA8lXQfURPNlHVE/<span style="color:#F580B1;">9N3Hj</span>/ccg
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> dZiCnzBjiSnbs0rKWxgxXaiYDiWjwpocwExbM4GgXR4yCrsHtwSi7bbAab8xGbvN7xX54Zbpvhcfb7oP
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">1Uf1b</span>+gDHwwCNBCbNJS3ujgFGbXlSx3ZFKuitPuap4gbQyJM0xKeaeaOOwojfuRLx4Pe8qJmeSBXnBSJ
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> /<span style="color:#F580B1;">6Sy8GAZUgsi96xVhzwEGg5wUKxh3DnH8PN6VgIob2z9xqN42j</span>+JQlH5IT8M64tIqnB/BXbgemQmuZOn
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">5o67R4PZASPHE3NrDbeYwhQhLRpPHI1YebBFCCXLL</span>+AUqTe+eSZPNFu6bvO8HiqlwySacJUf2kOFXAse
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">2K38wGqg6Y9C</span>/U7C5+<span style="color:#F580B1;">7nWxN9z7PX</span>+ONYdZvmICD3HKvW95zEKUlW0gYdKGwt5CU4Yn87qdrlvpaSXPvJ
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> krVgFe7rlQ4n6qnnGwEEXQiVjDsK1NRttPTA/oEQMmg/<span style="color:#F580B1;">5RU</span>/c/CoU9VlWdtw/dairwzHsiBN+w8Gh6cH
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> f8ywzK4RaBfEDEx9itj5RkXAm7few69R86+<span style="color:#F580B1;">7dS</span>+qxzlrpM5OlXS/Crja8s+AfEZi2U0ZJZZd6f7kWmUc
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> MKFP7H6zsNrDwW2p0XmS1MK8sDPIlHSARcniAbc6qmSC9lfEt7mMOqo8Fpf4LH/<span style="color:#F580B1;">5RGggKzSZqR09FIIm</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> LbmznqRqO6NynmInsl35SRf9bxmlkjmuDQqJgd4ef9Z5nN3jPWUBTDQZuJzxJ0nXfTBv/xCnhMBEGnOt
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> y0W9beM1qbKPKuMI/JBFCXiO9Cjc/nm/CLCnkk1JuU/azPXgvqLIBpcf3tVAYquWpimp2EVUZaB4Q+<span style="color:#F580B1;">64</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> hR5MBigeLPGb21EF/KS2dEKzT+WYo2rm2Zpni+LPrb8y+FEWVQeX0aSKtqN0pM5e8hlhswdCMpo0v6qf
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">9IzW10vW8EDhAJrq7KfswtmZwJ3KKIUdnjnVWnr5d0xhL2ACb2gMZm2Oq7lKcAtNQKYO2hxz7tAszRri</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> J71MwGpWMnB9J7SrgbTTrXfUwcm7EQxiXoKVVvphcs/CEucOhpufifqsCoxCr1xv5X5zbx59HAzZvagp
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">874bkRZWhYFv0lt8fhyst5w2K9rtfLkv5NX</span>+YzkTSo2qeqQdAa8ZHM2Vjvb2pqz9oSlpadcmJ8/<span style="color:#F580B1;">7</span>+ftr
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> qjCY6pPYgybqeXCAMBJvdlfVr+PRyplFB+<span style="color:#F580B1;">2ZgNyYoM2J9bc</span>/LYk2Vawtb3VX6To8u/y5cG3UlxdlHtT8
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> /oSuCoFCUSkrLx97p/EXd2xBORHnWH0KbWqquf0v35H6yASuMB4c8fT6pEYaM9fIXS5ZcBGkpJN4PPqz
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> kZwWXZSO8esKOds+sFOlwr0jSEU6eESSngxlSPiYdHQFAZSAV0U5vvRr4fNOVTsqf9p1lZkzCH4Smfvs
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">010OdjSWh2kslzkYCeYJlKli3NInTmcfQ</span>/<span style="color:#F580B1;">0LHogzL8a23inZxL20l8a3fZfpxq7Rj280LU9Z</span>/Oo11D/d
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">8THQa2bvw2WTDcdmC</span>/JGuQ6OP1dMXGN+KuxrXH1mhBb8t5es47u5nI66V20ALhvkhZ4p1TWm5m+Fb59l
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> En83Ni5MnxBxRl2AiRL2jRj+C1Lp1NHwzSY018ZH2R4EBbjFw8GjhntrcLYBu7GcxvUtHYTBje8Na+/c
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> GwJvDGVjYOmM5LDYgbi58Vo15Opiv7NTMQwOlE371lseqhdhSLu2V2GkqXYXAErPiyUJ0n0tTZQgIwrs
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> vFIW9wa0MjCmgov0XSVDl05s+<span style="color:#F580B1;">2xivHT24xKmYVpN8B0ND7YV0uiuP</span>/YwY/dpVBJtS4H7GBgWXU/rcaMO
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">0</span>/JDoxNaFs+f25NGTThR8EyYcqjUjdMamtQsk5jgPzu72+WnCrEXWlQgt7JS7JGALjna/dWf0VHxfQtG
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">0YcZIKBUQIE2</span>+t+RQsI3O2SzPVdJgEQxPk4OlwLOxeYveaOrXXb8smk3/Z+JgAC8lUkOW93AGx2tePu3
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">9ax4lEHYWNtbPTxyKu5fF0s</span>/<span style="color:#F580B1;">3Q</span>==
<span style="color:#919191;">' Convert a base64 string to a normal string</span>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">DecodeBase64$</span> (s <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>)
    <a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> BASE64_CHARACTERS = <span style="color:#FFB100;">"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"</span>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> buffer, result
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> i
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a> char1, char2, char3, char4
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(s) <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> <span style="color:#F580B1;">4</span>
        char1 = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(BASE64_CHARACTERS, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(s, i))) - <span style="color:#F580B1;">1</span>
        char2 = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(BASE64_CHARACTERS, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(s, i + <span style="color:#F580B1;">1</span>))) - <span style="color:#F580B1;">1</span>
        char3 = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(BASE64_CHARACTERS, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(s, i + <span style="color:#F580B1;">2</span>))) - <span style="color:#F580B1;">1</span>
        char4 = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(BASE64_CHARACTERS, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(s, i + <span style="color:#F580B1;">3</span>))) - <span style="color:#F580B1;">1</span>
        buffer = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="SHL" title="SHL"><span style="color:#4593D8;">_SHL</span></a>(char1, <span style="color:#F580B1;">2</span>) <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> <a href="SHR" title="SHR"><span style="color:#4593D8;">_SHR</span></a>(char2, <span style="color:#F580B1;">4</span>)) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="SHL" title="SHL"><span style="color:#4593D8;">_SHL</span></a>(char2 <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">15</span>, <span style="color:#F580B1;">4</span>) <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> <a href="SHR" title="SHR"><span style="color:#4593D8;">_SHR</span></a>(char3, <span style="color:#F580B1;">2</span>)) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="SHL" title="SHL"><span style="color:#4593D8;">_SHL</span></a>(char3 <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">6</span>) <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> char4)
        result = result + buffer
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <span style="color:#919191;">' Remove padding</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(s, <span style="color:#F580B1;">2</span>) = <span style="color:#FFB100;">"=="</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        result = <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(result, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(result) - <span style="color:#F580B1;">2</span>)
    <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(s, <span style="color:#F580B1;">1</span>) = <span style="color:#FFB100;">"="</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        result = <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(result, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(result) - <span style="color:#F580B1;">1</span>)
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <span style="color:#55FF55;">DecodeBase64</span> = result
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
<span style="color:#919191;">' Loads a binary file encoded with Bin2Data</span>
<span style="color:#919191;">' Usage:</span>
<span style="color:#919191;">'   1. Encode the binary file with Bin2Data</span>
<span style="color:#919191;">'   2. Include the file or it's contents</span>
<span style="color:#919191;">'   3. Load the file like so:</span>
<span style="color:#919191;">'       Restore label_generated_by_bin2data</span>
<span style="color:#919191;">'       Dim buffer As String</span>
<span style="color:#919191;">'       buffer = LoadResource   ' buffer will now hold the contents of the file</span>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">LoadResource$</span>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> ogSize, resize
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a> isCompressed
    <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> ogSize, resize, isCompressed <span style="color:#919191;">' read the header</span>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> buffer, result
    <span style="color:#919191;">' Read the whole resource data</span>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(result) &lt; resize
        <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> buffer
        result = result + buffer
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
    <span style="color:#919191;">' Decode the data</span>
    buffer = <span style="color:#55FF55;">DecodeBase64</span>(result)
    <span style="color:#919191;">' Expand the data if needed</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> isCompressed <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        result = <a href="INFLATE$" title="INFLATE$"><span style="color:#4593D8;">_INFLATE$</span></a>(buffer, ogSize)
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        result = buffer
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <span style="color:#55FF55;">LoadResource</span> = result
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 4</dt>
<dd>Load SVG vector graphics data from memory and display it on the screen.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="$RESIZE" title="$RESIZE"><span style="color:#55FF55;">$RESIZE</span></a>:<a class="mw-redirect" href="SMOOTH" title="SMOOTH"><span style="color:#4593D8;">SMOOTH</span></a>
<a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> svg_data
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> svg, buffer
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> buffer
    svg = svg + buffer
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP WHILE</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(buffer) &gt; <span style="color:#F580B1;">0</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> img <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: img = <a class="mw-selflink selflink"><span style="color:#4593D8;">_LOADIMAGE</span></a>(svg, <span style="color:#F580B1;">32</span>, <span style="color:#FFB100;">"memory"</span>)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(img) \ <span style="color:#F580B1;">2</span>, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(img) \ <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">32</span>)
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , img
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
svg_data:
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"&lt;svg xmlns='http://www.w3.org/2000/svg' width='1000pt' height='1000pt' viewBox='0 0 1000 1000'&gt;&lt;g fill='#201701'"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"&gt;&lt;path d='M107 94c-3-1 2-4 2-1l-2 1ZM96 672h35l24 168 220-43 4 21-255 42-28-188ZM521 768l41-8 5 25c0 2-3 3-4 3l-"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"36 6-6-26Z' opacity='.1'/&gt;&lt;/g&gt;&lt;g fill='#020092'&gt;&lt;path d='m107 94 2-1 683 134 76 328 2 7 23 101-176 35-3-5-24-104"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">" 108-11 14 65 59-9-40-168h-60l17 78-84 7-18-82c0-1 0-3-2-2h-21l-17-71 169 7-12-54-26-1c-5-16-8-32-11-49 9 1 17 3"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">" 26 3l-12-53-220-38 29 146c-25-3-50-9-74-14l-28-144-329-57 20 134c-15-1-30-5-46-8v-1L107 94Z'/&gt;&lt;path d='m284 200"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">" 140 22 6 33-25-2c4 23 9 46 12 70l-116-23h-1l-16-100ZM640 255l90 13 7 34-85-11c-2 0-5 0-5-3l-7-33ZM137 300l46 8 "</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"10 69 31 1c3 28 9 56 13 85l80 5 8 2-120 1 3 22-43-2-28-191ZM305 330l77 13c2 0 4 2 4 4-26 0-53-3-79-4l-2-13ZM656 "</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"330l89 8 9 39-89-5-9-42ZM519 368c8-1 16 2 24 3l50 8 4 15c11 1 23 0 35 2l7 33-22-2 9 40h-16l9 44c-20-1-41-1-61-3-"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"6 0-12 0-18-2l31-1-3-17 38 3c-1-11-4-21-7-31-24-2-48-6-72-7l3 15-60 1c-5-27-12-54-15-81l59 3 6 28 72 9-5-27-63-9"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"-5-24ZM325 425l77 1 8 43-77 1c-3-15-7-30-8-45Z'/&gt;&lt;/g&gt;&lt;path fill='#00bbfd' d='m158 142 329 57 28 144 4 25 5 24-10"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"-1-59-3-27-1 7 39h-33l-77-1-7-43-94-4-31-1-10-69-5-32-20-134m126 58 16 100h1c0 10 3 20 4 30l2 13c26 1 53 4 79 4l"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"36 3-5-27c-3-24-8-47-12-70l25 2-6-33-140-22Z'/&gt;&lt;path fill='#037efe' d='m560 211 220 38 12 53c-9 0-17-2-26-3 3 17"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">" 6 33 11 49l26 1 12 54-169-7h-14c-12-2-24-1-35-2l-4-15-4-22-29-146m80 44 7 33c0 3 3 3 5 3l85 11-7-34-90-13m16 75"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">" 9 42 89 5-9-39-89-8Z'/&gt;&lt;g fill='#070636'&gt;&lt;path d='m71 256 61 11v1c2 11 4 21 4 32l-23-4 29 195c8 1 16-2 23 3l11 "</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"75h-24c7 38 12 76 17 114l16 106 22-4 2 13 446-88c5 2 10 0 14 0l35-6v-4l12-2c2 10 6 20 7 31a19145 19145 0 0 0-202"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">" 39l-146 29-220 43-24-168-37-255-23-161ZM868 555c2 2 2 5 2 7l-2-7Z' opacity='.4'/&gt;&lt;/g&gt;&lt;g fill='#030173'&gt;&lt;path d="</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"'M132 268c16 3 31 7 46 8l5 32-46-8h-1c0-11-2-21-4-32ZM301 300l116 23 5 27-36-3c0-2-2-4-4-4l-77-13c-1-10-4-20-4-3"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"0ZM515 343c24 5 49 11 74 14l4 22-50-8c-8-1-16-4-24-3l-4-25ZM224 378l94 4 7 43c1 15 5 30 8 45h-8l-8-2-80-5c-4-29-"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"10-57-13-85ZM428 387l27 1c3 27 10 54 15 81h-60l-8-43h33l-7-39ZM514 391l10 1 63 9 5 27-72-9-6-28ZM632 396h14l17 7"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"1h-37l-9-40 22 2-7-33ZM527 453c24 1 48 5 72 7 3 10 6 20 7 31l-38-3-4-20h-34l-3-15ZM165 491l43 2 37 243 359-59-22"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"-115c-79 5-157 12-236 18l-11-67 205-7c6 2 12 2 18 2 20 2 41 2 61 3l17 84 54-6 24 104 3 5h-1l-12 2-49 10-446 88-2"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"-13-31-216-11-75v-3Z'/&gt;&lt;path d='m491 609 6-1 8 44-143 19-8-47 137-15Z'/&gt;&lt;/g&gt;&lt;path fill='#013f59' d='m113 296 23 "</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"4h1l28 191v3c-7-5-15-2-23-3l-29-195Z' opacity='.4'/&gt;&lt;path fill='#000314' d='M26 404c23 3 46 9 68 13l37 255H96l28"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">" 188 255-42-4-21 146-29 6 26 36-6c1 0 4-1 4-3l-5-25 11-2 11 50-23 5-441 86c-7 2-14 4-22 4L26 404Z' opacity='.1'/"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"&gt;&lt;path fill='#f87d03' d='M771 466h60l40 168-59 9-14-65-108 11-54 6-17-84-9-44h74c2-1 2 1 2 2l18 82 84-7-17-78Z'/"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"&gt;&lt;path fill='#febd04' d='m470 469 60-1h34l4 20 3 17-31 1-205 7 11 67c79-6 157-13 236-18l22 115-359 59-37-243-3-2"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"2 120-1h8l77-1h60m21 140-137 15 8 47 143-19-8-44-6 1Z'/&gt;&lt;g fill='#5d470f'&gt;&lt;path d='M152 569h24l31 216-22 4-16-10"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">"6c-5-38-10-76-17-114ZM655 710l49-10v4l-35 6c-4 0-9 2-14 0Z' opacity='.4'/&gt;&lt;/g&gt;&lt;/svg&gt;"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#FFB100;">""</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h3><span class="mw-headline" id="More_examples">More examples</span></h3>
<ul><li><a href="Program_ScreenShots" title="Program ScreenShots">Program ScreenShots</a></li>
<li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="ThirtyTwoBit_SUB" title="ThirtyTwoBit SUB">ThirtyTwoBit SUB</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a>, <a href="ICON" title="ICON">_ICON</a></li>
<li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a>, <a href="MAPTRIANGLE" title="MAPTRIANGLE">_MAPTRIANGLE</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a></li>
<li><a href="PRINTIMAGE" title="PRINTIMAGE">_PRINTIMAGE</a> (printer)</li>
<li><a href="PALETTECOLOR_(function)" title="PALETTECOLOR (function)">_PALETTECOLOR (function)</a>, <a href="COPYPALETTE" title="COPYPALETTE">_COPYPALETTE</a>, <a href="ICON" title="ICON">_ICON</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="SAVEIMAGE" title="SAVEIMAGE">_SAVEIMAGE</a></li>
<li><a href="Hardware_images" title="Hardware images">Hardware images</a></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a>, <a href="Icons_and_Cursors" title="Icons and Cursors">Icons and Cursors</a>, <a href="GIF_Images" title="GIF Images">GIF Images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714181406
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.138 seconds
Real time usage: 0.154 seconds
Preprocessor visited node count: 3570/1000000
Post‐expand include size: 20185/2097152 bytes
Template argument size: 6047/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 7031/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   82.390      1 -total
 13.68%   11.272    219 Template:Cl
 10.13%    8.346    134 Template:Text
  3.38%    2.785      1 Template:Cm
  3.16%    2.606      2 Template:Small
  2.94%    2.425      1 Template:PageDescription
  2.89%    2.379      1 Template:PageSyntax
  2.79%    2.296     14 Template:Parameter
  2.71%    2.235      1 Template:PageSeeAlso
  2.71%    2.234      1 Template:PageAvailability
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:170-0!canonical and timestamp 20240714181406 and revision id 8660.
 -->
</div>
</div>
</div>
</div>
</body>
</html>