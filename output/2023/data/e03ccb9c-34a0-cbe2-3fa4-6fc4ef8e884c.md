# Contains Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
WireMaterialTypeSet..::..Contains Method   
[WireMaterialTypeSet Class](b682dc26-30ab-9a2c-a195-dba38099d7da.md "WireMaterialTypeSet Class") See Also  
---  
Tests for the existence of a wire material type within the set.
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public virtual bool Contains(
	WireMaterialType item
)
```
  
Visual Basic  
---  
```text
Public Overridable Function Contains ( _
	item As WireMaterialType _
) As Boolean
```
  
Visual C++  
---  
```text
public:
virtual bool Contains(
	WireMaterialType^ item
)
```
  
# ### Parameters
item
    Type: [Autodesk.Revit.DB.Electrical..::..WireMaterialType](3d05ec79-0289-c6d1-2a13-7e6b07241afd.md "WireMaterialType Class")The wire material type to be searched for.
# ### Return Value
The Contains method returns True if the wire material type is within the set, otherwise False.
# See Also
[WireMaterialTypeSet Class](b682dc26-30ab-9a2c-a195-dba38099d7da.md "WireMaterialTypeSet Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to 