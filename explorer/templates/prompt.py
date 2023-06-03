def prompt_templates():
    return {
        "Simple Forecast Prompt": "Perform a basic analysis of the dataset stored in your memory and provide a forecast for the next 1, 7 15 and 30 days. Present the results in markdown. Use your tools as needed to complete the request. When you need to run a pip install command, use the terminal tool instead",
        "Time Series Prediction Prompt with Prophet Model and Ensemble Smoothing": "Use the information stored in your memory to describe the dynamics of the time series behavior and create the prediction for the next 7 days and return the results in markdown string. The dataframe frame includes the columns: {cols}, where ts_id is an identifier for this series with code: {ts_id}. ds is the date, y is the value of the time series, Prediction values can be included or could be calculated by you such that prediction is the predicted value, lower_bound is the lower bound of the prediction, upper_bound is the upper bound of the prediction, abs_error is the absolute error of the prediction. The prediction values are created by a custom prophet model, use them for feature engineering with an ensemble model with TFT and NHITs in the pytorch forecasting library to further smooth the prediction. In order to run pip install or other shell related calls, use the % prefix to run shell commands. When running the data processing jobs, keep a state of the dataframe so that it can be reused in the next step. Only show the specific code used to generate the prediction at the end of the processes when formating the final answer",
        "Time Series Prediction Simplified Prompt": "Generate a markdown string with predicted values for the next 7 days of a time series identified by {ts_id}. Use a custom Prophet model to generate the predictions and smooth them using an ensemble model with TFT and NHITs in the PyTorch forecasting library. You can run shell commands with the % prefix and reuse the dataframe in subsequent steps. The predicted values should include 'prediction', 'lower_bound', 'upper_bound', and 'abs_error'. Only include the code used to generate the prediction in the final answer.",
    }
