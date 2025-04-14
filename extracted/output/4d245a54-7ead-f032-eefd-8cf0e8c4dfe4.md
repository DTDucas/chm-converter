# AddPoint Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
IndexStreamPoint..::..AddPoint Method   
[IndexStreamPoint Class](b2ab0423-2e31-d5a2-ef70-197ca1bf9687.md "IndexStreamPoint Class") See Also  
---  
Inserts a [IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.md "IndexPoint Class") into the stream and associated buffer. 
**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public void AddPoint(
	IndexPoint point
)
```
  
Visual Basic  
---  
```text
Public Sub AddPoint ( _
	point As IndexPoint _
)
```
  
Visual C++  
---  
```text
public:
void AddPoint(
	IndexPoint^ point
)
```
  
# ### Parameters
point
    Type: [Autodesk.Revit.DB.DirectContext3D..::..IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.md "IndexPoint Class") The point to be inserted. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown if the associated buffer is not mapped. -or- Thrown if the associated buffer has insufficient space. |

# See Also
[IndexStreamPoint Class](b2ab0423-2e31-d5a2-ef70-197ca1bf9687.md "IndexStreamPoint Class")
[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)