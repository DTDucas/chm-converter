# StructuralInstanceUsageFilter Class (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
StructuralInstanceUsageFilter Class  
[Members](aa5e4d8b-97b7-7a23-864e-f5d3a06bd551.md "StructuralInstanceUsageFilter Members") See Also  
---  
A filter used to find elements that are structural family instances (typically columns, beams or braces) of the given structural usage. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public class StructuralInstanceUsageFilter : ElementSlowFilter
```
  
Visual Basic  
---  
```text
Public Class StructuralInstanceUsageFilter _
	Inherits ElementSlowFilter
```
  
Visual C++  
---  
```text
public ref class StructuralInstanceUsageFilter : public ElementSlowFilter
```
  
# Remarks
This filter is a slow filter, but it uses a quick filter to eliminate non-candidate elements before the elements are obtained and expanded. Therefore this filter does not have to be paired with another quick filter to minimize the number of Elements that are expanded. 
# Inheritance Hierarchy
System..::..Object [Autodesk.Revit.DB..::..ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md "ElementFilter Class") [Autodesk.Revit.DB..::..ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.md "ElementSlowFilter Class") Autodesk.Revit.DB.Structure..::..StructuralInstanceUsageFilter
# See Also
[StructuralInstanceUsageFilter Members](aa5e4d8b-97b7-7a23-864e-f5d3a06bd551.md "StructuralInstanceUsageFilter Members")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 