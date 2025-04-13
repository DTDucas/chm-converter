

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Element..::..Geometry Property   
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Retrieves the geometric representation of the element.

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public [GeometryElement](09eaeb08-58bb-8049-8925-f3a5aa846fdc.md) this[
    	[Options](aa41fc13-9f81-836c-4271-82568ba5d7e8.md) options
    ] { get; }  
  
Visual Basic  
---  
      
    
    Public ReadOnly Property Geometry ( _
    	options As [Options](aa41fc13-9f81-836c-4271-82568ba5d7e8.md) _
    ) As [GeometryElement](09eaeb08-58bb-8049-8925-f3a5aa846fdc.md)
    	Get  
  
Visual C++  
---  
      
    
    public:
    property [GeometryElement](09eaeb08-58bb-8049-8925-f3a5aa846fdc.md)^ Geometry[[Options](aa41fc13-9f81-836c-4271-82568ba5d7e8.md)^ options] {
    	[GeometryElement](09eaeb08-58bb-8049-8925-f3a5aa846fdc.md)^ get ([Options](aa41fc13-9f81-836c-4271-82568ba5d7e8.md)^ options);
    }  
  
#### Parameters

options
    Type: [Autodesk.Revit.DB..::..Options](aa41fc13-9f81-836c-4271-82568ba5d7e8.md)User preferences for parsing of geometry.

#### Field Value

An object that provides access to the geometry of the element.

# Remarks

This call will retrieve 3d representation of the element. nullNothingnullptra null reference (Nothing in Visual Basic) will be returned for symbols, annotations or details. This involves extensive parsing or Revit's data structures, so try to minimize calls if performance is critical.

Geometry objects provided from this method are obtained directly from the element. When the element is changed for any reason, the geometry will be recalculated by Revit and geometry objects obtained before the change are likely to no longer be valid. If you need to preserve geometry information obtained an element even after changes to that element, you should copy the geometry objects or save the properties independently.

Although the geometry obtained from this method comes directly from the element, any attempt to modify any of the geometry objects will operate only on a disconnected copy of the original geometry object from the element. The modification will not affect the geometry of the original element from which it was obtained - to change the geometry of the element you must use methods that directly affect the geometry calculated or stored by Revit for this element.

If you require that the geometry items obtained contain valid [Reference objects](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.md), be sure to set the ComputeReferences property of the Options.

# Examples

CopyC#
    
    
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

CopyVB.NET
    
    
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

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)