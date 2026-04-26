import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.

    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)

    Returns: float
    """

    n_samples = X.shape[0]
    unique_labels = np.unique(labels)

    # Step 1: compute distance matrix
    dist_matrix = np.linalg.norm(
        X[:, np.newaxis] - X[np.newaxis, :],
        axis=2
    )

    silhouettes = []

    for i in range(n_samples):

        current_label = labels[i]

        # Points in same cluster
        same_cluster = labels == current_label

        # Exclude itself
        same_cluster[i] = False

        # Compute a(i)
        if np.sum(same_cluster) > 0:
            a = np.mean(dist_matrix[i][same_cluster])
        else:
            a = 0

        # Compute b(i)
        b = np.inf

        for label in unique_labels:

            if label == current_label:
                continue

            other_cluster = labels == label

            if np.sum(other_cluster) > 0:
                dist = np.mean(dist_matrix[i][other_cluster])
                b = min(b, dist)

        # Compute silhouette
        if max(a, b) > 0:
            s = (b - a) / max(a, b)
        else:
            s = 0

        silhouettes.append(s)

    return np.mean(silhouettes)