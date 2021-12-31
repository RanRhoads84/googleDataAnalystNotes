# Functions in spreadsheets

## Auto Filling

The lower-right corner of each cell has a fill handle. It is a small green square in Excel and a small blue one in Google Sheets

- Click the fill handle for a cell and drag it down a column to auto-fill other cells un the column with the same formula or function used in that cell
- Click the fill handle for a cell and drag it across a row to auto-fill other cells in the row with the same formula or function

## Relative, Absolute and Mixed References

- **Relative** references (cells referenced without a dollar sign, like A2) will change when you copy and paste the function into a different cell. With relative references, the location of the cell that contains the function determines the cells used by the function.
- **Absolute** references (cells fully referenced with a dollar sign, like $A$2) will not change when you copy and paste the function into a different cell. With absolute references, the cells are referenced always remain the same.
- **Mixed** references (Cells partially referenced with a dollar sigh, like $A2 or A$2) will change when you copy and paste the function into a different cell. With mixed references, the location of the cell that contains the function determines the cells used by the function, but only the row or column is relative, not both.
- In spreadsheets, you can press the F4 key to toggle between relative, absolute, and mixed references in a function. Click the cell containing the function, highlight the referenced cells in the formula bar, and then press F4 to toggle between and select relative, absolute, or mixed referencing.

## Data Ranges

- When you click a cell that contains a function, colored data ranges in the formula bar indicate which cells are being used in the spreadsheet. There are different colors for each unique range in a function.
- Colored data ranges help prevent you from getting lost in complex functions.
- In spreadsheets, you can press the F2 key to highlight the range of data used by a function. click the cell containing the function, highlight the rage of data used by the function in the formula bar, and then press F2. The spreadsheet will go to and highlight the cells specified by the range.

## Data Ranges Evaluated for a Condition

**COUNTIF** is an example of a function that returns a value based on a condition that the data range is evaluated for. The function counts the number of cells that meet the criteria, For example, in an expense spreadsheet, use COUNTIF to count the number of cells that contain a reimbursement for "airfare".
