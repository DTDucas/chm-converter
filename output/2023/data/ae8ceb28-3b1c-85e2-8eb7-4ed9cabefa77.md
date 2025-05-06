# IsEqual Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
RoutingCriterionBase..::..IsEqual Method   
[RoutingCriterionBase Class](6164e8ca-7eb1-2207-c596-d129e1aa146d.md "RoutingCriterionBase Class") See Also  
---  
Verify if two criteria are the same. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public bool IsEqual(
	RoutingCriterionBase pOther
)
```
  
Visual Basic  
---  
```text
Public Function IsEqual ( _
	pOther As RoutingCriterionBase _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsEqual(
	RoutingCriterionBase^ pOther
)
```
  
# ### Parameters
pOther
    Type: [Autodesk.Revit.DB..::..RoutingCriterionBase](6164e8ca-7eb1-2207-c596-d129e1aa146d.md "RoutingCriterionBase Class")
# ### Return Value
True if the criterion is equal to the other, false otherwise 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[RoutingCriterionBase Class](6164e8ca-7eb1-2207-c596-d129e1aa146d.md "RoutingCriterionBase Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 