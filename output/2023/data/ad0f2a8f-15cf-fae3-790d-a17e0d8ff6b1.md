# GetAnalyticalNodeData Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
AnalyticalNodeData..::..GetAnalyticalNodeData Method   
[AnalyticalNodeData Class](24e7600a-2ae0-f25c-c36a-62b5bfcdc2eb.md "AnalyticalNodeData Class") See Also  
---  
Returns AnalyticalNodeData associated with this element, if it exists. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2021 
# Syntax
C#  
---  
```text
public static AnalyticalNodeData GetAnalyticalNodeData(
	Element element
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetAnalyticalNodeData ( _
	element As Element _
) As AnalyticalNodeData
```
  
Visual C++  
---  
```text
public:
static AnalyticalNodeData^ GetAnalyticalNodeData(
	Element^ element
)
```
  
# ### Parameters
element
    Type: [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") The element from which we try to obtain AnalyticalNodeData. 
# Remarks
If the input element doesn't have AnalyticalNodeData than it retuns nullNothingnullptra null reference (Nothing in Visual Basic). The input element should be a ReferencePoint. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[AnalyticalNodeData Class](24e7600a-2ae0-f25c-c36a-62b5bfcdc2eb.md "AnalyticalNodeData Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 