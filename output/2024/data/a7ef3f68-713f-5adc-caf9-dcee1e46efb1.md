# SetOptions Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DirectShapeType..::..SetOptions Method   
[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.md "DirectShapeType Class") See Also  
---  
Sets the options to use for this DirectShapeType. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2021 
# Syntax
C#  
---  
```text
public void SetOptions(
	DirectShapeTypeOptions options
)
```
  
Visual Basic  
---  
```text
Public Sub SetOptions ( _
	options As DirectShapeTypeOptions _
)
```
  
Visual C++  
---  
```text
public:
void SetOptions(
	DirectShapeTypeOptions^ options
)
```
  
# ### Parameters
options
    Type: [Autodesk.Revit.DB..::..DirectShapeTypeOptions](ce6d1f15-bceb-5ad2-f3d1-d93f0447da44.md "DirectShapeTypeOptions Class") Options to use for this DirectShapeType. 
# Remarks
The new options take effect immediately. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The DirectShapeTypeOptions provided are not valid for this DirectShapeType. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.md "DirectShapeType Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 