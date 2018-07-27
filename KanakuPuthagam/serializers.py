from rest_framework import serializers
from KanakuPuthagam.models  import Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name','created_on','modified_on')