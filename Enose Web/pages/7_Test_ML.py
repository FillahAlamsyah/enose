import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
import plotly.express as px
import plotly.figure_factory as ff

# Simulated dataset (replace this with your actual dataset)
# Example: df = pd.read_csv('your_dataset.csv')
df = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'feature2': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'label': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

# Train-test split
X = df.drop('label', axis=1)
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Sidebar for model selection
st.sidebar.title("Machine Learning Analysis")
model_choice = st.sidebar.selectbox("Choose a model", ("SVM", "KNN", "ANN"))

# Model initialization
model = None
if model_choice == "SVM":
    model = SVC()
elif model_choice == "KNN":
    model = KNeighborsClassifier()
elif model_choice == "ANN":
    model = MLPClassifier()

# Parameter tuning using GridSearchCV
st.sidebar.subheader("Parameter Tuning")
params = {}
if model_choice == "SVM":
    params = {
        'C': st.sidebar.slider('C', 0.1, 10.0, 1.0),
        'kernel': st.sidebar.selectbox('Kernel', ['linear', 'rbf'])
    }
    model = SVC(**params)
elif model_choice == "KNN":
    params = {
        'n_neighbors': st.sidebar.slider('n_neighbors', 1, 15, 5),
        'weights': st.sidebar.selectbox('Weights', ['uniform', 'distance'])
    }
    model = KNeighborsClassifier(**params)
elif model_choice == "ANN":
    params = {
        'hidden_layer_sizes': st.sidebar.slider('Hidden Layer Sizes', 50, 200, 100),
        'activation': st.sidebar.selectbox('Activation', ['relu', 'tanh', 'logistic'])
    }
    model = MLPClassifier(**params)

# Fit the model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
fig = ff.create_annotated_heatmap(z=conf_matrix, x=["Predicted 0", "Predicted 1"], y=["Actual 0", "Actual 1"])

# Classification Report
class_report = classification_report(y_test, y_pred, output_dict=True)
class_report_df = pd.DataFrame(class_report).transpose()

# Display results
st.title("Machine Learning Analysis")
st.header("Confusion Matrix")
st.plotly_chart(fig)

st.header("Classification Report")
st.dataframe(class_report_df)

