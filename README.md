
 Email Spam Detection System

A machine learning-based web application that classifies emails as **Spam or Ham (Not Spam)** using NLP, TF-IDF, and rule-based feature engineering.

---

 Project Overview

This project detects spam emails using a hybrid approach:

* TF-IDF (word + bigrams)
* Engineered spam-indicator features
* Logistic Regression classifier
* Streamlit web interface for real-time predictions

---

 Dataset

This project uses the **SMS Spam Collection Dataset**, a widely used dataset for spam detection tasks.

 Dataset Details

* Contains ~5,500 SMS/email messages
* Labels:

  * `ham` → Legitimate messages
  * `spam` → Unwanted / promotional messages

---

 How to Download Dataset

 Method 1 (Direct Download)

Download from Kaggle:

 [https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

---

 Steps:

1. Go to the link above

2. Click **Download**

3. Extract the ZIP file

4. You will get:

   ```
   spam.csv
   ```

5. Place `spam.csv` in your project folder:

   ```
   EmailClassificationProject/
   ├── spam.csv
   ├── train.py
   ├── app.py
   ```

---

 Method 2 (Manual Copy)

You can also directly use this file name in your code:

```
spam.csv
```

Make sure it has columns like:

* `v1` → label (ham/spam)
* `v2` → message text

---

 Tech Stack

* Python 🐍
* Pandas & NumPy
* NLTK (NLP preprocessing)
* Scikit-learn (ML models)
* Streamlit (UI)
* Joblib (model saving)

---

 Project Structure

```
EmailClassificationProject/
│
├── spam.csv                 # Dataset
├── train.py                 # Model training script
├── app.py                   # Streamlit UI
├── model.pkl               # Trained model
├── vectorizer.pkl          # TF-IDF vectorizer
└── README.md
```

---

 How It Works

 1. Text Preprocessing

* Lowercasing
* Removing special characters
* Stopword removal
* Stemming

 2. Feature Engineering

* TF-IDF (unigrams + bigrams)
* Spam indicators:

  * numbers in text
  * discount words (% / “off”)
  * urgency words (free, win, urgent)
  * message length

 3. Model Training

* Logistic Regression (balanced weights)
* Trained on combined feature space

---

 ▶️ How to Run

 1. Install dependencies

```bash id="dep1"
pip install pandas numpy nltk scikit-learn streamlit joblib scipy
```

---

 2. Download dataset

* Download `spam.csv` from Kaggle link above
* Place it in project folder

---

3. Train model

```bash id="train1"
python train.py
```

This generates:

* `model.pkl`
* `vectorizer.pkl`

---

### 4. Run Streamlit app

```bash id="run1"
python -m streamlit run app.py
```

---

 Example Predictions

| Email Text                           | Result  |
| ------------------------------------ | ------- |
| "Get 50% off on your first order!"   | 🚫 Spam |
| "Meeting at 10 AM tomorrow"          | ✅ Ham   |
| "Urgent! Claim your free reward now" | 🚫 Spam |

---

  Key Features

✔ Hybrid ML + rule-based system
✔ Handles promotional spam patterns
✔ Fast and lightweight model
✔ Real-time web interface

---

 Future Improvements

* BERT-based deep learning model
* REST API using FastAPI
* Cloud deployment (Render / AWS)
* Advanced spam probability dashboard

---

 Author

Shahzeb Khan
Machine Learning Developer


