# CreateBinary Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
IFCData..::..CreateBinary Method   
[IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.md "IFCData Class") See Also  
---  
Creates a binary data object. 
**Namespace:** [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static IFCData CreateBinary(
	string value
)
```
  
Visual Basic  
---  
```text
Public Shared Function CreateBinary ( _
	value As String _
) As IFCData
```
  
Visual C++  
---  
```text
public:
static IFCData^ CreateBinary(
	String^ value
)
```
  
# ### Parameters
value
    Type: System..::..String The string value. 
# ### Return Value
The IFCData object. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.md "IFCData Class")
[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")
Send comments on this topic to 