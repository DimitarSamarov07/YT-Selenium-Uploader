import datetime
import datetime as dt
import os.path
from enum import Enum


class VideoVisibility(Enum):
    PUBLIC = 1
    UNLISTED = 2
    PRIVATE = 3
    SCHEDULED = 4


class FileUpload:
    def __init__(self):
        self.videoPath = ""
        self.title = ""
        self.tags = ""
        self.description = ""
        self.thumbnailPath = ""
        self.privacy = ""
        self.scheduleDatetime = dt.datetime.now()

    def setVideo(self, videoPath, privacy: VideoVisibility):
        self.videoPath = videoPath
        self.privacy = privacy

    def setMetadata(self, title, description, tags: []):
        self.title = title
        self.description = description
        self.tags = tags

    def setThumbnail(self, thumbnailPath):
        if os.path.exists(thumbnailPath):
            self.thumbnailPath = thumbnailPath
        else:
            raise FileNotFoundError("A thumbnail does not exist at the given path.")

    def getTagsSeparated(self, separator: str):
        return separator.join(self.tags)

    def configureSchedule(self, day, month, year, hour, minute):

        if self.privacy != VideoVisibility.SCHEDULED:
            self.privacy = VideoVisibility.SCHEDULED

        self.scheduleDatetime = datetime.datetime(year, month, day, hour, minute)

    def retrieveScheduleDates(self):
        if self.privacy is VideoVisibility.SCHEDULED:
            datePart = self.scheduleDatetime.strftime("%b %d, %Y")
            timePart = self.scheduleDatetime.strftime("%I:%M %p")
            return [datePart, timePart]

