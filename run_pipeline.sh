time python train_user_classification_model.py -dataset location
time python train_defense_model_defensemodel.py  -dataset location
time python defense_framework.py -dataset location -qt evaluation
time python train_attack_shadow_model.py  -dataset location -adv adv1
time python evaluate_nn_attack.py -dataset location -scenario full -version v0

