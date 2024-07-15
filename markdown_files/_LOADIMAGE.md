# _LOADIMAGE
> The _LOADIMAGE function loads an image into memory and returns valid LONG image handle values that are less than -1.

## SYNTAX
`handle& = _LOADIMAGE ( fileName$ [, [ mode& ][, requirements$ ]])`

## PARAMETERS
* filename$ is literal or variable [STRING](STRING.md) file name value.
* Optional mode& [LONG](LONG.md) values can be: 32 = 32-bit image. 33 = 32-bit hardware image. 256 = 8-bit (256 color) image using the QB64-PE master palette. 257 = 8-bit (256 color) image using an adaptive palette.
	* 32 = 32-bit image.
	* 33 = 32-bit hardware image.
	* 256 = 8-bit (256 color) image using the QB64-PE master palette.
	* 257 = 8-bit (256 color) image using an adaptive palette.
* 32 = 32-bit image.
* 33 = 32-bit hardware image.
* 256 = 8-bit (256 color) image using the QB64-PE master palette.
* 257 = 8-bit (256 color) image using an adaptive palette.
* Optional requirements$ [STRING](STRING.md) values can be a combination of ( version 3.6.0 and up ): HARDWARE : Loads the image as a 32-bit hardware image. This can be used instead of mode 33 (above). ADAPTIVE : Loads the image as an 8-bit (256 color) image using an adaptive palette. This can be used instead of mode 257 (above). MEMORY : This will treat filename$ as a memory buffer containing the image file instead of a file name. SXBR2 : Applies the Super-xBR 2x pixel scaler on the image. MMPX2 : Applies the MMPX Style-Preserving 2x pixel scaler on the image. HQ2XA : Applies the High Quality Cartoon 2x pixel scaler on the image. HQ2XB : Applies the High Quality Complex 2x pixel scaler on the image. HQ3XA : Applies the High Quality Cartoon 3x pixel scaler on the image. HQ3XB : Applies the High Quality Complex 3x pixel scaler on the image.
	* HARDWARE : Loads the image as a 32-bit hardware image. This can be used instead of mode 33 (above).
	* ADAPTIVE : Loads the image as an 8-bit (256 color) image using an adaptive palette. This can be used instead of mode 257 (above).
	* MEMORY : This will treat filename$ as a memory buffer containing the image file instead of a file name.
	* SXBR2 : Applies the Super-xBR 2x pixel scaler on the image.
	* MMPX2 : Applies the MMPX Style-Preserving 2x pixel scaler on the image.
	* HQ2XA : Applies the High Quality Cartoon 2x pixel scaler on the image.
	* HQ2XB : Applies the High Quality Complex 2x pixel scaler on the image.
	* HQ3XA : Applies the High Quality Cartoon 3x pixel scaler on the image.
	* HQ3XB : Applies the High Quality Complex 3x pixel scaler on the image.
* HARDWARE : Loads the image as a 32-bit hardware image. This can be used instead of mode 33 (above).
* ADAPTIVE : Loads the image as an 8-bit (256 color) image using an adaptive palette. This can be used instead of mode 257 (above).
* MEMORY : This will treat filename$ as a memory buffer containing the image file instead of a file name.
* SXBR2 : Applies the Super-xBR 2x pixel scaler on the image.
* MMPX2 : Applies the MMPX Style-Preserving 2x pixel scaler on the image.
* HQ2XA : Applies the High Quality Cartoon 2x pixel scaler on the image.
* HQ2XB : Applies the High Quality Complex 2x pixel scaler on the image.
* HQ3XA : Applies the High Quality Cartoon 3x pixel scaler on the image.
* HQ3XB : Applies the High Quality Complex 3x pixel scaler on the image.


## DESCRIPTION
* Image file formats JPG, PNG, TGA, BMP, PSD, GIF, HDR, PIC, PNM, PCX, SVG and QOI are supported. A path can also be given.
* The mode& parameter can be 32, 33,256 or 257. Omit to use the current graphic screen settings.
* Mode 33 images are hardware accelerated and are created using [_LOADIMAGE](_LOADIMAGE.md) or [_COPYIMAGE](_COPYIMAGE.md) ( version 1.000 and up ).
* Mode 256 images are loaded using the QB64-PE master VGA palette. This is the same palette that is used for 256 color screens like [SCREEN](SCREEN.md) 13.
* Mode 257 images are loaded using an adaptive palette making these images look better than mode 256 when used with 32-bit color screens ( version 3.1.0 and up ).
* Loaded images can be read invisibly using [POINT](POINT.md) . Image coordinates start at 0 up to the [_WIDTH](_WIDTH.md) - 1 and [_HEIGHT](_HEIGHT.md) - 1.
* Images can be made into a program [SCREEN](SCREEN.md) or page adopting the size and palette settings or placed using [_PUTIMAGE](_PUTIMAGE.md) .
* Returns -1 as an invalid handle if it can't load the image. Valid [LONG](LONG.md) handle returns are less than -1 ( handle& < -1).
* Valid images only need to be loaded once. The handle can be used repeatedly until freed.
* Images are not deallocated when the [SUB](SUB.md) or [FUNCTION](FUNCTION.md) they are created in ends. Free them with [_FREEIMAGE](_FREEIMAGE.md) .
* Use the various pixel scalers to scale and load extremely low resolution (retro) graphics without blurring.


## EXAMPLES

```vb
i& = _LOADIMAGE("mypic.jpg", 32)
SCREEN i&
```

* Program ScreenShots
* SaveImage [SUB](SUB.md)
* ThirtyTwoBit [SUB](SUB.md)

```vb
i& = _LOADIMAGE("mypic.jpg", 32)
SCREEN i&
```

* [_FREEIMAGE](_FREEIMAGE.md) , [_ICON](_ICON.md)
* [_PUTIMAGE](_PUTIMAGE.md) , [_MAPTRIANGLE](_MAPTRIANGLE.md)
* [_NEWIMAGE](_NEWIMAGE.md) , [_COPYIMAGE](_COPYIMAGE.md)
* [_PRINTIMAGE](_PRINTIMAGE.md) (printer)
* [_PALETTECOLOR](_PALETTECOLOR.md) (function) , [_COPYPALETTE](_COPYPALETTE.md) , [_ICON](_ICON.md)
* [SCREEN](SCREEN.md)
* [_SAVEIMAGE](_SAVEIMAGE.md)
* Hardware images
* Bitmaps , Icons and Cursors , GIF Images

```vb
i& = _LOADIMAGE("mypic.jpg", 32)
SCREEN i&
```



## MORE EXAMPLES
* Program ScreenShots
* SaveImage [SUB](SUB.md)
* ThirtyTwoBit [SUB](SUB.md)


# SEE ALSO
* [_FREEIMAGE](_FREEIMAGE.md) , [_ICON](_ICON.md)
* [_PUTIMAGE](_PUTIMAGE.md) , [_MAPTRIANGLE](_MAPTRIANGLE.md)
* [_NEWIMAGE](_NEWIMAGE.md) , [_COPYIMAGE](_COPYIMAGE.md)
* [_PRINTIMAGE](_PRINTIMAGE.md) (printer)
* [_PALETTECOLOR](_PALETTECOLOR.md) (function) , [_COPYPALETTE](_COPYPALETTE.md) , [_ICON](_ICON.md)
* [SCREEN](SCREEN.md)
* [_SAVEIMAGE](_SAVEIMAGE.md)
* Hardware images
* Bitmaps , Icons and Cursors , GIF Images

