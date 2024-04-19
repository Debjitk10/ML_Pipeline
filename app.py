from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            housing_median_age=float(request.form.get('housing_median_age')),
            total_rooms=float(request.form.get('total_rooms')),
            total_bedrooms=float(request.form.get('total_bedrooms')),
            population=float(request.form.get('population')),
            households=float(request.form.get('households')),
            median_income=float(request.form.get('median_income')),
            ocean_proximity=request.form.get('ocean_proximity')
        )
        new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(new_data)

        result = round(pred[0], 2)

        return render_template('result.html', final_result=result)

if __name__ == '__main__':
    app.run(debug=True)
