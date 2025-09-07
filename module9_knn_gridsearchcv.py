import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def get_dataset(size, name=""):
    """Function to get user input for dataset pairs"""
    x_data = []
    y_data = []
    
    print(f"\nEnter {size} pairs for {name} dataset:")
    for i in range(size):
        print(f"\nPair {i+1}:")
        x = float(input("Enter x value (real number): "))
        y = int(input("Enter y value (non-negative integer): "))
        while y < 0:
            print("Error: y must be non-negative!")
            y = int(input("Enter y value (non-negative integer): "))
        
        x_data.append(x)
        y_data.append(y)
    
    return np.array(x_data).reshape(-1, 1), np.array(y_data)

def find_best_k(X_train, y_train, X_test, y_test, k_range):
    """Function to find the best k value and its corresponding accuracy"""
    best_k = 1
    best_accuracy = 0.0
    
    for k in k_range:
        # Create and train kNN classifier
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        
        # Make predictions and calculate accuracy
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Update best k if current accuracy is higher
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
            
    return best_k, best_accuracy

def main():
    # Get training set size
    N = int(input("Enter the size of training set (N): "))
    while N <= 0:
        print("Error: N must be positive!")
        N = int(input("Enter the size of training set (N): "))
    
    # Get training data
    X_train, y_train = get_dataset(N, "training")
    
    # Get test set size
    M = int(input("\nEnter the size of test set (M): "))
    while M <= 0:
        print("Error: M must be positive!")
        M = int(input("Enter the size of test set (M): "))
    
    # Get test data
    X_test, y_test = get_dataset(M, "test")
    
    # Find best k and its accuracy
    k_range = range(1, 11)  # 1 to 10
    best_k, best_accuracy = find_best_k(X_train, y_train, X_test, y_test, k_range)
    
    # Output results
    print(f"\nBest k: {best_k}")
    print(f"Test accuracy: {best_accuracy:.4f}")

if __name__ == "__main__":
    main()
