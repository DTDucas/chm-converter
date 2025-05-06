# FlowState Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
PipePressureDropData..::..FlowState Property   
[PipePressureDropData Class](d9c2df4c-512f-3f0c-4c04-2f5cc5afa7d8.md "PipePressureDropData Class") See Also  
---  
The flowState of the pipe. 
**Namespace:** [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.md "Autodesk.Revit.DB.Plumbing Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public PipeFlowState FlowState { get; set; }
```
  
Visual Basic  
---  
```text
Public Property FlowState As PipeFlowState
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property PipeFlowState FlowState {
	PipeFlowState get ();
	void set (PipeFlowState value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[PipePressureDropData Class](d9c2df4c-512f-3f0c-4c04-2f5cc5afa7d8.md "PipePressureDropData Class")
[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.md "Autodesk.Revit.DB.Plumbing Namespace")
Send comments on this topic to 