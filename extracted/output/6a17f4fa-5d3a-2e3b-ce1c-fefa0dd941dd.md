

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
PathReinforcement..::..GetCurveElementIds Method   
[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Retrieves the set of ElementIds of curves forming the boundary of the Path Reinforcement. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public IList<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> GetCurveElementIds()  
  
Visual Basic  
---  
      
    
    Public Function GetCurveElementIds As IList(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md))  
  
Visual C++  
---  
      
    
    public:
    IList<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ GetCurveElementIds()  
  
#### Return Value

A collection of ElementIds of ModelCurve elements. 

# Remarks

Each ElementId in the collection is an Id of an Element of type ModelCurve. 

# Examples

CopyC#
    
    
    private void Getinfo_PathReinforcementCurve(PathReinforcement pathReinforcement)
    {
        string message = "Path Reinforcement Curves : ";
    
        // Get path reinforcement curves by iterating the Curves property
        IList<ElementId> curveIds = pathReinforcement.GetCurveElementIds();
        foreach (Autodesk.Revit.DB.ElementId ii in curveIds)
        {
            ModelCurve pathReinforcementCurve = doc.GetElement(ii) as ModelCurve;
            if (null == pathReinforcementCurve)
            {
                continue;
            }
    
            Autodesk.Revit.DB.Curve curve = pathReinforcementCurve.GeometryCurve;
    
            // Get curve start point
            message += "\nCurve start point:(" + curve.GetEndPoint(0).X + ", "
                + curve.GetEndPoint(0).Y + ", " + curve.GetEndPoint(0).Z + ")";
            // Get curve end point
            message += "; Curve end point:(" + curve.GetEndPoint(1).X + ", "
                + curve.GetEndPoint(1).Y + ", " + curve.GetEndPoint(1).Z + ")";
    
    
        }
        TaskDialog.Show("Revit", message);
    
    }

CopyVB.NET
    
    
    Private Sub Getinfo_PathReinforcementCurve(pathReinforcement As PathReinforcement)
        Dim message As String = "Path Reinforcement Curves : "
    
        ' Get path reinforcement curves by iterating the Curves property
        Dim curveIds As IList(Of ElementId) = pathReinforcement.GetCurveElementIds()
        For Each ii As Autodesk.Revit.DB.ElementId In curveIds
            Dim pathReinforcementCurve As ModelCurve = TryCast(doc.GetElement(ii), ModelCurve)
            If pathReinforcementCurve Is Nothing Then
                Continue For
            End If
    
            Dim curve As Autodesk.Revit.DB.Curve = pathReinforcementCurve.GeometryCurve
    
            ' Get curve start point
            message += ((vbLf & "Curve start point:(" + curve.GetEndPoint(0).X & ", ") + curve.GetEndPoint(0).Y & ", ") + curve.GetEndPoint(0).Z & ")"
            ' Get curve end point
    
    
    
            message += (("; Curve end point:(" + curve.GetEndPoint(1).X & ", ") + curve.GetEndPoint(1).Y & ", ") + curve.GetEndPoint(1).Z & ")"
        Next
        TaskDialog.Show("Revit", message)
    
    End Sub

# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)