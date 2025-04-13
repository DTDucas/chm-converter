

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
TopographySurface..::..Create Method (Document, IList<(Of <(<'XYZ>)>)>, IList<(Of <(<'PolymeshFacet>)>)>)  
[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new topography surface element from facets and adds it to the document. 

**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2019.2 

# Syntax

C#  
---  
      
    
    [ObsoleteAttribute("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements.  It is recommended that Toposolid elements should be used in place of TopographySurface elements.")]
    public static [TopographySurface](64242f41-69e1-84be-f21b-84783e81364a.md) Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	IList<[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)> points,
    	IList<[PolymeshFacet](a7315aaf-631d-96af-368c-65f86b6c00ef.md)> facets
    )  
  
Visual Basic  
---  
      
    
    <ObsoleteAttribute("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements.  It is recommended that Toposolid elements should be used in place of TopographySurface elements.")> _
    Public Shared Function Create ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	points As IList(Of [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)), _
    	facets As IList(Of [PolymeshFacet](a7315aaf-631d-96af-368c-65f86b6c00ef.md)) _
    ) As [TopographySurface](64242f41-69e1-84be-f21b-84783e81364a.md)  
  
Visual C++  
---  
      
    
    [ObsoleteAttribute(L"This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements.  It is recommended that Toposolid elements should be used in place of TopographySurface elements.")]
    public:
    static [TopographySurface](64242f41-69e1-84be-f21b-84783e81364a.md)^ Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	IList<[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)^>^ points, 
    	IList<[PolymeshFacet](a7315aaf-631d-96af-368c-65f86b6c00ef.md)^>^ facets
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document to be modified. 

points
    Type: System.Collections.Generic..::..IList<(Of <(<'[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)>)>)> A collection of points. The points represent an enclosed area in the XY plane. 

facets
    Type: System.Collections.Generic..::..IList<(Of <(<'[PolymeshFacet](a7315aaf-631d-96af-368c-65f86b6c00ef.md)>)>)> Triangle facets composing a polygon mesh. Every facet contains 3 integers representing vertex indices. 

#### Return Value

The new topography surface. 

# Remarks

The document will be regenerated during the creation of this topography surface element. The topography surface created by facet cannot modify its triangle points and facets. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | document is not a project document. -or- There are invalid facets. Facets with more than two points with same x, y are not allowed. -or- There is(are) reference gap(s) between input arguments: points and facets. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md) | The document has no open transaction. |
  
# See Also

[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.md)

[Create Overload](7951a6bc-55e8-14bf-c8dc-47ee4a463165.md)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)