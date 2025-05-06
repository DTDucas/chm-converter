# RotationZ Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
AnalyticalLinkType..::..RotationZ Property   
[AnalyticalLinkType Class](9362135d-6ea6-ff5a-e026-b6c247a497a1.md "AnalyticalLinkType Class") See Also  
---  
Fixity of rotation around Z. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public AnalyticalFixityState RotationZ { get; set; }
```
  
Visual Basic  
---  
```text
Public Property RotationZ As AnalyticalFixityState
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property AnalyticalFixityState RotationZ {
	AnalyticalFixityState get ();
	void set (AnalyticalFixityState value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: The fixity state rotationZ is not valid for Analytical Link Type parameters. |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[AnalyticalLinkType Class](9362135d-6ea6-ff5a-e026-b6c247a497a1.md "AnalyticalLinkType Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 