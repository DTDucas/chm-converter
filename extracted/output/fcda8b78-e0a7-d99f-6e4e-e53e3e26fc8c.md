

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
VectorAtPoint Class  
[Members](d2038b2b-73d0-45d9-249a-541f256fa249.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Stores vectors at one domain point. Each vector corresponds to a "measurement" for which this vector was calculated. 

**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 

# Syntax

C#  
---  
      
    
    public class VectorAtPoint : [ValueAtPointBase](67c49547-b5b9-59ad-8106-65d90886a381.md)  
  
Visual Basic  
---  
      
    
    Public Class VectorAtPoint _
    	Inherits [ValueAtPointBase](67c49547-b5b9-59ad-8106-65d90886a381.md)  
  
Visual C++  
---  
      
    
    public ref class VectorAtPoint : public [ValueAtPointBase](67c49547-b5b9-59ad-8106-65d90886a381.md)  
  
# Examples

CopyC#
    
    
    // Place analysis results in the form of vectors at each of a beam or column's analytical model curve
    Transform transform = analyticalElem.GetTransform();
    int index = spatialFieldManager.AddSpatialFieldPrimitive(curve, Transform.Identity);
    
    IList<double> doubleList = new List<double>();
    doubleList.Add(curve.GetEndParameter(0)); // vectors will be at each end of the analytical model curve
    doubleList.Add(curve.GetEndParameter(1));
    FieldDomainPointsByParameter pointsByParameter = new FieldDomainPointsByParameter(doubleList);
    
    List<XYZ> xyzList = new List<XYZ>();
    xyzList.Add(curve.ComputeDerivatives(0, true).BasisX.Normalize()); // vectors will be tangent to the curve at its ends
    IList<VectorAtPoint> vectorList = new List<VectorAtPoint>();
    vectorList.Add(new VectorAtPoint(xyzList));
    xyzList.Clear();
    xyzList.Add(curve.ComputeDerivatives(1, true).BasisX.Normalize().Negate());
    vectorList.Add(new VectorAtPoint(xyzList));
    FieldValues fieldValues = new FieldValues(vectorList);

CopyVB.NET
    
    
    ' Place analysis results in the form of vectors at each of a beam or column's analytical model curve
    Dim analyticalModel As Autodesk.Revit.DB.Structure.AnalyticalElement = Nothing
    Dim relManager As Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager = Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(doc)
    
    If (relManager Is Nothing) Then
       Exit Sub
    End If
    
       Dim counterpartId As ElementId = relManager.GetAssociatedElementId(familyInstance.Id)
       If (counterpartId Is Nothing) Then
       Exit Sub
    End If
    
    analyticalModel = doc.GetElement(counterpartId)
    
    Dim curve As Curve = analyticalModel.GetCurve()
    Dim transform__1 As Transform = familyInstance.GetTransform()
       Dim index As Integer = spatialFieldManager.AddSpatialFieldPrimitive(curve, Transform.Identity)
    
       Dim doubleList As IList(Of Double) = New List(Of Double)()
       doubleList.Add(curve.GetEndParameter(0))
       ' vectors will be at each end of the analytical model curve
       doubleList.Add(curve.GetEndParameter(1))
       Dim pointsByParameter As New FieldDomainPointsByParameter(doubleList)
    
       Dim xyzList As New List(Of XYZ)()
       xyzList.Add(curve.ComputeDerivatives(0, True).BasisX.Normalize())
       ' vectors will be tangent to the curve at its ends
       Dim vectorList As IList(Of VectorAtPoint) = New List(Of VectorAtPoint)()
       vectorList.Add(New VectorAtPoint(xyzList))
       xyzList.Clear()
       xyzList.Add(curve.ComputeDerivatives(1, True).BasisX.Normalize().Negate())
       vectorList.Add(New VectorAtPoint(xyzList))
       Dim fieldValues As New FieldValues(vectorList)

# Inheritance Hierarchy

System..::..Object [Autodesk.Revit.DB..::..ValueAtPointBase](67c49547-b5b9-59ad-8106-65d90886a381.md) Autodesk.Revit.DB.Analysis..::..VectorAtPoint

# See Also

[VectorAtPoint Members](d2038b2b-73d0-45d9-249a-541f256fa249.md)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)