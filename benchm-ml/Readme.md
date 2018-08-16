A minimal benchmark for scalability, speed and accuracy of commonly used open source implementations (R packages, Python scikit-learn, H2O, xgboost, Spark MLlib etc.) of the top machine learning algorithms for binary classification (random forests, gradient boosted trees, deep neural networks etc.).

# setup

```Shell

apt-get install r-base-dev libcurl4-openssl-dev libssl-dev

```

```Shell  Python

R --vanilla << EOF
install.packages(c("data.table","readr","randomForest","gbm","glmnet","ROCR","devtools"), repos="http://cran.rstudio.com")
devtools::install_github("dmlc/xgboost", subdir = "R-package")
EOF

```

https://datawookie.netlify.com/blog/2015/12/installing-xgboost-on-ubuntu/

https://github.com/szilard/benchm-ml

https://datawookie.netlify.com/blog/



