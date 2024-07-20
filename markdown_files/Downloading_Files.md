## Downloading Files
---

### QB64-PE starting in v3.5.0 includes built-in support for making HTTP requests and receiving their responses. This functionality is implemented in _OPENCLIENT , and the resulting HTTP handle can then be provided the various existing or new stream commands to interact with the response.

#### EXAMPLES
```vb
' Content of the HTTP response is returned.
' The statusCode is also assigned.
FUNCTION Download$(url AS STRING, statusCode AS LONG)
   DIM h AS LONG, content AS STRING, s AS STRING

   h = _OPENCLIENT("HTTP:" + url)

   statusCode = _STATUSCODE(h)

   WHILE NOT EOF(h)
       _LIMIT 60
       GET #h, , s
       content = content + s
   WEND

   CLOSE #h

   Download$ = content
END FUNCTION
```
  
```vb
FUNCTION DownloadWithProgress$(url AS STRING, statusCode AS LONG)
   DIM h AS LONG, content AS STRING, s AS STRING, length AS LONG
   DIM progress AS DOUBLE

   h = _OPENCLIENT("HTTP:" + url)

   statusCode = _STATUSCODE(h)

   length = LOF(h)

   WHILE NOT EOF(h)
       _LIMIT 60
       GET #h, , s
       content = content + s

       ' Display a progress bar if the Content-Length was provided
       IF length <> -1 THEN
           progress = CDBL(LEN(content)) / length

           LOCATE 1, 1
           PRINT "[";
           PRINT STRING$(progress * 78, "*");
           PRINT STRING$(78 - progress * 78, " ");
           PRINT "]";
       ELSE
           LOCATE 1, 1
           PRINT "[ Downloading..."; STRING$(80 - 17, " "); "]";
       END IF
   WEND

   CLOSE #h

   Download$ = content
END FUNCTION
```
  
```vb
SUB DownloadMultipleWithProgress()
   DIM handles(1 To 3) AS LONG
   DIM content(1 To 3) AS STRING
   DIM length(1 to 3) AS LONG
   DIM i AS LONG, progress AS DOUBLE
   DIM EndOfFile AS LONG, s AS STRING

   handles(1) = _OPENCLIENT("HTTP:https://www.google.com")
   handles(2) = _OPENCLIENT("HTTP:https://www.google.com")
   handles(3) = _OPENCLIENT("HTTP:https://www.google.com")

   FOR i = 1 To UBOUND(handles)
       length(i) = LOF(handles(i))
   NEXT

   DO
       _LIMIT 60
       EndOfFile = -1

       FOR i = 1 To UBOUND(handles)
           IF handles(i) = 0 THEN _CONTINUE

           IF EOF(handles(i)) THEN
               CLOSE #handles(i)
               handles(i) = 0
               _CONTINUE
           END IF

           EndOfFile = 0

           GET #handles(i), , s
           content(i) = content(i) + s

           ' Display a progress bar if the
           ' Content-Length was provided
           IF length <> -1 THEN
               progress = CDBL(LEN(content(i))) / length(i)
               LOCATE i, 1
               PRINT "[";
               PRINT STRING$(progress * 78, "*");
               PRINT STRING$(78 - progress * 78, " ");
               PRINT "]";
           ELSE
               LOCATE i, 1
               PRINT "[ Downloading..."; STRING$(80 - 17, " "); "]";
           END IF
       NEXT
   LOOP While NOT EndOfFile

   ' The content() array now contains the results of the downloads
END SUB
```
  
```vb
' Returns the status code of the HTTP response
FUNCTION DownloadToFile&(url AS STRING, fileHandle AS LONG)
   DIM h AS LONG, content AS STRING, s AS STRING

   h = _OPENCLIENT("HTTP:" + url)

   DownloadToFile& = _STATUSCODE(h)

   WHILE NOT EOF(h)
       _LIMIT 60
       GET #h, , s
       PUT #fileHandle, , s
   WEND

   CLOSE #h
END FUNCTION
```
  

