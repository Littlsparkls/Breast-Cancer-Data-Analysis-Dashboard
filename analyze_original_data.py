{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "\n",
    "# 1. Load Data\n",
    "# Column names for the Original Wisconsin Breast Cancer Database\n",
    "columns = ['Sample_code_number', 'Clump_Thickness', 'Uniformity_of_Cell_Size', \n",
    "           'Uniformity_of_Cell_Shape', 'Marginal_Adhesion', 'Single_Epithelial_Cell_Size', \n",
    "           'Bare_Nuclei', 'Bland_Chromatin', 'Normal_Nucleoli', 'Mitoses', 'Class']\n",
    "\n",
    "df = pd.read_csv('breast-cancer-wisconsin.data.csv', header=None)\n",
    "\n",
    "# 2. Data Cleaning\n",
    "# Drop the artifact 'index' column (col 0)\n",
    "df = df.drop(columns=[0])\n",
    "# Drop the first row (index 0) which contains corrupted/header-like data\n",
    "df = df.iloc[1:]\n",
    "\n",
    "df.columns = columns\n",
    "\n",
    "# 'Bare_Nuclei' contains '?' for missing values. Replace with NaN and drop or impute.\n",
    "df['Bare_Nuclei'] = df['Bare_Nuclei'].replace('?', np.nan)\n",
    "df.dropna(inplace=True)\n",
    "\n",
    "# Convert all columns to numeric\n",
    "df = df.apply(pd.to_numeric)\n",
    "\n",
    "# Map Class: 2 -> Benign, 4 -> Malignant (for clarity in plots)\n",
    "df['Class_Label'] = df['Class'].map({2: 'Benign', 4: 'Malignant'})\n",
    "\n",
    "# 3. Analysis: Correlation Heatmap\n",
    "plt.figure(figsize=(12, 10))\n",
    "# Calculate correlation only on numeric columns (excluding ID and Class_Label)\n",
    "corr_matrix = df.drop(columns=['Sample_code_number', 'Class_Label']).corr()\n",
    "\n",
    "sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)\n",
    "plt.title('Correlation Matrix of Cytological Features (Original Dataset)')\n",
    "plt.tight_layout()\n",
    "plt.savefig('original_data_correlation.png')\n",
    "\n",
    "print(\"Original dataset analysis complete. Correlation map saved.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1+"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
