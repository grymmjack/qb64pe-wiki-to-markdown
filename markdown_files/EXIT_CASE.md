## EXIT CASE
---

### The EXIT CASE statement does exit from a CASE in a SELECT [EVERY]CASE block.

#### SYNTAX

`EXIT CASE`

#### DESCRIPTION
* Use [EXIT](./EXIT.md) [CASE](./CASE.md) to immediately exit from a [CASE](./CASE.md) .
* In [SELECT](./SELECT.md) [EVERYCASE](./EVERYCASE.md) blocks execution will proceed with the next matching [CASE](./CASE.md) .
* In regular [SELECT](./SELECT.md) [CASE](./CASE.md) blocks execution will proceed after [END](./END.md) [SELECT](./SELECT.md) , i.e. [EXIT](./EXIT.md) [CASE](./CASE.md) and [EXIT](./EXIT.md) [SELECT](./SELECT.md) behave the same way here.


#### SEE ALSO
* [SELECT](./SELECT.md) [CASE](./CASE.md)
* [EXIT](./EXIT.md) [SELECT](./SELECT.md)
* [END](./END.md) [SELECT](./SELECT.md)
