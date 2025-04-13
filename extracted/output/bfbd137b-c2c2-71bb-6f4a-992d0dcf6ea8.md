

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
DirectShape Class  
[Members](12ae45fe-e79f-573a-bf55-7c851591b770.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
This class is used to store externally created geometric shapes. Primary intended use is for importing shapes from other data formats such as IFC or STEP. A DirectShape object may be assigned a category. That will affect how that object is displayed in Revit. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 

# Syntax

C#  
---  
      
    
    public class DirectShape : [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
Visual Basic  
---  
      
    
    Public Class DirectShape _
    	Inherits [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
Visual C++  
---  
      
    
    public ref class DirectShape : public [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
# Remarks

DirectShape is not a replacement for "real" Wall, Roof, Window, etc. It would typically be used where there is not enough information to create, e.g., a Wall, or full functionality of a Wall object is not needed. Some category-specific functionality may be available. If you need to modify a shape held by a DirectShape object, use Revit Geometry API, and then store the modified shape back to the DirectShape object. 

# Examples

CopyC#
    
    
    // Create a DirectShape Sphere
    public void CreateSphereDirectShape(Document doc)
    {
        List<Curve> profile = new List<Curve>();
    
        // first create sphere with 2' radius
        XYZ center = XYZ.Zero;
        double radius = 2.0;    
        XYZ profile00 = center;
        XYZ profilePlus = center + new XYZ(0, radius, 0);
        XYZ profileMinus = center - new XYZ(0, radius, 0);
    
        profile.Add(Line.CreateBound(profilePlus, profileMinus));
        profile.Add(Arc.Create(profileMinus, profilePlus, center + new XYZ(radius, 0, 0)));
    
        CurveLoop curveLoop = CurveLoop.Create(profile);
        SolidOptions options = new SolidOptions(ElementId.InvalidElementId, ElementId.InvalidElementId);
    
        Frame frame = new Frame(center, XYZ.BasisX, -XYZ.BasisZ, XYZ.BasisY);
        if (Frame.CanDefineRevitGeometry(frame) == true)
        {
            Solid sphere = GeometryCreationUtilities.CreateRevolvedGeometry(frame, new CurveLoop[] { curveLoop }, 0, 2 * Math.PI, options);
            using (Transaction t = new Transaction(doc, "Create sphere direct shape"))
            {
                t.Start();
                // create direct shape and assign the sphere shape
                DirectShape ds = DirectShape.CreateElement(doc, new ElementId(BuiltInCategory.OST_GenericModel));
    
                ds.ApplicationId = "Application id";
                ds.ApplicationDataId = "Geometry object id";
                ds.SetShape(new GeometryObject[] { sphere });
                t.Commit();
            }
        }
    }

CopyVB.NET
    
    
    ' Create a DirectShape Sphere
    Public Sub CreateSphereDirectShape(doc As Document)
        Dim profile As New List(Of Curve)()
    
        ' first create sphere with 2' radius
        Dim center As XYZ = XYZ.Zero
        Dim radius As Double = 2.0
        Dim profile00 As XYZ = center
        Dim profilePlus As XYZ = center + New XYZ(0, radius, 0)
        Dim profileMinus As XYZ = center - New XYZ(0, radius, 0)
    
        profile.Add(Line.CreateBound(profilePlus, profileMinus))
        profile.Add(Arc.Create(profileMinus, profilePlus, center + New XYZ(radius, 0, 0)))
    
        Dim curveLoop__1 As CurveLoop = CurveLoop.Create(profile)
        Dim options As New SolidOptions(ElementId.InvalidElementId, ElementId.InvalidElementId)
    
        Dim frame__2 As New Frame(center, XYZ.BasisX, -XYZ.BasisZ, XYZ.BasisY)
        If Frame.CanDefineRevitGeometry(frame__2) = True Then
            Dim sphere As Solid = GeometryCreationUtilities.CreateRevolvedGeometry(frame__2, New CurveLoop() {curveLoop__1}, 0, 2 * Math.PI, options)
            Using t As New Transaction(doc, "Create sphere direct shape")
                t.Start()
                ' create direct shape and assign the sphere shape
                Dim ds As DirectShape = DirectShape.CreateElement(doc, New ElementId(BuiltInCategory.OST_GenericModel))
    
                ds.ApplicationId = "Application id"
                ds.ApplicationDataId = "Geometry object id"
                ds.SetShape(New GeometryObject() {sphere})
                t.Commit()
            End Using
        End If
    End Sub

# Inheritance Hierarchy

System..::..Object [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) Autodesk.Revit.DB..::..DirectShape

# See Also

[DirectShape Members](12ae45fe-e79f-573a-bf55-7c851591b770.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)