# IsValidValue Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
AssetPropertyDoubleArray3d..::..IsValidValue Method   
[AssetPropertyDoubleArray3d Class](f0623332-e4b1-3b6f-7247-8ee16a27251c.md "AssetPropertyDoubleArray3d Class") See Also  
---  
Checks that the value is a valid value for this property. 
**Namespace:** [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.md "Autodesk.Revit.DB.Visual Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2018.1 
# Syntax
C#  
---  
```text
public bool IsValidValue(
	XYZ xyz
)
```
  
Visual Basic  
---  
```text
Public Function IsValidValue ( _
	xyz As XYZ _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsValidValue(
	XYZ^ xyz
)
```
  
# ### Parameters
xyz
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class") The value to be checked. 
# ### Return Value
True if the value is valid for the property. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Cannot check validity for a property not being edited in AppearanceAssetEditScope. |

# See Also
[AssetPropertyDoubleArray3d Class](f0623332-e4b1-3b6f-7247-8ee16a27251c.md "AssetPropertyDoubleArray3d Class")
[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.md "Autodesk.Revit.DB.Visual Namespace")
Send comments on this topic to 