# Embrace Changelogs

What do engineers, writes, and data analysts have in common? Change.

Engineers use engineering change orders (ECOs) to keep track of new project design details and proposed changes to existing products.
Writers use document revision histories to keep track of changes to document flow and edits. And data analysts use changelogs to keep track of data transformation and cleaning. Here are some examples of these:

![Changelogs](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/pr6P4pdeTFi-j-KXXhxY5w_2b7d8a3b5343431c9a50d00357b92e25_Screen-Shot-2021-01-25-at-1.56.25-PM.png?expiry=1644451200000&hmac=CaBSER8QX8bupNv5fOWtkdxpy2lSRkyKugdnSMcSOSc)

## Automated Version control takes you most of the way

Most software applications have a kind of history tracking built in. For example, in Google Sheets, you can check the version history of an entire sheet or an individual cell and go back to an earlier version. In Microsoft Excel, you can use a feature called **Track Changes**. And in **Big Query** you can view the history to check what has changed.

## How it works;

### Google Sheets

1. Right click the cell and select _*Show Edit History*_
2. Click the left arrow or right arrow to move backward and forward in the navigate through the history

### Microsoft Excel

1. If Track Changes has been enabled for the spreadsheet; click **Review**
2. Under **Track Changes**, click the **Accept/Reject Changes** option to accept or reject any change made.

### Big Query

- Bring up a previous version (without reverting to it) and figure out what changed by comparing it to the current version.

## Changelogs take you down the last mile

A Changelog can build on your automated version history by giving you an eve more detailed record of your work. This is where data analysts record all the changes they make to the data. Here is another way of looking at it. Version histories record _what_ was done in a data change for a project, buy doesn't tell us _why_. Changelogs are super useful for helping us understand the reasons changes have been made. Changelogs have no set format and you can even make your entries in a blank document. But if you are using a shared changelog, it is best to agree with other data analysts on the format of all your log entires.

## Typically, a changelog records this type of information:

- Data, file, formula, query, or any other component that has changed
- Description of what changed
- Date of the change
- Person who made the change
- Person who approved the change
- Version number
- Reason for the change

Let's say you made a change to a formula in a spreadsheet because you observed it in another report and you wanted your data to match and be consistent. If you found out later that the report was actually using the wrong formula, an automated version history would help you _undo_ the change.
But if you also recorded the reason for the change in a changelog, you could go back to the creators of the report and let them know about the incorrect formula. If the change happened awhile ago you might not remember who to follow up with. Fortunately, your changelog would have that information ready for you. By following up, you would ensure data integrity outside your project. You would also be showing personal integrity as someone who can be trusted with data. That is the power of a changelog.

Finally, a changelog is important for when lots of changes to a spreadsheet or query have been made. imagine an analyst made four changes and they change they want to revert to is change #2. instead of clicking the undo feature three times to undo change #2 (and losing changes #3 and #4) the analysts can undo just change #2 and keep all the other changes. Now our example was for just 4 changes, but try to think about how important that changelog would be if there were hundreds of changes to keep track of.

## What also happens in real life

A junior analyst probably only needs to know the above with one exception. If an analyst is making changes to an existing SQL query that is shared across the company, the company most likely uses what is called a _Version Control System_ (GIT)
An example might be a query that pulls daily revenue to build a dashboard for senior management.

Here is how a version control system affects a change to a query:

1. A company has official versions of important queries in their version control system,
2. An analyst makes sure the most up-to-date version of the query is the one they will change. This is called _Syncing_
3. The analyst makes the change to the query.
4. The analyst might ask someone to review this change. This is called a _Code Review_ and cam be informally or formally done. An informal review could be as simple as asking a senior analyst to take a look at the change.
5. After a review approves the changer, the analyst submits the updated version of the query to the repo in the company's version control system. This is called a _Code Commit_. A best practice is to document exactly what the change was and why it was made in a comments area. Going back to our example of a query that pulls daily revenue, a comment might be: _Updated revenue to include revenue coming from the new product "Calypso"_
6. After the change is submitted, everyone else in the company will be able to access and use this new query when they sync to the most up-to-date queries stored in the version control system.
7. If the query has a problem or business needs change, the analyst can _undo_ the change to the query using the version control system. The analyst can look at a chronological list of all changes made to the query and who made each change. Then after finding their own change, the analyst can revert to the previous version
8. The query is back to what it was before the analyst made the change. And everyone at the company sees this reverted, original query, too.
