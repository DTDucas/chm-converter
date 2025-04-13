

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Element..::..BoundingBox Property   
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Retrieves a box that circumscribes all geometry of the element.

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public [BoundingBoxXYZ](3c452286-57b1-40e2-2795-c90bff1fcec2.md) this[
    	[View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md) A_0
    ] { get; }  
  
Visual Basic  
---  
      
    
    Public ReadOnly Property BoundingBox ( _
    	A_0 As [View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md) _
    ) As [BoundingBoxXYZ](3c452286-57b1-40e2-2795-c90bff1fcec2.md)
    	Get  
  
Visual C++  
---  
      
    
    public:
    property [BoundingBoxXYZ](3c452286-57b1-40e2-2795-c90bff1fcec2.md)^ BoundingBox[[View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)^ A_0] {
    	[BoundingBoxXYZ](3c452286-57b1-40e2-2795-c90bff1fcec2.md)^ get ([View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)^ A_0);
    }  
  
#### Parameters

A_0
    Type: [Autodesk.Revit.DB..::..View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)

# Remarks

Pass in a view to query view-specific (e.g., cut) geometry or nullNothingnullptra null reference (Nothing in Visual Basic) for model geometry. If the view box is not known or cannot be calculated, this will return the model box; if the model box is not known, this will return nullNothingnullptra null reference (Nothing in Visual Basic). The box will always be aligned to the default axes of the model coordinate system (thus no rotation should be applied to the return value). Also note that this bounding box volume may enclose geometry that is not obvious. For example, the "flip controls" that could be part of a family will be included in the computation of the bounding box even though they are not always visible in the family instance of the family.

# Examples

CopyC#
    
    
    private void GetElementBoundingBox(Autodesk.Revit.DB.Document document, Autodesk.Revit.DB.Element element)
    {
        // Get the BoundingBox instance for current view.
        BoundingBoxXYZ box = element.get_BoundingBox(document.ActiveView);
        if (null == box)
        {
            throw new Exception("Selected element doesn't contain a bounding box.");
        }
    
        string info = "Bounding box is enabled: " + box.Enabled.ToString();
    
        // Give the user some information.
        TaskDialog.Show("Revit",info);
    }

CopyVB.NET
    
    
    Private Sub GetElementBoundingBox(document As Autodesk.Revit.DB.Document, element As Autodesk.Revit.DB.Element)
        ' Get the BoundingBox instance for current view.
        Dim box As BoundingBoxXYZ = element.BoundingBox(document.ActiveView)
        If box Is Nothing Then
            Throw New Exception("Selected element doesn't contain a bounding box.")
        End If
    
        Dim info As String = "Bounding box is enabled: " & box.Enabled.ToString()
    
        ' Give the user some information.
        TaskDialog.Show("Revit", info)
    End Sub

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)