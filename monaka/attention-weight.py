class AttentionWeight():
    def __init__(self, attention_weight):
        self._check_attention_weight(attention_weight)
        self.set_attention_weight(attention_weight)

    def get_attention_weight(self):
        return self.set_attention_weight

    def set_attention_weight(self, attention_weight):
        self.attention_weight = attention_weight

    def _check_attention_weight(self, attention_weight):
      if type(attention_weight) != list:
            raise ValueError("attention weight must be 'list'.")

class AttentionWeight1D(AttentionWeight):
    def __init__(self, attention_weight):
        self._check_attention_weight(attention_weight)
        self.set_attention_weight(attention_weight)

    def _check_attention_weight(self, attention_weight):
        super()._check_attention_weight(attention_weight)

        for weight in attention_weight:
            if type(weight) not in [int, float]:
                raise ValueError("elements in attention weight must be 'int' or 'float'.")

class AttentionWeight2D(AttentionWeight):
    def __init__(self, attention_weight):
        self._check_attention_weight(attention_weight)
        self.set_attention_weight(attention_weight)

    def _check_attention_weight(self, attention_weight):
        super()._check_attention_weight(attention_weight)

        for weights in attention_weight:
            if type(weights) != list:
                raise ValueError("elements in attention weight must be 'list'.")
