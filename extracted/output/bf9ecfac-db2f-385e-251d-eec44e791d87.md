# Create Method (Connector, ElectricalSystemType)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ElectricalSystem..::..Create Method (Connector, ElectricalSystemType)  
[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.md "ElectricalSystem Class") See Also  
---  
Creates a new MEP Electrical System element from an unused Connector. 
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018 
# Syntax
C#  
---  
```text
public static ElectricalSystem Create(
	Connector connector,
	ElectricalSystemType elecSysType
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	connector As Connector, _
	elecSysType As ElectricalSystemType _
) As ElectricalSystem
```
  
Visual C++  
---  
```text
public:
static ElectricalSystem^ Create(
	Connector^ connector, 
	ElectricalSystemType elecSysType
)
```
  
# ### Parameters
connector
    Type: [Autodesk.Revit.DB..::..Connector](11e07082-b3f2-26a1-de79-16535f44716c.md "Connector Class") The Connector to create this Electrical System. 
elecSysType
    Type: [Autodesk.Revit.DB.Electrical..::..ElectricalSystemType](90f62108-9cd1-a66a-a123-8372307f4e7f.md "ElectricalSystemType Enumeration") The System Type of electrical system. 
# ### Return Value
If successful a new MEP Electrical System element within the project, otherwise nullNothingnullptra null reference (Nothing in Visual Basic). 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md "DisabledDisciplineException Class") | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also
[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.md "ElectricalSystem Class")
[Create Overload](b3ea7251-7230-ac0a-d5cc-0806b0c0ec1e.md "Create Method")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)