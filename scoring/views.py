from scoring.models import ViewScene,ProtChoice,CmpdChoice,MolChoice,ScoreChoice
from scoring.serializers import ViewSceneSerializer,ProtChoiceSerializer,CmpdChoiceSerializer,\
    MolChoiceSerializer,ScoreChoiceSerializer
from rest_framework import viewsets

class ViewSceneView(viewsets.ModelViewSet):
    queryset = ViewScene.objects.filter()
    serializer_class = ViewSceneSerializer
    filter_fields = ('user_id',)

class ProtChoiceView(viewsets.ModelViewSet):
    queryset = ProtChoice.objects.filter()
    serializer_class = ProtChoiceSerializer
    filter_fields = ('user_id','prot_id','prot_id__target_id','choice_type')

class MolChoiceView(viewsets.ModelViewSet):
    queryset = MolChoice.objects.filter()
    serializer_class = MolChoiceSerializer
    filter_fields = ('user_id','mol_id','mol_id__prot_id__target_id','choice_type')

class CmpdChoiceView(viewsets.ModelViewSet):
    queryset = CmpdChoice.objects.filter()
    serializer_class = CmpdChoiceSerializer
    filter_fields = ('user_id','cmpd_id','choice_type')

class ScoreChoiceView(viewsets.ModelViewSet):
    queryset = ScoreChoice.objects.filter()
    serializer_class = ScoreChoiceSerializer
    filter_fields = ('user_id','mol_id','prot_id','is_done','mol_id__prot_id__target_id','prot_id__target_id','choice_type')