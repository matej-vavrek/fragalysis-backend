from django.conf.urls import include,url
from rest_framework.authtoken import views as drf_views
from rest_framework.routers import DefaultRouter
from api import views
from scoring import views as score_views

router = DefaultRouter()
# Register the basic data
router.register(r'molecules', views.MoleculeView)
router.register(r'mdl', views.MDLView)
router.register(r'compounds', views.CompoundView)
router.register(r'targets', views.TargetView)
router.register(r'proteins', views.ProteinView)

# Register the molecular choices
router.register(r'scorechoice',score_views.ScoreChoiceView)
router.register(r'molchoice',score_views.MolChoiceView)
router.register(r'protchoice',score_views.ProtChoiceView)
router.register(r'cmpdchoice',score_views.CmpdChoiceView)
router.register(r'viewscene',score_views.ViewSceneView)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
]