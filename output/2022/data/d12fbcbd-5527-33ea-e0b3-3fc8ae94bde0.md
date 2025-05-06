# Value Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
AssetPropertyBoolean..::..Value Property   
[AssetPropertyBoolean Class](ad822813-a51f-cf85-3252-5fe21b4d701b.md "AssetPropertyBoolean Class") See Also  
---  
The value of the property. 
**Namespace:** [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.md "Autodesk.Revit.DB.Visual Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public bool Value { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Value As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool Value {
	bool get ();
	void set (bool value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: The input value is invalid for this AssetPropertyBoolean property. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | When setting this property: The asset property is not editable. |

# See Also
[AssetPropertyBoolean Class](ad822813-a51f-cf85-3252-5fe21b4d701b.md "AssetPropertyBoolean Class")
[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.md "Autodesk.Revit.DB.Visual Namespace")
Send comments on this topic to 