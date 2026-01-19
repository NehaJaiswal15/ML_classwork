# CART Decision Tree – Lawn Tractor Ownership

This project demonstrates a **CART (Classification and Regression Tree)** model built using a small dataset to predict **lawn tractor ownership** based on **Income** and **Lot Size**.

## Description
- A Decision Tree classifier is trained using the **Gini index**
- The model predicts whether a household is an **Owner** or **Nonowner**
- The trained decision tree is visualized for interpretability

## Dataset
- Features:
  - `Income`
  - `Lot_Size`
- Target:
  - `Ownership` (Owner / Nonowner)

## Steps Performed
1. Create dataset using pandas
2. Train a CART decision tree (`criterion='gini'`)
3. Predict ownership for a new household
4. Visualize the decision tree structure