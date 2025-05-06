# BoundingBox Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
Element..::..BoundingBox Property   
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") Example See Also  
---  
Retrieves a box that circumscribes all geometry of the element.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public BoundingBoxXYZ this[
	View A_0
] { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property BoundingBox ( _
	A_0 As View _
) As BoundingBoxXYZ
	Get
```
  
Visual C++  
---  
```text
public:
property BoundingBoxXYZ^ BoundingBox[View^ A_0] {
	BoundingBoxXYZ^ get (View^ A_0);
}
```
  
# ### Parameters
A_0
    Type: [Autodesk.Revit.DB..::..View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md "View Class")
# Remarks
Pass in a view to query view-specific (e.g., cut) geometry or nullNothingnullptra null reference (Nothing in Visual Basic) for model geometry. If the view box is not known or cannot be calculated, this will return the model box; if the model box is not known, this will return nullNothingnullptra null reference (Nothing in Visual Basic). The box will always be aligned to the default axes of the model coordinate system (thus no rotation should be applied to the return value). Also note that this bounding box volume may enclose geometry that is not obvious. For example, the "flip controls" that could be part of a family will be included in the computation of the bounding box even though they are not always visible in the family instance of the family.
# Examples
CopyC#
```text
private void GetElementBoundingBox(Autodesk.Revit.DB.Document document, Autodesk.Revit.DB.Element element)
{
    // Get the BoundingBox instance for current view.
    BoundingBoxXYZ box = element.get_BoundingBox(document.ActiveView);
    if (null == box)
    {
        throw new Exception("Selected element doesn't contain a bounding box.");
    }

    string info = "Bounding box is enabled: " + box.Enabled.ToString();

    // Give the user some information.
    TaskDialog.Show("Revit",info);
}
```

CopyVB.NET
```text
Private Sub GetElementBoundingBox(document As Autodesk.Revit.DB.Document, element As Autodesk.Revit.DB.Element)
    ' Get the BoundingBox instance for current view.
    Dim box As BoundingBoxXYZ = element.BoundingBox(document.ActiveView)
    If box Is Nothing Then
        Throw New Exception("Selected element doesn't contain a bounding box.")
    End If

    Dim info As String = "Bounding box is enabled: " & box.Enabled.ToString()

    ' Give the user some information.
    TaskDialog.Show("Revit", info)
End Sub
```

# See Also
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 