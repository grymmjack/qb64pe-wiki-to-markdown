## Creating Icon Bitmaps
---

### The following program can be used to view Icon or Cursor images and save them as Bitmaps. When you answer Y the bitmap is saved with a black background so that it can be PUT using XOR on to the AND image. The AND image will be black and white if the image is irregularly shaped(not a full box image). It is placed first using PUT with the AND action or can be placed using _PUTIMAGE with the color white _ALPHA being set to 0. In that case, try just placing the XOR image with the color black 0 alpha with _SETALPHA .

#### SEE ALSO
* Creating Icons from Bitmaps
* Bitmaps , Icons and Cursors
* [_CLEARCOLOR](./_CLEARCOLOR.md)
* [_ALPHA](./_ALPHA.md) , [_ICON](./_ICON.md)
* SaveIcon32 (create icons from any image)
