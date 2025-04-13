

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
AnnotationSymbol Methods  
[AnnotationSymbol Class](b8ea2b7b-6d1c-d0d3-aaf3-b95003c385b8.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [AnnotationSymbol](b8ea2b7b-6d1c-d0d3-aaf3-b95003c385b8.md) type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [AddCoping](a0fc20d1-36fc-a230-d41f-f7163184d328.md) | Adds a coping (cut) to a steel beam. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [addLeader](558c4f77-a51a-28a9-3c1e-41bdcede3f98.md) | add a leader to this annotation symbol. |
|  | [ArePhasesModifiable](329b02eb-5ee4-1715-2fbf-2cbbc0d3ff2a.md) | Returns true if the properties CreatedPhaseId and DemolishedPhaseId can be modified for this Element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [CanBeHidden](887010c4-de58-96b6-0931-4c226e6b142b.md) | Indicates if the element can be hidden in the view. (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [CanBeLocked](5ef8834b-168d-02ac-2f29-5d43f5da87f2.md) | Identifies if the element can be locked.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [CanDeleteSubelement](c9795398-2d2c-db8e-a4e7-ca99d69fcc1d.md) | Checks if given subelement can be removed from the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [CanHaveTypeAssigned()()()()](051e2945-b690-5387-d083-7cdb7cb75332.md) | Identifies if the element can have a type assigned.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [ChangeTypeId(ElementId)](479b5d94-abd3-db42-27d7-6a3eda12f285.md) | Changes the type of the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [DeleteEntity](ef0fa7d8-8152-6300-285d-1c0cdc08e5a7.md) | Deletes the existing entity created by %schema% in the element  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [DeleteSubelement](de199938-feea-7437-c19f-162714b70dcd.md) | Removes a subelement from the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [DeleteSubelements](6410b135-88fe-b111-769f-f14e86b42a05.md) | Removes the subelements from the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [Dispose](e3b07ee4-f500-1b95-c786-8984289a5143.md) | (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [duplicate](272c1e6e-c696-24fe-52e5-26bcb961f815.md) | Duplicate this annotation symbol. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | [EvaluateAllParameterValues](5250da77-1e16-13c6-fed6-5ef29997e6f9.md) | Evaluates all the parameters' values of the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [EvaluateParameterValues](1a6ca65f-09d9-a4e6-9365-3ed64e3097fc.md) | Evaluate the parameters' values of the element on the given parameter ID set.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [flipFacing](66eb8785-4225-509c-b6a3-0bf9fe1612b2.md) | The orientation of family instance facing will be flipped. If it can not be flipped, return false, otherwise return true. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [FlipFromToRoom](ae1158c1-1fb0-0558-0ea4-e1cf76bb8a1e.md) | Flips the settings of "From Room" and "To Room" for the door or window instance.  (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [flipHand](c31b55a1-ce2e-a86c-ede0-21a883e7d4e4.md) | The orientation of family instance hand will be flipped. If it can not be flipped, return false, otherwise return true. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetCopingIds](6886b519-4a44-373f-59ab-4ceee51dd096.md) | Lists the elements currently used as coping cutters for this element. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetDependentElements](56e875d3-014b-a996-69c3-e6ed9b885f5c.md) | Get all elements that, from a logical point of view, are the children of this Element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetEntity](09d80bf1-c1d0-aa2e-4f18-e5a5e9c9d93f.md) | Returns the existing entity corresponding to the Schema if it has been saved in the Element, or an invalid entity otherwise.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetEntitySchemaGuids](742313cb-1bea-f873-e5ca-1bfac782286b.md) | Returns the Schema guids of any Entities stored in this element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetExternalFileReference](e784fb6e-94f4-09bd-1f9c-17e6968e18a5.md) | Gets information pertaining to the external file referenced by the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetExternalResourceReference](fb4b9493-1d7b-5387-c171-2078225183ca.md) | Gets the ExternalResourceReference associated with a specified external resource type.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetExternalResourceReferenceExpanded](1a28171e-8460-d849-4e7d-9a306a22cd6e.md) | Gets the collection of ExternalResourceReference associated with a specified external resource type.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetExternalResourceReferences](7df4341b-5102-8016-d6fa-45bc27e8c3af.md) | Gets the map of the external resource references referenced by the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetExternalResourceReferencesExpanded](954cb21e-5c4e-1e52-7e35-1eb0ed4b050b.md) | Gets the expanded map of the external resource references referenced by the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetFamilyPointPlacementReferences](59db15da-7e87-a85f-bacf-e8a636d17022.md) | Returns the Point Placement References for the Family Instance. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetGeneratingElementIds](112590d2-de20-dd1f-ae05-df7dfb3b410f.md) | Returns the ids of the element(s) that generated the input geometry object.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetGeometryObjectFromReference](536b3d7a-ec8d-29f6-5957-751468c98dd0.md) | Retrieve one geometric primitive contained in the element given a reference.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
|  | [GetLeaders](2819f7b4-0c4b-35ed-2ca3-5221bd53fa2d.md) | Returns a collection of leaders currently attached to the annotation. |
|  | [GetMaterialArea](02417c40-bcc4-f04c-9897-cf47737e8739.md) | Gets the area of the material with the given id.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetMaterialIds](6011352e-151b-b8ac-14cc-45970f2fe5ad.md) | Gets the element ids of all materials present in the element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetMaterialVolume](99b50d87-bfa6-ca67-e205-47b22cad6587.md) | Gets the volume of the material with the given id.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetMonitoredLinkElementIds](42b25291-f1b9-d240-c876-1b53f24f60e0.md) | Provides the link instance IDs when the element is monitoring.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetMonitoredLocalElementIds](47ca1e8c-f79d-a18b-505b-73a4358d2264.md) | Provides the local element IDs when the element is monitoring.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetOrderedParameters](4bf4c0da-f841-0943-f9e0-246a666c1775.md) | Gets the parameters associated to the element in order.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetOriginalGeometry](d28a0880-bff8-1acc-ddf1-ce3205f2e8b3.md) | Returns the original geometry of the instance, before the instance is modified by joins, cuts, coping, extensions, or other post-processing. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetParameter](fc4e5245-d2e5-e31d-a6e3-177106e75e10.md) | Retrieves a parameter from the element given identifier. (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetParameterFormatOptions](476c8179-f938-d047-db7c-776cf7e2929c.md) | Returns a FormatOptions override for the element Parameter, or a default FormatOptions if no override exists.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetParameters](0cf342ef-c64f-b0b7-cbec-da8f3428a7dc.md) | Retrieves the parameters from the element via the given name. (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetPhaseStatus](eedf5981-b5e2-dda7-cb5e-01a4d4fc7f6c.md) | Gets the status of a given element in the input phase  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetReferenceByName](d44a95cc-f2c7-1fa9-9180-fefed6d70ed6.md) | Gets the family instance reference corresponding to the named reference plane in the instance's family.  (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetReferenceName](aaf6b45c-9139-b984-b824-2888ca32a95a.md) | Gets the name of the reference plane in the family corresponding to the given family instance reference.  (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetReferences](a8a7dc74-db8e-a7b6-a9c8-869397cca6b4.md) | Gets family instance references corresponding to the reference planes or reference lines of the given reference type in the instance's family.  (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetReferenceType](0405fced-1ac6-a6a9-9f59-21eb81ca2241.md) | Gets the type of the reference plane or reference line in the instance's family corresponding to the given family instance reference.  (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetSpatialElementCalculationPoint](433caf59-49b1-97df-38ac-8f01a620bef5.md) | Gets the location of the calculation point for this instance. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetSpatialElementFromToCalculationPoints](21810873-d413-f6e4-ca33-d2ee4e93643e.md) | Gets the locations for the calculation points for this instance. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetSubComponentIds](be37702c-1dcd-bc14-aa35-45f06f20210a.md) | Gets the sub component ElementIds of the current family instance. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetSubelements](feabfd59-bd0f-ab61-34a1-d0d22f58c881.md) | Returns the collection of element subelements.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetSweptProfile](9bc9e2db-5ef1-8264-1426-01f4a6081844.md) | Gets the object that describes the profile that is swept along the driving curve for this instance. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [GetTotalTransform](8c8aff2b-5ff9-e43a-3b5c-308cd0174f1f.md) | Gets the total transform, which includes the true north transform for instances like import instances.  (Inherited from [Instance](08603dd9-976d-a9fe-add7-2a8450b8006c.md).) |
|  | [GetTransform](50aa275d-031e-ce19-9cfd-18a7a341ed19.md) | Gets the transform of the instance.  (Inherited from [Instance](08603dd9-976d-a9fe-add7-2a8450b8006c.md).) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | [GetTypeId](cc66ca8e-302e-f072-edca-d847bcf14c86.md) | Returns the identifier of this element's type.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [GetValidTypes()()()()](086554ba-3c70-9c0f-8a09-55a4da4ef905.md) | Obtains a set of types that are valid for this element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [HasModifiedGeometry](0f1f1713-8013-2f62-6e84-41749e1dcc95.md) | Identifies if the geometry of this FamilyInstance has been modified from the automatically generated default. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [HasPhases](5d850f8a-4a50-406b-6c59-b85d49dcbb2e.md) | Returns true if this Element has the properties CreatedPhaseId and DemolishedPhaseId.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [HasSweptProfile](dbbd4aa9-720b-3a1c-3085-7b94b6d73b58.md) | Indicates if this instance can be represented as a swept profile. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [IsCreatedPhaseOrderValid](b2bcaf7f-c453-d6e2-fd85-083783e935f3.md) | Returns true if createdPhaseId and demolishedPhaseId are in order.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [IsDemolishedPhaseOrderValid](46ec60b6-b1c5-25aa-c544-34379298c7b8.md) | Returns true if createdPhaseId and demolishedPhaseId are in order.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [IsExternalFileReference](2bf6162f-0b0f-88cb-9c67-d4bd435537b5.md) | Determines whether this Element represents an external file.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [IsHidden](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.md) | Identifies if the element has been permanently hidden in the view. (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [IsMonitoringLinkElement](fde81756-5518-4924-c14e-f9ef2bb3fa6e.md) | Indicate whether an element is monitoring any elements in any linked models.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [IsMonitoringLocalElement](9a41a87c-2b3b-b6ed-1743-98c002b20ce3.md) | Indicate whether an element is monitoring other local elements.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [IsPhaseCreatedValid](ae48b10d-4a66-ee2c-85bf-f426435d0dbe.md) | Returns true if createdPhaseId is an allowed value for the property CreatedPhaseId in this Element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [IsPhaseDemolishedValid](f97c9af7-fcbe-f617-d7ff-cfd4fb5af37f.md) | Returns true if demolishedPhaseId is an allowed value for the property DemolishedPhaseId in this Element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [IsValidType(ElementId)](c3ca4ee5-c2b3-beb3-ee51-cc6cafc82c93.md) | Checks if given type is valid for this element.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [LookupParameter](4400b9f8-3787-0947-5113-2522ff5e5de2.md) | Attempts to find a parameter on the element which has the given name. (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [RefersToExternalResourceReference](0a4aabb3-f684-0800-7bf5-31540831593f.md) | Determines whether this Element uses external resources associated with a specified external resource type.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [RefersToExternalResourceReferences](387c00cd-3932-76e6-152b-bfe4efb8fbc1.md) | Determines whether this Element uses external resources.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [RemoveCoping](c0ccd04c-f952-011f-4b0f-25862792d619.md) | Removes a coping (cut) from a steel beam. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [removeLeader](10347b43-8255-d40b-4507-9843af642b4f.md) | remove a leader of this annotation symbol. |
|  | [rotate](634dc711-7d00-a176-9c61-c53c27c89849.md) | The family instance will be flipped by 180 degrees. If it can not be rotated, return false, otherwise return true. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [SetCopingIds](751280c8-4507-4837-add9-f6a83a1997fe.md) | Specifies the set of coping cutters on this element. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | [SetEntity](e90c01ab-3d2f-2f46-3e88-8297e686dc80.md) | Stores the entity in the element. If an Entity described by the same Schema already exists, it is overwritten.  (Inherited from [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md).) |
|  | [Split](8f32a065-ba3c-79c7-8141-63183b4cdece.md) | Splits the family instance element at a point on its defining curve. (Inherited from [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md).) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
  
# See Also

[AnnotationSymbol Class](b8ea2b7b-6d1c-d0d3-aaf3-b95003c385b8.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)