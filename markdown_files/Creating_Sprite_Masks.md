## Creating Sprite Masks
---

### Sometimes your program may need to place a shaped sprite over background objects. To do that you cannot use the default PUT using XOR. XOR only works on black backgrounds! It distorts underlying colors. You could use the PSET option, but that places a square sprite only. To get irregularly shaped objects you need to create a "mask" of the sprite. After you have created your sprite with a BLACK background, GET the image to an array . You can BSAVE it if you wish. Then create a mask of the sprite at the sprites current location. Use the GET box area coordinates(minX, maxX and minY, maxY) of sprite in the following routine:

#### SEE ALSO
* [INP](./INP.md) , Scancodes (Example 3)
* [GET](./GET.md) , [PUT](./PUT.md)
* Icons and Cursors
* Creating Icons from Bitmaps
