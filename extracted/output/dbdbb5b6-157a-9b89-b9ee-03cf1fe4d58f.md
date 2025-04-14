# HasReflection Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Transform..::..HasReflection Property   
[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.md "Transform Class") See Also  
---  
The boolean value that indicates whether this transformation produces reflection.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public bool HasReflection { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property HasReflection As Boolean
	Get
```
  
Visual C++  
---  
```text
public:
property bool HasReflection {
	bool get ();
}
```
  
# Remarks
Reflection transformation changes the handedness of a coordinate system. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown when this transformation is not conformal and the reflection is undefined. |

# See Also
[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.md "Transform Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)