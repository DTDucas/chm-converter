# IsPhaseDemolishedValid Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Element..::..IsPhaseDemolishedValid Method   
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") See Also  
---  
Returns true if demolishedPhaseId is an allowed value for the property DemolishedPhaseId in this Element. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public bool IsPhaseDemolishedValid(
	ElementId demolishedPhaseId
)
```
  
Visual Basic  
---  
```text
Public Function IsPhaseDemolishedValid ( _
	demolishedPhaseId As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsPhaseDemolishedValid(
	ElementId^ demolishedPhaseId
)
```
  
# ### Parameters
demolishedPhaseId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The id of a Phase or invalidElementId. 
# ### Return Value
True if demolishedPhaseId is an allowed value for the property DemolishedPhaseId in this Element, false otherwise. 
# Remarks
Acts as a validator for setting the property DemolishedPhaseId. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 