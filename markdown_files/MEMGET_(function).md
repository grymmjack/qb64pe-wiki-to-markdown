## _MEMGET (function)
---

### The _MEMGET function returns a value from a specific memory block name at the specified OFFSET using a certain variable type.

#### SYNTAX

`returnValue = _MEMGET ( memoryBlock , bytePosition , variableType )`

#### PARAMETERS
* Returns a value of the variableType designated. The holding variable must match that [TYPE](./TYPE.md) .
* memoryBlock is a [_MEM](./_MEM.md) variable type memory block name created by [_MEMNEW](./_MEMNEW.md) or the [_MEM](./_MEM.md) function.
* bytePosition is the memoryBlock . OFFSET memory start position plus any bytes to move into the block.
* variableType is a variable [TYPE](./TYPE.md) like [_BYTE](./_BYTE.md) , [INTEGER](./INTEGER.md) , [SINGLE](./SINGLE.md) , [DOUBLE](./DOUBLE.md) , etc.


#### DESCRIPTION
* memoryBlock . OFFSET returns the starting byte position of the block. Add bytes to move into the block.
* The variable type held in the memory block can determine the next bytePosition to read.
* [LEN](./LEN.md) can be used to determine the byte size of numerical or user defined Variable Types regardless of the value held.
* [STRING](./STRING.md) values should be of a defined length. Variable length strings can actually move around in memory and not be found.
* [_MEMGET](./_MEMGET.md) variable values that are assigned a variable type other than a memory type do not need to be freed.


#### EXAMPLES
##### Example: DEF SEG and VARPTR are no longer necessary to do things in memory just like POKE and PEEK do.
```vb
DIM o AS _MEM
o = _MEM(d&) 'OLD... o% = VARPTR(d&)
_MEMPUT o, o.OFFSET + 1, 3 AS _UNSIGNED _BYTE 'a POKE
v = _MEMGET(o, o.OFFSET + 1, _UNSIGNED _BYTE) 'a PEEK
PRINT v     'prints 3
PRINT d&    'prints 768 because the 2nd byte of d& has been set to 3 or 3 * 256
_MEMFREE o
```
  


#### SEE ALSO
* [_MEM](./_MEM.md) , MEM (function)
* [_MEMGET](./_MEMGET.md) , [_MEMPUT](./_MEMPUT.md)
* [_MEMNEW](./_MEMNEW.md) , [_MEMFILL](./_MEMFILL.md)
* [_MEMCOPY](./_MEMCOPY.md)
