from simiclasso.clus_regression import simicLASSO_op
from simiclasso.weighted_AUC_mat import main_fn

p2df = '/root/SimiC/Tutorial/Data/ClonalKinetics_filtered.DF.pickle' #Path to the gene expression matrix
p2assignment = '/root/SimiC/Tutorial/Data/ClonalKinetics_filtered.clustAssign.txt' #Path to the assignment file
p2tf = '/root/SimiC/Tutorial/Data/ClonalKinetics_filtered.TFs.pickle' #Path to the list of TFs
p2saved_file = '/root/SimiC/Tutorial/Test_Results/ClonalKinetics_filtered_CrosVal_Ws.pickle' #Path to the results file

# similarity = True 
# max_rcd_iter = 100000
# percent_of_target = 1 # 1 means 100% of the target genes
# num_TFs = -1 # -1 means all TFs
# num_target_genes = -1 # -1 means all target genes
# df_with_label = False #If the assignment of the cells are provided on a separate file, like in our case, set to FALSE.
# k_cluster = None

similarity = True
k_cluster = None
num_TFs = -1
num_target_genes = -1
max_rcd_iter = 100000
df_with_label = False

percent_of_target = 1
cross_val = True

## Perform the cross-validation to asses the paramenter lambda1 and lambda2
cross_val = True 
simicLASSO_op(p2df, p2assignment, similarity, p2tf, p2saved_file,  k_cluster, num_TFs, num_target_genes, 
                max_rcd_iter = max_rcd_iter, df_with_label = df_with_label,
                cross_val=cross_val)

# # We decide to set the Lambda1 to 0.01 and the Lambda2 to 0.01. Now we can run 
# # SimiC setting these parameters and perform the weighted AUC calculations.
# lambda1 = 0.01
# lambda2 = 0.01
# p2saved_file = '/root/SimiC/Tutorial/Test_Results/ClonalKinetics_filtered_L1{0}_L2{1}_test_Ws.pickle'.format(lambda1, lambda2) #Path to the results file
# cross_val = False
# simicLASSO_op(p2df, p2assignment, similarity, p2tf, p2saved_file,  k_cluster, num_TFs, num_target_genes, 
#                 max_rcd_iter = max_rcd_iter, df_with_label = df_with_label,
#                 lambda1=lambda1, lambda2 = lambda2, cross_val=cross_val)

# p2AUC = '/root/SimiC/Tutorial/Test_Results/ClonalKinetics_filtered_L1{0}_L2{1}_test_AUCs.pickle'.format(lambda1, lambda2)
# main_fn(p2df, p2saved_file, p2AUC, percent_of_target = percent_of_target)


