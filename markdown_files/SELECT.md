# SELECT CASE
> SELECT CASE is used to determine the program flow by comparing the value of a variable to specific CASE values.

## SYNTAX
`SELECT [EVERY] CASE testExpression CASE expressionList1 [statement-block1] [ CASE expressionList2 [statement-block2]]... [ CASE ELSE [statementblock-n]]`

## EXAMPLES
> Example 1: SELECT CASE can use literal or variable STRING or numerical values in CASE comparisons:

```vb
INPUT "Enter a whole number value from 1 to 40: ", value
value1 = 10
value2 = 20
value3 = 30

SELECT CASE value
 CASE value1: PRINT "Ten only"
 CASE value1 TO value2: PRINT "11 to 20 only" '10 is already evaluated
 CASE value1, value2, value3: PRINT "30 only" '10 and 20 are already evaluated
 CASE IS > value2: PRINT "greater than 20 but not 30" '30 is already evaluated
 CASE ELSE: PRINT "Other value" 'values less than 10
END SELECT
```

> Example 2: SELECT CASE will execute the first CASE statement that is true and ignore all CASE evaluations after that:

```vb
INPUT "Enter a whole number value from 1 to 40: ", value
value1 = 10
value2 = 20
value3 = 30

SELECT CASE value
 CASE value1: PRINT "Ten only"
 CASE value1 TO value2: PRINT "11 to 20 only" '10 is already evaluated
 CASE value1, value2, value3: PRINT "30 only" '10 and 20 are already evaluated
 CASE IS > value2: PRINT "greater than 20 but not 30" '30 is already evaluated
 CASE ELSE: PRINT "Other value" 'values less than 10
END SELECT
```

> Example 3: Same as Example 2 but, SELECT EVERYCASE will execute every CASE statement that is true.

```vb
INPUT "Enter a whole number value from 1 to 40: ", value
value1 = 10
value2 = 20
value3 = 30

SELECT CASE value
 CASE value1: PRINT "Ten only"
 CASE value1 TO value2: PRINT "11 to 20 only" '10 is already evaluated
 CASE value1, value2, value3: PRINT "30 only" '10 and 20 are already evaluated
 CASE IS > value2: PRINT "greater than 20 but not 30" '30 is already evaluated
 CASE ELSE: PRINT "Other value" 'values less than 10
END SELECT
```

> Example 4: SELECT CASE evaluates string values by the ASC code value according to ASCII .

```vb
INPUT "Enter a whole number value from 1 to 40: ", value
value1 = 10
value2 = 20
value3 = 30

SELECT CASE value
 CASE value1: PRINT "Ten only"
 CASE value1 TO value2: PRINT "11 to 20 only" '10 is already evaluated
 CASE value1, value2, value3: PRINT "30 only" '10 and 20 are already evaluated
 CASE IS > value2: PRINT "greater than 20 but not 30" '30 is already evaluated
 CASE ELSE: PRINT "Other value" 'values less than 10
END SELECT
```

> Example 5: EVERYCASE is used to draw sections of digital numbers in a simulated LED readout using numbers from 0 to 9:

```vb
INPUT "Enter a whole number value from 1 to 40: ", value
value1 = 10
value2 = 20
value3 = 30

SELECT CASE value
 CASE value1: PRINT "Ten only"
 CASE value1 TO value2: PRINT "11 to 20 only" '10 is already evaluated
 CASE value1, value2, value3: PRINT "30 only" '10 and 20 are already evaluated
 CASE IS > value2: PRINT "greater than 20 but not 30" '30 is already evaluated
 CASE ELSE: PRINT "Other value" 'values less than 10
END SELECT
```


```vb
INPUT "Enter a whole number value from 1 to 40: ", value
value1 = 10
value2 = 20
value3 = 30

SELECT CASE value
 CASE value1: PRINT "Ten only"
 CASE value1 TO value2: PRINT "11 to 20 only" '10 is already evaluated
 CASE value1, value2, value3: PRINT "30 only" '10 and 20 are already evaluated
 CASE IS > value2: PRINT "greater than 20 but not 30" '30 is already evaluated
 CASE ELSE: PRINT "Other value" 'values less than 10
END SELECT
```

* [IF](IF.md)...[THEN](THEN.md) , Boolean

```vb
INPUT "Enter a whole number value from 1 to 40: ", value
value1 = 10
value2 = 20
value3 = 30

SELECT CASE value
 CASE value1: PRINT "Ten only"
 CASE value1 TO value2: PRINT "11 to 20 only" '10 is already evaluated
 CASE value1, value2, value3: PRINT "30 only" '10 and 20 are already evaluated
 CASE IS > value2: PRINT "greater than 20 but not 30" '30 is already evaluated
 CASE ELSE: PRINT "Other value" 'values less than 10
END SELECT
```



# SEE ALSO
* [IF](IF.md)...[THEN](THEN.md) , Boolean

