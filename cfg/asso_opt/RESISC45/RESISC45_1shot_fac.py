_base_ = 'RESISC45_base.py'
n_shots = 1
data_root = 'exp/asso_opt/RESISC45/RESISC45_1shot_fac'
lr = 5e-5
bs = 8

concept_type = "all_submodular"
concept_select_fn = "submodular"
submodular_weights = [1e7, 5]