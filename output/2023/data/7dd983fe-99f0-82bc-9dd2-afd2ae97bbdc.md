# BuiltInFailures.InfillFailures Properties (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2023 API  
---  
BuiltInFailures..::..InfillFailures Properties  
[BuiltInFailures..::..InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.md "BuiltInFailures.InfillFailures Class") See Also  
---  
The [BuiltInFailures..::..InfillFailures](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.md "BuiltInFailures.InfillFailures Class") type exposes the following members.
# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [CannotDeleteInfill](914040e3-dcd3-b686-53a9-b93b93aa16fb.md "CannotDeleteInfill Property") | Can't delete infilling element without deleting its insert or host. |
| [FamilyInstanceIsNotCuttingHost](fd95a0c2-367e-00cb-69c3-812819d35e1c.md "FamilyInstanceIsNotCuttingHost Property") | Instance is not cutting host. |
| [InfillCannotChangeType](877afc0f-3a3a-484b-0361-65a5738cdab3.md "InfillCannotChangeType Property") | Infilling element replaced by a later phase insert must be the same type as the insert's host. |
| [InfillCannotHaveDiffThickness](69e99bb2-78d2-d3e0-af2e-71084838b771.md "InfillCannotHaveDiffThickness Property") | This infilling element must have the same thickness as its host. |
| [InfillDifferentPhase](7df3db53-ead3-daca-4174-602548754230.md "InfillDifferentPhase Property") | Wall and instance have different phasing settings. Automatic creation of the infilling wall fails. |
| [InfillLost](bd49fc31-fcc7-8440-bfba-e3047688a6f5.md "InfillLost Property") | Standalone infilling Wall is separated from its insert. |
| [InfillNoSlopeGlazing](00feb0be-205e-2c2d-abdf-939d3a672fb5.md "InfillNoSlopeGlazing Property") | Could not change type due to highlighted infilling element. 'Sloped glazing' infills are not allowed. |
| [InfillNoThicknessCeiling](f5c1f72a-852f-b090-a83e-871619fcd092.md "InfillNoThicknessCeiling Property") | Could not change type due to highlighted infilling element. 'Basic Ceiling' infills are only compatible with 'Basic Ceiling' hosts. |
| [InfillNoThicknessMultiface](7930961a-26d0-fa5d-60c1-0598db0896fe.md "InfillNoThicknessMultiface Property") | Highlighted infilling element could not have thickness different from its host because it spans multiple faces. |
| [InPlaceFamilyNotCuttingHost](d19b81bb-d410-2798-b78a-8b22fa10597e.md "InPlaceFamilyNotCuttingHost Property") | Instance of in-place family is not cutting host. |
| [InsertJoinedWall](f0b21b56-7868-cb17-6436-23adc86199d5.md "InsertJoinedWall Property") | Insert conflicts with joined Wall. |
| [InsertOverlapsOrOut](206e7d23-9a5b-7631-ac1d-895bdef74419.md "InsertOverlapsOrOut Property") | Highlighted inserts overlap with other inserts or completely miss their hosts. |
| [MovedInfillToHost](03424834-8711-9e91-367b-8c414dc092d3.md "MovedInfillToHost Property") | Infilling element was automatically moved to keep it aligned to host. |

# See Also
[BuiltInFailures..::..InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.md "BuiltInFailures.InfillFailures Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 