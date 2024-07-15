# AND
> The logical AND numerical operator compares two values in respect of their bits. If both bits at a certain position in both values are set, then that bit position is set in the result.

## SYNTAX
`result = firstvalue AND secondvalue`

## DESCRIPTION
* [AND](AND.md) compares the bits of the firstvalue against the bits of the secondvalue , the result is stored in the result variable.
* If both bits are on (1) then the result is on (1).
* All other conditions return 0 (bit is off).
* [AND](AND.md) is often used to see if a bit is on by comparing a value to an exponent of 2.
* Can turn off a bit by subtracting the bit on value from 255 and using that value to [AND](AND.md) a byte value.


## EXAMPLES
> Example 1:

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

> Example 2:

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

> Example 3: Finding the binary bits on in an INTEGER value.

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

* [OR](OR.md) , [XOR](XOR.md) , [NOT](NOT.md) (logical operators)
* [AND](AND.md) (boolean)
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
* [OR](OR.md) , [XOR](XOR.md) , [NOT](NOT.md) (logical operators)
* [AND](AND.md) (boolean)
* Binary , Boolean

