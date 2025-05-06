# AnalyticalModelSelector Constructor (Curve) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
AnalyticalModelSelector Constructor (Curve)  
[AnalyticalModelSelector Class](d286b023-8822-10ad-6702-53c86a6c9e70.md "AnalyticalModelSelector Class") See Also  
---  
Creates a selector based on a specific analytical curve. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public AnalyticalModelSelector(
	Curve curve
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	curve As Curve _
)
```
  
Visual C++  
---  
```text
public:
AnalyticalModelSelector(
	Curve^ curve
)
```
  
# ### Parameters
curve
    Type: [Autodesk.Revit.DB..::..Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class") The curve upon which this selector acts. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The input curve points to a helical curve and is not supported for this operation. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[AnalyticalModelSelector Class](d286b023-8822-10ad-6702-53c86a6c9e70.md "AnalyticalModelSelector Class")
[AnalyticalModelSelector Overload](9e76852b-a21f-b2d7-93a3-66b844047368.md "AnalyticalModelSelector Constructor")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 