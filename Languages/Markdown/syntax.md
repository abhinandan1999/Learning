#### <u>Newline</u>
To add a new line in markdown, just add forward slash "\<br>" at the end of line

#### <u>Bold</u>:
For any word to be bold in markdown it should be within ** word**

For ex: **Bold**

#### <u>Italics</u>:
To italicize any word in markdown, keep it between * text* or _ text_

For ex: *Hello* _world_

#### <u>Headings</u>
There are six types of headings. 
The largest one starts with # and last one has ######
Note: Please add a space after #

#### <u>Links</u>
To add a link use square brackets followed by link in parentheses.
[Link_name](https://www.javatpoint.com/link-in-markdown)

#### <u>Images</u>
Images in Markdown can be created by inserting the **image name** inside the square brackets and **image link URL** inside the parenthesis with an exclamation symbol at the beginning.
![image_name](Image_path)
Image path could be:
1) Either link to the image
2) Local Path to image

#### <u>Blockquotes</u>
The blockquotes refers to the quotes that requires a special attention from the normal text. The blockquotes can be specified using the greater than symbol (>) at the starting line.

>    Hello
>    world

Note: There should be one tab space between the greater than symbol and the text. Otherwise, it will be considered as a normal text rather than the blockquotes.

#### <u>Lists</u>
There are two types of lists:
1) Ordered List
- Unordered List

Ordered List can be created by simply typing the number.
Unordered lists are created by typing * or -

1) List A
	1) Sublist A

* Unordered List A
	* Unordered sublist A


#### <u>Underline</u>
To underline any text keep it between <u>text</u>

#### <u>Text Highlight</u>
To highlight text in markdown we can start and end sentence with two double equalto sign without space between them.

==Highlight==

#### <u>Codeblocks</u>
The code in Markdown is represented using the three backtick symbols at the starting and the three backticks symbols at the end.

Note: The text should be inserted between the three backtick symbols, but not in the same line. Markdown ignore the text specified on the same line as that of symbols.

```
import pandas as pd
```

#### <u>Comments</u>
There are three ways to comments:
1. <!--Comments 1-->
2. %% Comments 2 %%
3.  %%Select the word or line and press "ctrl + /"%%

#### <u>Footnotes</u>
Footnotes allow us to specify the notes or reference without affecting the document appearance. It is represented as a symbol in the form of a **superscript** followed by a number/word. When we specify a footnote, a superscript number as the reference link appears, which redirects the user to the bottom of the page.

To create a footnote in Markdown, add a number inside the square brackets followed by a caret symbol (^).

Note: In Obsidian it works reverse: ^[Footnote message]

Ex:
Footnote ^[What the hell] Footnote 2^[2 means 2]

#### <u>Strikethrough</u>
To create a strikethrough symbol, keep it between double tilde symbol without spaces.

For ex:
~~Strike it~~

#### <u>Superscript</u>
To create a superscript, keep it between  <sup>character</sup>
A<sup>2</sup>


#### <u>Subscript</u>
To create a superscript, keep it between  <sub>character</sub>
A<sub>2</sub>



#### <u>Definition List</u>
To create a definition, we need to type the main heading of the definition in the first and the definition part in the second line starting with the colon.

Definition
: This is the definition




#### <u>Task List</u>
The task lists can be created using a hyphen followed by the square brackets.
Note: There should be one space between - and [space] Task Item
- [ ]    Option A
- [ ]    Option B

#### <u>Tables</u>
To create a table, use the pipe symbols as follows and for alignment use colon symbol as follows:
| col_1 | col_2 | col_3 |
|:------|:-------:|------:|
|data1|data2   |data 3|

| Name | Description | Comments |
|:-------|:-------------:|-------------:|
| Hello  | World          | India           |

#### <u>Latex Syntax</u>
Text can be converted to latex by encapsulating it between \$$ text $$ text <br>
Example:
$$ P(w) $$
