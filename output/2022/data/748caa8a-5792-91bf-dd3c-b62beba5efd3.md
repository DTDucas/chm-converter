# Create Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
Wire..::..Create Method   
[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.md "Wire Class") Example See Also  
---  
Creates a new wire. 
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public static Wire Create(
	Document document,
	ElementId wireTypeId,
	ElementId viewId,
	WiringType wiringType,
	IList<XYZ> vertexPoints,
	Connector startConnectorTo,
	Connector endConnectorTo
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	document As Document, _
	wireTypeId As ElementId, _
	viewId As ElementId, _
	wiringType As WiringType, _
	vertexPoints As IList(Of XYZ), _
	startConnectorTo As Connector, _
	endConnectorTo As Connector _
) As Wire
```
  
Visual C++  
---  
```text
public:
static Wire^ Create(
	Document^ document, 
	ElementId^ wireTypeId, 
	ElementId^ viewId, 
	WiringType wiringType, 
	IList<XYZ^>^ vertexPoints, 
	Connector^ startConnectorTo, 
	Connector^ endConnectorTo
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document. 
wireTypeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The id of the wire type of the newly created wire. 
viewId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The view in which the wire is to be visible. This must be the id of a floor plan or reflected ceiling plan view. 
wiringType
    Type: [Autodesk.Revit.DB.Electrical..::..WiringType](fb484864-f9d0-7335-1f91-d7ac587f15fb.md "WiringType Enumeration") Specifiies the wiring type for the newly created wire. The shape of the wire is determined by this value and the total number of points supplied via the vertexPoints and endpoint connectors. If the wiring type is WiringType.Arc: 
  * If there are 2 total points supplied, the wire is a straight-line wire.
  * If there are 3 total points supplied, the wire is a circular arc wire.
  * If there are 4 or more points, the wire is a spline wire.

If the wiring type is WiringType.Chamfer, a polyline wire will be created connecting all the points. 
vertexPoints
    Type: System.Collections.Generic..::..IList<(Of <(<'[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class")>)>)> The vertex point of the wire. If the startConnectorTo is nullNothingnullptra null reference (Nothing in Visual Basic), the first vertex of the vertexPoints will be the start point, otherwise, the start connector origin will be the start point. If the endConnectorTo is nullNothingnullptra null reference (Nothing in Visual Basic), the last vertex of the vertexPoints will be the end point, otherwise, the end connector origin will be the end point. 
startConnectorTo
    Type: [Autodesk.Revit.DB..::..Connector](11e07082-b3f2-26a1-de79-16535f44716c.md "Connector Class") The connector to which the wire start point connects. If nullNothingnullptra null reference (Nothing in Visual Basic), the start point connects to no existing connector. If set with a connector, the connector's origin will be added to the wire's vertices as the start point. 
endConnectorTo
    Type: [Autodesk.Revit.DB..::..Connector](11e07082-b3f2-26a1-de79-16535f44716c.md "Connector Class") The connector to which the wire end point connects. If nullNothingnullptra null reference (Nothing in Visual Basic), the end point connects to no existing connector. If set with a connector, the connector's origin will be added to the wire's vertices as the end point. 
# ### Return Value
The wire created. 
# Examples
CopyC#
```text
// Create an unconnected straight line wire between two points
public Wire CreateWire(Document document)
{
    Wire wire = null;

    FilteredElementCollector collector = new FilteredElementCollector(document);
    IList<Element> wireTypes = collector.OfCategory(BuiltInCategory.OST_Wire).WhereElementIsElementType().ToElements();
    WireType wireType = wireTypes.First() as WireType;

    if (wireType != null)
    {
        IList<XYZ> wireVertices = new List<XYZ>();
        wireVertices.Add(new XYZ(0, 0, 0));
        wireVertices.Add(new XYZ(2, 0, 0));

        wire = Wire.Create(document, wireType.Id, document.ActiveView.Id, WiringType.Arc, wireVertices, null, null);
    }

    return wire;
}
```

CopyVB.NET
```text
  ' Create an unconnected straight line wire between two points
  Public Function CreateWire(document As Document) As Wire
   Dim wire__1 As Wire = Nothing

   Dim collector As New FilteredElementCollector(document)
   Dim wireTypes As IList(Of Element) = collector.OfCategory(BuiltInCategory.OST_Wire).WhereElementIsElementType().ToElements()
   Dim wireType As WireType = TryCast(wireTypes.First(), WireType)

   If wireType IsNot Nothing Then
      Dim wireVertices As IList(Of XYZ) = New List(Of XYZ)()
      wireVertices.Add(New XYZ(0, 0, 0))
      wireVertices.Add(New XYZ(2, 0, 0))

      wire__1 = Wire.Create(document, wireType.Id, document.ActiveView.Id, WiringType.Arc, wireVertices, Nothing, _
         Nothing)
   End If

   Return wire__1
End Function
```

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | wireTypeId is not a valid WireType id. -or- viewId does not represent a view valid for a Wire element. Either a floor plan or reflected ceiling plan is expected. -or- vertexPoints is not valid, because one or more points are coincident by comparing the X and Y of the points, or there are not at least two points including the connectors. -or- startConnectorTo cannot be connected to a wire, as it is not an electrical connector. -or- endConnectorTo cannot be connected to a wire, as it is not an electrical connector. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md "DisabledDisciplineException Class") | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also
[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.md "Wire Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to 