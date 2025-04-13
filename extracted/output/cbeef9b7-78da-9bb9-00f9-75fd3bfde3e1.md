

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
DocumentEntryPoint Members  
[DocumentEntryPoint Class](99996ba9-d1a7-d27e-c0ce-eb271a4c35bb.md) Constructors Methods Properties Events See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [DocumentEntryPoint](99996ba9-d1a7-d27e-c0ce-eb271a4c35bb.md) type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
|  | [DocumentEntryPoint](e19310c9-e2b9-489e-99cc-4d377ef64396.md) | Initializes a new instance of the [DocumentEntryPoint](99996ba9-d1a7-d27e-c0ce-eb271a4c35bb.md) class |
  
# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [AcquireCoordinates](ecc5f396-6aa4-ffbb-32df-b9a20e82b7d5.md) | Acquires coordinates from the specified link instance.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [AutoJoinElements](a3c929fb-6164-c7bb-d140-4178fb07fd4e.md) | Forces the elements in the Revit document to automatically join to their neighbors where appropriate. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [CanEnableCloudWorksharing](efceae4b-4d93-9097-cf8a-a223aa9412fb.md) | Checks if cloud worksharing can be enabled for the cloud model.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [CanEnableWorksharing](5fb244f2-6e43-f1d3-2013-55df4a5157aa.md) | Checks if worksharing can be enabled in the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Close()()()()](da2f27b9-7255-4950-82a2-86e1432ff9f0.md) | Closes the document, save the changes if there are. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Close(Boolean)](5948b03d-5537-33d4-6e38-a8f16d5d6779.md) | Closes the document with the option to save. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [CombineElements](5c33a711-2891-f353-5f39-24ba175be452.md) | Combine a set of combinable elements into a geometry combination. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ConvertDetailToModelCurves](4620e606-df11-67c6-a386-ade6fbb9911a.md) | Converts a group of DetailCurves to equivalent ModelCurves. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ConvertModelToDetailCurves](5566ffcf-1724-589b-15a1-6e829a986ec2.md) | Converts a group of ModelCurves to equivalent DetailCurves. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ConvertModelToSymbolicCurves](ee3b6765-5af9-acd8-5132-42484ab20924.md) | Converts a group of ModelCurves to equivalent SymbolicCurves. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ConvertSymbolicToModelCurves](f7f3a66a-d57a-a20e-d860-8e3a3f889566.md) | Converts a group of SymbolicCurves to equivalent ModelCurves. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Delete(ElementId)](a0461dd1-71d9-4581-1604-2ef8c211dd60.md) | Deletes an element from the document given the id of that element.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Delete(ICollection<(Of <<'(ElementId>)>>))](f4ce9113-b164-954e-5025-7b4edbdcc07d.md) | Deletes a set of elements from the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Dispose](3c64e1bd-1db3-0a71-c9fa-f70e136cd676.md) | (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [EditFamily](56e636ee-5008-0ee5-9d6c-5f622dedfbcb.md) | Gets the document of a loaded family to edit. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [EnableCloudWorksharing](4146e816-565e-85d8-ce94-93ec505a0924.md) | Enables cloud worksharing for a cloud model  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [EnableWorksharing](7c29717e-1d8c-4e02-20ad-65c53ea8eaaa.md) | Enables worksharing in the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Equals](f0efbd19-9399-1ee7-96e5-fe1dbbaa0815.md) | Determines whether the specified Object equals to this Object.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [EraseSchemaAndAllEntities](50debcb0-3c4f-b32b-2edb-8a6ef7b4bf8d.md) | Erases Schema and all its Entities from the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, IList<(Of <<'(ElementId>)>>), PDFExportOptions)](93d66d57-c20e-a103-39a1-77bc2ea05183.md) | Exports a selection of views in PDF format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, GBXMLExportOptions)](adf1b78e-dcab-7b46-80fa-a470f0fd848b.md) | Export the model in gbXML (green-building) format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, IFCExportOptions)](7efa4eb3-8d94-b8e7-f608-3dbae751331d.md) | Exports the document to the Industry Standard Classes (IFC) format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, NavisworksExportOptions)](1b9538a9-a76b-0a40-2aed-e02f6974a43a.md) | Exports a Revit project to the Navisworks .nwc format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, OBJExportOptions)](203a88aa-d6e1-d96d-7ee0-f67356aae796.md) | Exports a view specified in the export options to the OBJ format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, STLExportOptions)](fc32cc69-4691-e62c-61e3-57cf20dd9edf.md) | Exports a view specified in the export options to the STL format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, ViewSet, DWFExportOptions)](2074006f-9a45-43f5-dff7-3205100eb371.md) | Exports the current view or a selection of views in DWF format. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, ViewSet, DWFXExportOptions)](d055fb60-5271-a2f6-de50-eb0d03911986.md) | Exports the current view or a selection of views in DWFX format. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, ViewSet, FBXExportOptions)](02b2efba-9d7c-88bc-b43e-a541e169d832.md) | Exports the document in 3D-Studio Max (FBX) format. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, ICollection<(Of <<'(ElementId>)>>), DGNExportOptions)](7acf3783-1b09-12be-6683-529fa85ff764.md) | Exports a selection of views in DGN format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, ICollection<(Of <<'(ElementId>)>>), DWGExportOptions)](44ee91ff-c9f3-7df5-b8c0-81c17ac75dc7.md) | Exports a selection of views in DWG format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, ICollection<(Of <<'(ElementId>)>>), DXFExportOptions)](fd65887a-3d13-3ff1-ec95-7c0379317c85.md) | Exports a selection of views in DXF format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Export(String, String, ICollection<(Of <<'(ElementId>)>>), SATExportOptions)](e5cd0800-8544-c2d1-d21a-19ae33e9168c.md) | Exports the current view or a selection of views in SAT format.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ExportImage](b98a3e71-39fa-bf7a-cb3d-591d8b1fcd93.md) | Exports a view or set of views into an image file.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [FinishInitializationEO](7c75cb69-106c-f322-374e-7e2f0733a53c.md) | For Revit Macros internal use only. |
|  | [GetAllUnusedElements](fc50a373-b2a9-8839-14c1-e64b693e445c.md) | Returns the list of element ids that are not used. The list of unused element ids may include elements that can't be deleted.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetChangedElements](0799eb9e-5ce8-2668-eb3d-aecfd121b2d6.md) | Extracts a collection containing the ids of elements that have been created, modified or deleted between the input baseVersion and the document's current version.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetCloudFolderId](e4177a0c-9c2a-5cd4-2f53-11d2c95004eb.md) | Gets ForgeDM folder id where the model locates.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetCloudModelPath](087a7c14-1a6e-7022-c47b-923e90f4c5be.md) | Gets the cloud model path of the cloud model.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetCloudModelUrn](7c2bced8-b309-b67f-2b82-13299c617a0b.md) | A ForgeDM Urn identifying the model.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetDefaultElementTypeId](b62f6563-aca4-56dc-4697-7717932187b3.md) | Gets the default element type id with the given DefaultElementType id.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetDefaultFamilyTypeId](34d20683-dfea-b1f8-14cf-750611b218ed.md) | Gets the default family type id with the given family category id.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetDocumentPreviewSettings](ab0a9756-1ee1-df01-f8ef-10f7fbdec80f.md) | Returns the preview settings for the given document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetElement(String)](b5a1473c-21c4-6c29-f1cf-26822c955260.md) | Gets the Element referenced by a unique id string.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetElement(ElementId)](d9848d7d-5917-2433-8454-f65f5ac03964.md) | Gets the Element referenced by the input ElementId.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetElement(Reference)](4d674a3e-cd18-6b3d-b1b2-247713fe3c9f.md) | Gets the Element referenced by the input reference.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetHashCode](006a71c2-4393-e036-9987-14467342a7d3.md) | Gets the hash code of this document instance.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetHubId](e9756087-8232-88ca-c2ac-90ba51a87914.md) | Gets ForgeDM hub id where the model locates. It is cached in session.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetPaintedMaterial](6f40681b-18ba-6d8d-b00f-9f3922466a37.md) | Get the material painted on the element's face. Returns invalidElementId if the face is not painted.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetPrintSettingIds](81790544-e1d9-ebaa-037b-c2d12d2a6387.md) | Retrieves all Print Settings of current project.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetProjectId](902d5aa9-9f3f-a9e9-0d0a-4c95fa820890.md) | Gets ForgeDM project id where the model locates.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetRoomAtPoint(XYZ)](656d34c2-1e53-7278-ab83-fefaff7f40a4.md) | Gets a room containing the point. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetRoomAtPoint(XYZ, Phase)](7dbcac93-ec82-5f60-4a54-a427f3e1cc1e.md) | Gets a room containing the point. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetSpaceAtPoint(XYZ)](73543682-0f14-1b49-a881-d694aa17192b.md) | Gets a space containing the point. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetSpaceAtPoint(XYZ, Phase)](aeb0a0c9-2d9d-1705-ad93-31956a63704d.md) | Gets a space containing the point. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetSubelement(String)](9fd1a0fa-17f1-95a0-6feb-e9609fe0c7f1.md) | Gets the subelement referenced by a unique id string.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetSubelement(Reference)](3dbd4eab-664f-0048-13a9-959c27fce729.md) | Gets the subelement referenced by the input reference.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetSubelement(ElementId, Int32)](61f62003-12e1-6806-dcb6-3781c54ca830.md) | Gets the subelement referenced by a parent id and subelement id.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | [GetTypeOfStorage](39a19e04-d424-9e7d-0d82-866172fb26d9.md) | Get the storage type of the identified built-in parameter.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetUnits](9ed56178-e9ae-b4bc-1c0e-e6a867ae3557.md) | Gets the Units object.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetUnusedElements](dcb1f497-dfa6-bb3a-b9dd-f9a580f990f2.md) | Returns the list of element ids that are not used and can be deleted from the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetWarnings](4774613d-600a-e1b5-b5aa-f1ee3b14394c.md) | Returns list of failure messages generated from persistent (reviewable) warnings accumulated in the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetWorksetId](a8a13d95-549e-dffd-5ffe-8cef809c703b.md) | Get Id of the Workset which owns the element.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetWorksetTable](b02ace6c-4643-cea6-9545-ea41822731f3.md) | Get the WorksetTable of this document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [GetWorksharingCentralModelPath](6d42ee05-5738-8685-2165-57f9809f3161.md) | Gets the central model path of the worksharing model.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [HasAllChangesFromCentral](67bb59c4-77cf-7cb4-d289-489ba85e09b2.md) | Returns whether the model in the current session is up to date with central.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, GBXMLImportOptions)](7a6bffbf-b0fe-b047-1008-36d57f495417.md) | Imports a Green-Building XML file into the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, AXMImportOptions, View)](14f9266e-e989-3654-e32a-b4e412846698.md) | Imports an AXM file into the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, ImportOptions3DM, View)](64303015-53a6-3bde-e8ee-838d927956f0.md) | Imports a 3DM file into the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, OBJImportOptions, View)](96eda242-d5f0-f72f-87fc-5400e70b7903.md) | Imports an OBJ file into the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, SATImportOptions, View)](c71d8882-24ad-1621-13f3-c83a8be8ef85.md) | Imports an SAT file into the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, SKPImportOptions, View)](c7a6df28-b5af-de54-fb1e-8874296525b9.md) | Imports a SKP file into the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, STLImportOptions, View)](3a99879a-efe1-8611-01c3-2de9af62341f.md) | Imports an STL file into the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, DGNImportOptions, View, ElementId%)](8e1bc344-210c-b202-8f37-8197b781beff.md) | Imports a DGN file to the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Import(String, DWGImportOptions, View, ElementId%)](1b1413fd-1358-709b-77a8-e383d6c1301e.md) | Imports a DWG or DXF file to the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Initialize](6a99b8ac-b10c-b841-dbaa-2749c01af925.md) | For Revit Macros internal use only. |
|  | [IsBackgroundCalculationInProgress](d465e75a-0fc5-33c1-9d5e-dc711bcaef49.md) | Indicates whether there are any background calculations in progress for this document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsDefaultElementTypeIdValid](a322128b-9244-ce7f-fb5e-06aa50d5dca5.md) | Checks whether the element type id is valid for the give DefaultElmentType id.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsDefaultFamilyTypeIdValid](5bb8f467-d26c-449d-9031-ba072fcb48b4.md) | Checks whether the family type id is valid for the give family category.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsPainted](638f398e-bb20-53c4-55a6-454d8a0a1029.md) | Checks if the element's face is painted with a material.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Link(String, DWFImportOptions)](4d18bcd5-77bb-a1fe-6789-dfcf5afee849.md) | Links Markups in a DWF file into the project document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Link(String, ImportOptions3DM, View)](10dac8a0-bf4c-d238-9635-9b2aa58e156b.md) | Links a 3DM file into the project document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Link(String, OBJImportOptions, View)](201f87c1-50c8-2542-d7a5-0dc2b2e706a0.md) | Links an OBJ file into the project document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Link(String, SATImportOptions, View)](c3629b13-f58b-78f3-1a81-29340774199a.md) | Links an SAT file into the project document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Link(String, SKPImportOptions, View)](cc612dab-6830-d114-4213-d52acc5bd377.md) | Links a SKP file into the project document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Link(String, STLImportOptions, View)](d2a98d4f-d64e-6941-2c5b-fc43ead1b6f3.md) | Links an STL file into the project document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Link(String, DGNImportOptions, View, ElementId%)](a5c932ef-4e3b-bf83-c7df-e9cc827eeaeb.md) | Links a DGN file into the project document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Link(String, DWGImportOptions, View, ElementId%)](f3112a35-91c2-7783-f346-8f21d7cb99b5.md) | Links a DWG or DXF file into the project document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [LoadFamily(String)](3fefb883-07ab-e638-edf9-9c8b8f00c0f0.md) | Loads an entire family and all its types/symbols into the document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [LoadFamily(Document)](6a91dc8e-6c2b-52b9-dfc4-d56fa472852b.md) | Loads the contents of this family document into another document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [LoadFamily(String, Family%)](67277d5a-0ddf-b617-c9c9-911ecb928af9.md) | Loads an entire family and all its types/symbols into the document and provides a reference to the loaded family. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [LoadFamily(Document, IFamilyLoadOptions)](cb950c8e-f440-c6db-8563-d1dd16ef3fee.md) | Loads the contents of this family document into another document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [LoadFamily(String, IFamilyLoadOptions, Family%)](5d34b8dd-9137-da2f-9df7-172304d0cc08.md) | Loads an entire family and all its types/symbols into the document and provides a reference to the loaded family. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [LoadFamilySymbol(String, String)](78c15d1f-7c29-29bf-7b55-e416b21cb16b.md) | Loads only a specified family type/symbol from a family file into the document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [LoadFamilySymbol(String, String, FamilySymbol%)](ba726add-04f7-7757-6557-4e32e8b1008b.md) | Loads only the specified family type/symbol from a family file into the document and provides a reference to the loaded family symbol. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [LoadFamilySymbol(String, String, IFamilyLoadOptions, FamilySymbol%)](255f2e8c-8990-8617-7f16-a77915b8a52e.md) | Loads only the specified family type/symbol from a family file into the document and provides a reference to the loaded family symbol. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [MakeTransientElements](0decdddc-ae4a-d46d-d141-9d37e7973e05.md) | This method encapsulates the process of creating transient elements in the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [OnShutdownEO](cc1b5aad-72ee-9e67-18f3-7ae2eb3be1f9.md) | For Revit Macros internal use only. |
|  | [Paint(ElementId, Face, ElementId)](9268395e-a9cb-ff79-20ab-1ed261220513.md) | Paint the element's face with specified material.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Paint(ElementId, Face, FamilyParameter)](f59f8872-e8d7-5d00-0e8c-44a36a843861.md) | Paint the element's face with specified material.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PostFailure](7184ff0a-f30e-03fb-904f-fb557df6fa37.md) | Posts a failure to be displayed to the user at the end of transaction.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Print(ViewSet)](3acc25be-ddb8-99e8-ea8c-ef0b86b6eb8c.md) | Prints a set of views with default view template and default print settings. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Print(ViewSet, View)](3db1fadb-0349-f0cd-c3cc-c9aa90454880.md) | Prints a set of views with a specified view template and default print settings. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Print(ViewSet, Boolean)](6030120a-4523-3d02-5e38-6ed684c174cb.md) | Prints a set of views with default view template and default print settings. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Print(ViewSet, View, Boolean)](fb631da2-2261-4683-a957-5b63ac985d62.md) | Prints a set of views with a specified view template and default print settings. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PublishCoordinates](04419593-f258-dc77-b18a-24a29733b75f.md) | Publish coordinates to the specified ProjectLocation of the link instance.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Regenerate](22468e2c-9772-8478-0816-c9759aa43428.md) | Updates the elements in the Revit document to reflect all changes. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ReloadLatest](f60968b0-faa6-92f9-5e73-a201fe87a1ad.md) | Fetches changes from central (due to one or more synchronizations with central) and merges them into the current session.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [RemovePaint](7ba7c440-7ed5-c3ff-9b9e-4413bf22a0c4.md) | Remove the material painted on the element's face. If the face is currently not painted,it will do nothing.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ResetSharedCoordinates](9d41f633-f649-c77b-5c30-463f8ebb01a3.md) | Reset shared coordinates for the host model/file.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Save()()()()](8dec13b6-71f4-45d2-74e3-b109153721b5.md) | Saves the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Save(SaveOptions)](e567811b-4502-e938-c956-dce0e5cc17c2.md) | Saves the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.md) | Saves the document to a given file path.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SaveAs(String, SaveAsOptions)](df74c7e1-a98a-7751-676a-e9b074566f62.md) | Saves the document to a given file path.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SaveAs(ModelPath, SaveAsOptions)](db245ec6-e07a-b989-077a-a2947e308345.md) | Saves the document to a given path.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SaveAsCloudModel](2fd26edf-b1f8-905b-e5d7-b56eaa2a2eeb.md) | Saves current non-workshared or workshared model as a cloud model or workshared cloud model in BIM 360 Docs or Autodesk Docs.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SaveCloudModel](394bbf2c-5161-49de-773e-c019d558eb9f.md) | Saves cloud model.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SaveToProjectAsImage](0bc4b117-ffd3-616f-d378-bfcbb1fdae2f.md) | Creates an image view from the currently active view.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SeparateElements](3611bd74-e12a-ac93-0d33-6b5d23500bc5.md) | Separate a set of combinable elements out of combinations they currently belong to. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SetDefaultElementTypeId](bcd1ffba-2ddf-83b2-a243-fb0cfdba0b7c.md) | Sets the default element type id of the given DefaultElementType id.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SetDefaultFamilyTypeId](1f0d5aac-4602-b479-82b4-dc54a030c0a3.md) | Sets the default family type id for the given family category.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SetUnits](44eccb2b-65c6-a6d7-f6ac-07017fc12332.md) | Sets the units.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SynchronizeWithCentral](7de73a7b-68f0-87f2-f6a9-97d824024877.md) | Performs reload latest until the model in the current session is up to date and then saves changes back to central. A save to central is performed even if no changes were made.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | [UnpostFailure](5bc2e2e4-cdf8-18ad-d910-31f5fe400b74.md) | Deletes the posted failure message associated with a given FailureMessageKey.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
  
# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [ActiveProjectLocation](cd6733bb-4510-bb58-5ca5-21ededb30cdf.md) | Retrieve the active project location. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ActiveView](043960ac-dde4-0f45-249f-8161646a4362.md) | The document's active view. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [AddinFolder](47ffdf8b-ca4e-9b70-f7b3-f29ef39be302.md) | The full path to the Revit Macros module. |
|  | [Application](b517ce21-cec3-4cf3-e74b-aa0f219f6724.md) | Returns the Application in which the Document resides. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Create](f87f97d5-8402-62b5-4d6d-defe60c8f8ee.md) | An object that can be used to create new instances of Autodesk Revit API elements within a project. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [CreationGUID](4d2418fc-e00a-f5b8-609e-8f027eeed992.md) | A unique identifier generated when the Document was first created.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [DisplayUnitSystem](4da5af7a-3b64-b064-cd72-cbc0e9fa2135.md) | Provides access to display unit type with in the document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [FamilyCreate](693b2a55-b3a2-5d18-fcc4-e24448a16039.md) | An object that can be used to create new instances of Autodesk Revit API elements within a family document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [FamilyManager](478fde66-c9f0-86b5-204a-c95f18b69ca1.md) | The family manager object provides access to family types and parameters. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsDetached](0792283e-f112-0a57-d0d9-e79e6b9ea5b9.md) | Identifies if a workshared document is detached. Also, see [IsWorkshared](7f368167-6543-9be9-67a3-c6e1696ae060.md) (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsFamilyDocument](076721f1-772c-f8ec-2097-c3e674b37537.md) | Identifies if the current document is a family document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsLinked](5d44b5d0-b33f-26b6-10f4-b76d1bc4c949.md) | Identifies if a document is a linked RVT.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsModelInCloud](e12f7980-ba6c-2e72-6687-f0bf807ff014.md) | Identifies if document is stored on Autodesk cloud services.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsModifiable](af884262-3ba2-b0a0-d7ef-f0a49c1bf1bc.md) | Identifies if the document is modifiable.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsModified](1e67b9dd-2fca-0a54-91f6-620e550f6f56.md) | The state of changes made to the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsReadOnly](7e813a1b-9163-2509-f280-82572598432b.md) | Identifies if the document is read-only or can possibly be modified.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsReadOnlyFile](c189f723-1465-0353-2ec1-57183905d73a.md) | Signals whether the document was opened from a read-only file.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsValidObject](41477e88-aa81-4648-aa8b-8f2d482d4705.md) | Specifies whether the .NET object represents a valid Revit entity.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [IsWorkshared](7f368167-6543-9be9-67a3-c6e1696ae060.md) | Identifies if worksharing (i.e. editing permissions and multiple worksets) have been enabled in the document. Also, see [IsDetached](0792283e-f112-0a57-d0d9-e79e6b9ea5b9.md) (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [MassDisplayTemporaryOverride](c1ad0cf9-2063-7a9b-f087-fc1e4e8b7158.md) | This setting controls temporary display in views of objects with mass category or subcategories.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [MullionTypes](ce7bf7aa-4e38-fad1-15ed-816529815dbf.md) | This property is used to retrieve all the mullion types in current system. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [OwnerFamily](95b303dc-1569-492d-6863-fbe49f6189b0.md) | Get the Family of this Family Document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PanelTypes](8e6c5a87-528c-c13e-ed48-0e7c5af688d5.md) | Retrieves a set of PanelType objects that contains all the panel types that are currently loaded into the project. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ParameterBindings](ce28ad7d-30b7-29d9-8f81-c75aebc03581.md) | Retrieves an object from which mappings between parameter definitions and categories can be found. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PathName](8a92a6fd-ce25-cd86-2068-f9dcb24d72d6.md) | The fully qualified path of the document's disk file.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Phases](362b427f-bf0d-6509-e541-9d5cc48e1837.md) | Retrieves all of the phases in the document. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PlanTopologies](b782b091-bcd9-6759-9e39-4cd7a5bf3143.md) | Get the PlanTopologies of the current project in the last phase. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PlanTopologies[([( Phase])]) ](6cead23c-595a-8f54-8692-aa9daad9fb8d.md) | Gets the PlanTopologies of the current project in a given phase. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PlanTopology[([( Level])]) ](fb7a12ec-d4d7-b3a5-3613-5ee23d45c52f.md) | Get the PlanTopology of a given level in the last phase. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PlanTopology[([( Level, Phase])]) ](215a0d2b-0f9f-1532-cb15-d1f6a2af029a.md) | Get the PlanTopology of a given level in a given phase. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [PrintManager](514e70ec-341c-148a-aeea-eabcd8cf7ca1.md) | Retrieve the PrintManager of current project.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ProjectInformation](4db36834-e324-b199-7a5a-e3218e95da37.md) | Return the Project Information of the current project. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ProjectLocations](87be3885-b1aa-ba8c-f82e-a5a0f7455c3a.md) | Retrieve all the project locations associated with this project (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ReactionsAreUpToDate](55afb606-0de5-3f44-04e7-ccbe4a852c6a.md) | Reports if the analytical model has regenerated in a document with reaction loads. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Settings](1581b3ec-eaef-9ad9-3d57-cf75a4f09b58.md) | Provides access to general application settings, such as Categories. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [SiteLocation](0567eac8-811f-aed3-1ef3-c909992ceca7.md) | Returns the site location information. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [Title](4cee7916-d799-fc83-daf3-97cb03900b72.md) | The document's title.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [TypeOfStorage](895089ae-ad3f-200e-fa73-36979efd9ac8.md) | Get the storage type of the specified BuiltInParameter. (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [WorksharingCentralGUID](93287b85-2c12-ff55-177e-2a419fa893df.md) | The central GUID of the server-based model.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
  
# Events

|  | Name | Description |
| --- | --- | --- |
|  | [DocumentClosing](8f200255-a515-0c02-656b-b241e0011228.md) | Subscribe to the DocumentClosing event to be notified when Revit is just about to close a document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [DocumentPrinted](8d74cf02-9271-3c6c-00f5-bc7b48d52c56.md) | Subscribe to the DocumentPrinted event to be notified immediately after Revit has finished printing a view or ViewSet of the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [DocumentPrinting](77aa9939-8f41-1725-80dc-864ca1f7a49c.md) | Subscribe to the DocumentPrinting event to be notified when Revit is just about to print a view or ViewSet of the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [DocumentSaved](2f482b62-410e-2db9-b6b9-c64abedcbc4c.md) | Subscribe to the DocumentSaved event to be notified immediately after Revit has finished saving a document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [DocumentSavedAs](7ace570d-870f-be20-e493-e80ffa27f454.md) | Subscribe to the DocumentSavedAs event to be notified immediately after Revit has finished saving document with a new file name.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [DocumentSaving](26a118b5-c583-a9b2-c935-c11b270e140e.md) | Subscribe to the DocumentSaving event to be notified when Revit is just about to save a document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [DocumentSavingAs](e46e0d8f-5bcb-46bf-5def-03af68327b9e.md) | Subscribe to the DocumentSavingAs event to be notified when Revit is just about to save the document with a new file name.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ViewPrinted](ace39293-a976-d22b-4798-42bb8e82b307.md) | Subscribe to the ViewPrinted event to be notified immediately after Revit has finished printing a view of the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
|  | [ViewPrinting](941de0b6-a0f9-eb5a-5f25-9aa4d9da699a.md) | Subscribe to the ViewPrinting event to be notified when Revit is just about to print a view of the document.  (Inherited from [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md).) |
  
# See Also

[DocumentEntryPoint Class](99996ba9-d1a7-d27e-c0ce-eb271a4c35bb.md)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)