# module6_knn-regr.py

import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        """Store training data"""
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """Predict using k-NN regression"""
        # Calculate distances between X and all training points
        distances = np.abs(self.X_train - X)  # Manhattan distance for 1D
        
        # Get indices of k nearest neighbors
        nearest_neighbors_idx = np.argsort(distances)[:self.k]
        
        # Get the y values of k nearest neighbors
        nearest_neighbors_y = self.y_train[nearest_neighbors_idx]
        
        # Return mean of k nearest neighbors
        return np.mean(nearest_neighbors_y)

def main():
    try:
        # Get N (number of points)
        N = int(input("Enter the number of points (N): "))
        if N <= 0:
            raise ValueError("N must be positive")

        # Get k (number of neighbors)
        k = int(input("Enter the number of neighbors (k): "))
        if k <= 0:
            raise ValueError("k must be positive")
        if k > N:
            raise ValueError("k cannot be greater than N")

        # Initialize arrays for storing points
        X = np.zeros(N)
        y = np.zeros(N)

        # Get N points from user
        print("\nEnter the points (x,y) one by one:")
        for i in range(N):
            X[i] = float(input(f"Enter x value for point {i+1}: "))
            y[i] = float(input(f"Enter y value for point {i+1}: "))

        # Create and fit the model
        model = KNNRegressor(k)
        model.fit(X, y)

        # Get prediction point
        X_pred = float(input("\nEnter X value for prediction: "))

        # Make prediction
        y_pred = model.predict(X_pred)
        print(f"\nPredicted Y value: {y_pred}")

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()