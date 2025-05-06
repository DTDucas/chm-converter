# GetMaterialByGUID Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FabricationConfiguration..::..GetMaterialByGUID Method   
[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.md "FabricationConfiguration Class") See Also  
---  
Gets the material identifier by its GUID. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public int GetMaterialByGUID(
	Guid materialGUID
)
```
  
Visual Basic  
---  
```text
Public Function GetMaterialByGUID ( _
	materialGUID As Guid _
) As Integer
```
  
Visual C++  
---  
```text
public:
int GetMaterialByGUID(
	Guid materialGUID
)
```
  
# ### Parameters
materialGUID
    Type: System..::..Guid The material GUID. 
# ### Return Value
The material identifier. Returns 0 if not found. 
# See Also
[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.md "FabricationConfiguration Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 