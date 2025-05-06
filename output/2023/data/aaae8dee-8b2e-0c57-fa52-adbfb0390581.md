# GetBendProfileWithFillets Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
FabricSheet..::..GetBendProfileWithFillets Method   
[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.md "FabricSheet Class") See Also  
---  
Returns the profile with generated fillets that defines the shape of the Fabric Sheet bending. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public CurveLoop GetBendProfileWithFillets()
```
  
Visual Basic  
---  
```text
Public Function GetBendProfileWithFillets As CurveLoop
```
  
Visual C++  
---  
```text
public:
CurveLoop^ GetBendProfileWithFillets()
```
  
# ### Return Value
The bend profile with generated fillets that defines the shape of the fabric sheet bending for bent fabric sheet, for flat fabric sheet nullNothingnullptra null reference (Nothing in Visual Basic) will be returned. 
# Remarks
Returned curve loop is created automatically as a result of adding fillets to bend profile. The returned profile defines the center-curve of a wire. Note that bent Fabric Sheets can have planar geometry, but flat Fabric Sheets are always planar. 
# See Also
[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.md "FabricSheet Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 