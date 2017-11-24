from abc import ABC, abstractmethod

class ImageTask(ABC):

    @abstractmethod
    def create_image(self): pass


class ImageSubTask(ImageTask):
    def create_image(self):
        return "image ready"


subTask = ImageSubTask()
print(subTask.create_image())
