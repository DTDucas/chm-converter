# IsValidHost Method (Element) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarHostData..::..IsValidHost Method (Element)  
[RebarHostData Class](2b39b172-ad0f-e1c6-99a4-3b828346200c.md "RebarHostData Class") See Also  
---  
Identifies whether a given element can host reinforcement. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public static bool IsValidHost(
	Element element
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsValidHost ( _
	element As Element _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsValidHost(
	Element^ element
)
```
  
# ### Parameters
element
    Type: [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") The element to check. 
# ### Return Value
True if the input Element can host reinforcement elements, false otherwise. 
# Remarks
Many different elements are allowed to host reinforcement, for example, beams, walls, columns, or parts. Often there are specific restrictions about whether an element can host rebar beyond its type or category. For example, the material type of the element may determine this. Or for parts, the part must have been created from layers that have their role set to Structure. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[RebarHostData Class](2b39b172-ad0f-e1c6-99a4-3b828346200c.md "RebarHostData Class")
[IsValidHost Overload](aaff4dec-529b-0e41-aeb5-e632c4ad084c.md "IsValidHost Method")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 