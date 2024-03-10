### Pascal Triangle

```markdown

If the input n is less than or equal to 0, it returns an empty list.
Initialize the pascal list with the first row of Pascal's triangle, which is [1].
While the number of rows in pascal is not equal to n, continue the following steps:
Get the last row of pascal and store it in the variable row.
Create a new row new with the first element as 1.
Iterate over the elements in the row list (except the last element) and calculate the sum of each pair of adjacent elements. Append these sums to the new list.
Add 1 to the end of the new list.
Append the newly created row new to the pascal list.
Repeat steps 4-8 until the number of rows in pascal is equal to n.
Finally, return the generated Pascal's triangle as a list of lists.


```