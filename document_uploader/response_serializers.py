from rest_framework import serializers


class FileUploadResponseOBJECT(object):
    def __init__(self, TXNSTATUS, FILES=None):
        self.TXNSTATUS = TXNSTATUS
        files = []
        if FILES:
            for file in FILES:
                media_object = {}
                media_object["name"] = file.file.name.split("t_C")[0]
                media_object["url"] = file.file.url
                files.append(media_object)
        self.FILES = files


class FileUploadResponseSERIALIZER(serializers.Serializer):
    FILES = serializers.CharField(required=False)
    TXNSTATUS = serializers.CharField()
