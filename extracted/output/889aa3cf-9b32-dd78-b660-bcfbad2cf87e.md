

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
AreaReinforcement Class  
[Members](9df1087e-e276-d4d7-76d6-99a2bb7daad2.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
An object that represents an Area Reinforcement within the Autodesk Revit project. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public class AreaReinforcement : [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
Visual Basic  
---  
      
    
    Public Class AreaReinforcement _
    	Inherits [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
Visual C++  
---  
      
    
    public ref class AreaReinforcement : public [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
# Remarks

This object derived from the Element base object and such supports all the methods of that object such as the ability to retrieve the parameters of that object. The Area Reinforcement element is available only in the Autodesk Revit Structure product. 

# Examples

CopyC#
    
    
    public void GetInfo_AreaReinforcement(AreaReinforcement areaReinforcement)
    {
        string message = "AreaReinforcement : ";
    
        // Show the AreaReinforcement Type information
        //message += "\nType : " + areaReinforcement.AreaReinforcementType.Name;
    
        // Show the AreaReinforcement bar information
        IList<ElementId> rebarInSystemIds = areaReinforcement.GetRebarInSystemIds();
        message += "\nNumber of distinct bar shapes : " + rebarInSystemIds.Count;
    
        for (int i = 0; i < rebarInSystemIds.Count; i++)
        {
            RebarInSystem ris = doc.GetElement(rebarInSystemIds[0]) as RebarInSystem;
            message += "\nBar count : " + ris.Quantity;
            message += "\nBar type name : " + ris.Name;
            message += "\nBar length : " + ris.LookupParameter("Bar Length").AsDouble();
        }
    
        // Show the AreaReinforcement Curves information
        IList<ElementId> curveIds = areaReinforcement.GetBoundaryCurveIds();
        message += "\nArea Reinforcement has " + curveIds.Count + " boundary curves.";
        foreach (Autodesk.Revit.DB.ElementId ii in curveIds)
        {
            AreaReinforcementCurve reinCurve = doc.GetElement(ii) as AreaReinforcementCurve;
            if (null == reinCurve)
            {
                continue;
            }
            Curve curve = reinCurve.Curve; // get the location curve
            XYZ start = curve.GetEndPoint(0);  // get the start point of the curve
            XYZ end = curve.GetEndPoint(1);    // get the end point of the curve
            message += "\nCurve: Start point (" + start.X + ", " + start.Y + ", " + start.Z + ")";
            message += "\n       End point (" + end.X + ", " + end.Y + ", " + end.Z + ")";
        }
    
        TaskDialog.Show("Revit", message);
    }

CopyVB.NET
    
    
    Public Sub GetInfo_AreaReinforcement(areaReinforcement As AreaReinforcement)
        Dim message As String = "AreaReinforcement : "
    
        ' Show the AreaReinforcement Type information
        'message += "\nType : " + areaReinforcement.AreaReinforcementType.Name;
    
    
        ' Show the AreaReinforcement bar information
        Dim rebarInSystemIds As IList(Of ElementId) = areaReinforcement.GetRebarInSystemIds()
        message += vbLf & "Number of distinct bar shapes : " & rebarInSystemIds.Count
    
        For i As Integer = 0 To rebarInSystemIds.Count - 1
            Dim ris As RebarInSystem = TryCast(doc.GetElement(rebarInSystemIds(0)), RebarInSystem)
            message += vbLf & "Bar count : " + ris.Quantity
            message += vbLf & "Bar type name : " + ris.Name
            message += vbLf & "Bar length : " & ris.LookupParameter("Bar Length").AsDouble()
        Next
    
        ' Show the AreaReinforcement Curves information
        Dim curveIds As IList(Of ElementId) = areaReinforcement.GetBoundaryCurveIds()
        message += vbLf & "Area Reinforcement has " & curveIds.Count & " boundary curves."
        For Each ii As Autodesk.Revit.DB.ElementId In curveIds
            Dim reinCurve As AreaReinforcementCurve = TryCast(doc.GetElement(ii), AreaReinforcementCurve)
            If reinCurve Is Nothing Then
                Continue For
            End If
            Dim curve As Curve = reinCurve.Curve
            ' get the location curve
            Dim start As XYZ = curve.GetEndPoint(0)
            ' get the start point of the curve
            Dim [end] As XYZ = curve.GetEndPoint(1)
            ' get the end point of the curve
            message += ((vbLf & "Curve: Start point (" + start.X & ", ") + start.Y & ", ") + start.Z & ")"
            message += ((vbLf & "       End point (" + [end].X & ", ") + [end].Y & ", ") + [end].Z & ")"
        Next
    
        TaskDialog.Show("Revit", message)
    End Sub

# Inheritance Hierarchy

System..::..Object [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) Autodesk.Revit.DB.Structure..::..AreaReinforcement

# See Also

[AreaReinforcement Members](9df1087e-e276-d4d7-76d6-99a2bb7daad2.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)