import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import sys

def main():
    try:
        # Read N (number of training points)
        N = int(input("Enter N (positive integer): "))
        if N <= 0:
            print("Error: N must be a positive integer")
            return
        
        # Read k (number of neighbors)
        k = int(input("Enter k (positive integer): "))
        if k <= 0:
            print("Error: k must be a positive integer")
            return
        
        # Check if k <= N
        if k > N:
            print("Error: k must be less than or equal to N")
            return
        
        # Initialize arrays using NumPy
        X_train = np.zeros((N, 1))  # Feature array (x values)
        y_train = np.zeros(N)       # Target array (y values)
        
        # Read N training points
        print(f"Please provide {N} (x, y) points:")
        for i in range(N):
            x = float(input(f"Enter x value for point {i+1}: "))
            y = float(input(f"Enter y value for point {i+1}: "))
            
            # Store in NumPy arrays
            X_train[i, 0] = x
            y_train[i] = y
        
        # Calculate variance of labels in training dataset
        variance = np.var(y_train, ddof=0)  # Population variance
        print(f"Variance of labels in training dataset: {variance}")
        
        # Create and train k-NN Regressor using Scikit-learn
        knn_regressor = KNeighborsRegressor(n_neighbors=k)
        knn_regressor.fit(X_train, y_train)
        
        # Read test point X
        X_test = float(input("Enter X value for prediction: "))
        
        # Make prediction
        X_test_array = np.array([[X_test]])  # Reshape for sklearn
        y_pred = knn_regressor.predict(X_test_array)
        
        # Output result
        print(f"k-NN Regression result (Y): {y_pred[0]}")
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()