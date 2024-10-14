#https://xgboost.readthedocs.io/en/stable/get_started.html
from xgboost import XGBClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def run():
    # Read data
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data['data'], data['target'], test_size=.2)

    # Create model instance
    model = XGBClassifier(n_estimators=2, max_depth=2, learning_rate=1, objective='binary:logistic')

    # Fit model
    model.fit(X_train, y_train)

    # Make predictions on test data
    preds = model.predict(X_test)

    # Calculate accuracy score on test data predictions
    accuracy = accuracy_score(y_test, preds)
    print("Accuracy: {}%".format(round(accuracy * 100.0)))

    # ## Store model

    # In[ ]:


    import pickle
    import tarfile

    pickle_name = 'model.pkl'
    tar_name = 'model.tar.gz'

    try:
        # Save the model as a pickled file
        with open(pickle_name, 'wb') as pickle_file:
            pickle.dump(model, pickle_file)
        
        # Create a tar.gz file
        with tarfile.open(tar_name, 'w:gz') as tar:
            # Add the model file to the tar.gz file
            tar.add(pickle_name)
        
        print(f"Model saved successfully as '{pickle_name}' and archived as '{tar_name}'.")
    except Exception as e:
        print(f"Error occurred: {e}")

# ## Upload model to s3

# In[ ]:

if __name__ == "__main__":
    run()

# import boto3

# # Set up Boto3 client for S3
# s3 = boto3.client('s3')

# # Define the file path of the file to upload
# file_path = tar_name

# # Define the name of the bucket where you want to upload the file
# bucket_name = 'mlbucket13'

# # Define the key (i.e., object name) under which you want to store the file in the bucket
# key = f'mastersagemaker/part2/{tar_name}'

# # Upload the file to S3
# try:
#     s3.upload_file(file_path, bucket_name, key)
#     print("File uploaded successfully.")
# except Exception as e:
#     print(f"Error uploading file: {e}")
