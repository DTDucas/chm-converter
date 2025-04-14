# GetBendData Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarContainerItem..::..GetBendData Method   
[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.md "RebarContainerItem Class") See Also  
---  
Gets the RebarBendData, containing bar and hook information, of the instance. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public RebarBendData GetBendData()
```
  
Visual Basic  
---  
```text
Public Function GetBendData As RebarBendData
```
  
Visual C++  
---  
```text
public:
RebarBendData^ GetBendData()
```
  
# Remarks
Internally, the bend data is used by many RebarShape methods to generate shape geometry. 
# See Also
[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.md "RebarContainerItem Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)