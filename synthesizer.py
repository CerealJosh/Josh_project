import numpy as np
import pandas as pd

# Define the original scenarios with their base values
base_scenarios = {
    'Wood': [2.5, 2.0, 1.5, 1.0, 0.7, 2.5, 40, 30],
    'Paper': [2.8, 2.3, 1.7, 1.2, 0.9, 2.8, 42, 28],
    'Cloth': [2.3, 1.9, 1.3, 1.0, 0.6, 2.2, 38, 32],
    'LPG': [4.5, 1.8, 4.5, 1.0, 1.5, 2.5, 30, 45],
    'Magnesium': [1.0, 0.8, 0.7, 1.0, 0.7, 1.0, 60, 20],
    'Sodium': [1.5, 1.0, 1.0, 1.2, 0.8, 1.5, 55, 25],
    'No Fire': [0.5, 0.4, 0.3, 0.2, 0.2, 0.5, 25, 50],
}

# Function to generate synthetic data with slight variations
def generate_synthetic_data(base_values, n_samples=1000):
    synthetic_data = []
    for _ in range(n_samples):
        # Apply a small random variation to each sensor value
        variation = np.random.uniform(-0.2, 0.2, len(base_values) - 2)  # no variation for temperature and humidity
        new_values = np.array(base_values[:6]) + variation
        # Include temperature and humidity without variation
        new_values = np.append(new_values, base_values[6:])
        synthetic_data.append(new_values.round(1).tolist())
    return synthetic_data

# Generate synthetic data for each scenario
synthetic_dataset = []
for scenario, base_values in base_scenarios.items():
    data = generate_synthetic_data(base_values, n_samples=50000)
    for entry in data:
        synthetic_dataset.append(entry + [scenario])

# Convert to DataFrame for easy viewing
columns = ['MQ-2', 'MQ-3', 'MQ-5', 'MQ-7', 'MQ-8', 'MQ-135', 'DHT_11 Temperature', 'DHT_11 Humidity', 'Scenario_label']
synthetic_df = pd.DataFrame(synthetic_dataset, columns=columns)

synthetic_df.head(20)
print(synthetic_df)

output_file_path = 'synthetic_fire_dataset.csv'
synthetic_df.to_csv(output_file_path, index=False)
