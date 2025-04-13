

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
PlanViewRange Class  
[Members](a4646f2b-a4ae-f631-196e-e0aaf4e9576f.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
This class represents the view range of a plan view or a plan region. It records the element ids of the levels which a plane is relative to and the offset of each plane from that level. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 

# Syntax

C#  
---  
      
    
    public class PlanViewRange : IDisposable  
  
Visual Basic  
---  
      
    
    Public Class PlanViewRange _
    	Implements IDisposable  
  
Visual C++  
---  
      
    
    public ref class PlanViewRange : IDisposable  
  
# Examples

CopyC#
    
    
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

CopyVB.NET
    
    
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

# Inheritance Hierarchy

System..::..Object Autodesk.Revit.DB..::..PlanViewRange

# See Also

[PlanViewRange Members](a4646f2b-a4ae-f631-196e-e0aaf4e9576f.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)