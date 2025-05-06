# PickObjects Method (ObjectType, ISelectionFilter) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Selection..::..PickObjects Method (ObjectType, ISelectionFilter)  
[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.md "Selection Class") See Also  
---  
Prompts the user to select multiple objects which pass a customer filter.
**Namespace:** [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.md "Autodesk.Revit.UI.Selection Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public IList<Reference> PickObjects(
	ObjectType objectType,
	ISelectionFilter selectionFilter
)
```
  
Visual Basic  
---  
```text
Public Function PickObjects ( _
	objectType As ObjectType, _
	selectionFilter As ISelectionFilter _
) As IList(Of Reference)
```
  
Visual C++  
---  
```text
public:
IList<Reference^>^ PickObjects(
	ObjectType objectType, 
	ISelectionFilter^ selectionFilter
)
```
  
# ### Parameters
objectType
    Type: [Autodesk.Revit.UI.Selection..::..ObjectType](2d0cbbba-d4ab-84b7-b081-36c14769d82c.md "ObjectType Enumeration")Specifies the type of object to be selected.
selectionFilter
    Type: [Autodesk.Revit.UI.Selection..::..ISelectionFilter](d552f44b-221c-0ecd-d001-41a5099b2f9f.md "ISelectionFilter Interface")The selection filter.
# ### Return Value
A collection of references selected by the user.
Note: if the user cancels the operation (for example, through ESC), the method will throw an OperationCanceledException instance. 
# Remarks
The user will be shown "Finish" and "Cancel" buttons on the dialog bar to complete the selection operation. Uncheck the "Multiple" check-box to select single object and it will return the selected object directly.
Revit users will be permitted to manipulate the Revit view (zooming, panning, and rotating the view), but will not be permitted to click other items in the Revit user interface. Users are not permitted to switch the active view, close the active document or Revit application in the pick session, otherwise an exception will be thrown.
The selection will not be automatically added to the active selection buffer.
Note: this method must not be called during dynamic update, otherwise ForbiddenForDynamicUpdateException will be thrown.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | Thrown when the objectType is not a recognized value. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | Thrown when the selectionFilter is nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.md "OperationCanceledException Class") | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |
| [Autodesk.Revit.Exceptions..::..ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.md "ForbiddenForDynamicUpdateException Class") | Thrown if this method is called during dynamic update. |

# See Also
[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.md "Selection Class")
[PickObjects Overload](e5a547a2-3cf5-7638-2daa-ea85b4d3de2d.md "PickObjects Method")
[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.md "Autodesk.Revit.UI.Selection Namespace")
Send comments on this topic to 