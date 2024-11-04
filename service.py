import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

# Step 1: Get the latest model with respect to the iris_clf dataset
iris_clf_runner = bentoml.sklearn.get("iris_clf:latest").to_runner()

# Step 2: Create a service
# In runners, you can use various options such as transformation and others. It works similarly to a pipeline.
svc = bentoml.Service("iris_classifier", runners=[iris_clf_runner])

# Step 3: Create an API
@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result = iris_clf_runner.predict.run(input_series)
    return result