# FamilyInstanceFilter Class (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
FamilyInstanceFilter Class  
[Members](0ab03be9-6cb6-27b2-32b1-25057f96492e.md "FamilyInstanceFilter Members") Example See Also  
---  
A filter used to find elements that are family instances of the given family symbol. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public class FamilyInstanceFilter : ElementSlowFilter
```
  
Visual Basic  
---  
```text
Public Class FamilyInstanceFilter _
	Inherits ElementSlowFilter
```
  
Visual C++  
---  
```text
public ref class FamilyInstanceFilter : public ElementSlowFilter
```
  
# Remarks
This filter is a slow filter, but it uses a quick filter to eliminate non-candidate elements before the elements are obtained and expanded. Therefore this filter does not have to be paired with another quick filter to minimize the number of Elements that are expanded. 
# Examples
CopyC#
```text
// Creates a FamilyInstance filter for elements that are family instances of the given family symbol in the document

// Find all family symbols whose name is "W10X49"
FilteredElementCollector collector = new FilteredElementCollector(document);
collector = collector.OfClass(typeof(FamilySymbol));

// Get Element Id for family symbol which will be used to find family instances
var query = from element in collector where element.Name == "W10X49" select element;
List<Element> famSyms = query.ToList<Element>();
ElementId symbolId = famSyms[0].Id;

// Create a FamilyInstance filter with the FamilySymbol Id
FamilyInstanceFilter filter = new FamilyInstanceFilter(document, symbolId);

// Apply the filter to the elements in the active document
collector = new FilteredElementCollector(document);
ICollection<Element> familyInstances = collector.WherePasses(filter).ToElements();
```

CopyVB.NET
```text
' Creates a FamilyInstance filter for elements that are family instances of the given family symbol in the document

' Find all family symbols whose name is "W10X49"
Dim collector As New FilteredElementCollector(document)
collector = collector.OfClass(GetType(FamilySymbol))

' Get Element Id for family symbol which will be used to find family instances
Dim query As System.Collections.Generic.IEnumerable(Of Autodesk.Revit.DB.Element)
query = From element In collector _
 Where element.Name = "Level 1" _
 Select element

Dim famSyms As List(Of Element) = query.ToList()
Dim symbolId As ElementId = famSyms(0).Id

' Create a FamilyInstance filter with the FamilySymbol Id
Dim filter As New FamilyInstanceFilter(document, symbolId)

' Apply the filter to the elements in the active document
collector = New FilteredElementCollector(document)
Dim familyInstances As ICollection(Of Element) = collector.WherePasses(filter).ToElements()
```

# Inheritance Hierarchy
System..::..Object [Autodesk.Revit.DB..::..ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md "ElementFilter Class") [Autodesk.Revit.DB..::..ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.md "ElementSlowFilter Class") Autodesk.Revit.DB..::..FamilyInstanceFilter
# See Also
[FamilyInstanceFilter Members](0ab03be9-6cb6-27b2-32b1-25057f96492e.md "FamilyInstanceFilter Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 