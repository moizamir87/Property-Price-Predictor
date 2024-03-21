import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    """
    Function to predict the estimated price of a home based on its location, square feet area, number of bedrooms, and bathrooms.

    Parameters:
    - location (str): The location of the home.
    - sqft (float): The square feet area of the home.
    - bhk (int): The number of bedrooms.
    - bath (int): The number of bathrooms.

    Returns:
    - float: The estimated price of the home.
    """
    try:
        # Get the index of the location in the data columns
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        # If the location is not found, set index to -1
        loc_index = -1

    # Create an array with zeros initialized
    x = np.zeros(len(__data_columns))
    # Set the values for square feet, bedrooms, and bathrooms
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    # If location is found, set its index to 1
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict the price using the model and return the rounded value
    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    """
    Function to load the saved artifacts such as data columns, locations, and the trained model.
    """
    print("Loading saved artifacts...start")
    global __data_columns, __locations, __model

    # Load data columns from JSON file
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        # Extract location names from data columns (first 3 columns are sqft, bath, bhk)
        __locations = __data_columns[3:]

    # Load the trained model from the pickle file
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts...done")


def get_location_names():
    """
    Function to get the list of location names.
    """
    return __locations


def get_data_columns():
    """
    Function to get the list of data columns.
    """
    return __data_columns


if __name__ == '__main__':
    # Load saved artifacts and perform some test predictions
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
