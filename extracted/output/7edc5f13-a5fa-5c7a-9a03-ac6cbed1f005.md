# PlanViewRange Class

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
PlanViewRange Class  
[Members](a4646f2b-a4ae-f631-196e-e0aaf4e9576f.md "PlanViewRange Members") Example See Also  
---  
This class represents the view range of a plan view or a plan region. It records the element ids of the levels which a plane is relative to and the offset of each plane from that level. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public class PlanViewRange : IDisposable
```
  
Visual Basic  
---  
```text
Public Class PlanViewRange _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class PlanViewRange : IDisposable
```
  
# Examples
CopyC#
```text
private ElementId GetViewRangeTopClipPlane(Document doc, View view)
{
    ElementId topClipPlane = ElementId.InvalidElementId;

    if (view is ViewPlan)
    {
        ViewPlan viewPlan = view as ViewPlan;
        PlanViewRange viewRange = viewPlan.GetViewRange();

        topClipPlane = viewRange.GetLevelId(PlanViewPlane.TopClipPlane);
        double dOffset = viewRange.GetOffset(PlanViewPlane.TopClipPlane);

        if (topClipPlane != ElementId.InvalidElementId)
        {
            Element levelAbove = doc.GetElement(topClipPlane);
            TaskDialog.Show(view.Name, "Top Clip Plane: " + levelAbove.Name + "\r\nTop Offset: " + dOffset + " ft");
        }
    }

    return topClipPlane;
}
```

CopyVB.NET
```text
Private Function GetViewRangeTopClipPlane(doc As Document, view As View) As ElementId
    Dim topClipPlane As ElementId = ElementId.InvalidElementId

    If TypeOf view Is ViewPlan Then
        Dim viewPlan As ViewPlan = TryCast(view, ViewPlan)
        Dim viewRange As PlanViewRange = viewPlan.GetViewRange()

        topClipPlane = viewRange.GetLevelId(PlanViewPlane.TopClipPlane)
        Dim dOffset As Double = viewRange.GetOffset(PlanViewPlane.TopClipPlane)

        If topClipPlane.Value > 0 Then
            Dim levelAbove As Element = doc.GetElement(topClipPlane)
            TaskDialog.Show(view.Name, "Top Clip Plane: " + levelAbove.Name + vbCr & vbLf & "Top Offset: " + dOffset + " ft")
        End If
    End If

    Return topClipPlane
End Function
```

# Inheritance Hierarchy
System..::..Object Autodesk.Revit.DB..::..PlanViewRange
# See Also
[PlanViewRange Members](a4646f2b-a4ae-f631-196e-e0aaf4e9576f.md "PlanViewRange Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)