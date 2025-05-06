# BentFabricStraightWiresLocation Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FabricSheet..::..BentFabricStraightWiresLocation Property   
[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.md "FabricSheet Class") See Also  
---  
Specifies the location of straight bars with respect to bent bars in the fabric sheet. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public BentFabricStraightWiresLocation BentFabricStraightWiresLocation { get; set; }
```
  
Visual Basic  
---  
```text
Public Property BentFabricStraightWiresLocation As BentFabricStraightWiresLocation
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property BentFabricStraightWiresLocation BentFabricStraightWiresLocation {
	BentFabricStraightWiresLocation get ();
	void set (BentFabricStraightWiresLocation value);
}
```
  
# Remarks
This parameter applies only to bent fabric sheets. The side on wich straight wires will be loacted is determined by the start and end point of the first bent profile segment that specifies the direction of the curve loop on plane. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: the data-setting method is not applicable to fabric sheets that are flat |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.md "InvalidObjectException Class") | When setting this property: The data-setting method is not applicable to fabric sheets that are flat. |

# See Also
[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.md "FabricSheet Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 