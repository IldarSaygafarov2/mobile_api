from rest_framework import serializers
from .models import Photo, PDFFile, PhotoItem


class PDFFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFFile
        fields = ['pk', 'file']
        read_only_fields = ['pk']


class PhotoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoItem
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    photo_items = PhotoItemSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Photo
        fields = ['pk', 'photo_items', 'uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        photo = Photo.objects.create(**validated_data)

        for image in uploaded_images:
            PhotoItem.objects.create(photo=photo, image=image)

        return photo
