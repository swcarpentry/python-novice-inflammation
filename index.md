---
layout: lesson
root: .
permalink: index.html
---

The best way to learn how to program is to do something useful,
so this introduction to Python is built around a common scientific task:
**data analysis**.

### Scenario: A Miracle Arthritis Inflammation Cure

Our imaginary colleague "Dr. Maverick" has invented a new miracle drug that promises to
cure arthritis inflammation flare-ups after only 3 weeks since initially taking the
medication! Naturally, we wish to see the clinical trial data, and after months of asking
for the data they have finally provided us with a CSV spreadsheet containing the clinical
trial data.

The CSV file contains the number of inflammation flare-ups per day for the 60 patients
in the initial clinical trial, with the trial lasting 40 days. Each row corresponds to a
patient, and each column corresponds to a day in the trial. Once a patient has their first
inflammation flare-up they take the medication and wait a few weeks for it to take effect
and reduce flare-ups.

To see how effective the treatment is we would like to:

1. Calculate the average inflammation per day across all patients.
2. Plot the result to discuss and share with colleagues.

![3-step flowchart shows inflammation data records for patients moving to the Analysis step
where a heat map of provided data is generated moving to the Conclusion step that asks the
question, How does the medication affect patients?](
fig/lesson-overview.svg "Lesson Overview")


### Data Format
The data sets are stored in
[comma-separated values]({{ page.root }}/reference.html#comma-separated-values) (CSV) format:

- each row holds information for a single patient,
- columns represent successive days.

The first three rows of our first file look like this:
~~~
0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1
~~~
{: .source}
Each number represents the number of inflammation bouts that a particular patient experienced on a
given day.

For example, value "6" at row 3 column 7 of the data set above means that the third
patient was experiencing inflammation six times on the seventh day of the clinical study.

In order to analyze this data and report to our colleagues, we'll have to learn a little bit
about programming.

> ## Prerequisites
>
> You need to understand the concepts of **files** and **directories** and how to start a Python
> interpreter before tackling this lesson. This lesson sometimes references Jupyter
> Notebook although you can use any Python interpreter mentioned in the [Setup][lesson-setup].
>
> The commands in this lesson pertain to **Python 3**.
{: .prereq}

### Getting Started
To get started, follow the directions on the "[Setup][lesson-setup]" page to download data
and install a Python interpreter.

{% include links.md %}
