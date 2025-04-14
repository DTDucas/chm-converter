# TextRange Class

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
TextRange Class  
[Members](3036d128-6be4-2e14-a1b4-fae307429140.md "TextRange Members") See Also  
---  
An object that is used to identify a range of characters in a [FormattedText](79a92343-2342-8325-1b51-f12c4fb05481.md "FormattedText Class"). 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public class TextRange : IDisposable
```
  
Visual Basic  
---  
```text
Public Class TextRange _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class TextRange : IDisposable
```
  
# Remarks
A TextRange consists of a start, which is a zero-based index into the text, and a length, which is the number of characters in the range. The length can be zero. 
# Inheritance Hierarchy
System..::..Object Autodesk.Revit.DB..::..TextRange
# See Also
[TextRange Members](3036d128-6be4-2e14-a1b4-fae307429140.md "TextRange Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)