class Tablet:

    _VALID_MODELS = ['lite', 'pro', 'max']

    def __init__(self, model, added_storage=0):
        if model not in self._VALID_MODELS:
            raise ValueError(f"{model} is not a valid model")
        self._model = model
        self.added_storage = 0
        self.add_storage(added_storage)

    model = property()

    @property
    def memory(self):
        if self._model == 'lite':
            return 2
        elif self._model == 'pro':
            return 3
        elif self._model == 'max':
            return 4

    @property
    def base_storage(self):
        if self._model == 'lite':
            return 32
        elif self._model == 'pro':
            return 64
        elif self._model == 'max':
            return 128

    def add_storage(self, storage):
        if self.base_storage + self.added_storage + storage > 1024:
            raise ValueError(
                f'total storage must be less then 1024. current storage is {self.base_storage + self.added_storage}')
        self.added_storage += storage

    @property
    def storage(self):
        return self.base_storage + self.added_storage

    @storage.setter
    def storage(self, new_storage):
        if new_storage > 1024:
            raise ValueError(f'total storage must be less then 1024. storage {new_storage}')
        if new_storage < self.base_storage:
            raise ValueError(f'new storage is lower then base storage. base storage {self.base_storage}')
        self.added_storage = new_storage - self.base_storage

    def __repr__(self):
        return f'Tablet(model={self._model}, added_storage={self.added_storage})'



