# GetAssignedElectricalSystems Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
MEPModel..::..GetAssignedElectricalSystems Method   
[MEPModel Class](dd78bce5-2ed6-ed3c-f329-1663bf08afa6.md "MEPModel Class") See Also  
---  
Retrieves the electrical systems this electrical panel currently is assigned to. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2021 
# Syntax
C#  
---  
```text
public ISet<ElectricalSystem> GetAssignedElectricalSystems()
```
  
Visual Basic  
---  
```text
Public Function GetAssignedElectricalSystems As ISet(Of ElectricalSystem)
```
  
Visual C++  
---  
```text
public:
ISet<ElectricalSystem^>^ GetAssignedElectricalSystems()
```
  
# Remarks
This property returns a set of Electrical Systems. If there are no electrical systems created for this model, this property will be an empty set. This method supersedes an older _AssignedElectricalSystems_ property which has been deprecated. 
# See Also
[MEPModel Class](dd78bce5-2ed6-ed3c-f329-1663bf08afa6.md "MEPModel Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 