# NumberOfBarPositions Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarContainerItem..::..NumberOfBarPositions Property   
[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.md "RebarContainerItem Class") See Also  
---  
The number of potential bars in the set. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public int NumberOfBarPositions { get; set; }
```
  
Visual Basic  
---  
```text
Public Property NumberOfBarPositions As Integer
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property int NumberOfBarPositions {
	int get ();
	void set (int value);
}
```
  
# Remarks
The number of positions is equal to the number of actual bars (the Quantity), plus one or two more positions depending on IncludeFistBar and IncludeLastBar. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: the number of bar positions numberOfBarPositions is less than 1 or more than 1002. |
| [Autodesk.Revit.Exceptions..::..InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.md "InapplicableDataException Class") | When setting this property: This rebar element represents a single bar (the layout rule is Single). |

# See Also
[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.md "RebarContainerItem Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)