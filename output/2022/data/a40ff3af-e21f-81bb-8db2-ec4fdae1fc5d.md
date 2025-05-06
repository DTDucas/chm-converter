# Initialize Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
IFCTransformSetter..::..Initialize Method   
[IFCTransformSetter Class](75b9525d-3b8d-70d8-55de-a193b9eb5e76.md "IFCTransformSetter Class") See Also  
---  
Initializes the transformation in the transform setter. 
**Namespace:** [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public void Initialize(
	ExporterIFC exporterIFC,
	Transform transform
)
```
  
Visual Basic  
---  
```text
Public Sub Initialize ( _
	exporterIFC As ExporterIFC, _
	transform As Transform _
)
```
  
Visual C++  
---  
```text
public:
void Initialize(
	ExporterIFC^ exporterIFC, 
	Transform^ transform
)
```
  
# ### Parameters
exporterIFC
    Type: [Autodesk.Revit.DB.IFC..::..ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.md "ExporterIFC Class") The exporter. 
transform
    Type: [Autodesk.Revit.DB..::..Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.md "Transform Class") The transform. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[IFCTransformSetter Class](75b9525d-3b8d-70d8-55de-a193b9eb5e76.md "IFCTransformSetter Class")
[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")
Send comments on this topic to 