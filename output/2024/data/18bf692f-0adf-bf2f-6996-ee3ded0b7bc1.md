# SetElementsToDimension Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
MultiReferenceAnnotationOptions..::..SetElementsToDimension Method   
[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.md "MultiReferenceAnnotationOptions Class") See Also  
---  
Sets the elements which the dimension will witness. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public void SetElementsToDimension(
	ICollection<ElementId> elementsToDimension
)
```
  
Visual Basic  
---  
```text
Public Sub SetElementsToDimension ( _
	elementsToDimension As ICollection(Of ElementId) _
)
```
  
Visual C++  
---  
```text
public:
void SetElementsToDimension(
	ICollection<ElementId^>^ elementsToDimension
)
```
  
# ### Parameters
elementsToDimension
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> The elements which the dimension will witness. 
# Remarks
The dimension will automatically find geometric references in the elements. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | some elements do not match the reference category required by the MultiReferenceAnnotationType. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The MultiReferenceAnnotationType assigned to the options can't create MultiReferenceAnnotations by element. |

# See Also
[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.md "MultiReferenceAnnotationOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 