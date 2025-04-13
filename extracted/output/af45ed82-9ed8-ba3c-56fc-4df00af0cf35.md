

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ControlledApplication..::..ViewPrinting Event  
[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Subscribe to the ViewPrinting event to be notified when Revit is just about to print a view of the document. 

**Namespace:** [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2010 

# Syntax

C#  
---  
      
    
    public event EventHandler<[ViewPrintingEventArgs](8e7d048f-a50b-7903-6001-6716f7eabdb5.md)> ViewPrinting  
  
Visual Basic  
---  
      
    
    Public Event ViewPrinting As EventHandler(Of [ViewPrintingEventArgs](8e7d048f-a50b-7903-6001-6716f7eabdb5.md))  
  
Visual C++  
---  
      
    
    public:
     event EventHandler<[ViewPrintingEventArgs](8e7d048f-a50b-7903-6001-6716f7eabdb5.md)^>^ ViewPrinting {
    	void add (EventHandler<[ViewPrintingEventArgs](8e7d048f-a50b-7903-6001-6716f7eabdb5.md)^>^ value);
    	void remove (EventHandler<[ViewPrintingEventArgs](8e7d048f-a50b-7903-6001-6716f7eabdb5.md)^>^ value);
    }  
  
# Remarks

This event is raised when Revit is just about to print a view of the document. If multiple views are combined to a single file, this event will be raised only once. 

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode. 

Event is not cancellable. The 'Cancellable' property of event's argument is always False.

The following API functions are not available for the current document during this event: 

  * All overloads of Autodesk.Revit.DB.Document.Export()
  * Autodesk.Revit.DB.Document.Print()
  * [Print()()()()](1ea1e825-8044-7a27-d9b9-ca463443c3b9.md) and similar overloads.
  * [SubmitPrint()()()()](0c9524b7-33b5-8c76-2843-c7024f03e4d7.md) and similar overloads.
  * [Close()()()()](da2f27b9-7255-4950-82a2-86e1432ff9f0.md) and similar overloads.
  * [Save()()()()](8dec13b6-71f4-45d2-74e3-b109153721b5.md) .
  * [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.md) and similar overloads.



Exception [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) will be thrown if any of the above methods is called during this event.

Another event [ViewPrinted](5f995f6a-15d8-b1c3-9bc4-3bd203dc16f6.md) will be raised immediately after view printing is finished.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.md)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)