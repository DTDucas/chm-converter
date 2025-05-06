# Name Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
WireMaterialType..::..Name Property   
[WireMaterialType Class](3d05ec79-0289-c6d1-2a13-7e6b07241afd.md "WireMaterialType Class") See Also  
---  
Get name of wire material type. 
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public override string Name { set; }
```
  
Visual Basic  
---  
```text
Public Overrides WriteOnly Property Name As String
	Set
```
  
Visual C++  
---  
```text
public:
virtual property String^ Name {
	void set (String^ value) override;
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Set name can't be supported. |

# See Also
[WireMaterialType Class](3d05ec79-0289-c6d1-2a13-7e6b07241afd.md "WireMaterialType Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to 