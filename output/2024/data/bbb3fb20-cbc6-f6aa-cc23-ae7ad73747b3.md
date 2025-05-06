# CreateSet Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
AlignmentStationLabel..::..CreateSet Method   
[AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.md "AlignmentStationLabel Class") See Also  
---  
Creates a collection of [AlignmentStationLabel](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.md "AlignmentStationLabel Class") objects along with their underlying [SpotDimension](f3c633ac-1595-cb8d-5c1b-66eb3eefb433.md "SpotDimension Class") elements. 
**Namespace:** [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.md "Autodesk.Revit.DB.Infrastructure Namespace")**Assembly:** Autodesk.CivilAlignments.DBApplication (in Autodesk.CivilAlignments.DBApplication.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2021.1 
# Syntax
C#  
---  
```text
public static ICollection<AlignmentStationLabel> CreateSet(
	Alignment alignment,
	View view,
	AlignmentStationLabelSetOptions options
)
```
  
Visual Basic  
---  
```text
Public Shared Function CreateSet ( _
	alignment As Alignment, _
	view As View, _
	options As AlignmentStationLabelSetOptions _
) As ICollection(Of AlignmentStationLabel)
```
  
Visual C++  
---  
```text
public:
static ICollection<AlignmentStationLabel^>^ CreateSet(
	Alignment^ alignment, 
	View^ view, 
	AlignmentStationLabelSetOptions^ options
)
```
  
# ### Parameters
alignment
    Type: [Autodesk.Revit.DB.Infrastructure..::..Alignment](6594712d-3b22-9b08-ab4c-782df88f36d1.md "Alignment Class")The alignment on which the alignment station label is placed.
view
    Type: [Autodesk.Revit.DB..::..View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md "View Class")The view for which the alignment station label is created.
options
    Type: [Autodesk.Revit.DB.Infrastructure..::..AlignmentStationLabelSetOptions](15f4337d-738d-ec32-e7bc-4f2c569f4c59.md "AlignmentStationLabelSetOptions Class")The alignment station options of the label set to be created.
# See Also
[AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.md "AlignmentStationLabel Class")
[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.md "Autodesk.Revit.DB.Infrastructure Namespace")
Send comments on this topic to 