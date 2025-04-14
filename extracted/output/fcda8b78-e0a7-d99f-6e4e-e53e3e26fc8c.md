# VectorAtPoint Class

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
VectorAtPoint Class  
[Members](d2038b2b-73d0-45d9-249a-541f256fa249.md "VectorAtPoint Members") Example See Also  
---  
Stores vectors at one domain point. Each vector corresponds to a "measurement" for which this vector was calculated. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public class VectorAtPoint : ValueAtPointBase
```
  
Visual Basic  
---  
```text
Public Class VectorAtPoint _
	Inherits ValueAtPointBase
```
  
Visual C++  
---  
```text
public ref class VectorAtPoint : public ValueAtPointBase
```
  
# Examples
CopyC#
```text
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
```

CopyVB.NET
```text
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
```

# Inheritance Hierarchy
System..::..Object [Autodesk.Revit.DB..::..ValueAtPointBase](67c49547-b5b9-59ad-8106-65d90886a381.md "ValueAtPointBase Class") Autodesk.Revit.DB.Analysis..::..VectorAtPoint
# See Also
[VectorAtPoint Members](d2038b2b-73d0-45d9-249a-541f256fa249.md "VectorAtPoint Members")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)