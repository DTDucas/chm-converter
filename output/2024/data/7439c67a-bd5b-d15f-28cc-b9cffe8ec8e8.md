# ElementFilterIsAcceptableForParameterFilterElement Method (Document, ISet(ElementId), ElementFilter) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ParameterFilterElement..::..ElementFilterIsAcceptableForParameterFilterElement Method (Document, ISet<(Of <(<'ElementId>)>)>, ElementFilter)  
[ParameterFilterElement Class](b231dc85-516a-5e75-c634-c6cd81b43fc5.md "ParameterFilterElement Class") See Also  
---  
Checks that an ElementFilter is acceptable for use in defining the filtering rules for a given list of categories (i.e., for view filtering). 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2019 
# Syntax
C#  
---  
```text
public static bool ElementFilterIsAcceptableForParameterFilterElement(
	Document aDocument,
	ISet<ElementId> categories,
	ElementFilter elementFilter
)
```
  
Visual Basic  
---  
```text
Public Shared Function ElementFilterIsAcceptableForParameterFilterElement ( _
	aDocument As Document, _
	categories As ISet(Of ElementId), _
	elementFilter As ElementFilter _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool ElementFilterIsAcceptableForParameterFilterElement(
	Document^ aDocument, 
	ISet<ElementId^>^ categories, 
	ElementFilter^ elementFilter
)
```
  
# ### Parameters
aDocument
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document in which to create the ParameterFilterElement. 
categories
    Type: System.Collections.Generic..::..ISet<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> The categories for the new ParameterFilterElement. 
elementFilter
    Type: [Autodesk.Revit.DB..::..ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md "ElementFilter Class") The ElementFilter to validate. 
# Remarks
ElementFilter is either an ElementParameterFilter or an ElementLogicalFilter representing a Boolean combination of ElementParameterFilters. In addition, we check that each ElementParameterFilter satisfies the following conditions: Its array of FilterRules is not empty and contains: 
  * Any number of FilterRules of type FilterValueRule, FilterInverseRule, and SharedParameterApplicableRule or 
  * Exactly one FilterCategoryRule containing only one category from categories stored by this ParameterFilterElement or 
  * Exactly two rules: the first one is a FilterCategoryRule containing only one category from categories stored by this ParameterFilterElement and the second one is a FilterRule of type FilterValueRule, FilterInverseRule, or SharedParameterApplicableRule. 

Note that cases in the second and third bullet are currently allowed only if the parent node of ElementParameterFilter is LogicalOrFilter. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ParameterFilterElement Class](b231dc85-516a-5e75-c634-c6cd81b43fc5.md "ParameterFilterElement Class")
[ElementFilterIsAcceptableForParameterFilterElement Overload](1ea4b742-414d-a165-1306-aed309bbb1ef.md "ElementFilterIsAcceptableForParameterFilterElement Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 