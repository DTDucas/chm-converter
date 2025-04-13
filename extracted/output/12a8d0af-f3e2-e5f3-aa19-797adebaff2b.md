

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
IExportContextBase..::..OnPolyline Method   
[IExportContextBase Interface](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
This method is called when a Polyline is being output. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    [RenderNodeAction](39f98799-628b-8d65-765c-ca86949ce7ed.md) OnPolyline(
    	[PolylineNode](d0d38779-f0a4-e975-e71d-c8e7026cadfd.md) node
    )  
  
Visual Basic  
---  
      
    
    Function OnPolyline ( _
    	node As [PolylineNode](d0d38779-f0a4-e975-e71d-c8e7026cadfd.md) _
    ) As [RenderNodeAction](39f98799-628b-8d65-765c-ca86949ce7ed.md)  
  
Visual C++  
---  
      
    
    [RenderNodeAction](39f98799-628b-8d65-765c-ca86949ce7ed.md) OnPolyline(
    	[PolylineNode](d0d38779-f0a4-e975-e71d-c8e7026cadfd.md)^ node
    )  
  
#### Parameters

node
    Type: [Autodesk.Revit.DB..::..PolylineNode](d0d38779-f0a4-e975-e71d-c8e7026cadfd.md) An output node that represents a Polyline. 

#### Return Value

Return RenderNodeAction.Proceed if you wish to receive tessellated geometry (polyline segments) for this polyline, or otherwise return RenderNodeAction.Skip. 

Note for 2D export: if the export is performed for the view in non-Wireframe display style tesselated geometry will be output regardless of the return value.

# Remarks

Note that this method is invoked only if the custom exporter was set up to include geometric objects in the output stream. See [IncludeGeometricObjects](2ce1075e-380e-01e7-6459-b7467c2a2414.md) for mode details. 

Note for 2D export: if the export is performed for the view in non-Wireframe display style this method will be called regardless of whether the object will be eventially output, i.e. even if it's occluded by another element.

# See Also

[IExportContextBase Interface](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)