# ExclusionFilter Constructor (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ExclusionFilter Constructor   
[ExclusionFilter Class](28581bc9-42ad-9178-edcc-e33f42090bc9.md "ExclusionFilter Class") See Also  
---  
Constructs a new instance of a filter to exclude elements automatically. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public ExclusionFilter(
	ICollection<ElementId> idsToExclude
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	idsToExclude As ICollection(Of ElementId) _
)
```
  
Visual C++  
---  
```text
public:
ExclusionFilter(
	ICollection<ElementId^>^ idsToExclude
)
```
  
# ### Parameters
idsToExclude
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> The ids to exclude from the results. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The input collection of ids was empty, or its contents were not valid for iteration. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ExclusionFilter Class](28581bc9-42ad-9178-edcc-e33f42090bc9.md "ExclusionFilter Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 