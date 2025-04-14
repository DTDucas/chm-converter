# GetAllRevisionCloudIds Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ViewSheet..::..GetAllRevisionCloudIds Method   
[ViewSheet Class](af2ee879-173d-df3a-9793-8d5750a17b49.md "ViewSheet Class") See Also  
---  
Gets the ids of the revision clouds which appear on the sheet's revision schedules. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2023.1 
# Syntax
C#  
---  
```text
public ISet<ElementId> GetAllRevisionCloudIds()
```
  
Visual Basic  
---  
```text
Public Function GetAllRevisionCloudIds As ISet(Of ElementId)
```
  
Visual C++  
---  
```text
public:
ISet<ElementId^>^ GetAllRevisionCloudIds()
```
  
# ### Return Value
The ids of the revisions clouds which appear on the sheet's revision schedules. 
# Remarks
The sheet's revision schedules include the revisions that are associated with revision clouds that are visible on the sheet. Revision schedules may also include revisions that have been additionally added to the sheet via the Revisions On Sheets parameter. Use [GetAdditionalRevisionIds()()()()](6d852f22-cf1b-3bcb-c255-184998d1334c.md "GetAdditionalRevisionIds Method") to get the additionally added revisions. 
# See Also
[ViewSheet Class](af2ee879-173d-df3a-9793-8d5750a17b49.md "ViewSheet Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)