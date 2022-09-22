# Classificaation Tabular Datasets

This repository contains numerous benchmark tabular datasets for testing various classification algorithms.

All datasets are splitted to train and test parts. If whole unsplitted dataset was accessible it is also splitted into 10-fold cross validation datasets. Each dataset contains target column names **class** for prediction. Files in parquet data format is used which could be easily loaded using pandas Python package.

| Dataset name                                                                                            | Rows    | Columns | Missing values | Classes |
| ------------------------------------------------------------------------------------------------------- | ------- | ------- | -------------- | ------- |
| [adult](https://archive.ics.uci.edu/ml/datasets/adult/)                                                 | 32561   | 15      | yes            | 2       |
| [anneal](https://archive.ics.uci.edu/ml/datasets/Annealing)                                             | 898     | 39      | no             | 5       |
| [audiology](https://archive.ics.uci.edu/ml/datasets/Audiology+%28Standardized%29)                       | 226     | 70      | yes            | 24      |
| [auto-mpg](https://archive.ics.uci.edu/ml/datasets/auto+mpg)                                            | 398     | 8       | yes            | 3       |
| [autos](https://archive.ics.uci.edu/ml/datasets/Automobile)                                             | 205     | 26      | yes            | 6       |
| [balance-scale](https://archive.ics.uci.edu/ml/datasets/balance+scale)                                  | 625     | 5       | no             | 3       |
| [breast-cancer](<https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(diagnostic)>)         | 286     | 10      | yes            | 2       |
| [bupa-liver-disorders](https://archive.ics.uci.edu/ml/datasets/liver+disorders)                         | 345     | 7       | no             | 2       |
| [car](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation)                                           | 1728    | 7       | no             | 4       |
| [churn](https://www.kaggle.com/competitions/customer-churn-prediction-2020/data)                        | 4250    | 20      | no             | 2       |
| [cleveland](https://archive.ics.uci.edu/ml/datasets/heart+disease)                                      | 303     | 14      | yes            | 5       |
| [connect-4](http://archive.ics.uci.edu/ml/datasets/connect-4)                                           | 67557   | 43      | no             | 3       |
| [covertype](https://archive.ics.uci.edu/ml/datasets/Covertype?ref=datanews.io)                          | 581011  | 55      | no             | 7       |
| [credit-a](https://archive.ics.uci.edu/ml/datasets/Credit+Approval)                                     | 690     | 16      | yes            | 2       |
| [credit-g](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29)                    | 1000    | 21      | no             | 2       |
| [cylinder-bands](https://archive.ics.uci.edu/ml/datasets/Cylinder+Bands)                                | 540     | 36      | yes            | 2       |
| [diabetes](https://archive.ics.uci.edu/ml/datasets/Diabetes)                                            | 768     | 8       | no             | 2       |
| [echocardiogram](https://archive.ics.uci.edu/ml/datasets/Echocardiogram)                                | 131     | 12      | yes            | 2       |
| [ecoli](https://archive.ics.uci.edu/ml/datasets/ecoli)                                                  | 336     | 8       | no             | 8       |
| [flag](https://archive.ics.uci.edu/ml/datasets/Flags)                                                   | 194     | 29      | no             | 4       |
| [glass](https://archive.ics.uci.edu/ml/datasets/glass+identification)                                   | 214     | 10      | no             | 6       |
| [haberman](https://archive.ics.uci.edu/ml/datasets/haberman's+survival)                                 | 306     | 4       | no             | 2       |
| [hayes-roth](https://archive.ics.uci.edu/ml/datasets/Hayes-Roth)                                        | 132     | 5       | no             | 3       |
| [heart-c](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)                                        | 303     | 14      | yes            | 5       |
| [heart-statlog](<https://archive.ics.uci.edu/ml/datasets/statlog+(heart)>)                              | 270     | 14      | no             | 2       |
| [hepatitis](https://archive.ics.uci.edu/ml/datasets/hepatitis)                                          | 155     | 20      | yes            | 2       |
| [horse-colic](https://archive.ics.uci.edu/ml/datasets/Horse+Colic)                                      | 368     | 23      | yes            | 2       |
| [hr-evaluation](https://www.kaggle.com/datasets/muhammadimran112233/employees-evaluation-for-promotion) | 54808   | 12      | yes            | 2       |
| [hungarian-heart-disease](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)                        | 294     | 14      | yes            | 2       |
| [iris](https://archive.ics.uci.edu/ml/datasets/iris)                                                    | 150     | 5       | no             | 3       |
| [lymphography](https://archive.ics.uci.edu/ml/datasets/Lymphography)                                    | 148     | 19      | no             | 4       |
| [magic](https://archive.ics.uci.edu/ml/datasets/magic+gamma+telescope)                                  | 19020   | 11      | no             | 2       |
| [monk-1](https://archive.ics.uci.edu/ml/datasets/MONK's+Problems)                                       | 324     | 7       | no             | 2       |
| [monk-2](https://archive.ics.uci.edu/ml/datasets/MONK's+Problems)                                       | 369     | 7       | no             | 2       |
| [monk-3](https://archive.ics.uci.edu/ml/datasets/MONK's+Problems)                                       | 322     | 7       | no             | 2       |
| [mushroom](https://archive.ics.uci.edu/ml/datasets/mushroom)                                            | 8124    | 23      | yes            | 2       |
| [nursery](https://archive.ics.uci.edu/ml/datasets/nursery)                                              | 12960   | 8       | no             | 5       |
| [phoneme](https://www.openml.org/search?type=data&sort=runs&id=1489&status=active)                      | 5404    | 6       | no             | 2       |
| [poker-hand](https://archive.ics.uci.edu/ml/datasets/Poker+Hand)                                        | 1025010 | 11      | no             | 10      |
| [segment](https://archive.ics.uci.edu/ml/datasets/image+segmentation)                                   | 2310    | 20      | no             | 7       |
| [seismic-bumps](https://archive.ics.uci.edu/ml/datasets/seismic-bumps)                                  | 2584    | 19      | no             | 2       |
| [sonar](<http://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks)>)          | 208     | 61      | no             | 2       |
| [soybean](<https://archive.ics.uci.edu/ml/datasets/Soybean+(Large)>)                                    | 683     | 36      | yes            | 19      |
| [tic-tac-toe](https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame)                              | 958     | 10      | no             | 2       |
| [titanic](https://www.kaggle.com/c/titanic)                                                             | 2001    | 4       | no             | 2       |
| [vote](https://archive.ics.uci.edu/ml/datasets/congressional+voting+records)                            | 435     | 17      | yes            | 2       |
| [wilt](https://archive.ics.uci.edu/ml/datasets/wilt)                                                    | 4839    | 6       | no             | 2       |
| [wine](https://archive.ics.uci.edu/ml/datasets/wine)                                                    | 178     | 14      | no             | 3       |
| [zoo](https://archive.ics.uci.edu/ml/datasets/zoo)                                                      | 101     | 17      | no             | 7       |
