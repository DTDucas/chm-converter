# SetArcTypeSpiral Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarShapeDefinitionByArc..::..SetArcTypeSpiral Method   
[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.md "RebarShapeDefinitionByArc Class") See Also  
---  
Set the RebarShapeDefinitionByArc.Type property to Spiral. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public void SetArcTypeSpiral(
	double height,
	double pitch,
	int baseFinishingTurns,
	int topFinishingTurns
)
```
  
Visual Basic  
---  
```text
Public Sub SetArcTypeSpiral ( _
	height As Double, _
	pitch As Double, _
	baseFinishingTurns As Integer, _
	topFinishingTurns As Integer _
)
```
  
Visual C++  
---  
```text
public:
void SetArcTypeSpiral(
	double height, 
	double pitch, 
	int baseFinishingTurns, 
	int topFinishingTurns
)
```
  
# ### Parameters
height
    Type: System..::..Double The height of the spiral (assuming the spiral is vertical). 
pitch
    Type: System..::..Double The pitch, or vertical distance traveled in one rotation. 
baseFinishingTurns
    Type: System..::..Int32 The number of finishing turns at the lower end of the spiral. 
topFinishingTurns
    Type: System..::..Int32 The number of finishing turns at the upper end of the spiral. 
# Remarks
In order to create a spiral definition, you must provide default values for height, pitch, and finishing turns. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | baseFinishingTurns is not between 0 and 100. -or- topFinishingTurns is not between 0 and 100. |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | The given value for height must be greater than 0 and no more than 30000 feet. -or- The given value for pitch must be greater than 0 and no more than 30000 feet. |

# See Also
[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.md "RebarShapeDefinitionByArc Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)