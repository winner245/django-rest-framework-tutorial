from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet 


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
 

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # why do we need to explicitly specify the owner filed here while Snippet model already has this field?
    # Because the owner field stored in the snippet model is a FK, which is an ID. But we need the username of the owner. 
    owner = serializers.ReadOnlyField(source='owner.username')  
    
    # The highlight field in the snippet model is the entire HTML content, but here we just need its url.
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html') 
    
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'owner', 'highlight', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # 对于 model 中不存在的 field，需要额外指定
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
