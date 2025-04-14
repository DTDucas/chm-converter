# PickElementsByRectangle Method (String)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Selection..::..PickElementsByRectangle Method (String)  
[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.md "Selection Class") Example See Also  
---  
Prompts the user to select multiple elements by drawing a rectangle while showing a custom status prompt string.
**Namespace:** [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.md "Autodesk.Revit.UI.Selection Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public IList<Element> PickElementsByRectangle(
	string statusPrompt
)
```
  
Visual Basic  
---  
```text
Public Function PickElementsByRectangle ( _
	statusPrompt As String _
) As IList(Of Element)
```
  
Visual C++  
---  
```text
public:
IList<Element^>^ PickElementsByRectangle(
	String^ statusPrompt
)
```
  
# ### Parameters
statusPrompt
    Type: System..::..StringThe message shown on the status bar.
# ### Return Value
A collection of elements selected by the user. 
Note: if the user cancels the operation (for example, through ESC), the method will throw an OperationCanceledException instance. 
# Remarks
Revit users will be permitted to manipulate the Revit view (zooming, panning, and rotating the view), but will not be permitted to click other items in the Revit user interface. Users are not permitted to switch the active view, close the active document or Revit application in the pick session, otherwise an exception will be thrown.
The selection will not be automatically added to the active selection buffer.
Note: this method must not be called during dynamic update, otherwise ForbiddenForDynamicUpdateException will be thrown.
# Examples
CopyC#
```text
// Use the rectangle picking tool to identify model elements to select.
IList<Element> pickedElements = uidoc.Selection.PickElementsByRectangle("Select by rectangle");
if (pickedElements.Count > 0)
{ 
    // Collect Ids of all picked elements
    IList<ElementId> idsToSelect = new List<ElementId>(pickedElements.Count);
    foreach (Element element in pickedElements)
    {
        idsToSelect.Add(element.Id);
    }

    // Update the current selection
    uidoc.Selection.SetElementIds(idsToSelect);
    TaskDialog.Show("Revit", string.Format("{0} elements added to Selection.", idsToSelect.Count));
}
```

CopyVB.NET
```text
' Use the rectangle picking tool to identify model elements to select.
Dim pickedElements As IList(Of Element) = uidoc.Selection.PickElementsByRectangle("Select by rectangle")
If pickedElements.Count > 0 Then
    ' Collect Ids of all picked elements
    Dim idsToSelect As IList(Of ElementId) = New List(Of ElementId)(pickedElements.Count)
    For Each element As Element In pickedElements
        idsToSelect.Add(element.Id)
    Next

    ' Update the current selection
    uidoc.Selection.SetElementIds(idsToSelect)
    TaskDialog.Show("Revit", String.Format("{0} elements added to Selection.", idsToSelect.Count))
End If
```

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | Thrown when the statusPrompt is nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.md "OperationCanceledException Class") | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |
| [Autodesk.Revit.Exceptions..::..ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.md "ForbiddenForDynamicUpdateException Class") | Thrown if this method is called during dynamic update. |

# See Also
[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.md "Selection Class")
[PickElementsByRectangle Overload](b486efdd-0c0d-589f-2dfd-b16d32dca046.md "PickElementsByRectangle Method")
[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.md "Autodesk.Revit.UI.Selection Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)