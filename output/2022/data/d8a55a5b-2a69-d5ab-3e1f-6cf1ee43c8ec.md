# Geometry Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
Element..::..Geometry Property   
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") Example See Also  
---  
Retrieves the geometric representation of the element.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public GeometryElement this[
	Options options
] { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property Geometry ( _
	options As Options _
) As GeometryElement
	Get
```
  
Visual C++  
---  
```text
public:
property GeometryElement^ Geometry[Options^ options] {
	GeometryElement^ get (Options^ options);
}
```
  
# ### Parameters
options
    Type: [Autodesk.Revit.DB..::..Options](aa41fc13-9f81-836c-4271-82568ba5d7e8.md "Options Class")User preferences for parsing of geometry.
# ### Field Value
An object that provides access to the geometry of the element.
# Remarks
This call will retrieve 3d representation of the element. nullNothingnullptra null reference (Nothing in Visual Basic) will be returned for symbols, annotations or details. This involves extensive parsing or Revit's data structures, so try to minimize calls if performance is critical.
Geometry objects provided from this method are obtained directly from the element. When the element is changed for any reason, the geometry will be recalculated by Revit and geometry objects obtained before the change are likely to no longer be valid. If you need to preserve geometry information obtained an element even after changes to that element, you should copy the geometry objects or save the properties independently.
Although the geometry obtained from this method comes directly from the element, any attempt to modify any of the geometry objects will operate only on a disconnected copy of the original geometry object from the element. The modification will not affect the geometry of the original element from which it was obtained - to change the geometry of the element you must use methods that directly affect the geometry calculated or stored by Revit for this element.
If you require that the geometry items obtained contain valid [Reference objects](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.md "Reference Class"), be sure to set the ComputeReferences property of the Options.
# Examples
CopyC#
```text
public void GetCurvesFromABeam(Autodesk.Revit.DB.FamilyInstance beam,
                               Autodesk.Revit.DB.Options options)
{
    Autodesk.Revit.DB.GeometryElement geomElem = beam.get_Geometry(options);

    Autodesk.Revit.DB.CurveArray curves = new CurveArray();
    System.Collections.Generic.List<Autodesk.Revit.DB.Solid> solids = new System.Collections.Generic.List<Autodesk.Revit.DB.Solid>(); 

    //Find all solids and insert them into solid array
    AddCurvesAndSolids(geomElem, ref curves, ref solids);
}

private void AddCurvesAndSolids(Autodesk.Revit.DB.GeometryElement geomElem,
                                ref Autodesk.Revit.DB.CurveArray curves,
                                ref System.Collections.Generic.List<Autodesk.Revit.DB.Solid> solids)
{
    foreach (Autodesk.Revit.DB.GeometryObject geomObj in geomElem)
    {
        Autodesk.Revit.DB.Curve curve = geomObj as Autodesk.Revit.DB.Curve;
        if (null != curve)
        {
            curves.Append(curve);
            continue;
        }
        Autodesk.Revit.DB.Solid solid = geomObj as Autodesk.Revit.DB.Solid;
        if (null != solid)
        {
            solids.Add(solid);
            continue;
        }
        //If this GeometryObject is Instance, call AddCurvesAndSolids
        Autodesk.Revit.DB.GeometryInstance geomInst = geomObj as Autodesk.Revit.DB.GeometryInstance;
        if (null != geomInst)
        {
            Autodesk.Revit.DB.GeometryElement transformedGeomElem
              = geomInst.GetInstanceGeometry(geomInst.Transform);
            AddCurvesAndSolids(transformedGeomElem, ref curves, ref solids);
        }
    }
}
```

CopyVB.NET
```text
  Public Sub GetCurvesFromABeam(beam As Autodesk.Revit.DB.FamilyInstance, options As Autodesk.Revit.DB.Options)
      Dim geomElem As Autodesk.Revit.DB.GeometryElement = beam.Geometry(options)

      Dim curves As Autodesk.Revit.DB.CurveArray = New CurveArray()
   Dim solids As New System.Collections.Generic.List(Of Autodesk.Revit.DB.Solid)

      'Find all solids and insert them into solid array
      AddCurvesAndSolids(geomElem, curves, solids)
  End Sub

Private Sub AddCurvesAndSolids(geomElem As Autodesk.Revit.DB.GeometryElement, ByRef curves As Autodesk.Revit.DB.CurveArray, ByRef solids As System.Collections.Generic.List(Of Autodesk.Revit.DB.Solid))
   For Each geomObj As Autodesk.Revit.DB.GeometryObject In geomElem
      Dim curve As Autodesk.Revit.DB.Curve = TryCast(geomObj, Autodesk.Revit.DB.Curve)
      If curve IsNot Nothing Then
         curves.Append(curve)
         Continue For
      End If
      Dim solid As Autodesk.Revit.DB.Solid = TryCast(geomObj, Autodesk.Revit.DB.Solid)
      If solid IsNot Nothing Then
         solids.Add(solid)
         Continue For
      End If
      'If this GeometryObject is Instance, call AddCurvesAndSolids
      Dim geomInst As Autodesk.Revit.DB.GeometryInstance = TryCast(geomObj, Autodesk.Revit.DB.GeometryInstance)
      If geomInst IsNot Nothing Then
         Dim transformedGeomElem As Autodesk.Revit.DB.GeometryElement = geomInst.GetInstanceGeometry(geomInst.Transform)
         AddCurvesAndSolids(transformedGeomElem, curves, solids)
      End If
   Next
End Sub
```

# See Also
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 