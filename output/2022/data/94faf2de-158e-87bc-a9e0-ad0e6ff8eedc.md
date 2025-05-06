# Set3DContextHandle Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ExporterIFC..::..Set3DContextHandle Method   
[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.md "ExporterIFC Class") See Also  
---  
Sets the IfcRepresentationContext or IfcRepresentationSubContext handle to be used for 3D entities (Model entities). 
**Namespace:** [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public void Set3DContextHandle(
	IFCAnyHandle contextHandle,
	string subContextName
)
```
  
Visual Basic  
---  
```text
Public Sub Set3DContextHandle ( _
	contextHandle As IFCAnyHandle, _
	subContextName As String _
)
```
  
Visual C++  
---  
```text
public:
void Set3DContextHandle(
	IFCAnyHandle^ contextHandle, 
	String^ subContextName
)
```
  
# ### Parameters
contextHandle
    Type: [Autodesk.Revit.DB.IFC..::..IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.md "IFCAnyHandle Class") The IfcRepresentationContext for 3D entities. 
subContextName
    Type: System..::..String The name of the IfcRepresentationSubContext, or the IfcRepresentationContext if the string is empty, for 3D entities. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.md "ExporterIFC Class")
[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")
Send comments on this topic to 