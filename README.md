# Data
* run `python data/cifar10/get_data.py` to download the `data_complete.npz` file into the folder `data/cifar10/`.
* other two important data files are `data/cifar10/shuffle_index.npz` and `result/cifar10/code_publish/attack/noise_data_evaluation.npz`.

# Usage

## Load data
```
import numpy as np
data = np.load([.npz file path])
```

## Data format

* `data_complete.npz`: `data['x']` contains a list of all input images, saved as tensors. For example, `data['x'][3]` is the input image with id 3. `data['y']` contains a list of corresponding labels, ranging from 0 to 9.

* `shuffle_index`: `data['x']` contains a list of id's. Please note that ***we only use the first 10000 id's as the training set***. Therefore, you should get the true training set like this:
```
data_train_x = data_complete['x'][shuffle_index['x'][0:10000]]
```

* `noise_data_evaluation.npz`: `data['defense_output']` contains a list of MemGuarded confidence vectors. You do ***not*** need `shuffle_index` to interpret the data, however. `data['defense_output'][0:10000]` is all you want. Note that due to the strange behavior of `keras` package MemGuard is using, `data['defense_output'][i][j]` is the guarded predicted probability of category **(j + 1) mod 10** rather than **j**. If you are unsure, check `data['tc_output']`, which is of the same format and including the unguarded confidence vectors.

