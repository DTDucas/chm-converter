# SetOwnerHistoryHandle Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ExporterIFC..::..SetOwnerHistoryHandle Method   
[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.md "ExporterIFC Class") See Also  
---  
Sets the handle to the IfcOwnerHistory for the file. 
**Namespace:** [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public void SetOwnerHistoryHandle(
	IFCAnyHandle ownerHistory
)
```
  
Visual Basic  
---  
```text
Public Sub SetOwnerHistoryHandle ( _
	ownerHistory As IFCAnyHandle _
)
```
  
Visual C++  
---  
```text
public:
void SetOwnerHistoryHandle(
	IFCAnyHandle^ ownerHistory
)
```
  
# ### Parameters
ownerHistory
    Type: [Autodesk.Revit.DB.IFC..::..IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.md "IFCAnyHandle Class") The handle. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.md "ExporterIFC Class")
[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")
Send comments on this topic to 