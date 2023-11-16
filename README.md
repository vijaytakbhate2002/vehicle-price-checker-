# Vehicle Price Checking System with ML

## Overview

This project is a Vehicle Price Checking System powered by Machine Learning. It provides a user-friendly interface to predict the price of both bikes and cars based on various input parameters. The application is built using Streamlit.

## Files

- **app.py**: This is the main application file. Run this file to start the Streamlit app.

### Bike Section

- **bike_brands**: File containing the list of bike brands.
- **bike_names**: File containing the list of bike names.
- **bike_city**: File containing the list of cities for bikes.
- **bike_owner**: File containing (first owner, second owner, third owner or fourth or above owner).
- **bike_price_model**: ML model file for predicting bike prices.
- **requirements.txt**: File listing all the dependencies for the project.

### Car Section

- **car_brands**: File containing the list of car brands.
- **car_names**: File containing the list of car names.
- **car_price_model**: ML model file for predicting car prices.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/vehicle-price-checking.git
    cd vehicle-price-checking
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```bash
    python app.py
    ```

4. **Access the Prediction Tool:**
    - Open your web browser and go to [http://localhost:8501](http://localhost:8501)
    - Navigate to the "Bike" or "Car" section and input the required parameters.
    - Receive predictions for bike or car prices.

## Important Notes

- This tool is designed for both technical and non-technical users.
- Predictions are based on machine learning models, and results may vary.

## Contributing

If you would like to contribute or report issues, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to reach out with any questions or feedback!
