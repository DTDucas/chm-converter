# GetPhaseStatus Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Element..::..GetPhaseStatus Method   
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") See Also  
---  
Gets the status of a given element in the input phase 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public ElementOnPhaseStatus GetPhaseStatus(
	ElementId phaseId
)
```
  
Visual Basic  
---  
```text
Public Function GetPhaseStatus ( _
	phaseId As ElementId _
) As ElementOnPhaseStatus
```
  
Visual C++  
---  
```text
public:
ElementOnPhaseStatus GetPhaseStatus(
	ElementId^ phaseId
)
```
  
# ### Parameters
phaseId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") Id of the phase. 
# ### Return Value
The status of the element in the phase. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The id does not represent a valid phase. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 