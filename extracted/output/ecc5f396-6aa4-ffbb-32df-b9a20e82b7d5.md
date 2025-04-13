

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Document..::..AcquireCoordinates Method   
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Acquires coordinates from the specified link instance. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018 

# Syntax

C#  
---  
      
    
    public void AcquireCoordinates(
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) linkInstanceId
    )  
  
Visual Basic  
---  
      
    
    Public Sub AcquireCoordinates ( _
    	linkInstanceId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) _
    )  
  
Visual C++  
---  
      
    
    public:
    void AcquireCoordinates(
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ linkInstanceId
    )  
  
#### Parameters

linkInstanceId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) The ElementId of the link instance (such as RevitLinkInstance or ImportInstance) from which the coordinates would be acquired. 

# Remarks

When you acquire coordinates from the linked model, the shared coordinates of the linked model become the shared coordinates of the host model, based on the position of the linked model instance in the host model. There is no change to the host model's internal coordinates. 

The host model also acquires True North from the linked model. The origin of the linked model's shared coordinates becomes the origin of the host model's shared coordinates. 

When a Revit model acquires coordinates from a linked DWG file, the World Coordinate System (WCS) of the selected linked DWG file becomes the shared coordinate system of the host Revit model, based on the position of the linked DWG instance. The Y axis of the DWG becomes True North, and the origin of the DWG becomes the origin of the shared coordinate system of the Revit model.

On acquiring coordinates from a geo-referenced model, the geolocation information will be pulled from the linked model to the host model.

Unlike UI operation Acquire Coordinates, calling the API would always overwrite the geolocation information in the host model even if it is different from the one in the linked model, or the linked model has empty geolocation information (in which case the geolocation information in the host model would be removed).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The element linkInstanceId does not exist in the document |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | This Document is not a project document. -or- This Document is in an edit mode. -or- The coordinate system of the selected model are the same as the host model. -or- Cannot acquire coordinates from a model placed multiple times. -or- Failed to acquire coordinates from the link instance. |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md) | The document has no open transaction. |
  
# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)