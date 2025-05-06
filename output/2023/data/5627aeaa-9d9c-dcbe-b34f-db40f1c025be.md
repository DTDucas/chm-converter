# IsCancelled Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
RevitAPIEventArgs..::..IsCancelled Method   
[RevitAPIEventArgs Class](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class") See Also  
---  
Indicates whether the event is being cancelled. 
**Namespace:** [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.md "Autodesk.Revit.DB.Events Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public bool IsCancelled()
```
  
Visual Basic  
---  
```text
Public Function IsCancelled As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsCancelled()
```
  
# Remarks
If the event is cancellable and an event delegate wishes to cancel the event, it may call the Cancel() method if it is available for a particular event's arguments. 
# See Also
[RevitAPIEventArgs Class](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class")
[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.md "Autodesk.Revit.DB.Events Namespace")
Send comments on this topic to 