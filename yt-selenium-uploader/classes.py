import os.path


class FileUpload:
    def __init__(self):
        self.videoPath = ""
        self.title = ""
        self.tags = ""
        self.description = ""
        self.thumbnailPath = ""
        self.privacy = ""

    def setVideo(self, videoPath, privacy):
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
