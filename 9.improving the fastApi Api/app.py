from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from schema.user_input_pydantic_model import UserInput
from models.predict import model,predict_output
from schema.predicted_response import PredictionResponse


app = FastAPI()

@app.get('/')
def home():
  return {"message":"Insurance Premium Prediction Api"}

@app.get('/health')
def health_checkup():
  return {
     "status":"ok",
     "model_version":"v1"
  }


@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    input_df = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(input_df)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))



# Prevent subprocess import errors
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)


