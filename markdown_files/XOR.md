# XOR (boolean)
> XOR evaluates two conditions and if either of them is True then it returns True, if both of them are True then it returns False, if both of them are False then it returns False.

## SYNTAX
`condition XOR condition2`

## DESCRIPTION
* Either condition or condition2 must be True for the evaluation to return True.
* It is called "exclusive [OR](OR.md)" because the conditions cannot both be True for it to return True like the [OR](OR.md) evaluation.
* condition and condition2 can themselves contain [XOR](XOR.md) evaluations.


## EXAMPLES
> Example: Dilemma...

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

* [OR](OR.md) (boolean) , [AND](AND.md) (boolean)
* [IF](IF.md)...[THEN](THEN.md)

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
* [OR](OR.md) (boolean) , [AND](AND.md) (boolean)
* [IF](IF.md)...[THEN](THEN.md)

