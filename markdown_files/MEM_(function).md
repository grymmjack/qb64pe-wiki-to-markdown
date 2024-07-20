## _MEM (function)
---

### The _MEM function returns a _MEM block referring to the largest possible continuous memory region beginning at a variable's offset.

#### SYNTAX

`memoryBlock = _MEM ( referenceVariable )`

#### PARAMETERS
* The memoryBlock created will hold the referenceVariable or array value(s), type and byte size in a separate memory area.
* The secure syntax referenceVariable is an existing variable's referenced memory block.
* The unsecure syntax's designated offset and byteSize cannot be guaranteed. Avoid if possible.


#### DESCRIPTION
* The memoryBlock [_MEM](./_MEM.md) type variable holds the following read-only elements: OFFSET, SIZE, [TYPE](./TYPE.md) and ELEMENTSIZE.
* All values created by memory functions MUST be freed using [_MEMFREE](./_MEMFREE.md) with a valid [_MEM](./_MEM.md) variable type.
* [_MEM](./_MEM.md) function cannot reference variable length [STRING](./STRING.md) variable values. String values must be designated as a fixed- length string.


#### EXAMPLES
##### Example: Assigning values to reference variables in memory.
```vb
DIM SHARED m(3) AS _MEM
DIM SHARED Saved(3)

m(1) = _MEM(x)
m(2) = _MEM(y)
m(3) = _MEM(z)

x = 3: y = 5: z = 8
PRINT x, y, z
Save x, y, z
x = 30: y = 50: z = 80
PRINT x, y, z

RestoreIt
PRINT x, y, z

_MEMFREE m(1)
_MEMFREE m(2)
_MEMFREE m(3)
END

SUB Save (n1, n2, n3)
Saved(1) = n1
Saved(2) = n2
Saved(3) = n3
END SUB

SUB RestoreIt
_MEMPUT m(1), m(1).OFFSET, Saved(1)
_MEMPUT m(2), m(2).OFFSET, Saved(2)
_MEMPUT m(3), m(3).OFFSET, Saved(3)
END SUB
```
  


#### SEE ALSO
* [_MEM](./_MEM.md)
* [_MEMNEW](./_MEMNEW.md) , [_MEMCOPY](./_MEMCOPY.md) , [_MEMFREE](./_MEMFREE.md)
* [_MEMGET](./_MEMGET.md) , [_MEMPUT](./_MEMPUT.md) , [_MEMFILL](./_MEMFILL.md)
* [_MEMIMAGE](./_MEMIMAGE.md) , [_MEMSOUND](./_MEMSOUND.md)
