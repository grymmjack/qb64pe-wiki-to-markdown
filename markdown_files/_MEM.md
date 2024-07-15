# _MEM
> The _MEM variable type can be used when working with memory blocks. It has no variable type suffix.

## SYNTAX
`DIM m AS _MEM`

## DESCRIPTION


## EXAMPLES
> Example 1: Demonstration of .IMAGE to determine an image's dimensions, .TYPE to verify the type and _MEMEXISTS to check image has not been freed

```vb
TYPE memory_type
 OFFSET AS _OFFSET       'start location of block(changes with byte position)
 SIZE AS _OFFSET         'size of block remaining at offset(changes with position)
 TYPE AS _OFFSET         'type description of variable used(never changes)
 ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)
 IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used
 SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used
END TYPE

The above TYPE is for clarification purposes only. It doesn't need to be pasted ina program to use _MEM.

IMPORTANT NOTE: As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.
```


```vb
TYPE memory_type
 OFFSET AS _OFFSET       'start location of block(changes with byte position)
 SIZE AS _OFFSET         'size of block remaining at offset(changes with position)
 TYPE AS _OFFSET         'type description of variable used(never changes)
 ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)
 IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used
 SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used
END TYPE

The above TYPE is for clarification purposes only. It doesn't need to be pasted ina program to use _MEM.

IMPORTANT NOTE: As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.
```

> Example 2: Converts the current destination SCREEN 13 image memory altered by PSET to a STRING value. SCREEN 13 only.

```vb
TYPE memory_type
 OFFSET AS _OFFSET       'start location of block(changes with byte position)
 SIZE AS _OFFSET         'size of block remaining at offset(changes with position)
 TYPE AS _OFFSET         'type description of variable used(never changes)
 ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)
 IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used
 SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used
END TYPE

The above TYPE is for clarification purposes only. It doesn't need to be pasted ina program to use _MEM.

IMPORTANT NOTE: As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.
```

> Example 3: Using _MEM to convert _OFFSET to _INTEGER64.

```vb
TYPE memory_type
 OFFSET AS _OFFSET       'start location of block(changes with byte position)
 SIZE AS _OFFSET         'size of block remaining at offset(changes with position)
 TYPE AS _OFFSET         'type description of variable used(never changes)
 ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)
 IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used
 SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used
END TYPE

The above TYPE is for clarification purposes only. It doesn't need to be pasted ina program to use _MEM.

IMPORTANT NOTE: As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.
```

> Explanation: The above will print two numbers which should match.  These numbers will vary, as they're representations of where X is stored in memory, and that position is going to vary every time the program is run.  What it should illustrate, however, is a way to convert _OFFSET to _INTEGER64 values, which can sometimes be useful when trying to run calculations involving mem.SIZE, mem.TYPE, or mem.ELEMENTSIZE.

```vb
TYPE memory_type
 OFFSET AS _OFFSET       'start location of block(changes with byte position)
 SIZE AS _OFFSET         'size of block remaining at offset(changes with position)
 TYPE AS _OFFSET         'type description of variable used(never changes)
 ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)
 IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used
 SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used
END TYPE

The above TYPE is for clarification purposes only. It doesn't need to be pasted ina program to use _MEM.

IMPORTANT NOTE: As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.
```


```vb
TYPE memory_type
 OFFSET AS _OFFSET       'start location of block(changes with byte position)
 SIZE AS _OFFSET         'size of block remaining at offset(changes with position)
 TYPE AS _OFFSET         'type description of variable used(never changes)
 ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)
 IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used
 SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used
END TYPE

The above TYPE is for clarification purposes only. It doesn't need to be pasted ina program to use _MEM.

IMPORTANT NOTE: As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.
```

* [_MEM](_MEM.md) (function) , [_MEMELEMENT](_MEMELEMENT.md)
* [_MEMNEW](_MEMNEW.md) , [_MEMCOPY](_MEMCOPY.md) , [_MEMFREE](_MEMFREE.md)
* [_MEMGET](_MEMGET.md) , [_MEMPUT](_MEMPUT.md) , [_MEMFILL](_MEMFILL.md)
* [_MEMIMAGE](_MEMIMAGE.md) , [_MEMSOUND](_MEMSOUND.md)

```vb
TYPE memory_type
 OFFSET AS _OFFSET       'start location of block(changes with byte position)
 SIZE AS _OFFSET         'size of block remaining at offset(changes with position)
 TYPE AS _OFFSET         'type description of variable used(never changes)
 ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)
 IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used
 SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used
END TYPE

The above TYPE is for clarification purposes only. It doesn't need to be pasted ina program to use _MEM.

IMPORTANT NOTE: As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.
```



# SEE ALSO
* [_MEM](_MEM.md) (function) , [_MEMELEMENT](_MEMELEMENT.md)
* [_MEMNEW](_MEMNEW.md) , [_MEMCOPY](_MEMCOPY.md) , [_MEMFREE](_MEMFREE.md)
* [_MEMGET](_MEMGET.md) , [_MEMPUT](_MEMPUT.md) , [_MEMFILL](_MEMFILL.md)
* [_MEMIMAGE](_MEMIMAGE.md) , [_MEMSOUND](_MEMSOUND.md)

