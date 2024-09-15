Crontab Translator

Overview

The Crontab Translator is a tool that takes crontab expressions and translates them into natural language. This tool ensures that crontab expressions follow specific input rules and provides a readable interpretation of the schedule.

Allowed User Inputs

The following inputs are allowed in crontab expressions:

Single Digit: Represents a specific value (e.g., 5 for the 5th minute or hour).
* (Asterisk): Represents "any" value (e.g., * in the minute field means every minute).
/ (Step): Specifies intervals (e.g., */5 means every 5 units).
- (Range): Defines a range of values (e.g., 1-5 means from the 1st to the 5th unit).
, (Comma): Lists multiple values (e.g., 1,3,5 means the 1st, 3rd, and 5th units).
Note: Combinations of these inputs are not allowed. For example, 5-10,15 is invalid. Use only one type of input in each field.

Functionality

Expression Validation: The program checks if the crontab expression is valid based on the allowed inputs.
Natural Language Translation: Converts valid crontab expressions into a readable, natural language description.
Examples

Valid Expressions
0 12 * * *
Translation: "Every day at noon."
*/15 9-17 * * *
Translation: "Every 15 minutes between 9:00 AM and 5:00 PM."
0 0 1 * *
Translation: "At midnight on the 1st of every month."
Invalid Expressions
5-10,15
Explanation: This is invalid because it combines ranges and lists.
*/5-10
Explanation: This is invalid because it combines step and range.
How to Use

Input a Crontab Expression: Enter a crontab expression following the allowed input rules.
Receive Translation: The program will validate the expression and provide a natural language translation if it is valid.
