# GetOffset Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
IPointCloudAccess..::..GetOffset Method   
[IPointCloudAccess Interface](d5e8d1d7-9375-ce6b-ff4f-6d4764c92736.md "IPointCloudAccess Interface") See Also  
---  
Implement this method to return the offset stored in the point cloud. 
**Namespace:** [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.md "Autodesk.Revit.DB.PointClouds Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
XYZ GetOffset()
```
  
Visual Basic  
---  
```text
Function GetOffset As XYZ
```
  
Visual C++  
---  
```text
XYZ^ GetOffset()
```
  
# ### Return Value
The offset vector of this point cloud's coordinate system. 
# Remarks
All points are assumed to be offset by the same offset vector. The offset should be expressed in the same units as used by the point coordinates (the scale conversion factor is not applied). The offset will be used by Revit if the user chooses to place an instance relative to another point cloud (the "Auto - Origin To Last Placed" placement option). 
# See Also
[IPointCloudAccess Interface](d5e8d1d7-9375-ce6b-ff4f-6d4764c92736.md "IPointCloudAccess Interface")
[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.md "Autodesk.Revit.DB.PointClouds Namespace")
Send comments on this topic to 