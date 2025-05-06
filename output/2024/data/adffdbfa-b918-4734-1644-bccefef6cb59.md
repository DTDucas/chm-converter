# BuiltInFailures.ImportFailures Members (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2024 API  
---  
BuiltInFailures..::..ImportFailures Members  
[BuiltInFailures..::..ImportFailures Class](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.md "BuiltInFailures.ImportFailures Class") Properties See Also  
---  
Provides a container of all Revit built-in FailureDefinitionId instances.
The [BuiltInFailures..::..ImportFailures](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.md "BuiltInFailures.ImportFailures Class") type exposes the following members.
# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [ATFContainedUnsupportedGeometricData](48884c0e-99a0-f504-3c1a-6e6464627385.md "ATFContainedUnsupportedGeometricData Property") | The original model contains unsupported geometric data such as curves or points. |
| [ATFNonUniformScalingTransform](20ac0edb-b4da-951b-db57-a1ce2c2fa59b.md "ATFNonUniformScalingTransform Property") | The imported geometry contains non-uniform scaling transformations which Revit does not support. Some objects may be displaced or distorted. |
| [BadFaceFoundInDwg](26ecad6f-f1c9-82a0-a93f-07893ca4618c.md "BadFaceFoundInDwg Property") | One or more hatch regions were found in the imported file with unconnected boundaries. These hatch regions will be ignored. |
| [CannotChangeImportSymbol](0f49b99b-e706-261d-b68c-73d836b8a7a6.md "CannotChangeImportSymbol Property") | Can't change an imported or linked element's symbol type. |
| [CannotExplodeElement](b9f70cfe-0c26-f422-679b-e3166fc29b67.md "CannotExplodeElement Property") | Can't explode the imported object. |
| [CannotImportFile](1cccb9c4-dec6-41ca-b440-c32b2f49180b.md "CannotImportFile Property") | Can't import file. |
| [ElementRenamedOnImport](e49bd060-0b15-6311-fbea-2e50b9d09e34.md "ElementRenamedOnImport Property") | There were duplicate names between the active model and the imported element. To avoid duplicate names, the imported element has been renamed. |
| [FailedToSetWorkplane](c225b987-3ca3-4fa8-0d75-dcd829efc59e.md "FailedToSetWorkplane Property") | Could not set Work Plane of [Import].\n\nPlease use the Work Plane tool to set a Work Plane for this view. |
| [IFCCantUpdateLinkedFile](2802ee0b-6ad3-3752-9323-1bb88c999f54.md "IFCCantUpdateLinkedFile Property") | The cached version of this IFC file is already loaded into another document in this session, and can't be updated. To update the IFC file, please close all other documents containing the link, and then update. |
| [IFCGenericImportWarning](3d7dc58d-83c0-f515-7575-b7bdf85e5b55.md "IFCGenericImportWarning Property") | The following problems were encountered in the IFC file: [Description] |
| [IFCGenericRevitImportWarning](10ead511-26d4-29f2-6c73-3ba590583701.md "IFCGenericRevitImportWarning Property") | Revit had the following problems importing the IFC file: [Description] |
| [IFCPartialSchemaSupport](65a99147-4571-7ad1-e62b-d1f48c678071.md "IFCPartialSchemaSupport Property") | IFC versions 4 and above are only partially supported by Open IFC. Consider using Link IFC instead. |
| [ImportedModelIsEmpty](bc5cf153-9213-9817-74ef-0715df5341a2.md "ImportedModelIsEmpty Property") | Imported model is empty. |
| [ImportModelOutOfRange](349d1b36-172d-e603-4501-991d30b0dc5c.md "ImportModelOutOfRange Property") | The imported model is out of range. |
| [ImportModelTooLarge](19fe739a-b6c0-5435-ff2a-00a67ae78405.md "ImportModelTooLarge Property") | The imported model is too large. |
| [ImportScaleTooLarge](78a38c0a-85c8-5592-1a3d-929f949aeebd.md "ImportScaleTooLarge Property") | This scale factor would make the imported object too large. Reverting to the previous scale factor. |
| [ImportSymbolBaseLevelInvalid](87a7be79-852d-6ac8-208d-e90fe98a9086.md "ImportSymbolBaseLevelInvalid Property") |
| [ImportTooFarAway](f118c891-0c30-a2e1-c66e-d6681acf7205.md "ImportTooFarAway Property") | Imported objects located a large distance from the model might not display properly. The 'Center-to-Center' option will be used. |
| [ImportTooManyElmentsToExplode](9e04d13e-c412-0f7d-bfea-154e52cf6b73.md "ImportTooManyElmentsToExplode Property") | Import Instance has [Number] elements. Imports with more than 10,000 elements cannot be exploded. |
| [LostAcisObjectsOnImport](db2ec814-2d4e-b2e0-ef22-84ff6790b854.md "LostAcisObjectsOnImport Property") | Some ACIS objects could not be imported. To import them, use AutoCAD to convert them into polymesh objects and reimport. |
| [SomeObjectsNotExploded](2ca3b49b-9378-3032-7c59-f3a1b2e9ae3d.md "SomeObjectsNotExploded Property") | Import contained some 3D data or points which can't be exploded. |
| [TextNotImported](c03d7029-6539-e072-126c-78b46c0fe580.md "TextNotImported Property") | Text is only imported if the "Current View Only" option is selected. To see the text in the original file, import again with this check box selected in the Import Dialog. |
| [TooManyPickFaces](a64a00d5-acc4-0b27-cb5b-2c24f755cbfa.md "TooManyPickFaces Property") | Too many faces were created from imported meshes. Host by Face tools may not select the imported meshes correctly. Decrease the complexity of the file or try importing only selected layers to resolve. |
| [WorksetCreatedForLinkWarning](ad3826c2-1cde-0e01-0bee-f92853fbabd4.md "WorksetCreatedForLinkWarning Property") | Newly created link types and instances were placed in new workset [workset name] |

# See Also
[BuiltInFailures..::..ImportFailures Class](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.md "BuiltInFailures.ImportFailures Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 