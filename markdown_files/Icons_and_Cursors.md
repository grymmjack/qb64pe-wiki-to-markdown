## Icons and Cursors
---

### 

#### SYNTAX

`The AND mask is read as a one BPP black and white image with each _BIT being on(white) or off(black). It is white where the background may show and black where the colors (including black) from the XOR mask will show. It is placed using the AND action by Windows first. Then the XOR mask is placed on top using an XOR action. The following SUB procedure can adapt to 24 bit colors so that colors will not be affected. Make sure that the BPP value is SHARED or pass it using a parameter!`

#### SEE ALSO
* $EXEICON
* [_ICON](./_ICON.md)
* Creating Sprite Masks
* Bitmaps , GIF Images
* Icon Extraction
