# ImageRowHeight Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
ViewSchedule..::..ImageRowHeight Property   
[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md "ViewSchedule Class") See Also  
---  
Defines the image row height in the schedule. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public double ImageRowHeight { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ImageRowHeight As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double ImageRowHeight {
	double get ();
	void set (double value);
}
```
  
# ### Field Value
The row height for any rows containing images in the schedule. The value is 0.0 by default if not customized. 
# Remarks
If there is at least one image field in the schedule, then setting this property will force all rows containing images to be resized to the indicated height value (when viewed as a ScheduleSheetInstance on a ViewSheet). Setting this property will have no effect if HasImageField returns false. 
This height will be maintained until the user or application restores the original image sizes (in API: [RestoreImageSize()()()()](e9c47953-6070-46ac-5d24-cef0a9cd5b51.md "RestoreImageSize Method")). 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: The given value for imageRowHeight must be greater than 0 and no more than 30000 feet. |

# See Also
[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md "ViewSchedule Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 