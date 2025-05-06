# IsValidLineWeight Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FilledRegionType..::..IsValidLineWeight Method   
[FilledRegionType Class](850ae173-379b-bfd6-7295-3950ccc229ca.md "FilledRegionType Class") See Also  
---  
Indicates whether the given line weight value is valid. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static bool IsValidLineWeight(
	int lineWeight
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsValidLineWeight ( _
	lineWeight As Integer _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsValidLineWeight(
	int lineWeight
)
```
  
# ### Parameters
lineWeight
    Type: System..::..Int32 The line weight. 
# ### Return Value
True if it is a valid line weight value, false otherwise. 
# See Also
[FilledRegionType Class](850ae173-379b-bfd6-7295-3950ccc229ca.md "FilledRegionType Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 