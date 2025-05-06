# WriteJournalComment Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
Application..::..WriteJournalComment Method   
[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.md "Application Class") See Also  
---  
Writes a comment to the Revit journal file. 
**Namespace:** [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.md "Autodesk.Revit.ApplicationServices Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public void WriteJournalComment(
	string comment,
	bool timeStamp
)
```
  
Visual Basic  
---  
```text
Public Sub WriteJournalComment ( _
	comment As String, _
	timeStamp As Boolean _
)
```
  
Visual C++  
---  
```text
public:
void WriteJournalComment(
	String^ comment, 
	bool timeStamp
)
```
  
# ### Parameters
comment
    Type: System..::..String Text for journal comment. 
timeStamp
    Type: System..::..Boolean If a time stamp should be included in the journal comment. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.md "Application Class")
[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.md "Autodesk.Revit.ApplicationServices Namespace")
Send comments on this topic to 