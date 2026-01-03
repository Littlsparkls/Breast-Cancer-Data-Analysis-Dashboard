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
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "\n",
    "# 1. Load Data\n",
    "cols = ['ID', 'Diagnosis'] + [f'feature_{i}' for i in range(1, 31)]\n",
    "# Note: Adjusting for the 'index' column found in your specific files\n",
    "df = pd.read_csv('wdbc.data.csv', header=None)\n",
    "if str(df.iloc[0, 0]) == 'index': \n",
    "    df = df.drop(columns=[0]) # Drop artifact index column\n",
    "df.columns = cols\n",
    "\n",
    "# 2. Preprocessing\n",
    "# Convert Diagnosis to binary (M=1, B=0)\n",
    "df['Target'] = df['Diagnosis'].apply(lambda x: 1 if x == 'M' else 0)\n",
    "X = df.drop(columns=['ID', 'Diagnosis', 'Target'])\n",
    "y = df['Target']\n",
    "\n",
    "# Split data\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
    "\n",
    "# 3. Model Training\n",
    "model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# 4. Evaluation\n",
    "predictions = model.predict(X_test)\n",
    "print(\"Classification Report:\")\n",
    "print(classification_report(y_test, predictions, target_names=['Benign', 'Malignant']))\n",
    "\n",
    "# 5. Visualizing Results\n",
    "plt.figure(figsize=(8, 6))\n",
    "cm = confusion_matrix(y_test, predictions)\n",
    "sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', \n",
    "            xticklabels=['Predicted Benign', 'Predicted Malignant'],\n",
    "            yticklabels=['Actual Benign', 'Actual Malignant'])\n",
    "plt.title('Confusion Matrix: Diagnostic Prediction')\n",
    "plt.tight_layout()\n",
    "plt.savefig('confusion_matrix.png')\n",
    "print(\"Model trained and confusion matrix saved to 'confusion_matrix.png'\")\n"
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
