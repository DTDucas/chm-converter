# AddConnectedAsset Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
AssetProperty..::..AddConnectedAsset Method   
[AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.md "AssetProperty Class") See Also  
---  
Adds a new connected asset attached to this asset property, if it allows it. 
**Namespace:** [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.md "Autodesk.Revit.DB.Visual Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2018.1 
# Syntax
C#  
---  
```text
public void AddConnectedAsset(
	string schema
)
```
  
Visual Basic  
---  
```text
Public Sub AddConnectedAsset ( _
	schema As String _
)
```
  
Visual C++  
---  
```text
public:
void AddConnectedAsset(
	String^ schema
)
```
  
# ### Parameters
schema
    Type: System..::..String The schema name. 
# Remarks
Cannot add a connected asset if one is already connected. Use RemoveConnectedAsset() to avoid an exception being thrown. A new preset asset is created and connected to the property. For "UnifiedBitmap", it contains an empty property unifiedbitmap_Bitmap. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The schema name is not valid. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The asset property is not editable. -or- Cannot check validity for a property not being edited in AppearanceAssetEditScope. -or- Asset property is already connected to one asset. |

# See Also
[AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.md "AssetProperty Class")
[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.md "Autodesk.Revit.DB.Visual Namespace")
Send comments on this topic to 