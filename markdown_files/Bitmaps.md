## Bitmaps
---

### 

#### SYNTAX

`In BINARY files, numerical data can also be converted to ASCII characters by using MKI$ for INTEGERs or MKL$ for LONG values. GET can convert _MK$ values to numerical values and PUT can convert numerical values to STRING values. When the LONG MKL$ color values are PUT into bitmaps the Red value is placed as the third ASCII character and the blue becomes the first character. That not only happens to the BGR palette data, but the BGR 24 bit image color values PUT using the left 3 bytes.`

#### SEE ALSO
* [_LOADIMAGE](./_LOADIMAGE.md) , [_PUTIMAGE](./_PUTIMAGE.md)
* [SCREEN](./SCREEN.md)
* [TYPE](./TYPE.md) , [_ICON](./_ICON.md)
* Icons and Cursors
* GIF Images
* Bitmap Extraction from EXE
* $EXEICON (Icons viewed in Windows Explorer)
