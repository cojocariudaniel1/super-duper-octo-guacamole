import logging
import os

from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QPushButton, QLabel, QSizePolicy, \
    QFrame
from PySide6.QtCore import Signal, Slot, QThread, QObject, QCoreApplication

from backend.global_path import get_absolute_file_path
from frontend.assets.customWidget.LoadingBar import LoadingBar
from frontend.UserInterface.HomePageUI.UserInterfaceFile.DashBoardView import Ui_DashBoardView
from frontend.UserInterface.HomePageUI.controller.createPostWidget import CreatePostWidget
from frontend.UserInterface.PostUI.PythonUI.DetaliedPostWidget import DetailedPostWidget
from frontend.UserInterface.PostUI.PythonUI.FeedPostWidget import FeedPostWidget
from frontend.assets.customWidget.communitiesWidgetCW import CommunityWidget
from frontend.assets.customWidget.offlineFriendsCW import OfflineFriendWidget
from frontend.assets.customWidget.onlineFriendsCW import OnlineFriendWidget
from backend.Repository.CommunityRepository import CommunityRepository
from backend.Repository.RecommendationService import RecommendationService
from backend.Repository.UserRepository import get_friends_with_status

from backend.database_connect import Neo4jDriverSingleton
from backend.Repository.PostRepository import PostRepository
from frontend.UserInterface.PostUI.PythonUI.RecommendedPostsWidget import RecommendedPostsWidget

class PostWorker(QObject):
    finished = Signal(list)
    error = Signal(str)


    def __init__(self, repository, user_id=None, community_name=None, limit=10, offset=0):
        super().__init__()
        self.repository = repository
        self.user_id = user_id
        self.community_name = community_name
        self.limit = limit
        self.offset = offset

    @Slot()
    def load_posts(self):
        """Load posts based on current configuration"""
        try:
            if self.user_id:
                posts = self.repository.get_posts_by_user(self.user_id)
            elif self.community_name:
                posts = self.repository.get_posts_by_community(self.community_name)
            else:
                posts = self.repository.get_all_posts(limit=self.limit, offset=self.offset)
            self.finished.emit(posts)
        except Exception as e:
            self.error.emit(str(e))


class DashboardWindow(QWidget):
    dashboard_post_clicked = Signal(str)
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.ui = Ui_DashBoardView()
        self.ui.setupUi(self)
        self.loaded_post_ids = set()
        self.set_image(self.ui.logoLabel, "logo.png")
        self.set_button_icon(self.ui.notificationButton, "ButtonNotificationImage.png")
        self.set_button_icon(self.ui.profileButton, "UserSettings.png")
        self.set_button_icon(self.ui.shortcutSettingsButton, "ProfileSettingsShortcut.png")

        # Initialize database
        self.driver = Neo4jDriverSingleton.get_driver()
        self.post_repo = PostRepository(self.driver)
        self.community_repo = CommunityRepository(self.driver)
        # Create stacked widget for view switching
        self.stack = QStackedWidget(self)

        # -------------------- FEED CONTAINER --------------------
        self.feed_container = self.create_feed_container()

        # -------------------- DETAILED POST CONTAINER --------------------
        self.post_container = self.create_post_container()

        # -------------------- CREATE POST CONTAINER --------------------
        self.create_post_container = self.create_create_post_container()

        # Connect back button to show feed
        self.post_detail.back_to_feed.connect(self.show_feed)

        # Add containers to stack and set in scroll area
        self.stack.addWidget(self.feed_container)
        self.stack.addWidget(self.post_container)
        self.stack.addWidget(self.create_post_container)

        # Add stack to the post area layout
        self.ui.postAreea.addWidget(self.stack)

        # -------------------- LOADING BAR --------------------
        self.loading_bar = LoadingBar(self)
        self.loading_bar.setGeometry(0, 0, self.width(), 4)
        self.loading_bar.hide()

        # Variables for pagination
        self.current_offset = 0
        self.posts_per_page = 10

        # Create a button to show the Create Post page
        self.create_post_button = QPushButton("Create Post")
        self.create_post_button.clicked.connect(self.show_create_post)
        self.ui.HeaderBar.addWidget(self.create_post_button)

        # Initialize worker thread
        self.worker_thread = None
        # Load posts (initial batch)
        self.load_posts()
        self.load_friends_widgets()
        self.load_communities_acces_link()
        self.load_popular_tags()
        self.load_top_communities_grid()
        self.load_recommended_posts()



    def set_button_icon(self, button, icon_name, fallback_size=(32, 32)):
        """
        Sets an icon from the assets folder to a QPushButton

        Args:
            button (QPushButton): The button to set the icon to
            icon_name (str): Name of the icon file in assets/images/
            fallback_size (tuple): Size for fallback blank icon (width, height)
        """
        # Construct the full path
        icon_path = get_absolute_file_path(f"frontend/assets/images/{icon_name}")

        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
            if not icon.isNull():
                button.setIcon(icon)
                return

        # Fallback if icon not found
        print(f"Icon not found: {icon_path}")
        blank_pixmap = QPixmap(fallback_size[0], fallback_size[1])
        button.setIcon(QIcon(blank_pixmap))

    def set_image(self, label, image_name):
        """
        Sets an image from the assets folder to a QLabel

        Args:
            label (QLabel): The label to set the image to
            image_name (str): Name of the image file in assets/images/
        """
        # Construct the full path
        image_path = get_absolute_file_path(f"frontend/assets/images/{image_name}")

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                label.setPixmap(pixmap)
                return

        # Fallback if image not found
        print(f"Image not found: {image_path}")
        label.setPixmap(QPixmap(label.size()))  # Bla

    def create_feed_container(self):
        """Create and return the feed container."""
        feed_container = QWidget()
        feed_layout = QVBoxLayout(feed_container)
        self.posts_layout = QVBoxLayout()
        feed_layout.addLayout(self.posts_layout)
        feed_layout.addStretch(1)
        return feed_container

    def create_post_container(self):
        """Create and return the post detail container."""
        post_container = QWidget()
        post_layout = QVBoxLayout(post_container)
        self.post_detail = DetailedPostWidget(post_container)
        post_layout.addWidget(self.post_detail)
        post_layout.addStretch(1)
        return post_container

    def create_create_post_container(self):
        """Create and return the create post container."""
        create_post_container = QWidget()
        create_post_layout = QVBoxLayout(create_post_container)
        self.create_post_widget = CreatePostWidget(self.user_id, self.post_repo)
        create_post_layout.addWidget(self.create_post_widget)
        create_post_layout.addStretch(1)
        return create_post_container

    def show_create_post(self):
        """Switch to the Create Post view."""
        self.stack.setCurrentIndex(2)

    def load_posts(self):
        """Fetch posts from the database asynchronously."""
        self.loading_bar.start_loading()
        self.clear_layout(self.posts_layout)
        # Clear existing posts (except the first load)
        if self.current_offset == 0:
            while self.posts_layout.count():
                item = self.posts_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

        # Set up the worker thread
        self.worker_thread = QThread()
        self.worker = PostWorker(
            self.post_repo,
            limit=self.posts_per_page,
            offset=self.current_offset
        )
        self.worker.moveToThread(self.worker_thread)

        # Connect signals
        self.worker_thread.started.connect(self.worker.load_posts)
        self.worker.finished.connect(self.on_posts_loaded)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.error.connect(self.on_posts_error)
        self.worker.error.connect(self.worker_thread.quit)

        # Clean up thread when done
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        # Start the thread
        self.worker_thread.start()

        # Increment the offset for the next batch
        self.current_offset += self.posts_per_page

    def on_posts_loaded(self, posts):
        """Handle successfully loaded posts."""
        for post in posts:
            if post['id'] not in self.loaded_post_ids:  # <--- Verifică dacă deja a fost adăugat
                self.add_post(post)
                self.loaded_post_ids.add(post['id'])  # <--- Salvează ID-ul postării
        self.loading_bar.stop_loading()

    def on_posts_error(self, error_msg):
        """Handle post loading errors."""
        print(f"Error loading posts: {error_msg}")
        self.loading_bar.stop_loading()

    def add_post(self, post_data):
        """Add a new post to the feed layout."""
        post_widget = FeedPostWidget(post_data, self.user_id)
        # Connect the signals - make sure this line is present
        post_widget.post_clicked.connect(self.show_post_detail)  # This is crucial

        # Other connections
        post_widget.comment_clicked.connect(self.handle_comment)
        post_widget.reply_clicked.connect(self.handle_reply)

        # Add spacing between posts
        self.posts_layout.addWidget(post_widget)
        # Add delimiter line between posts
        delimiter = QWidget()
        delimiter.setFixedHeight(1)
        delimiter.setStyleSheet("background-color: #3a3a3a;")
        self.posts_layout.addWidget(delimiter)
        self.posts_layout.addSpacing(5)

    def show_post_detail(self, post_id):
        print(f"Emitting dashboard_post_clicked for post {post_id}")
        try:
            print(f"DashboardWindow emitting signal from instance: {id(self)}")

            self.dashboard_post_clicked.emit(post_id)
            QCoreApplication.processEvents()
            print("Emission successful")
        except Exception as e:
            print(f"Emission failed: {str(e)}")


    def handle_comment(self, post_id):
        """Handle comment button click."""
        print(f"Comment clicked for post {post_id}")
        # Implement comment functionality here

    def handle_reply(self, post_id):
        """Handle reply button click."""
        print(f"Reply clicked for post {post_id}")
        # Implement reply functionality here

    def show_feed(self):
        """Switch back to the feed view."""
        self.stack.setCurrentIndex(0)

    def load_communities_acces_link(self):
        """Load top communities from database and display them"""
        try:
            # Clear existing layout
            while self.ui.communitiesWidgetLayout.count():
                item = self.ui.communitiesWidgetLayout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            # Get top 4 communities from database
            communities = self.community_repo.get_top_communities(limit=4)

            # Add community widgets
            for community in communities:
                community_widget = CommunityWidget(
                    communityName=community["name"],
                    icon=community.get("icon")  # Pass the base64 icon from database
                )
                self.ui.communitiesWidgetLayout.addWidget(community_widget)

            self.ui.communitiesWidgetLayout.addStretch(1)

        except Exception as e:
            logging.critical(f"Error loading communities: {e}")

    def load_friends_widgets(self):
        """Load and display a list of online and offline friends from the database."""
        try:
            friends_data = get_friends_with_status(self.driver, self.user_id)

            # Clear existing layouts
            for layout in [self.ui.onlineFriendsLayout, self.ui.offlineFriendsLayout]:
                while layout.count():
                    item = layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()

            for friend in friends_data:
                if friend["status"] == "online":
                    widget = OnlineFriendWidget(friend["name"], friend["points"], friend["img"])
                    self.ui.onlineFriendsLayout.addWidget(widget)
                else:
                    widget = OfflineFriendWidget(friend["name"],friend["points"], friend["img"])
                    self.ui.offlineFriendsLayout.addWidget(widget)

            self.ui.onlineFriendsLayout.addStretch(1)
            self.ui.offlineFriendsLayout.addStretch(1)

        except Exception as e:
            logging.error(f"Error loading friends: {e}")

    def load_popular_tags(self):

        tags_data = [
            {"tagname": "Music"},
            {"tagname": "MidnightTech"},
            {"tagname": "WhatDoYouThink"},
            {"tagname": "ConspiracyCornerStories"},
            {"tagname": "AIRevolution"},
            {"tagname": "Health"},
            {"tagname": "QuantumLeap"},
            {"tagname": "SpaceTalk"},
            {"tagname": "EcoFuture"}
        ]

        try:
            while self.ui.popularHashtagsLayoutWidgetFirstRow.count():
                item = self.ui.popularHashtagsLayoutWidgetFirstRow.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            while self.ui.popularHashtagsLayoutWidgetSecondRow.count():
                item = self.ui.popularHashtagsLayoutWidgetSecondRow.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            # Add tags to rows
            max_per_row = 4
            for index, tag in enumerate(tags_data[:8]):  # Max 8 tags (4 per row)
                tag_label = QLabel(f"#{tag['tagname']}")

                # Apply stylesheet
                tag_label.setStyleSheet("""
                    font: 500 12pt "Raleway";
                    background-color: rgb(58, 58, 58);
                    border-radius: 18px;
                    color: white;
                    padding-left: 5px;
                """)

                # Set size policies
                tag_label.setMinimumHeight(37)
                tag_label.setSizePolicy(
                    QSizePolicy.Policy.MinimumExpanding,  # Horizontal
                    QSizePolicy.Policy.Fixed  # Vertical
                )

                # Add to appropriate row
                if index < max_per_row:
                    self.ui.popularHashtagsLayoutWidgetFirstRow.addWidget(tag_label)
                else:
                    self.ui.popularHashtagsLayoutWidgetSecondRow.addWidget(tag_label)
            self.ui.popularHashtagsLayoutWidgetFirstRow.addWidget(self._horizontal_spacer())
            self.ui.popularHashtagsLayoutWidgetSecondRow.addWidget(self._horizontal_spacer())

        except Exception as e:
            logging.critical(f"Error in load_popular_tags: {e}")

    def load_top_communities_grid(self):
        """Load top communities into 5 separate horizontal layout rows"""

        try:
            # Lista layout-urilor din UI pentru cele 5 rânduri
            layout_rows = [
                self.ui.CommRow_1,
                self.ui.CommRow_2,
                self.ui.CommRow_3,
                self.ui.CommRow_4,
                self.ui.CommRow_5
            ]

            # Golește toate layout-urile existente
            for layout in layout_rows:
                while layout.count():
                    item = layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()

            # Încarcă comunitățile din baza de date (ex: maxim 20 comunități)
            communities = [
                {"name": "PythonDev", "icon": "communityIcons/communityIcon1.png"},
                {"name": "Star Citizen", "icon": "communityIcons/communityIcon2.png"},
                {"name": "CasualRo", "icon": "communityIcons/communityIcon3.png"},
                {"name": "CrackWatch", "icon": "communityIcons/communityIcon4.png"},
                {"name": "pcmasterrace", "icon": "communityIcons/communityIcon5.png"},
                {"name": "Pc Build", "icon": "communityIcons/communityIcon6.png"},
                {"name": "TeamVitality", "icon": "communityIcons/communityIcon7.png"},

            ]

            # Parametru: max 4 pe rând
            max_per_row = 4

            # Adaugă comunitățile în rânduri
            for index, community in enumerate(communities):
                community_widget = CommunityWidget(
                    communityName=community["name"],
                    icon=community.get("icon")
                )
                row_index = index // max_per_row
                if row_index < len(layout_rows):

                    community_widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
                    community_widget.setMinimumWidth(0)
                    community_widget.updateGeometry()
                    layout_rows[row_index].addWidget(community_widget)

            # Adaugă spacere orizontale pentru aliniere frumoasă
            for layout in layout_rows:
                layout.addWidget(self._horizontal_spacer())

        except Exception as e:
            logging.critical(f"Error in load_top_communities_grid: {e}")

    def _horizontal_spacer(self):
        spacer = QFrame()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )
        return spacer

    def clear_layout(sel, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

    def load_recommended_posts(self):
        """Load recommended posts into the horizontal layout"""
        try:
            # Clear existing widgets

            while self.ui.recommendFeedHWidget.count():
                item = self.ui.recommendFeedHWidget.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            # Get some posts to recommend (using the same data as feed for now)

            reco_service = RecommendationService(self.driver)
            recommended_posts = reco_service.get_recommended_posts(self.user_id, limit=5)

            # Add recommended post widgets
            for post in recommended_posts:
                post_widget = RecommendedPostsWidget(post)
                post_widget.post_clicked.connect(self.show_post_detail)
                post_widget.comment_clicked.connect(self.handle_comment)

                # Add to horizontal layout
                self.ui.recommendFeedHWidget.addWidget(post_widget)

            # Add a spacer at the end
            self.ui.recommendFeedHWidget.addStretch()

        except Exception as e:
            logging.error(f"Error loading recommended posts: {e}")
