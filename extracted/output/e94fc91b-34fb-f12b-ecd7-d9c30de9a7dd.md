# SetFilter Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ReferenceIntersector..::..SetFilter Method   
[ReferenceIntersector Class](36f82b40-1065-2305-e260-18fc618e756f.md "ReferenceIntersector Class") See Also  
---  
Sets the ElementFilter used in intersection testing. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public void SetFilter(
	ElementFilter filter
)
```
  
Visual Basic  
---  
```text
Public Sub SetFilter ( _
	filter As ElementFilter _
)
```
  
Visual C++  
---  
```text
public:
void SetFilter(
	ElementFilter^ filter
)
```
  
# ### Parameters
filter
    Type: [Autodesk.Revit.DB..::..ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md "ElementFilter Class") The ElementFilter. Pass nullNothingnullptra null reference (Nothing in Visual Basic) to remove the existing filter. 
# See Also
[ReferenceIntersector Class](36f82b40-1065-2305-e260-18fc618e756f.md "ReferenceIntersector Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)