import pickle
import pandas as pd

crops_df = pd.read_csv("./dataset/Crop_recommendation.csv")
crops_df.dropna(subset=['label'], inplace=True)

from sklearn.model_selection import train_test_split

X = crops_df.iloc[:, :-1]
Y = crops_df.iloc[:, -1] 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42, n_jobs=-1).fit(X_train, Y_train)

pickle.dump(model, open("model.pkl", "wb"))