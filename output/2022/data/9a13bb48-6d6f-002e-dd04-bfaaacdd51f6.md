# SubVersionNumber Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ControlledApplication..::..SubVersionNumber Property   
[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.md "ControlledApplication Class") See Also  
---  
The minor version number of Revit 
**Namespace:** [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.md "Autodesk.Revit.ApplicationServices Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2018 
# Syntax
C#  
---  
```text
public string SubVersionNumber { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property SubVersionNumber As String
	Get
```
  
Visual C++  
---  
```text
public:
property String^ SubVersionNumber {
	String^ get ();
}
```
  
# Remarks
SubVersionNumber of Revit may have additional APIs and functionality not available in the standard customer releases. Add-ins written to support standard Revit releases should be compatible with SubVersionNumber releases, but add-ins written specifically targeting new features in SubVersionNumber releases would not be compatible with the standard releases. 
# See Also
[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.md "ControlledApplication Class")
[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.md "Autodesk.Revit.ApplicationServices Namespace")
Send comments on this topic to 