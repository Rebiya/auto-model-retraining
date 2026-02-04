(venv) rebu@rebu-HP-Pavilion-Laptop-15-cs1xxx:~/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining$ python main.py 
🚀 Auto Model Retraining System Started
🧹 Preprocessing raw data
✅ Preprocessing done
🏁 Initial training started

=== Training decision_tree ===
{'model': 'decision_tree', 'train_accuracy': 0.8084842030528931, 'test_accuracy': 0.7927608232789212, 'loss': 0.3890675355147533, 'precision_score': 0.6385135135135135, 'recall_score': 0.5053475935828877, 'f1_score': 0.564179104477612, 'roc_auc_score': 0.8364023870417733, 'confusion_matrix': '[[928,107],\n [185,189]]'}

=== Training knn ===
{'model': 'knn', 'train_accuracy': 0.8079517216897408, 'test_accuracy': 0.7814052519517388, 'loss': 0.4154909306354456, 'precision_score': 0.5901639344262295, 'recall_score': 0.5775401069518716, 'f1_score': 0.5837837837837838, 'roc_auc_score': 0.8298186468263195, 'confusion_matrix': '[[885,150],\n [158,216]]'}

=== Training logistic_regression_scratch ===
{'model': 'logistic_regression_scratch', 'train_accuracy': np.float64(0.7623358182463614), 'test_accuracy': 0.7636621717530163, 'loss': np.float64(0.6953047043468932), 'precision_score': 0.5410821643286573, 'recall_score': 0.7219251336898396, 'f1_score': 0.6185567010309279, 'roc_auc_score': 0.8389676819344337, 'confusion_matrix': '[[806,229],\n [104,270]]'}

=== Training logistic_regression_sklearn ===
{'model': 'logistic_regression_sklearn', 'train_accuracy': 0.7987220447284346, 'test_accuracy': 0.7828246983676366, 'loss': 0.41733362079559533, 'precision_score': 0.585, 'recall_score': 0.6256684491978609, 'f1_score': 0.6046511627906976, 'roc_auc_score': 0.8417861479242553, 'confusion_matrix': '[[869,166],\n [140,234]]'}

=== Training random_forest ===
{'model': 'random_forest', 'train_accuracy': 0.793574724884629, 'test_accuracy': 0.7579843860894251, 'loss': 0.4190243937838155, 'precision_score': 0.5298372513562387, 'recall_score': 0.7834224598930482, 'f1_score': 0.6321467098166127, 'roc_auc_score': 0.8418662326590716, 'confusion_matrix': '[[775,260],\n [ 81,293]]'}

=== Training svm ===
{'model': 'svm', 'train_accuracy': 0.7724529641462549, 'test_accuracy': 0.7437899219304471, 'loss': 0.39985152045835776, 'precision_score': 0.511504424778761, 'recall_score': 0.7727272727272727, 'f1_score': 0.6155484558040468, 'roc_auc_score': 0.8210648686352011, 'confusion_matrix': '[[759,276],\n [ 85,289]]'}

All models trained and evaluated successfully.
✅ Initial training completed
🚀 Starting Celery worker...
⏱️ Starting Celery beat scheduler...
✅ System is live. Retraining every 5 minutes.
celery beat v5.6.2 (recovery) is starting.
__    -    ... __   -        _
LocalTime -> 2026-02-04 15:05:28
Configuration ->
    . broker -> redis://localhost:6379/0
    . loader -> celery.loaders.app.AppLoader
    . scheduler -> celery.beat.PersistentScheduler
    . db -> celerybeat-schedule
    . logfile -> [stderr]@%INFO
    . maxinterval -> 5.00 minutes (300s)
[2026-02-04 15:05:28,970: INFO/MainProcess] beat: Starting...
 
 -------------- celery@rebu-HP-Pavilion-Laptop-15-cs1xxx v5.6.2 (recovery)
--- ***** ----- 
-- ******* ---- Linux-6.14.0-37-generic-x86_64-with-glibc2.39 2026-02-04 15:05:29
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         auto_model_retraining:0x749432a5c3b0
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     redis://localhost:6379/0
- *** --- * --- .> concurrency: 8 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . src.tasks.retrain_models

[2026-02-04 15:05:31,439: INFO/MainProcess] Connected to redis://localhost:6379/0
[2026-02-04 15:05:31,449: INFO/MainProcess] mingle: searching for neighbors
[2026-02-04 15:05:32,475: INFO/MainProcess] mingle: all alone
[2026-02-04 15:05:32,510: INFO/MainProcess] celery@rebu-HP-Pavilion-Laptop-15-cs1xxx ready.
[2026-02-04 15:10:00,010: INFO/MainProcess] Scheduler: Sending due task retrain-every-5-minutes (src.tasks.retrain_models)
[2026-02-04 15:10:00,020: INFO/MainProcess] Task src.tasks.retrain_models[5f241a4a-e740-4ecc-84b4-38356570de51] received
[2026-02-04 15:10:00,023: WARNING/ForkPoolWorker-8] 🔁 Celery triggered retraining...
[2026-02-04 15:10:00,024: WARNING/ForkPoolWorker-8] 🚀 Starting retraining pipeline
[2026-02-04 15:10:08,539: WARNING/ForkPoolWorker-8] Loading latest combined dataset version: 2
[2026-02-04 15:10:08,835: WARNING/ForkPoolWorker-8] Saved combined dataset version 3
[2026-02-04 15:10:08,843: WARNING/ForkPoolWorker-8] 
=== Retraining decision_tree on combined dataset version 3 ===
[2026-02-04 15:10:09,318: WARNING/ForkPoolWorker-8] {'model': 'decision_tree', 'train_accuracy': 0.8108462143044276, 'test_accuracy': 0.7920511000709723, 'loss': 0.3993331024621148, 'precision_score': 0.7055837563451777, 'recall_score': 0.3716577540106952, 'f1_score': 0.4868651488616462, 'roc_auc_score': 0.8261076235500788, 'confusion_matrix': '[[977, 58],\n [235,139]]'}
[2026-02-04 15:10:09,318: WARNING/ForkPoolWorker-8] 
=== Retraining knn on combined dataset version 3 ===
[2026-02-04 15:10:11,515: WARNING/ForkPoolWorker-8] {'model': 'knn', 'train_accuracy': 0.797353942887084, 'test_accuracy': 0.7828246983676366, 'loss': 0.44223381079557467, 'precision_score': 0.6049382716049383, 'recall_score': 0.5240641711229946, 'f1_score': 0.5616045845272206, 'roc_auc_score': 0.8224108088558216, 'confusion_matrix': '[[907,128],\n [178,196]]'}
[2026-02-04 15:10:11,515: WARNING/ForkPoolWorker-8] 
=== Retraining logistic_regression_scratch on combined dataset version 3 ===
[2026-02-04 15:10:13,226: WARNING/ForkPoolWorker-8] {'model': 'logistic_regression_scratch', 'train_accuracy': np.float64(0.7216400314383024), 'test_accuracy': 0.7530163236337828, 'loss': np.float64(0.7936833727286248), 'precision_score': 0.524904214559387, 'recall_score': 0.732620320855615, 'f1_score': 0.6116071428571429, 'roc_auc_score': 0.8344674365134723, 'confusion_matrix': '[[787,248],\n [100,274]]'}
[2026-02-04 15:10:13,226: WARNING/ForkPoolWorker-8] 
=== Retraining logistic_regression_sklearn on combined dataset version 3 ===
[2026-02-04 15:10:13,775: WARNING/ForkPoolWorker-8] {'model': 'logistic_regression_sklearn', 'train_accuracy': 0.7867435158501441, 'test_accuracy': 0.7963094393186657, 'loss': 0.4670677851316363, 'precision_score': 0.6338461538461538, 'recall_score': 0.5508021390374331, 'f1_score': 0.5894134477825465, 'roc_auc_score': 0.8357022914567672, 'confusion_matrix': '[[916,119],\n [168,206]]'}
[2026-02-04 15:10:13,775: WARNING/ForkPoolWorker-8] 
=== Retraining random_forest on combined dataset version 3 ===
[2026-02-04 15:10:14,573: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:10:14,710: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:10:14,838: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:10:14,892: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:10:15,425: WARNING/ForkPoolWorker-8] {'model': 'random_forest', 'train_accuracy': 0.8336389834948913, 'test_accuracy': 0.751596877217885, 'loss': 0.4099169435664733, 'precision_score': 0.5209790209790209, 'recall_score': 0.7967914438502673, 'f1_score': 0.6300211416490487, 'roc_auc_score': 0.8429783771215995, 'confusion_matrix': '[[761,274],\n [ 76,298]]'}
[2026-02-04 15:10:15,425: WARNING/ForkPoolWorker-8] 
=== Retraining svm on combined dataset version 3 ===
[2026-02-04 15:10:32,445: WARNING/ForkPoolWorker-8] {'model': 'svm', 'train_accuracy': 0.7669635839664658, 'test_accuracy': 0.7444996451383961, 'loss': 0.3945130378477868, 'precision_score': 0.5123674911660777, 'recall_score': 0.7754010695187166, 'f1_score': 0.6170212765957447, 'roc_auc_score': 0.8192745873052779, 'confusion_matrix': '[[759,276],\n [ 84,290]]'}
[2026-02-04 15:10:32,445: WARNING/ForkPoolWorker-8] 
Retraining completed successfully.
[2026-02-04 15:10:32,445: WARNING/ForkPoolWorker-8] ✅ Retraining finished
[2026-02-04 15:10:32,449: INFO/ForkPoolWorker-8] Task src.tasks.retrain_models[5f241a4a-e740-4ecc-84b4-38356570de51] succeeded in 32.426308599999174s: None
[2026-02-04 15:15:00,002: INFO/MainProcess] Scheduler: Sending due task retrain-every-5-minutes (src.tasks.retrain_models)
[2026-02-04 15:15:00,008: INFO/MainProcess] Task src.tasks.retrain_models[0bb7d697-0784-43ab-a251-5384ff67b9c7] received
[2026-02-04 15:15:00,011: WARNING/ForkPoolWorker-8] 🔁 Celery triggered retraining...
[2026-02-04 15:15:00,011: WARNING/ForkPoolWorker-8] 🚀 Starting retraining pipeline
[2026-02-04 15:15:08,875: WARNING/ForkPoolWorker-8] Loading latest combined dataset version: 3
[2026-02-04 15:15:09,202: WARNING/ForkPoolWorker-8] Saved combined dataset version 4
[2026-02-04 15:15:09,208: WARNING/ForkPoolWorker-8] 
=== Retraining decision_tree on combined dataset version 4 ===
[2026-02-04 15:15:09,673: WARNING/ForkPoolWorker-8] {'model': 'decision_tree', 'train_accuracy': 0.8107941971969511, 'test_accuracy': 0.7920511000709723, 'loss': 0.40636796185203705, 'precision_score': 0.7055837563451777, 'recall_score': 0.3716577540106952, 'f1_score': 0.4868651488616462, 'roc_auc_score': 0.8220646361311323, 'confusion_matrix': '[[977, 58],\n [235,139]]'}
[2026-02-04 15:15:09,674: WARNING/ForkPoolWorker-8] 
=== Retraining knn on combined dataset version 4 ===
[2026-02-04 15:15:12,018: WARNING/ForkPoolWorker-8] {'model': 'knn', 'train_accuracy': 0.7966560118023113, 'test_accuracy': 0.7835344215755855, 'loss': 0.4414356247159067, 'precision_score': 0.6095238095238096, 'recall_score': 0.5133689839572193, 'f1_score': 0.5573294629898403, 'roc_auc_score': 0.8195484254307783, 'confusion_matrix': '[[912,123],\n [182,192]]'}
[2026-02-04 15:15:12,018: WARNING/ForkPoolWorker-8] 
=== Retraining logistic_regression_scratch on combined dataset version 4 ===
[2026-02-04 15:15:14,379: WARNING/ForkPoolWorker-8] {'model': 'logistic_regression_scratch', 'train_accuracy': np.float64(0.7151462994836488), 'test_accuracy': 0.7473385379701917, 'loss': np.float64(0.806591807487288), 'precision_score': 0.5164835164835165, 'recall_score': 0.7540106951871658, 'f1_score': 0.6130434782608696, 'roc_auc_score': 0.8351675320984784, 'confusion_matrix': '[[771,264],\n [ 92,282]]'}
[2026-02-04 15:15:14,379: WARNING/ForkPoolWorker-8] 
=== Retraining logistic_regression_sklearn on combined dataset version 4 ===
[2026-02-04 15:15:15,064: WARNING/ForkPoolWorker-8] {'model': 'logistic_regression_sklearn', 'train_accuracy': 0.7827637078927957, 'test_accuracy': 0.794180269694819, 'loss': 0.47281248660483394, 'precision_score': 0.6329113924050633, 'recall_score': 0.5347593582887701, 'f1_score': 0.5797101449275363, 'roc_auc_score': 0.8333049161693663, 'confusion_matrix': '[[919,116],\n [174,200]]'}
[2026-02-04 15:15:15,064: WARNING/ForkPoolWorker-8] 
=== Retraining random_forest on combined dataset version 4 ===
[2026-02-04 15:15:15,946: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:15:16,099: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:15:16,235: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:15:16,288: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:15:16,721: WARNING/ForkPoolWorker-8] {'model': 'random_forest', 'train_accuracy': 0.8411605606097861, 'test_accuracy': 0.752306600425834, 'loss': 0.4005354442926802, 'precision_score': 0.521891418563923, 'recall_score': 0.7967914438502673, 'f1_score': 0.6306878306878307, 'roc_auc_score': 0.8433335916711876, 'confusion_matrix': '[[762,273],\n [ 76,298]]'}
[2026-02-04 15:15:16,722: WARNING/ForkPoolWorker-8] 
=== Retraining svm on combined dataset version 4 ===
[2026-02-04 15:15:38,640: WARNING/ForkPoolWorker-8] {'model': 'svm', 'train_accuracy': 0.7755102040816326, 'test_accuracy': 0.7487579843860894, 'loss': 0.38278213813388673, 'precision_score': 0.5180505415162455, 'recall_score': 0.767379679144385, 'f1_score': 0.6185344827586207, 'roc_auc_score': 0.8178976465421479, 'confusion_matrix': '[[768,267],\n [ 87,287]]'}
[2026-02-04 15:15:38,640: WARNING/ForkPoolWorker-8] 
Retraining completed successfully.
[2026-02-04 15:15:38,640: WARNING/ForkPoolWorker-8] ✅ Retraining finished
[2026-02-04 15:15:38,642: INFO/ForkPoolWorker-8] Task src.tasks.retrain_models[0bb7d697-0784-43ab-a251-5384ff67b9c7] succeeded in 38.63194565699814s: None
[2026-02-04 15:20:00,002: INFO/MainProcess] Scheduler: Sending due task retrain-every-5-minutes (src.tasks.retrain_models)
[2026-02-04 15:20:00,008: INFO/MainProcess] Task src.tasks.retrain_models[4f91e307-55b9-466a-a94d-5b3141c6ab5e] received
[2026-02-04 15:20:00,010: WARNING/ForkPoolWorker-8] 🔁 Celery triggered retraining...
[2026-02-04 15:20:00,011: WARNING/ForkPoolWorker-8] 🚀 Starting retraining pipeline
[2026-02-04 15:20:09,510: WARNING/ForkPoolWorker-8] Loading latest combined dataset version: 4
[2026-02-04 15:20:09,868: WARNING/ForkPoolWorker-8] Saved combined dataset version 5
[2026-02-04 15:20:09,875: WARNING/ForkPoolWorker-8] 
=== Retraining decision_tree on combined dataset version 5 ===
[2026-02-04 15:20:10,390: WARNING/ForkPoolWorker-8] {'model': 'decision_tree', 'train_accuracy': 0.8156126940004633, 'test_accuracy': 0.794889992902768, 'loss': 0.41040558005222966, 'precision_score': 0.6640926640926641, 'recall_score': 0.45989304812834225, 'f1_score': 0.5434439178515008, 'roc_auc_score': 0.8195161331989976, 'confusion_matrix': '[[948, 87],\n [202,172]]'}
[2026-02-04 15:20:10,390: WARNING/ForkPoolWorker-8] 
=== Retraining knn on combined dataset version 5 ===
[2026-02-04 15:20:13,109: WARNING/ForkPoolWorker-8] {'model': 'knn', 'train_accuracy': 0.7969654852907111, 'test_accuracy': 0.7814052519517388, 'loss': 0.43979134827866695, 'precision_score': 0.6071428571428571, 'recall_score': 0.5, 'f1_score': 0.5483870967741935, 'roc_auc_score': 0.8177491022759567, 'confusion_matrix': '[[914,121],\n [187,187]]'}
[2026-02-04 15:20:13,109: WARNING/ForkPoolWorker-8] 
=== Retraining logistic_regression_scratch on combined dataset version 5 ===
[2026-02-04 15:20:14,200: WARNING/ForkPoolWorker-8] {'model': 'logistic_regression_scratch', 'train_accuracy': np.float64(0.7142691684039842), 'test_accuracy': 0.7352732434350603, 'loss': np.float64(0.8174078557583785), 'precision_score': 0.5008726003490401, 'recall_score': 0.767379679144385, 'f1_score': 0.6061246040126715, 'roc_auc_score': 0.831814306750368, 'confusion_matrix': '[[749,286],\n [ 87,287]]'}
[2026-02-04 15:20:14,201: WARNING/ForkPoolWorker-8] 
=== Retraining logistic_regression_sklearn on combined dataset version 5 ===
[2026-02-04 15:20:15,126: WARNING/ForkPoolWorker-8] {'model': 'logistic_regression_sklearn', 'train_accuracy': 0.781445448227936, 'test_accuracy': 0.794889992902768, 'loss': 0.4771029615263353, 'precision_score': 0.6375404530744336, 'recall_score': 0.5267379679144385, 'f1_score': 0.5768667642752562, 'roc_auc_score': 0.8309307912888474, 'confusion_matrix': '[[923,112],\n [177,197]]'}
[2026-02-04 15:20:15,126: WARNING/ForkPoolWorker-8] 
=== Retraining random_forest on combined dataset version 5 ===
[2026-02-04 15:20:16,189: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:20:16,408: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:20:16,563: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:20:16,618: WARNING/ForkPoolWorker-8] /home/rebu/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining/venv/lib/python3.12/site-packages/sklearn/ensemble/_base.py:174: UserWarning: Loky-backed parallel loops cannot be called in a multiprocessing, setting n_jobs=1
  n_jobs = min(effective_n_jobs(n_jobs), n_estimators)

[2026-02-04 15:20:17,197: WARNING/ForkPoolWorker-8] {'model': 'random_forest', 'train_accuracy': 0.846421125781793, 'test_accuracy': 0.7444996451383961, 'loss': 0.3926466025574338, 'precision_score': 0.5119453924914675, 'recall_score': 0.8021390374331551, 'f1_score': 0.625, 'roc_auc_score': 0.841914025162107, 'confusion_matrix': '[[749,286],\n [ 74,300]]'}
[2026-02-04 15:20:17,198: WARNING/ForkPoolWorker-8] 
=== Retraining svm on combined dataset version 5 ===
[2026-02-04 15:20:42,906: WARNING/ForkPoolWorker-8] {'model': 'svm', 'train_accuracy': 0.7832985869817003, 'test_accuracy': 0.7480482611781405, 'loss': 0.371031275317555, 'precision_score': 0.5171790235081374, 'recall_score': 0.7647058823529411, 'f1_score': 0.6170442286947141, 'roc_auc_score': 0.8163398692810457, 'confusion_matrix': '[[768,267],\n [ 88,286]]'}
[2026-02-04 15:20:42,906: WARNING/ForkPoolWorker-8] 
Retraining completed successfully.
[2026-02-04 15:20:42,906: WARNING/ForkPoolWorker-8] ✅ Retraining finished
[2026-02-04 15:20:42,907: INFO/ForkPoolWorker-8] Task src.tasks.retrain_models[4f91e307-55b9-466a-a94d-5b3141c6ab5e] succeeded in 42.89737370999865s: None
^C🛑 Shutting down system

worker: Hitting Ctrl+C again will initiate cold shutdown, terminating all running tasks!

worker: Warm shutdown (MainProcess)
(venv) rebu@rebu-HP-Pavilion-Laptop-15-cs1xxx:~/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining$ ^C
(venv) rebu@rebu-HP-Pavilion-Laptop-15-cs1xxx:~/Desktop/Projects/Interns/Icog/training-tasks/auto-model-retraining$ 