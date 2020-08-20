# Import libraries
import pickle
# todo


class PredModel():
    '''
    Load, instantiate, and wrap predictive model
    '''
    def __init__(self, model_file):
        # todo: import pickled model from unit4, and load
        self.model = pickle.load(open(model_file, 'rb'))

    def predict(self, campaign):
        # todo: process input? Whatever we need to do before
        # inputing into model
        campaign_processed = None

        # get prediction
        result = self.model.predict(campaign_processed)

        # Do any processing before returning.

        return result
