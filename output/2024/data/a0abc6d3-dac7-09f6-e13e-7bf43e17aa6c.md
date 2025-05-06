# Insert Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
PlanCircuitSet..::..Insert Method   
[PlanCircuitSet Class](8398c79d-1108-6846-cc0c-b7b2b5c1d026.md "PlanCircuitSet Class") See Also  
---  
Insert the specified item into the set.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public virtual bool Insert(
	PlanCircuit item
)
```
  
Visual Basic  
---  
```text
Public Overridable Function Insert ( _
	item As PlanCircuit _
) As Boolean
```
  
Visual C++  
---  
```text
public:
virtual bool Insert(
	PlanCircuit^ item
)
```
  
# ### Parameters
item
    Type: [Autodesk.Revit.DB..::..PlanCircuit](9fdb77cb-c579-1cbd-71de-01f06a18ea3a.md "PlanCircuit Class")The item to be inserted into the set.
# ### Return Value
Returns whether the item was inserted into the set.
# See Also
[PlanCircuitSet Class](8398c79d-1108-6846-cc0c-b7b2b5c1d026.md "PlanCircuitSet Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 