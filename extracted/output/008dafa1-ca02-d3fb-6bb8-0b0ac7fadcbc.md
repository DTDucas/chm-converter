# SelectPanel Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ElectricalSystem..::..SelectPanel Method   
[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.md "ElectricalSystem Class") See Also  
---  
Set the panel for the Electrical System. 
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public void SelectPanel(
	FamilyInstance panel
)
```
  
Visual Basic  
---  
```text
Public Sub SelectPanel ( _
	panel As FamilyInstance _
)
```
  
Visual C++  
---  
```text
public:
void SelectPanel(
	FamilyInstance^ panel
)
```
  
# ### Parameters
panel
    Type: [Autodesk.Revit.DB..::..FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md "FamilyInstance Class") The panel of the electrical system. 
# Remarks
If successful, the panel will be set for the system. Otherwise the exception will be thrown. This method will only function with the Autodesk Revit MEP application. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md "DisabledDisciplineException Class") | None of the following disciplines is enabled: Mechanical Electrical Piping. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The panel does not have enough slots and Feed Through Lugs is unchecked or already in use. -or- Thrown when the panel cannot be set for the electrical system. |

# See Also
[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.md "ElectricalSystem Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)