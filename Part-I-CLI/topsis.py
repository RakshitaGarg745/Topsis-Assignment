import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    # Read input CSV
    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        raise Exception("Input file must contain at least 3 columns")

    # Separate fund names and criteria
    fund_names = data.iloc[:, 0]
    matrix = data.iloc[:, 1:].values.astype(float)

    # Parse weights and impacts
    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != matrix.shape[1]:
        raise Exception("Number of weights must match number of criteria")

    if len(impacts) != matrix.shape[1]:
        raise Exception("Number of impacts must match number of criteria")

    for imp in impacts:
        if imp not in ['+', '-']:
            raise Exception("Impacts must be + or -")

    # Step 1: Normalize the decision matrix
    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # Step 2: Apply weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Determine ideal best and worst
    ideal_best = []
    ideal_worst = []

    for j in range(len(impacts)):
        if impacts[j] == '+':
            ideal_best.append(weighted_matrix[:, j].max())
            ideal_worst.append(weighted_matrix[:, j].min())
        else:
            ideal_best.append(weighted_matrix[:, j].min())
            ideal_worst.append(weighted_matrix[:, j].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Calculate distances
    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate TOPSIS score
    score = dist_worst / (dist_best + dist_worst)

    # Step 6: Rank the alternatives
    rank = score.argsort()[::-1].argsort() + 1

    # Create output dataframe
    output = data.copy()
    output["Topsis Score"] = np.round(score, 2)
    output["Rank"] = rank

    # Save output file
    output.to_csv(output_file, index=False)
    print("TOPSIS result saved to:", output_file)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFile>")
        sys.exit(1)

    topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])



