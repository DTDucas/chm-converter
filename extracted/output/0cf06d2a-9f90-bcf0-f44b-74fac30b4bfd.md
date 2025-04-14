# IsEqual Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
PointCloudOverrideSettings..::..IsEqual Method   
[PointCloudOverrideSettings Class](48196ce4-89a6-8f23-a82c-190f0113380d.md "PointCloudOverrideSettings Class") See Also  
---  
Checks if the contents of two settings are equal. 
**Namespace:** [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.md "Autodesk.Revit.DB.PointClouds Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public bool IsEqual(
	PointCloudOverrideSettings other
)
```
  
Visual Basic  
---  
```text
Public Function IsEqual ( _
	other As PointCloudOverrideSettings _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsEqual(
	PointCloudOverrideSettings^ other
)
```
  
# ### Parameters
other
    Type: [Autodesk.Revit.DB.PointClouds..::..PointCloudOverrideSettings](48196ce4-89a6-8f23-a82c-190f0113380d.md "PointCloudOverrideSettings Class") The settings to be compared. 
# ### Return Value
True for equal, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[PointCloudOverrideSettings Class](48196ce4-89a6-8f23-a82c-190f0113380d.md "PointCloudOverrideSettings Class")
[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.md "Autodesk.Revit.DB.PointClouds Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)