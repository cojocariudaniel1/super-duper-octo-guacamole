from PySide6.QtCore import QObject, Slot, Signal

class PostWorker(QObject):
    finished = Signal(list)
    error = Signal(str)

    def __init__(self, repository, user_id=None, community_name=None):
        super().__init__()
        self.repository = repository
        self.user_id = user_id
        self.community_name = community_name

    @Slot()
    def load_posts(self):
        """Load posts based on current configuration"""
        try:
            if self.user_id:
                posts = self.repository.get_posts_by_user(self.user_id)
            elif self.community_name:
                posts = self.repository.get_posts_by_community(self.community_name)
            else:
                posts = self.repository.get_all_posts()
            self.finished.emit(posts)
        except Exception as e:
            self.error.emit(str(e))