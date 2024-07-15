# ELSEIF
> ELSEIF is used in an IF...THEN block statement to offer an alternative condition.

## SYNTAX
`IF condition THEN {code} ⋮`

## DESCRIPTION
* [ELSEIF](ELSEIF.md) statements require a separate code block line with [THEN](THEN.md) for each alternative condition.
* There can be more than one [ELSE](ELSE.md) [IF](IF.md) statement in a single-line [IF](IF.md) statement.
* If there is only one possible alternative condition (such as 0 or [NOT](NOT.md) 0), use [ELSE](ELSE.md) instead.
* If the comparisons are based on multiple conditions being true, it may require many [ELSEIF](ELSEIF.md) comparisons. [ELSE](ELSE.md) could help cover some of those conditions.
* You can use [SELECT](SELECT.md) [CASE](CASE.md) when [IF](IF.md) blocks have a long list of alterative [ELSEIF](ELSEIF.md) conditions.


## EXAMPLES
> Example 1: IF statement using ELSE IF in one statement line.

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

> Example 2: IF statement block

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

* Featured in our "Keyword of the Day" series
* [ELSE](ELSE.md) , [END](END.md) [IF](IF.md)
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
* Featured in our "Keyword of the Day" series
* [ELSE](ELSE.md) , [END](END.md) [IF](IF.md)
* [IF](IF.md)...[THEN](THEN.md)

