# Transform2D Constructor (Transform2D) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Transform2D Constructor (Transform2D)  
[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.md "Transform2D Class") See Also  
---  
The copy constructor. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2021 
# Syntax
C#  
---  
```text
public Transform2D(
	Transform2D other
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	other As Transform2D _
)
```
  
Visual C++  
---  
```text
public:
Transform2D(
	Transform2D^ other
)
```
  
# ### Parameters
other
    Type: [Autodesk.Revit.DB..::..Transform2D](49a13f08-08d7-95b1-d52e-65f90e6d4061.md "Transform2D Class") The transformation to use as input. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.md "Transform2D Class")
[Transform2D Overload](923b621e-f64c-7aac-3588-6b7d13d8957b.md "Transform2D Constructor")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 