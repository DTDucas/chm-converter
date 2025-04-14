# GetFaceReferences Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
MassSurfaceData..::..GetFaceReferences Method   
[MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.md "MassSurfaceData Class") See Also  
---  
Gets References to the faces that the MassSurfaceData provides properties for. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public IList<Reference> GetFaceReferences()
```
  
Visual Basic  
---  
```text
Public Function GetFaceReferences As IList(Of Reference)
```
  
Visual C++  
---  
```text
public:
IList<Reference^>^ GetFaceReferences()
```
  
# ### Return Value
Returns an array of References to Faces that the MassSurfaceData provides properties for. 
# Remarks
The results are always references to Faces. The Reference Type should be REFERENCE_TYPE_SURFACE. Currently Revit improperly reports it as REFERENCE_TYPE_NONE. 
# See Also
[MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.md "MassSurfaceData Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)