import pandas as pd
from sklearn.datasets import load_wine

from feature_gen.feature_gen_master import FeatureGenMaster
from feature_gen.implementation.constants import EnsembleMethod

all_ensemble_methods = [
    EnsembleMethod.GREEDY,
    EnsembleMethod.WEIGHTED_MAJORITY_VOTING
]

# Load the Iris dataset
data = load_wine()

# Create a DataFrame with the features and target
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Show the current features
print(df.columns)

f_g = FeatureGenMaster(df, 'target', min_number_of_target_unique_values=20)

f_g.start(
    ensemble_methods=all_ensemble_methods,
    random_state=42,
    max_iter=50,
    C=1e5,
    solver='liblinear',
    gamma=1,
    n_components=100,
    sgd_loss='hinge',
    sgd_max_iter=1000,
    sgd_tol=1e-2,
    xgb_n_estimators=100,
    generations_num=2,
    bootstrap_samples_count=1,
    first_population_size=4
)

print('Best new features', f_g.get_best_new_features())
print('Best original features', f_g.get_best_original_features())
print('Best all features', f_g.get_all_best_features())
print("All ensemble methods scores", f_g.get_all_ensemble_methods_scores())