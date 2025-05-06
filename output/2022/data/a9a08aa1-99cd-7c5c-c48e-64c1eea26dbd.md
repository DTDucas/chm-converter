# SetAlignmentMethod Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
AnalyticalModelStick..::..SetAlignmentMethod Method   
[AnalyticalModelStick Class](f9554dde-c9c3-dbb5-d603-0b922bc51fd9.md "AnalyticalModelStick Class") See Also  
---  
Sets the alignment method for a given selector. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public void SetAlignmentMethod(
	AnalyticalElementSelector selector,
	AnalyticalAlignmentMethod method
)
```
  
Visual Basic  
---  
```text
Public Sub SetAlignmentMethod ( _
	selector As AnalyticalElementSelector, _
	method As AnalyticalAlignmentMethod _
)
```
  
Visual C++  
---  
```text
public:
void SetAlignmentMethod(
	AnalyticalElementSelector selector, 
	AnalyticalAlignmentMethod method
)
```
  
# ### Parameters
selector
    Type: [Autodesk.Revit.DB.Structure..::..AnalyticalElementSelector](b8d93e4d-3543-637d-5a9d-affa1bced099.md "AnalyticalElementSelector Enumeration") End of the analytical model. 
method
    Type: [Autodesk.Revit.DB.Structure..::..AnalyticalAlignmentMethod](28fcae11-78b7-c34b-d307-20055e71a26e.md "AnalyticalAlignmentMethod Enumeration") The alignment method at a given end. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[AnalyticalModelStick Class](f9554dde-c9c3-dbb5-d603-0b922bc51fd9.md "AnalyticalModelStick Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 