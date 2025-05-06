# SetBoldStatus Method (TextRange, Boolean) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
FormattedText..::..SetBoldStatus Method (TextRange, Boolean)  
[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.md "FormattedText Class") See Also  
---  
Sets the characters in a given text range to be bold or not bold. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public void SetBoldStatus(
	TextRange textRange,
	bool isBold
)
```
  
Visual Basic  
---  
```text
Public Sub SetBoldStatus ( _
	textRange As TextRange, _
	isBold As Boolean _
)
```
  
Visual C++  
---  
```text
public:
void SetBoldStatus(
	TextRange^ textRange, 
	bool isBold
)
```
  
# ### Parameters
textRange
    Type: [Autodesk.Revit.DB..::..TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.md "TextRange Class") The given text range. 
isBold
    Type: System..::..Boolean The desired bold status of characters in the given text range. True to set bold, false to set not bold. 
# Remarks
To make the numbers or letters in a list bold, apply the bold status to the carriage return character that ends the list paragraph. 
The given text range should not be empty. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | This text range is empty. -or- This start index of this text range is not within the text range identifying the entire text. -or- The end of this text range is not within the text range identifying the entire text. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.md "FormattedText Class")
[SetBoldStatus Overload](03b043e7-7056-6476-b223-d81c15b5ccc3.md "SetBoldStatus Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 