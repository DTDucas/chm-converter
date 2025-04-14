# IExportContextBase Methods

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2024 API  
---  
IExportContextBase Methods  
[IExportContextBase Interface](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.md "IExportContextBase Interface") See Also  
---  
The [IExportContextBase](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.md "IExportContextBase Interface") type exposes the following members.
# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Finish](68714169-e994-41e3-f1c6-8f929b40565f.md "Finish Method") | This method is called at the very end of the export process, after all entities were processed (or after the process was cancelled).  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [IsCanceled](31f0b662-81a1-89b8-ab2a-0de99af3b753.md "IsCanceled Method") | This method is queried at the beginning of every element.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [OnCurve](6306ac1d-c259-5617-f71b-c13e54e5af0d.md "OnCurve Method") | This method is called when a Curve is being output. |
| [OnElementBegin](d218b0b3-bb24-0f73-806c-2ef90b16d882.md "OnElementBegin Method") | This method marks the beginning of an element to be exported.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [OnElementEnd](14aeeee7-9389-d7fc-5a40-2b7541ce95d1.md "OnElementEnd Method") | This method marks the end of an element being exported.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [OnFaceBegin](9a9f37ae-c8c2-7355-2c3b-f26762951f1d.md "OnFaceBegin Method") | This method marks the beginning of a Face to be exported.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [OnFaceEnd](49e6eaf6-80e3-53bd-14c2-8fe999afb70b.md "OnFaceEnd Method") | This method marks the end of the current face being exported.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [OnInstanceBegin](2db35bdb-8d14-a015-9bfb-9283f503edab.md "OnInstanceBegin Method") | This method marks the start of processing of an instance node (e.g. a family instance).  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [OnInstanceEnd](d1340660-fcc9-3bfd-58fb-8d114aa39517.md "OnInstanceEnd Method") | This method marks the end of processing of an Instance Node (e.g. a family instance).  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [OnLight](d56129ca-950b-34fc-89ac-f0fb2e7fe9f2.md "OnLight Method") | This method marks the beginning of export of a light which is enabled for rendering.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").) |
| [OnLineSegment](5fe0cee4-825b-9828-2c45-5e4c5019bc37.md "OnLineSegment Method") | This method is called after unhandled curve was tessellated to line segments and sent to the output. Note for 2D export: if the export is performed for the view in non-Wireframe display style, then |

  * this method is called outside of view, instance and link begin/end calls but still between OnElementBegin2D/OnElementEnd2D calls
  * this method is never called for annotation elements, i.e. their geometry should be processed in methods OnCurve and OnPolyline

  
| [OnLinkBegin](40d99b4a-e6aa-42d7-18ff-b546d1a5154e.md "OnLinkBegin Method")|  This method marks the beginning of a link instance to be exported.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").)  
| [OnLinkEnd](e6680c8d-bfb3-f873-3e3d-24aa8b29061e.md "OnLinkEnd Method")|  This method marks the end of a link instance being exported.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").)  
| [OnMaterial](9d2dc6b3-21a7-5362-2bf5-2cb11b42c2d4.md "OnMaterial Method")|  This method marks a change of the material.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").)  
| [OnPolyline](12a8d0af-f3e2-e5f3-aa19-797adebaff2b.md "OnPolyline Method")|  This method is called when a Polyline is being output.   
| [OnPolylineSegments](c3891505-dd89-50d4-519e-5380af669325.md "OnPolylineSegments Method")|  This method is called after unhandled curve was tessellated to polyline segments and sent to the output. Note for 2D export: if the export is performed for the view in non-Wireframe display style, then 
  * this method is called outside of view, instance and link begin/end calls but still between OnElementBegin2D/OnElementEnd2D calls
  * this method is never called for annotation elements, i.e. their geometry should be processed in methods OnCurve and OnPolyline

  
| [OnPolymesh](6a060c37-3225-217e-b150-2eaea3a22c29.md "OnPolymesh Method")|  This method is called when a tessellated polymesh of a 3d face is being output.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").)  
| [OnRPC](f84574d9-ef15-c317-c6dd-91304a0c174c.md "OnRPC Method")|  This method marks the beginning of export of an RPC object.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").)  
| [OnText](008311bb-c88d-3c22-dc06-f34a59f8329c.md "OnText Method")|  This method is called when a text annotation object is being output.   
| [OnViewBegin](959602b7-5257-d2c1-2c00-0b7649f145f5.md "OnViewBegin Method")|  This method marks the beginning of a 3D view to be exported.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").)  
| [OnViewEnd](5df27a2c-ae84-2d1d-635e-107ec0525ebb.md "OnViewEnd Method")|  This method marks the end of a 3D view being exported.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").)  
| [Start](2d93c3c6-c826-cd70-dc0a-b94f66324c35.md "Start Method")|  This method is called at the very start of the export process, still before the first entity of the model was send out.  (Inherited from [IExportContext](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.md "IExportContext Interface").)  
# See Also
[IExportContextBase Interface](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.md "IExportContextBase Interface")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)