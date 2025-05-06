# GetAllSpecs Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
UnitUtils..::..GetAllSpecs Method   
[UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.md "UnitUtils Class") See Also  
---  
Gets the identifiers of all available specs. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
[ObsoleteAttribute("This method is deprecated in Revit 2022 and may be removed in a future version of Revit. Please use the `GetAllMeasurableSpecs()` method instead.")]
public static IList<ForgeTypeId> GetAllSpecs()
```
  
Visual Basic  
---  
```text
<ObsoleteAttribute("This method is deprecated in Revit 2022 and may be removed in a future version of Revit. Please use the `GetAllMeasurableSpecs()` method instead.")> _
Public Shared Function GetAllSpecs As IList(Of ForgeTypeId)
```
  
Visual C++  
---  
```text
[ObsoleteAttribute(L"This method is deprecated in Revit 2022 and may be removed in a future version of Revit. Please use the `GetAllMeasurableSpecs()` method instead.")]
public:
static IList<ForgeTypeId^>^ GetAllSpecs()
```
  
# ### Return Value
The spec identifiers. 
# See Also
[UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.md "UnitUtils Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 