# GetPhaseStatusPresentation Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
PhaseFilter..::..GetPhaseStatusPresentation Method   
[PhaseFilter Class](3236c80e-48be-f657-951f-70490a43f065.md "PhaseFilter Class") See Also  
---  
Gets the phase status presentation. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public PhaseStatusPresentation GetPhaseStatusPresentation(
	ElementOnPhaseStatus status
)
```
  
Visual Basic  
---  
```text
Public Function GetPhaseStatusPresentation ( _
	status As ElementOnPhaseStatus _
) As PhaseStatusPresentation
```
  
Visual C++  
---  
```text
public:
PhaseStatusPresentation GetPhaseStatusPresentation(
	ElementOnPhaseStatus status
)
```
  
# ### Parameters
status
    Type: [Autodesk.Revit.DB..::..ElementOnPhaseStatus](bfc481cc-11c8-de0b-1d71-7b2ffa711780.md "ElementOnPhaseStatus Enumeration") The element phase status. 
# ### Return Value
The phase status presentation. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | status is invalid for presentation query. |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[PhaseFilter Class](3236c80e-48be-f657-951f-70490a43f065.md "PhaseFilter Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 