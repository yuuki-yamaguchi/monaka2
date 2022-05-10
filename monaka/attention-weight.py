class AttentionWeight():
    def __init__(self):
        pass
    
    @property
    def attention_weight(self):
        return self.__attention_weight

    @attention_weight.setter
    def attention_weight(self, attention_weight):
        if type(attention_weight) != list:
            raise ValueError("attention weight is must be 'list'.")   
        self.__attention_weigh = attention_weight