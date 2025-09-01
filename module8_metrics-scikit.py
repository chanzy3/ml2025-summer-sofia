import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Get number of points from user
    while True:
        try:
            n = int(input("Enter the number of points (N): "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    # Initialize numpy arrays for data storage
    x_values = np.zeros(n, dtype=int)  # Ground truth labels
    y_values = np.zeros(n, dtype=int)  # Predicted labels
    
    # Read N points from user
    print(f"\nPlease enter {n} points (x, y) where x is ground truth and y is predicted:")
    print("Both x and y should be either 0 or 1")
    
    for i in range(n):
        while True:
            try:
                print(f"\nPoint {i+1}:")
                x = int(input("  Enter x (ground truth, 0 or 1): "))
                if x not in [0, 1]:
                    print("  x must be either 0 or 1")
                    continue
                
                y = int(input("  Enter y (predicted, 0 or 1): "))
                if y not in [0, 1]:
                    print("  y must be either 0 or 1")
                    continue
                
                # Store values in numpy arrays
                x_values[i] = x
                y_values[i] = y
                break
                
            except ValueError:
                print("  Please enter valid integers (0 or 1)")
    
    # Display the collected data
    print("\nCollected data:")
    print("Point | Ground Truth (x) | Predicted (y)")
    print("------|------------------|-------------")
    for i in range(n):
        print(f"  {i+1:2}  |        {x_values[i]}         |      {y_values[i]}")
    
    # Calculate precision and recall using scikit-learn
    try:
        precision = precision_score(x_values, y_values, zero_division=0)
        recall = recall_score(x_values, y_values, zero_division=0)
        
        print("\n" + "="*40)
        print("RESULTS:")
        print("="*40)
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        
        # Additional information for better understanding
        print("\n" + "-"*40)
        print("INTERPRETATION:")
        print("-"*40)
        
        # Calculate confusion matrix components using numpy
        true_positives = np.sum((x_values == 1) & (y_values == 1))
        false_positives = np.sum((x_values == 0) & (y_values == 1))
        false_negatives = np.sum((x_values == 1) & (y_values == 0))
        true_negatives = np.sum((x_values == 0) & (y_values == 0))
        
        print(f"True Positives (TP):  {true_positives}")
        print(f"False Positives (FP): {false_positives}")
        print(f"False Negatives (FN): {false_negatives}")
        print(f"True Negatives (TN):  {true_negatives}")
        
        print(f"\nPrecision = TP / (TP + FP) = {true_positives} / ({true_positives} + {false_positives}) = {precision:.4f}")
        print(f"Recall = TP / (TP + FN) = {true_positives} / ({true_positives} + {false_negatives}) = {recall:.4f}")
        
    except Exception as e:
        print(f"\nError calculating metrics: {e}")

if __name__ == "__main__":
    main()