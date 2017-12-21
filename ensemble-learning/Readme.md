Test CatBoost

Use the following example to test CatBoost:

```

import numpy 
from catboost import CatBoostRegressor

dataset = numpy.array([[1,4,5,6],[4,5,6,7],[30,40,50,60],[20,15,85,60]])
train_labels = [1.2,3.4,9.5,24.5]
model = CatBoostRegressor(learning_rate=1, depth=6, loss_function='RMSE')
fit_model = model.fit(dataset, train_labels)

print fit_model.get_params()

```


https://tech.yandex.com/catboost/doc/dg/concepts/python-quickstart-docpage/
