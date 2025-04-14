# PanelConnectedLabel Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ElectricalLoadClassification..::..PanelConnectedLabel Property   
[ElectricalLoadClassification Class](c8aeb888-f4dd-4b93-063e-6aa118c0e471.md "ElectricalLoadClassification Class") See Also  
---  
The name template for the connected load parameter of the load classification. 
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public string PanelConnectedLabel { get; set; }
```
  
Visual Basic  
---  
```text
Public Property PanelConnectedLabel As String
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property String^ PanelConnectedLabel {
	String^ get ();
	void set (String^ value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: panelConnectedLabel is not a valid globalization format string. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[ElectricalLoadClassification Class](c8aeb888-f4dd-4b93-063e-6aa118c0e471.md "ElectricalLoadClassification Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)