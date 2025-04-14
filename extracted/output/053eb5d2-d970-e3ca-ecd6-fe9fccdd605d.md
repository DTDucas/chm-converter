# GetHtmlDescription Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
IPipePlumbingFixtureFlowServer..::..GetHtmlDescription Method   
[IPipePlumbingFixtureFlowServer Interface](ef369072-84eb-cace-a564-335aed35626b.md "IPipePlumbingFixtureFlowServer Interface") See Also  
---  
The method that Revit will invoke to get an HTML formatted description of the server. 
**Namespace:** [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.md "Autodesk.Revit.DB.Plumbing Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
string GetHtmlDescription()
```
  
Visual Basic  
---  
```text
Function GetHtmlDescription As String
```
  
Visual C++  
---  
```text
String^ GetHtmlDescription()
```
  
# ### Return Value
The HTML format description of the server. 
# Remarks
The HTML description is used by Revit unless it is empty or the server is not available, in which case, Revit will use the plain text description from IExternalServer.GetDescription(). 
# See Also
[IPipePlumbingFixtureFlowServer Interface](ef369072-84eb-cace-a564-335aed35626b.md "IPipePlumbingFixtureFlowServer Interface")
[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.md "Autodesk.Revit.DB.Plumbing Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)