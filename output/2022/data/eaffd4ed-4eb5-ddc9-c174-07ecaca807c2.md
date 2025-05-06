# AlternatingBarOrientation Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
PathReinforcement..::..AlternatingBarOrientation Property   
[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.md "PathReinforcement Class") See Also  
---  
Orientation of alternating bars of Path Reinforcement. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public ReinforcementBarOrientation AlternatingBarOrientation { get; set; }
```
  
Visual Basic  
---  
```text
Public Property AlternatingBarOrientation As ReinforcementBarOrientation
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ReinforcementBarOrientation AlternatingBarOrientation {
	ReinforcementBarOrientation get ();
	void set (ReinforcementBarOrientation value);
}
```
  
# Remarks
The orientation corresponds to the bars' rotation in the Path Reinforcement element. It indicates the postion of the major segment of the alternating Rebar Shape relative to the edges of a rectangular region which bounds the Path Reinforcement, where the top/exterior and bottom/interior come from the cover boundaries of the host, the near side edge is defined by the Path Reinforcement sketch line, and the far side edge is derived from bar length (defaulting to 5'). 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: This orientation is not allowed for alternating bars. |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md "DisabledDisciplineException Class") | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also
[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.md "PathReinforcement Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 