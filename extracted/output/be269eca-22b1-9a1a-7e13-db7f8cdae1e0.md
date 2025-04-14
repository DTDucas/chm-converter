# ExportCategory Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
EnergyDataSettings..::..ExportCategory Property   
[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.md "EnergyDataSettings Class") See Also  
---  
Value is a category indicating which discipline model will be used for GreenBuildingXML export. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public ElementId ExportCategory { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ExportCategory As ElementId
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ElementId^ ExportCategory {
	ElementId^ get ();
	void set (ElementId^ value);
}
```
  
# Remarks
OST_Rooms will use the architectural 3d rooms for export. OST_MEPSpaces will use the MEP 3d Spaces for export. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: The export category is neither OST_Rooms nor OST_MEPSpaces. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.md "EnergyDataSettings Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)