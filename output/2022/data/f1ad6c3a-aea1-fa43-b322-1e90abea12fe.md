# GetAvailableAttachedDetailGroupTypeIds Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
GroupType..::..GetAvailableAttachedDetailGroupTypeIds Method   
[GroupType Class](5ce7e921-2a43-d7f1-8ef9-8a397dd27b75.md "GroupType Class") See Also  
---  
Returns the attached detail groups available for this element group type. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2019.1 
# Syntax
C#  
---  
```text
public ISet<ElementId> GetAvailableAttachedDetailGroupTypeIds()
```
  
Visual Basic  
---  
```text
Public Function GetAvailableAttachedDetailGroupTypeIds As ISet(Of ElementId)
```
  
Visual C++  
---  
```text
public:
ISet<ElementId^>^ GetAvailableAttachedDetailGroupTypeIds()
```
  
# ### Return Value
Returns the collection of attached detail group Ids that match this group's type. 
# See Also
[GroupType Class](5ce7e921-2a43-d7f1-8ef9-8a397dd27b75.md "GroupType Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 