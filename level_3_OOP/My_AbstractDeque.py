from abc import abstractmethod, ABC

class My_Dequeu(ABC):

    @abstractmethod
    def __init__(self):
        # создается структура под двустороннюю очередь.
        pass

    # СТАТУСЫ:
    CONST_ADD_FRONT_NIL = 0     # addFront() еще не вызывался
    CONST_ADD_FRONT_OK = 1      # выполнился корректно
    CONST_ADD_TAIL_NIL = 0      # addTaile() еще не вызывался
    CONST_ADD_TAIL_OK = 1       # выполнился корректно
    CONST_REMOVE_FRONT_NIL = 0  # removeFront() еще не вызывался
    CONST_REMOVE_FRONT_OK = 1   # выполнился корректно
    CONST_REMOVE_FRONT_ERR = 2  # очередь пустая
    CONST_REMOVE_TAIL_NIL = 0   # removeTaile() еще не вызывался
    CONST_REMOVE_TAIL_OK = 1    # выполнился корректно
    CONST_REMOVE_TAIL_ERR = 2   # очередь пустая
    CONST_SIZE_NIL = 0          # size() еще не вызывался
    CONST_SIZE_OK = 1           # выполнился корректно

    # КОМАНДЫ:
    # постусловие: элемент добавлен в начало очереди
    @abstractmethod
    def addFront(self):
        # добавление элемента в голову
        pass

    # постусловие: элемент добавлен в конец очереди
    @abstractmethod
    def addTail(self):
        # добавление элемента в хвост
        pass

    # предусловие: очередь не пустая
    # постусловие: элемент удален из начала очереди
    @abstractmethod
    def removeFront(self):
        # удаляет элемент из головы очереди
        pass

    # предусловие: очередь не пустая
    # постусловие: элемент удален из конца очереди
    @abstractmethod
    def removeTail(self):
        # удаляет элемент из хвоста очереди
        pass

    # ЗАПРОСЫ:

    @abstractmethod
    def size(self):
        # возвращает кол-во элементов в очереди
        pass

    # ЗАПРОСЫ ДЛЯ СТАТУСОВ:
    
    @abstractmethod
    def get_addTail_status(self):
        pass

    @abstractmethod
    def get_addFront_status(self):
        pass

    @abstractmethod
    def get_removeTail_status(self):
        pass

    @abstractmethod
    def get_removeFront_status(self):
        pass

    @abstractmethod
    def get_size_status(self):
        pass