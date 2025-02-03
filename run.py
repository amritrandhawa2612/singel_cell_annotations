config = {
    'model_name': ['scgpt'],
    'task':'cell_type_annotation', #['cell_type_annotation', 'perturbation', 'clustering', 'gene_and_cell_embeddings']
    #'task': 'all',  # Options: 'pre-training', 'fine-tuning', 'evaluation', 'all'
    'ref_dataset_path': 'C:/Users/gaiacronus/Downloads/work/combine/modelresults/truncated_train.h5ad', #train
    'query_dataset_path': 'C:/Users/gaiacronus/Downloads/work/combine/modelresults/truncated_test.h5ad',  #test
    'epochs': 1,  # Optional
    'project':'modelresults',
    'scgpt_params': {
        'seed': 0,
        'epochs': 1,
        'batch_size': 32,
        'lr': 1e-4,
        'mask_ratio': 0.0,
        'n_bins': 51,
        'pretrained_path': 'C:/Users/gaiacronus/Downloads/work/combine/scgptmodel/best_model.pt',
        'freeze': False,
        'n_layers_cls': 3
    }
}