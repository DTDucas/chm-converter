# Insert Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
WireMaterialTypeSet..::..Insert Method   
[WireMaterialTypeSet Class](b682dc26-30ab-9a2c-a195-dba38099d7da.md "WireMaterialTypeSet Class") See Also  
---  
Insert the specified wire material type into the set.
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public virtual bool Insert(
	WireMaterialType item
)
```
  
Visual Basic  
---  
```text
Public Overridable Function Insert ( _
	item As WireMaterialType _
) As Boolean
```
  
Visual C++  
---  
```text
public:
virtual bool Insert(
	WireMaterialType^ item
)
```
  
# ### Parameters
item
    Type: [Autodesk.Revit.DB.Electrical..::..WireMaterialType](3d05ec79-0289-c6d1-2a13-7e6b07241afd.md "WireMaterialType Class")The wire material type to be inserted into the set.
# ### Return Value
Returns whether the wire material type was inserted into the set.
# See Also
[WireMaterialTypeSet Class](b682dc26-30ab-9a2c-a195-dba38099d7da.md "WireMaterialTypeSet Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to 