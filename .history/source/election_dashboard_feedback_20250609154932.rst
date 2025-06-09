2025 Federal Election Tableau Dashboard
======================================

Below is an example of feedback given to a public dashboard. Use this as a checklist when reviewing your own visualizations or dashboards for clarity and accuracy.

Feedback & Lessons Learned
--------------------------

Pie Chart Misrepresentation:
The bottom-right pie chart offering the gender breakdown of voters is incorrect. All genders are less than 30% rather than 100%, while men and women each make up only around a third of the pie chart. In reality, we should expect 90% or more of votes to come from men or women.

Default Map View:
The map defaults to votes from all genders between 18-24 years old in the 2004 election, even while the dropdown menus to the right are all set to "All". Could this be changed to reflect all genders of all ages across all federal elections from 2004 onwards?

Missing Legend:
Provinces are a different colour than territories, but there is no legend indicating this delineation. Can a legend be added at the bottom or top left corner of the map box?

Gradient Usage:
What is the purpose of the gradient being used across the provinces and territories in the "Provincial Distribution" section? A gradient typically implies something is increasing or decreasing, but province/territory is a nominal rather than an ordinal variable. It does not look bad, but perhaps the gradient could be based upon turnout rather than province/territory name? This would be more informative.

Turnout Calculation:
Votes divided by Eligible Electors do not equal turnout. Why is this? And what year(s) are "Votes", "Eligible Electors", and "Voter Turnout" covering?

Unclear or Inaccurate Text:
The statement "In 2004 to 2021, the average voter turnout for the selected age group was All in All was 20.55% to 98.08%". Some fixes are definitely needed here. These percentages are almost certainly incorrect (I don't think any age group has ever turned out as 20.55% or 98.08% in Canada), and the sentence should ideally read like "In 2004 to 2021, the average voter turnout for people ages [age group] was X%".
