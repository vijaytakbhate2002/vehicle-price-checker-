# Vehicle Price Checker

The Vehicle Price Checker is a Machine Learning-powered application designed to predict the prices of both bikes and cars. The user-friendly interface allows users to input various parameters and obtain a predicted price. The application is built using Streamlit for ease of use.

## Usage

### Select Vehicle Type

Choose between bikes and cars to predict the price for the respective category.

### Input Parameters

#### For Bikes:

- Brand
- Name
- City
- Owner Type

#### For Cars:

- Brand
- Name

### Result

View the predicted price based on the provided parameters.

## Folder Structure

- `app.py`: Main Streamlit application file.
- `bike_brands`, `bike_names`, `bike_city`, `bike_owner`: Files containing bike-related data.
- `bike_price_model`: Machine Learning model file for predicting bike prices.
- `car_brands`, `car_names`: Files containing car-related data.
- `car_price_model`: Machine Learning model file for predicting car prices.
- `requirements.txt`: List of project dependencies.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/vijaytakbhate2002/vehicle-price-checker-.git
   cd vehicle-price-checker-
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.
