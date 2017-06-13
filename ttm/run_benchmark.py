from sklearn_models import MultNB, BernNB, SVM
from keras_models import BasicNN
from benchmarks import benchmark


datasets = [
    '../data/r8-all-terms.txt',
    '../data/r52-all-terms.txt',
    '../data/20ng-all-terms.txt',
    '../data/webkb-stemmed.txt'
]

models = [
    BasicNN,
    (BasicNN, {'layers': 2}),
    (BasicNN, {'layers': 3, 'units': 64}),
    MultNB,
    BernNB,
    SVM
]

if __name__ == '__main__':
    for data_path in datasets:
        print
        print data_path
        for model_class in models:
            params = {}
            if type(model_class) == tuple:
                model_class, params = model_class

            score = benchmark(model_class, data_path, params)
            print "%.3f" % score, model_class(**params)
