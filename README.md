# Customer Churn Prediction

## Project Description
A complete end-to-end machine learning project that predicts whether a telecom customer will churn using SQL, Python, and Flask. Built on the Telco Customer Churn dataset, this project demonstrates a full data science pipeline from data storage to model deployment.

## Tech Stack
- Python, Flask, SQLite, SQLAlchemy
- scikit-learn, XGBoost, pandas, seaborn

## Key Features
- SQL pipeline for data storage and EDA queries
- Visual EDA with business insights
- Multiple models compared (Logistic Regression, Random Forest, XGBoost+SMOTE)
- Flask web app with HTML frontend
- Prediction logging to database with timestamp

## Model Results
| Model | Churn Recall | Accuracy |
|-------|-------------|----------|
| Logistic Regression | 0.53 | 79% |
| Random Forest | 0.46 | 79% |
| Random Forest (tuned) | 0.69 | 76% |
| XGBoost + SMOTE | 0.61 | 75% |

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run: `python app.py`
3. Open browser at `http://127.0.0.1:5000`

## Key Insights
1. **Contract Type**: Month-to-month customers churn at 43% vs 3% for two-year contracts
2. **Tenure**: Churned customers average 18 months tenure vs 37.6 months for retained customers
3. **Monthly Charges**: Churned customers pay ~$80/month vs ~$65 for retained customers
4. **Internet Service**: Fiber optic customers have significantly higher churn than DSL or no internet
