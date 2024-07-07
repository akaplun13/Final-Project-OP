Programming Concepts Final Project: Description
Deadline: Tuesday, 9th of July
Task:
You need to write a Python application to manage data sources and calculate metrics.
The application should have the following features:
– Main Menu:
○ When the application starts, the user sees a menu with three options:</br>
a. Check existing information;
b. Add a new data source (file);
c. Calculate metric.
– Check Existing Information:
○ The application shows the names of the last three added data sources and
their metrics. Example:
1) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV =
720$
2) Datasource: MicrosoftLTVs2015-2019.csv | Metric: Average LTV =
700$
3) Datasource: MicrosoftLTVs2010-2014.csv | Metric: Average LTV =
550$
– Add New Data Source (File):
○ The application asks for the path to a new data source file.
> Enter data source file path:
< C: /…/datasource.csv
○ The application displays the structure and total records of the file.
> Datasource structure:
col_1 name | col_2 name | … | col_n name
Total records: 10256
– Calculate Metric:
○ The user selects a data source from the added ones using keyboard
navigation.
> Select data source: - > (keyboard displays data source name
from the added ones)
Selected data source: datasource.csv | Total records: 10256
records
○ The application calculates and displays a metric for the selected data
source.
Based on the dataset, {metric name} was calculated. Value is:
{value}
– Return to Main Menu:
○ After each command, the user returns to the main menu.
Functional Requirements:
ID Description
F1 The application starts with a main menu showing three options:
– check existing information;
– add new data source (file);
– calculate the metric.
F2 The application displays the names of the last three added data sources and their
metrics.
F3 The application asks the user to enter the file path for a new data source and shows
the structure and total records.
F4 The application lets the user select a data source using keyboard navigation.
F5 The application calculates and shows the metric for the selected data source.
F6 The application returns to the main menu after each command.
Non-Functional Requirements:
ID Description
NF1 The application should be easy to use and understand.
NF2 The application should handle file paths and data structures efficiently.
NF3 The application should provide clear messages and instructions.
NF4 The application should be designed to allow future upgrades and changes.
NF5 The application should handle errors gracefully and show helpful error messages.
Common Use Cases:
ID Description
UC1 Start the application and view
the main menu
1. The user starts the application.
2. The application shows the main menu with options:
- Check existing information,
- Add new data source (file),
- Calculate metric.
UC2 The application should handle
file paths and data structures
efficiently
1. The user selects "Check existing information" from
the main menu.
2. The application shows the names of the last three
added data sources and their metrics
UC3 The application should
provide clear messages and
instructions
1. The user selects "Add new data source" from the
main menu.
2. The application asks for the file path of the new
data source.
3. The user enters the file path.
4. The application shows the structure and total
records of the data source.
UC4 The application should be
designed to allow future
upgrades and changes
1. The user selects "Calculate metric" from the main
menu.
2. The application lets the user select a data source
using keyboard navigation.
3. The user selects a data source.
4. The application calculates and shows the metric for
the selected data source.
UC5 The application should handle
errors gracefully and show
helpful error messages
1. After executing any command, the application takes
the user back to the main menu.
Grading Policy:
– (2 pts) Main menu:
○ The menu has three options, all selectable and route use to the chosen
command;
– (2 pts) Check existing information:
○ (0.5 pts for each) command implemented correctly and works as expected
for the following scenarios:
a. no datasets (or previous calculations) exist;
b. less than three datasets added;
c. more than three datasets were added;
○ (0.25 pts) the command shows meaningful errors if needed;
○ (0.25 pts) code quality (chosen data structures, variable names, etc.);
– (2 pts) add a new data source (file):
○ (1 pt) command implemented correctly;
○ (0.5 pts) datasets stored correctly;
○ (0.25 pts) the command shows meaningful errors if needed;
○ (0.25 pts) code quality (chosen data structures, variable names, etc.);
– (3 pts) calculate metric.
○ (1.5 pt) command implemented correctly;
○ (1 pt) calculated metric stored correctly;
○ (0.25 pts) the command shows meaningful errors if needed;
○ (0.25 pts) code quality (chosen data structures, variable names, etc.);
– (1 pts) main menu routing:
○ If a user wants to continue working after the command completion, the
main menu should be shown to him
– (2 pts) general code quality and application correctness (code structure, naming,
etc.);
– (2 pts) answers to the questions.
Notes:
– Metric Variants: The metric calculated depends on the variant assigned to each
student. Ask your instructor for details on the specific metric you need to
calculate.
– Data Source Files: The data source files are CSV files with a specific structure.
The application should be able to read and process these files.
– Data Source Structure: The structure of the data source files is predefined for
each variant. The application should display this structure when a new file is
added.
– Data Source Metrics: The metrics are calculated based on the data in the source
files. The application should be able to calculate and display the metrics for each
data source.
