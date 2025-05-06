# CycleCounterChanged Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarUpdateCurvesData..::..CycleCounterChanged Property   
[RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.md "RebarUpdateCurvesData Class") See Also  
---  
True if the cycle counter was changed, false otherwise.
The cycle counter value is changed when the free form Rebar element is selected and the user press Space key -or- by through [!:Autodesk::Revit::DB::Structure::RebarRebarFreeFormAccessor::CycleCounter] property. -or- by the server if it considers that the counter reaches the maximum value and reset it (set it to 0). 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public bool CycleCounterChanged { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property CycleCounterChanged As Boolean
	Get
```
  
Visual C++  
---  
```text
public:
property bool CycleCounterChanged {
	bool get ();
}
```
  
# See Also
[RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.md "RebarUpdateCurvesData Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 