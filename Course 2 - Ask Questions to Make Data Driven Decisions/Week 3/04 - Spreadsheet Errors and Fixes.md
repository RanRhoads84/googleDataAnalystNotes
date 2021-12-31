# Spreadsheet errors and fixes

When you are new to data analytics-and sometimes even when you aren't-spreadsheet struggles are real. It never feels good when you tuype in what you are sure is a perfect formula or function, only to get an error message. Understanding errors and how to fix them is a big part of keeping your data clean, so it's important to know how to deal with issues as they come up, and more importantly, not to get discouraged.

<br>

Remember, even the most advanced spreadsheet users come across problems from time to time.

<br>

As a follow up to what you learned in the video, here are a few best practices and helpful tips. These strategies will help you avoid spreadsheet errors to begin with, making your life in analytics a whole lot less stressful:

1. Filter data to make your spreadsheet less complex and busy.
2. Use and freeze headers so you know wheat is in each column, even when scrolling.
3. When multiplying numbers, use an asterisk (\*) not an X.
4. Start every forumlua and function with an equalsign (=)
5. Whenever you use an open parenthesis, make sure there is a closed parenthesis on the other end to match.
6. Change the font to something easy to read.
7. Set the border colors to white so that you are working in a blank sheet.
8. Create a tab with just the raw data, and a separate tab with just the data you need.

Now that you learned some basic ways to avoid errors, you can focus on what to do when that dreaded pop-up does appear. The following take is a reference you can use to look up common spreadsheet errors and examples of each. Knowing what the errors mean takes some of the fear out of getting them.

**#DIV/0!**

- A formula is trying to divide a value in a cell by ) (or an empty cell that has no value

**#ERROR!**

- (Google Sheets Only) Something can't be interpreted as it has been input. This is also know as a parsing error.

**#N/A!**

- A formula cant find the data

**#NAME?**

- The name of the formula or function used isn't recognized

**#NUM!**

- The spreadsheet cant perform a formula calculation because a cell has an invalid numeric value

**#REF!**

- A formula is referencing a cell that isn't valid

**#VALUE!**

- A general error indicating a problem with a formula or with referenced cells

If you are working with Excel, an interactive page, [How to correct a #VALUE! error](https://support.microsoft.com/en-us/office/how-to-correct-a-value-error-15e1b616-fbf2-4147-9c0b-0a11a20e409e), can help you narrow down the cause of this error. You can select a specific function from a drop-down list to display a link to tips to fix the error when using that function.

## Pro tip: Spotting errors in spreadsheets with conditional formatting

Conditional formatting can be used to highlight cells a different color based on their contents. This feature can be extremely helpful when you want to locate all errors in a large spreadsheet. For example, using conditional formatting, you can highlight in yellow all cells that contain an error, and then work to fix them.

Conditional formatting in Microsoft Excel

To set up conditional formatting in Microsoft Excel to highlight all cells in a spreadsheet that contain errors, do the following:

    1. Click the gray triangle above row number 1 and to the left of Column A to select all cells in the spreadsheet.

    2. From the main menu, click Home, and then click Conditional Formatting to select Highlight Cell Rules  More Rules.

    3. For Select a Rule Type, choose Use a formula to determine which cells to format.

    4. For Format values where this formula is true, enter =ISERROR(A1).

    5. Click the Format button, select the Fill tab, select yellow (or any other color), and then click OK.

    6. Click OK to close the format rule window.

To remove conditional formatting, click Home and select Conditional Formatting, and then click Manage Rules. Locate the format rule in the list, click Delete Rule, and then click OK.
Conditional formatting in Google Sheets

To set up conditional formatting in Google Sheets to highlight all cells in a spreadsheet that contain errors, do the following:

    1. Click the empty rectangle above row number 1 and to the left of Column A to select all cells in the spreadsheet. In the Step-by-step in spreadsheets video, this was called the Select All button.

    2. From the main menu, click Format and select Conditional Formatting to open the Conditional format rules pane on the right.

    3. While in the Single Color tab, under Format rules, use the drop-down to select Custom formula is, enter =ISERROR(A1), select yellow (or any other color) for the formatting style, and then click Done.

To remove conditional formatting, click Format and select Conditional Formatting, and then click the Trash icon for the format rule.
Spreadsheet error resources

To learn more and read about additional examples of errors and solutions, explore these resources:

    * Microsoft Formulas and Functions: This resource describes how to avoid broken formulas and how to correct errors in Microsoft Excel. This is a useful reference to have saved in case you run into a specific error and need to find solutions quickly while working in Excel.

    * When Your Formula Doesn’t Work: Formula Parse Errors in Google Sheets: This resource is a guide to finding and fixing some common errors in Google Sheets. If you are working with Google Sheets, you can use this as a quick reference for solving problems you might encounter working on your own.

With some practice and investigative determination, you will become much more comfortable handling errors in spreadsheets. Each error you can catch and fix will make your data clearer, cleaner, and more useful.
