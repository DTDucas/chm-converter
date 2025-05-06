# Create Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
HVACLoadSpaceType..::..Create Method   
[HVACLoadSpaceType Class](0fcf26fe-8542-3dc7-b9e8-8c89eda1a48d.md "HVACLoadSpaceType Class") See Also  
---  
Creates a space type. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018 
# Syntax
C#  
---  
```text
public static HVACLoadSpaceType Create(
	Document document,
	string name
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	document As Document, _
	name As String _
) As HVACLoadSpaceType
```
  
Visual C++  
---  
```text
public:
static HVACLoadSpaceType^ Create(
	Document^ document, 
	String^ name
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document. 
name
    Type: System..::..String The space type name. 
# ### Return Value
The new space type. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | name is an empty string or contains only whitespace. -or- name cannot include prohibited characters, such as "{, }, [, ], | , ;, less-than sign, greater-than sign, ?, `, ~". -or- The given value for name is already in use as a space type name. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[HVACLoadSpaceType Class](0fcf26fe-8542-3dc7-b9e8-8c89eda1a48d.md "HVACLoadSpaceType Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to 