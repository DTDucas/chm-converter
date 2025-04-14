# Assign Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
IFCExportOptions..::..Assign Method   
[IFCExportOptions Class](db8ed2bb-8949-7a7f-e09a-29f6c9916f42.md "IFCExportOptions Class") See Also  
---  
Assigns the values of the IFCExportOptions to this options object. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public void Assign(
	IFCExportOptions sourceOptions
)
```
  
Visual Basic  
---  
```text
Public Sub Assign ( _
	sourceOptions As IFCExportOptions _
)
```
  
Visual C++  
---  
```text
public:
void Assign(
	IFCExportOptions^ sourceOptions
)
```
  
# ### Parameters
sourceOptions
    Type: [Autodesk.Revit.DB..::..IFCExportOptions](db8ed2bb-8949-7a7f-e09a-29f6c9916f42.md "IFCExportOptions Class") The source IFCExportOptions. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[IFCExportOptions Class](db8ed2bb-8949-7a7f-e09a-29f6c9916f42.md "IFCExportOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)