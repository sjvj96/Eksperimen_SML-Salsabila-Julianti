import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_data():
    columns = [
        "age",
        "workclass",
        "fnlwgt",
        "education",
        "education_num",
        "marital_status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital_gain",
        "capital_loss",
        "hours_per_week",
        "native_country",
        "income"
    ]

    df = pd.read_csv(
        "../adult.data",
        header=None,
        names=columns,
        skipinitialspace=True,
        na_values="?"
    )

    return df


def preprocess(df):

    # Missing Value
    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns
    categorical_columns = df.select_dtypes(include=["object"]).columns

    numeric_imputer = SimpleImputer(strategy="median")
    categorical_imputer = SimpleImputer(strategy="most_frequent")

    df[numeric_columns] = numeric_imputer.fit_transform(df[numeric_columns])
    df[categorical_columns] = categorical_imputer.fit_transform(df[categorical_columns])

    # Encoding
    for column in categorical_columns:
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column])

    # Scaling
    X = df.drop("income", axis=1)
    y = df["income"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_scaled = pd.DataFrame(
        X_scaled,
        columns=X.columns
    )

    df_preprocessed = X_scaled.copy()
    df_preprocessed["income"] = y.values

    return df_preprocessed


def save_data(df):
    df.to_csv("adult_preprocessed.csv", index=False)


def main():

    print("Loading dataset...")
    df = load_data()

    print("Preprocessing...")
    df = preprocess(df)

    print("Saving dataset...")
    save_data(df)

    print("Selesai!")
    print(df.head())
    print(df.shape)


if __name__ == "__main__":
    main()