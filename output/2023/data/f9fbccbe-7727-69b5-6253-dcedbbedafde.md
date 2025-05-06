# CanLoadFamilies Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Family..::..CanLoadFamilies Method   
[Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.md "Family Class") See Also  
---  
Checks whether the document is in a state that allows the loading of families. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2020.1 
# Syntax
C#  
---  
```text
public static bool CanLoadFamilies(
	Document document
)
```
  
Visual Basic  
---  
```text
Public Shared Function CanLoadFamilies ( _
	document As Document _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool CanLoadFamilies(
	Document^ document
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document to check. 
# ### Return Value
True if loading of families is allowed, otherwise False. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.md "Family Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 