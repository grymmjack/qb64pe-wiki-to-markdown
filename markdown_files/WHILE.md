# WHILE...WEND
> The WHILE...WEND statement is used to repeat a block of statements while the condition is met.

## SYNTAX
`WHILE condition`

## DESCRIPTION
* condition is a numeric expression used to determine if the loop will execute.
* statements will execute repeatedly while condition is a non-zero value.
* [EXIT](EXIT.md) [WHILE](WHILE.md) can be used for emergency exits from the loop in QB64 only.
* A [DO](DO.md)...[LOOP](LOOP.md) can use the same [DO](DO.md) [WHILE](WHILE.md) condition to get the same results.
* [WHILE](WHILE.md) loops only run if the [WHILE](WHILE.md) condition is True.


## EXAMPLES
> Example 1: Reading an entire file. Example assumes the program has a file opened as #1

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

> Example 2: Clearing the keyboard buffer.

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

* [DO](DO.md)...[LOOP](LOOP.md)
* [FOR](FOR.md)...[NEXT](NEXT.md)
* [UNTIL](UNTIL.md)
* [_CONTINUE](_CONTINUE.md)

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
* [DO](DO.md)...[LOOP](LOOP.md)
* [FOR](FOR.md)...[NEXT](NEXT.md)
* [UNTIL](UNTIL.md)
* [_CONTINUE](_CONTINUE.md)

