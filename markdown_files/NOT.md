# NOT
> NOT is a boolean logical operator that will change a false statement to a true one and vice-versa.

## SYNTAX
`True = -1: False = NOT True`

## DESCRIPTION
* In QBasic, True = -1 and False = 0 in boolean logic and evaluation statements.
* [NOT](NOT.md) evaluates a value and returns the bitwise opposite, meaning that [NOT](NOT.md) 0 = -1 .
* Often called a negative logic operator, it returns the opposite of a value as true or false.
* Values are changed by their bit values so that each bit is changed to the opposite of on or off. See example 3 below.


## EXAMPLES
> Example 1: Alternating between two conditions in a program loop.

```vb
Table 3: The relational operations for condition checking.

In this table, A and B are the Expressions to compare. Both must represent
the same general type, i.e. they must result into either numerical values
or STRING values. If a test succeeds, then true (-1) is returned, false (0)
    if it fails, which both can be used in further Boolean evaluations.
┌─────────────────────────────────────────────────────────────────────────┐
│                          Relational Operations                          │
├────────────┬───────────────────────────────────────────┬────────────────┤
│ Operation  │                Description                │ Example usage  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A = B    │ Tests if A is equal to B.                 │ IF A = B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <> B   │ Tests if A is not equal to B.             │ IF A <> B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A < B    │ Tests if A is less than B.                │ IF A < B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A > B    │ Tests if A is greater than B.             │ IF A > B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <= B   │ Tests if A is less than or equal to B.    │ IF A <= B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A >= B   │ Tests if A is greater than or equal to B. │ IF A >= B THEN │
└────────────┴───────────────────────────────────────────┴────────────────┘
  The operations should be very obvious for numerical values. For strings
  be aware that all checks are done case sensitive (i.e. "Foo" <> "foo").
  The equal/not equal check is pretty much straight forward, but for the
  less/greater checks the ASCII value of the first different character is
                         used for decision making:

  E.g. "abc" is less than "abd", because in the first difference (the 3rd
       character) the "c" has a lower ASCII value than the "d".

  This behavior may give you some subtle results, if you are not aware of
                  the ASCII values and the written case:

  E.g. "abc" is greater than "abD", because the small letters have higher
       ASCII values than the capital letters, hence "c" > "D". You may use
       LCASE$ or UCASE$ to make sure both strings have the same case.
```

> Example 2: Reading a file until it reaches the End Of File.

```vb
Table 3: The relational operations for condition checking.

In this table, A and B are the Expressions to compare. Both must represent
the same general type, i.e. they must result into either numerical values
or STRING values. If a test succeeds, then true (-1) is returned, false (0)
    if it fails, which both can be used in further Boolean evaluations.
┌─────────────────────────────────────────────────────────────────────────┐
│                          Relational Operations                          │
├────────────┬───────────────────────────────────────────┬────────────────┤
│ Operation  │                Description                │ Example usage  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A = B    │ Tests if A is equal to B.                 │ IF A = B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <> B   │ Tests if A is not equal to B.             │ IF A <> B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A < B    │ Tests if A is less than B.                │ IF A < B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A > B    │ Tests if A is greater than B.             │ IF A > B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <= B   │ Tests if A is less than or equal to B.    │ IF A <= B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A >= B   │ Tests if A is greater than or equal to B. │ IF A >= B THEN │
└────────────┴───────────────────────────────────────────┴────────────────┘
  The operations should be very obvious for numerical values. For strings
  be aware that all checks are done case sensitive (i.e. "Foo" <> "foo").
  The equal/not equal check is pretty much straight forward, but for the
  less/greater checks the ASCII value of the first different character is
                         used for decision making:

  E.g. "abc" is less than "abd", because in the first difference (the 3rd
       character) the "c" has a lower ASCII value than the "d".

  This behavior may give you some subtle results, if you are not aware of
                  the ASCII values and the written case:

  E.g. "abc" is greater than "abD", because the small letters have higher
       ASCII values than the capital letters, hence "c" > "D". You may use
       LCASE$ or UCASE$ to make sure both strings have the same case.
```

> Example 3: So why does NOT 5 = -6 ? Because NOT changes every bit of a value into the opposite:

```vb
Table 3: The relational operations for condition checking.

In this table, A and B are the Expressions to compare. Both must represent
the same general type, i.e. they must result into either numerical values
or STRING values. If a test succeeds, then true (-1) is returned, false (0)
    if it fails, which both can be used in further Boolean evaluations.
┌─────────────────────────────────────────────────────────────────────────┐
│                          Relational Operations                          │
├────────────┬───────────────────────────────────────────┬────────────────┤
│ Operation  │                Description                │ Example usage  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A = B    │ Tests if A is equal to B.                 │ IF A = B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <> B   │ Tests if A is not equal to B.             │ IF A <> B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A < B    │ Tests if A is less than B.                │ IF A < B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A > B    │ Tests if A is greater than B.             │ IF A > B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <= B   │ Tests if A is less than or equal to B.    │ IF A <= B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A >= B   │ Tests if A is greater than or equal to B. │ IF A >= B THEN │
└────────────┴───────────────────────────────────────────┴────────────────┘
  The operations should be very obvious for numerical values. For strings
  be aware that all checks are done case sensitive (i.e. "Foo" <> "foo").
  The equal/not equal check is pretty much straight forward, but for the
  less/greater checks the ASCII value of the first different character is
                         used for decision making:

  E.g. "abc" is less than "abd", because in the first difference (the 3rd
       character) the "c" has a lower ASCII value than the "d".

  This behavior may give you some subtle results, if you are not aware of
                  the ASCII values and the written case:

  E.g. "abc" is greater than "abD", because the small letters have higher
       ASCII values than the capital letters, hence "c" > "D". You may use
       LCASE$ or UCASE$ to make sure both strings have the same case.
```


```vb
Table 3: The relational operations for condition checking.

In this table, A and B are the Expressions to compare. Both must represent
the same general type, i.e. they must result into either numerical values
or STRING values. If a test succeeds, then true (-1) is returned, false (0)
    if it fails, which both can be used in further Boolean evaluations.
┌─────────────────────────────────────────────────────────────────────────┐
│                          Relational Operations                          │
├────────────┬───────────────────────────────────────────┬────────────────┤
│ Operation  │                Description                │ Example usage  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A = B    │ Tests if A is equal to B.                 │ IF A = B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <> B   │ Tests if A is not equal to B.             │ IF A <> B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A < B    │ Tests if A is less than B.                │ IF A < B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A > B    │ Tests if A is greater than B.             │ IF A > B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <= B   │ Tests if A is less than or equal to B.    │ IF A <= B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A >= B   │ Tests if A is greater than or equal to B. │ IF A >= B THEN │
└────────────┴───────────────────────────────────────────┴────────────────┘
  The operations should be very obvious for numerical values. For strings
  be aware that all checks are done case sensitive (i.e. "Foo" <> "foo").
  The equal/not equal check is pretty much straight forward, but for the
  less/greater checks the ASCII value of the first different character is
                         used for decision making:

  E.g. "abc" is less than "abd", because in the first difference (the 3rd
       character) the "c" has a lower ASCII value than the "d".

  This behavior may give you some subtle results, if you are not aware of
                  the ASCII values and the written case:

  E.g. "abc" is greater than "abD", because the small letters have higher
       ASCII values than the capital letters, hence "c" > "D". You may use
       LCASE$ or UCASE$ to make sure both strings have the same case.
```

* [_BIT](_BIT.md) , &B , [_BYTE](_BYTE.md)
* [AND](AND.md) , [XOR](XOR.md) , [OR](OR.md)
* Binary , Boolean
* Mathematical Operations

```vb
Table 3: The relational operations for condition checking.

In this table, A and B are the Expressions to compare. Both must represent
the same general type, i.e. they must result into either numerical values
or STRING values. If a test succeeds, then true (-1) is returned, false (0)
    if it fails, which both can be used in further Boolean evaluations.
┌─────────────────────────────────────────────────────────────────────────┐
│                          Relational Operations                          │
├────────────┬───────────────────────────────────────────┬────────────────┤
│ Operation  │                Description                │ Example usage  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A = B    │ Tests if A is equal to B.                 │ IF A = B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <> B   │ Tests if A is not equal to B.             │ IF A <> B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A < B    │ Tests if A is less than B.                │ IF A < B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A > B    │ Tests if A is greater than B.             │ IF A > B THEN  │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A <= B   │ Tests if A is less than or equal to B.    │ IF A <= B THEN │
├────────────┼───────────────────────────────────────────┼────────────────┤
│   A >= B   │ Tests if A is greater than or equal to B. │ IF A >= B THEN │
└────────────┴───────────────────────────────────────────┴────────────────┘
  The operations should be very obvious for numerical values. For strings
  be aware that all checks are done case sensitive (i.e. "Foo" <> "foo").
  The equal/not equal check is pretty much straight forward, but for the
  less/greater checks the ASCII value of the first different character is
                         used for decision making:

  E.g. "abc" is less than "abd", because in the first difference (the 3rd
       character) the "c" has a lower ASCII value than the "d".

  This behavior may give you some subtle results, if you are not aware of
                  the ASCII values and the written case:

  E.g. "abc" is greater than "abD", because the small letters have higher
       ASCII values than the capital letters, hence "c" > "D". You may use
       LCASE$ or UCASE$ to make sure both strings have the same case.
```



# SEE ALSO
* [_BIT](_BIT.md) , &B , [_BYTE](_BYTE.md)
* [AND](AND.md) , [XOR](XOR.md) , [OR](OR.md)
* Binary , Boolean
* Mathematical Operations

