# GetNonControlledTemplateParameterIds Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
View..::..GetNonControlledTemplateParameterIds Method   
[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.md "View Class") See Also  
---  
Returns a list of parameters that are not marked as included when this view is used as a template. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public ICollection<ElementId> GetNonControlledTemplateParameterIds()
```
  
Visual Basic  
---  
```text
Public Function GetNonControlledTemplateParameterIds As ICollection(Of ElementId)
```
  
Visual C++  
---  
```text
public:
ICollection<ElementId^>^ GetNonControlledTemplateParameterIds()
```
  
# ### Return Value
The parameter ids that are not marked to be included. 
# Remarks
This is a subset of the parameters returned by [GetTemplateParameterIds()()()()](64761c8c-ed01-65b6-2b05-ebd7b02acd77.md "GetTemplateParameterIds Method"). 
# See Also
[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.md "View Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)