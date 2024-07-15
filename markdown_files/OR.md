# OR
> The OR numerical operator returns a comparative bit value of 1 if either value's bit is on.

## SYNTAX
`result = firstValue OR secondValue`

## DESCRIPTION
* If both bits are off, it returns 0.
* If one or both bits are on then it returns 1.
* [OR](OR.md) never turns off a bit and can be used only to turn a bit on.


## EXAMPLES
> Example 1: OR always turns bits on! Never off.

```vb
Table 4: The logical operations and its results.

      In this table, A and B are the Expressions to invert or combine.
             Both may be results of former Boolean evaluations.
 ┌────────────────────────────────────────────────────────────────────────┐
 │                           Logical Operations                           │
 ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
 │   A   │   B   │ NOT B │ A AND B │ A OR B │ A XOR B │ A EQV B │ A IMP B │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ true  │ true  │ false │  true   │ true   │  false  │  true   │  true   │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ true  │ false │ true  │  false  │ true   │  true   │  false  │  false  │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ false │ true  │ false │  false  │ true   │  true   │  false  │  true   │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ false │ false │ true  │  false  │ false  │  false  │  true   │  true   │
 └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘
  Note: In most BASIC languages incl. QB64 these are bitwise operations,
        hence the logic is performed for each corresponding bit in both
        operators, where true or false indicates whether a bit is set or
        not set. The outcome of each bit is then placed into the respective
        position to build the bit pattern of the final result value.

  As all Relational Operations return negative one (-1, all bits set) for
   true and zero (0, no bits set) for false, this allows us to use these
   bitwise logical operations to invert or combine any relational checks,
   as the outcome is the same for each bit and so always results into a
           true (-1) or false (0) again for further evaluations.
```

> Example 2: Turning a data register bit on.

```vb
Table 4: The logical operations and its results.

      In this table, A and B are the Expressions to invert or combine.
             Both may be results of former Boolean evaluations.
 ┌────────────────────────────────────────────────────────────────────────┐
 │                           Logical Operations                           │
 ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
 │   A   │   B   │ NOT B │ A AND B │ A OR B │ A XOR B │ A EQV B │ A IMP B │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ true  │ true  │ false │  true   │ true   │  false  │  true   │  true   │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ true  │ false │ true  │  false  │ true   │  true   │  false  │  false  │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ false │ true  │ false │  false  │ true   │  true   │  false  │  true   │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ false │ false │ true  │  false  │ false  │  false  │  true   │  true   │
 └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘
  Note: In most BASIC languages incl. QB64 these are bitwise operations,
        hence the logic is performed for each corresponding bit in both
        operators, where true or false indicates whether a bit is set or
        not set. The outcome of each bit is then placed into the respective
        position to build the bit pattern of the final result value.

  As all Relational Operations return negative one (-1, all bits set) for
   true and zero (0, no bits set) for false, this allows us to use these
   bitwise logical operations to invert or combine any relational checks,
   as the outcome is the same for each bit and so always results into a
           true (-1) or false (0) again for further evaluations.
```


```vb
Table 4: The logical operations and its results.

      In this table, A and B are the Expressions to invert or combine.
             Both may be results of former Boolean evaluations.
 ┌────────────────────────────────────────────────────────────────────────┐
 │                           Logical Operations                           │
 ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
 │   A   │   B   │ NOT B │ A AND B │ A OR B │ A XOR B │ A EQV B │ A IMP B │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ true  │ true  │ false │  true   │ true   │  false  │  true   │  true   │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ true  │ false │ true  │  false  │ true   │  true   │  false  │  false  │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ false │ true  │ false │  false  │ true   │  true   │  false  │  true   │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ false │ false │ true  │  false  │ false  │  false  │  true   │  true   │
 └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘
  Note: In most BASIC languages incl. QB64 these are bitwise operations,
        hence the logic is performed for each corresponding bit in both
        operators, where true or false indicates whether a bit is set or
        not set. The outcome of each bit is then placed into the respective
        position to build the bit pattern of the final result value.

  As all Relational Operations return negative one (-1, all bits set) for
   true and zero (0, no bits set) for false, this allows us to use these
   bitwise logical operations to invert or combine any relational checks,
   as the outcome is the same for each bit and so always results into a
           true (-1) or false (0) again for further evaluations.
```

* [AND](AND.md) , [XOR](XOR.md)
* [AND](AND.md) (boolean) , [OR](OR.md) (boolean)
* Binary , Boolean

```vb
Table 4: The logical operations and its results.

      In this table, A and B are the Expressions to invert or combine.
             Both may be results of former Boolean evaluations.
 ┌────────────────────────────────────────────────────────────────────────┐
 │                           Logical Operations                           │
 ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
 │   A   │   B   │ NOT B │ A AND B │ A OR B │ A XOR B │ A EQV B │ A IMP B │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ true  │ true  │ false │  true   │ true   │  false  │  true   │  true   │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ true  │ false │ true  │  false  │ true   │  true   │  false  │  false  │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ false │ true  │ false │  false  │ true   │  true   │  false  │  true   │
 ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
 │ false │ false │ true  │  false  │ false  │  false  │  true   │  true   │
 └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘
  Note: In most BASIC languages incl. QB64 these are bitwise operations,
        hence the logic is performed for each corresponding bit in both
        operators, where true or false indicates whether a bit is set or
        not set. The outcome of each bit is then placed into the respective
        position to build the bit pattern of the final result value.

  As all Relational Operations return negative one (-1, all bits set) for
   true and zero (0, no bits set) for false, this allows us to use these
   bitwise logical operations to invert or combine any relational checks,
   as the outcome is the same for each bit and so always results into a
           true (-1) or false (0) again for further evaluations.
```



# SEE ALSO
* [AND](AND.md) , [XOR](XOR.md)
* [AND](AND.md) (boolean) , [OR](OR.md) (boolean)
* Binary , Boolean

