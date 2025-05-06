# SetProjection Method (AnalyticalElementSelector, ElementId, StickElementProjectionZ) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
AnalyticalModelStick..::..SetProjection Method (AnalyticalElementSelector, ElementId, StickElementProjectionZ)  
[AnalyticalModelStick Class](f9554dde-c9c3-dbb5-d603-0b922bc51fd9.md "AnalyticalModelStick Class") Example See Also  
---  
Sets the analytical model projection to a preset value. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public void SetProjection(
	AnalyticalElementSelector selector,
	ElementId planeIdY,
	StickElementProjectionZ projectionZ
)
```
  
Visual Basic  
---  
```text
Public Sub SetProjection ( _
	selector As AnalyticalElementSelector, _
	planeIdY As ElementId, _
	projectionZ As StickElementProjectionZ _
)
```
  
Visual C++  
---  
```text
public:
void SetProjection(
	AnalyticalElementSelector selector, 
	ElementId^ planeIdY, 
	StickElementProjectionZ projectionZ
)
```
  
# ### Parameters
selector
    Type: [Autodesk.Revit.DB.Structure..::..AnalyticalElementSelector](b8d93e4d-3543-637d-5a9d-affa1bced099.md "AnalyticalElementSelector Enumeration") End of the analytical model. 
planeIdY
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") Plane on to which analytical model may be projected in Y direction. Plane identifies a Level, a Grid, or a Ref Plane. 
projectionZ
    Type: [Autodesk.Revit.DB.Structure..::..StickElementProjectionZ](174346c5-e7f3-58f1-1495-3836c9f973e3.md "StickElementProjectionZ Enumeration") Preset value for Analytical Model Stick projection Z. 
# Examples
CopyC#
```text
public void ChangeBeamProjection(FamilyInstance familyInstance)
{
    AnalyticalModelStick ams = familyInstance.GetAnalyticalModel() as AnalyticalModelStick;
    if (ams != null)
    {
         // Change the Z projection for the end of the beam
         StickElementProjectionZ orgEndProj = ams.GetProjectionZ(AnalyticalElementSelector.EndOrTop);
         StickElementProjectionZ newEndProj = StickElementProjectionZ.Bottom;
         using (Transaction tran = new Transaction(familyInstance.Document, "ChangeProjection"))
         {
             tran.Start();
             ams.SetProjection(AnalyticalElementSelector.EndOrTop, ElementId.InvalidElementId, newEndProj);
             tran.Commit();
         }

         TaskDialog.Show("AnalyticalModelStick", "AnalyticalModelStick ID: " + ams.Id + "; \nOriginal ProjectionZ value was: " + orgEndProj + "; \nNew ProjectionZ value: " + newEndProj);
    }
}
```

CopyVB.NET
```text
Public Sub ChangeBeamProjection(familyInstance As FamilyInstance)
   Dim ams As AnalyticalModelStick = TryCast(familyInstance.GetAnalyticalModel(), AnalyticalModelStick)
   If ams IsNot Nothing Then
      ' Change the Z projection for the end of the beam
      Dim orgEndProj As StickElementProjectionZ = ams.GetProjectionZ(AnalyticalElementSelector.EndOrTop)
      Dim newEndProj As StickElementProjectionZ = StickElementProjectionZ.Bottom
      Using tran As New Transaction(familyInstance.Document, "ChangeProjection")
         tran.Start()
         ams.SetProjection(AnalyticalElementSelector.EndOrTop, ElementId.InvalidElementId, newEndProj)
         tran.Commit()
      End Using

      TaskDialog.Show("AnalyticalModelStick", "AnalyticalModelStick ID: " + ams.Id.ToString + "; " & vbLf & "Original ProjectionZ value was: " + orgEndProj + "; " & vbLf & "New ProjectionZ value: " + newEndProj)
   End If
End Sub
```

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[AnalyticalModelStick Class](f9554dde-c9c3-dbb5-d603-0b922bc51fd9.md "AnalyticalModelStick Class")
[SetProjection Overload](13de285e-7d46-b5a4-be0b-3223ecc813bd.md "SetProjection Method")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 