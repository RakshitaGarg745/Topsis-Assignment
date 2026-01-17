## Part I – Command Line TOPSIS

### Description
A Python command-line program developed from scratch to compute TOPSIS scores and ranks for multiple alternatives based on user-defined weights and impacts.


### Usage
```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```
### Example
``` bash
python topsis.py data.csv "1,1,1,2" "+,+,-,+" output-result.csv
```
### Input File Format

1.CSV file with minimum 3 columns

2.First column contains alternative names

3.Remaining columns contain numeric criteria values

### Output File
The output CSV file contains:

1.Original data

2.Topsis Score

3.Rank

### Validations Implemented

1.Correct number of command-line arguments.

2.File not found handling.

3.Numeric validation for criteria columns.

4.Equal number of weights, impacts, and criteria.

5.Impacts must be either + or -

6.Weights and impacts must be comma-separated.
