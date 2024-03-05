from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [i for i in self.categories if i.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [i for i in self.topics if i.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = [i for i in self.documents if i.id == document_id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        self.categories = [i for i in self.categories if i.id != category_id]

    def delete_topic(self, topic_id):
      self.topics = [i for i in self.topics if i.id != topic_id]

    def delete_document(self, document_id):
        self.documents = [i for i in self.topics if i.id != document_id]

    def get_document(self, document_id):
        return [i for i in self.documents if i.id == document_id][0]

    def __repr__(self):

        return "\n".join([str(doc) for doc in self.documents])