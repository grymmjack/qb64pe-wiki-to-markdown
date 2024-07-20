## GET (HTTP statement)
---

### GET reads the response of an HTTP request that was opened using _OPENCLIENT .

#### SYNTAX

`GET # Handle , , String`

#### PARAMETERS
* Handle is the handle returned from [_OPENCLIENT](./_OPENCLIENT.md) when making an HTTP request.
* String is a regular [STRING](./STRING.md) variable.
* Fixed-Length-Variable is any variable with a type that has a fixed size.


#### DESCRIPTION


#### EXAMPLES
```vb
$UNSTABLE:HTTP

' This URL simply returns a fake JSON response
h& = _OPENCLIENT("HTTP:https://httpbin.org/json")

WHILE NOT EOF(h&)
   _LIMIT 100 ' Hitting GET too fast will simply slow down the download

   GET #h&, , s$

   ' Combine all the data we get from 'GET' into a single string containing the full response
   Content$ = Content$ + s$
WEND

CLOSE h&

' Prints out the full response from that HTTP request
PRINT Content$
```
  
```vb
{
 "slideshow": {
   "author": "Yours Truly",
   "date": "date of publication",
   "slides": [
     {
       "title": "Wake up to WonderWidgets!",
       "type": "all"
     },
     {
       "items": [
         "Why WonderWidgets are great",
         "Who buys WonderWidgets"
       ],
       "title": "Overview",
       "type": "all"
     }
   ],
   "title": "Sample Slide Show"
 }
}
```
  

