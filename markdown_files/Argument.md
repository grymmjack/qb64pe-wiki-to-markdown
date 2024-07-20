## Argument
---

### An argument or parameter is information that a statement , sub , function or metacommand needs to carry out the task it has been given. Sometimes a argument can be optional and is not needed for the task to be carried out, in such case it will use a default instead of the argument when carrying out the task.

#### EXAMPLES
##### Example 1: The color argument in PSET is optional
```vb
SCREEN 13
PSET (160, 100)
PSET (165, 100), 15
```
  
##### Example 2: Must place a comma to seperate arguments if you use any other argument after it.
```vb
SCREEN 13
LINE (160, 100)-(170, 110), , B
LINE (162, 102)-(168, 108), 4, BF
```
  
##### As you can see in the above example some statements have special arguments like B and BF in this case (B stands for Box and BF stands for Box Fill), if the argument isn't used then it will create a ordinary line.


#### SEE ALSO
* [SUB](./SUB.md) , [FUNCTION](./FUNCTION.md)
* Statement , Function (explanatory) , Sub (explanatory) , Metacommand , Expression
