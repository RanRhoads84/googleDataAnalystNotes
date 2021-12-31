# Quick Reference: Formulas in Spreadsheets

You have been learing a lot about spreadsheets and all kinds of time-saving calculations and organizational features they offer. One of the most valuable spreadsheet features is a formula. As a quick reminder, a formula is a set of instructions that does specific calculation using the data in a spreadsheet. Formulas make it easy for data analysts to do powerful calculations automatically, which helps them analyze data more effectively. Below is a quick-reference guide to help you get the most out of formulas.

## Formulas

**The Basics**

- When you write a formula in math, it generally ends with an equal sign (2+3 = ?). But with formulas [in spreadsheets] they always start with one instead, (=A2+A3, think “cell is equal to;). The equal sign tells the spreadsheet that what follows is part of a formula, not just a word or number in a cell.
- After you type the equal sign, most spreadsheet applications will display an autocomplete menu that lists valid formulas, names, and text strings (like intelli-sense). This is a great way to create and edit formulas while avoiding typing and syntax errors.
- A fun way to learn new formulas is just by typing an equal sign and a single letter. Choose one of the options that pops up and you will learn what that formula does.

## Mathematical Operators

- The mathematical operators used in a spreadsheet include
- Subtraction - Minus Sign (-)
- Addition - Plus Sign (+)
- Division - Forward Slash (/)
- Multiplication - asterisk (\*)

## Auto-Filling

The lower right corner of each cell has a fill handle. It is a small green square in Excel and a small Blue square in Sheets

- Click the fill handle for a cell and drag it down a column to auto-fill other cells in the column with the same value or formula in that cell.
- Click the fill handle for a cell and drag it across a row to auto-fill other cells in the row with the same value or formula in that cell.
- If you want to create a numbered sequence in a column or row, do the following;

  - Fill in the first two numbers of the sequence in two adjacent cells
  - Select to highlight the cells
  - Draw the fill handle to the last cell to complete the sequence of numbers.

- For example, to insert 1 through 100 in each row of a column, enter 1 in cells A1 and 2 in cell A2. Then, select to highlight both cells, click the fill handle in cell A2, and drag it down to cells A100. This auto-fills the numbers sequentially so you don't have to type them in each cell.

## Absolute Referencing

- Absolute referencing is marked by a dollar($) sign. For example, =$A$10 has the absolute referencing for both the column(A) and row(10) value.
- Relative references (which is what you normally do e.g. “=A10”) will change anytime the formula is copied “=A10” to the cell to the right would become “=B10”. With absolute referencing “=$A$10” copied to the cell to the right would remain “=$A$10” But if you copied $A$10 to the cell below it would change to $A11 because the row value isn’t an absolute reference.
- Absolute references will _NOT_ change when you copy and paste the formula in a different cell. The cell being referenced is always the same.
- To easily switch between absoulte and relative referencing in the formula bar, highlight the reference you want to change and press the “F4” key

## Data Range

- When you click into your formula, the colored ranges let you see which cells are being used in your spreadsheet. There are different colors for each unigue range in your formula.
- In a lot of spreadsheet apps you can press F2 (or enter) to highlight the range of data in the spreadsheet that is referenced in a formula. Click the cell with the formula, and then press F2 (or enter) to highlight the data in your spreadsheet.

## Combining with Functions

- COUNTIF() is a formula _and_ a function. This means the function runs based on criteria set by the formula. In this case, COUNT is the formula; it will be excuted IF the conditions you create are true. For example, you could use =COUNTIF(A1:A16, “7”) to count only the cells that contained the number 7. Combining formulas and funtions allows you to do more work with a single command.
