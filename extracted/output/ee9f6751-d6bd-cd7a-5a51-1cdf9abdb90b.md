# GetDoubleValue Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ColorFillSchemeEntry..::..GetDoubleValue Method   
[ColorFillSchemeEntry Class](065ddef3-065a-8bd5-9d34-4d2efd126e43.md "ColorFillSchemeEntry Class") See Also  
---  
Gets the Double value stored within the entry. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2022 
# Syntax
C#  
---  
```text
public double GetDoubleValue()
```
  
Visual Basic  
---  
```text
Public Function GetDoubleValue As Double
```
  
Visual C++  
---  
```text
public:
double GetDoubleValue()
```
  
# ### Return Value
The Double value contained in the entry. 
# Remarks
This method should only be used if the [StorageType](45659568-cb90-6712-3355-120f7cff9dd4.md "StorageType Property") property reports the type of the entry as a Double. 
# See Also
[ColorFillSchemeEntry Class](065ddef3-065a-8bd5-9d34-4d2efd126e43.md "ColorFillSchemeEntry Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)