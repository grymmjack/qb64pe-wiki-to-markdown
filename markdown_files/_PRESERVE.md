# _PRESERVE
> The _PRESERVE REDIM action preserves the current contents of dynamic arrays , when resizing or changing indices.

## SYNTAX
`REDIM _PRESERVE array( newLowerIndex& [TO newUpperIndex& ]) [AS variabletype]`

## DESCRIPTION
* [REDIM](REDIM.md) or the $[DYNAMIC](DYNAMIC.md) metacommand must be used when the array is first created to be able to resize and preserve.
* If [_PRESERVE](_PRESERVE.md) is not used, the current contents of the array are cleared by [REDIM](REDIM.md) . All element values of an array are preserved if the array size is increased. The remaining elements of the array are preserved if the array size is decreased. If the new index range is different from the original, all values will be moved to the new corresponding indices.
	* All element values of an array are preserved if the array size is increased.
	* The remaining elements of the array are preserved if the array size is decreased.
	* If the new index range is different from the original, all values will be moved to the new corresponding indices.
* All element values of an array are preserved if the array size is increased.
* The remaining elements of the array are preserved if the array size is decreased.
* If the new index range is different from the original, all values will be moved to the new corresponding indices.
* [REDIM](REDIM.md) [_PRESERVE](_PRESERVE.md) cannot change the number of array dimensions, but can change the number of elements.
* Always use the same array [TYPE](TYPE.md) suffix ( [AS](AS.md) type) or a new array type with the same name may be created.


## EXAMPLES
> Example 1: Changing the upper and lower array bounds

```vb
REDIM a(5 TO 10) ' create array as dynamic using REDIM
a(5) = 123
REDIM _PRESERVE a(20 TO 40)
PRINT a(20)
```

> Example 2: Sizing an array while storing file data.

```vb
REDIM a(5 TO 10) ' create array as dynamic using REDIM
a(5) = 123
REDIM _PRESERVE a(20 TO 40)
PRINT a(20)
```


```vb
REDIM a(5 TO 10) ' create array as dynamic using REDIM
a(5) = 123
REDIM _PRESERVE a(20 TO 40)
PRINT a(20)
```

* Featured in our "Keyword of the Day" series
* [REDIM](REDIM.md)
* $[DYNAMIC](DYNAMIC.md)
* Arrays

```vb
REDIM a(5 TO 10) ' create array as dynamic using REDIM
a(5) = 123
REDIM _PRESERVE a(20 TO 40)
PRINT a(20)
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* [REDIM](REDIM.md)
* $[DYNAMIC](DYNAMIC.md)
* Arrays

