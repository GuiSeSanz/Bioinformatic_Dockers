library(reticulate)
reticulate::use_python("/usr/local/bin/python")
jind <- import('jind')


# This is a test of the JIND R package
# Path to source batch
train_path <- "./data/train.pkl"
# Path to target batch
test_path <- "./data/test.pkl"
# Column containing cell-types
lname <- "labels" 

train_batch <- py_load_object(train_path)
test_batch <- py_load_object(test_path)

train_labels <- train_batch[,lname, drop=FALSE]
test_labels  <- test_batch[,lname, drop=FALSE]

common_genes <- intersect(colnames(train_batch[,names(train_batch) != lname]), 
                          colnames(test_batch[,names(train_batch) != lname]))


common_genes <- sort(common_genes)
train_batch <- train_batch[, common_genes]
test_batch  <- test_batch[,common_genes]



path <- "./data/JIND"
dir.create(path)


obj <- jind$JindLib(train_batch, train_labels, path=path)

py_save_object(obj, filename="./data/JIND/1234.pkl", pickle = "pickle")

mat = train_batch
mat_round = round(mat)

obj$preprocess(count_normalize=TRUE, logt=TRUE)
obj$dim_reduction(5000, 'Var')

train_config <- ('val_frac' = 0.2, 'seed' = 0, 'batch_size' = 128, 
                     'cuda' = FALSE, 'epochs' = 15)

obj$train_classifier(config=train_config, cmat=TRUE) # Creates confusion matrix on the validation data

obj$wrapper('self', config=train_config, cmat=TRUE)