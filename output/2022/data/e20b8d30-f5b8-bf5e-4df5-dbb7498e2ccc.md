# GetBendData Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
Rebar..::..GetBendData Method   
[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.md "Rebar Class") See Also  
---  
Gets the RebarBendData, containing bar and hook information, of the instance. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2009 
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
[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.md "Rebar Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 