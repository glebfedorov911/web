from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('app/templates/page/price_per_carat/', CaratView.as_view(), name='price_per_carat'),
    path('color_gem/', ColorView.as_view(), name='color_gem'),
    path('transparency_gem/', TransparencyView.as_view(), name='transparency_gem'),
    path('cut_gem/', CutView.as_view(), name='cut_gem'),
    path('free-vygem/', FreeVygemView.as_view(), name='free-vygem'),
    path('clarity_gem/', ClarityView.as_view(), name='clarity_gem'),
    path('shape_gem/', ShapeView.as_view(), name='shape_gem'),
    path('brilliancy_gem/', BrilliancyView.as_view(), name='brilliancy_gem'),
    path('name_gem/', GemnameView.as_view(), name='name_gem'),
    path('valuenotprice/', ValuenotpriceView.as_view(), name='valuenotprice'),
    path('gemologist/', GemologistView.as_view(), name='gemologist'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('pay/', PayView.as_view(), name='pay'),
    path('salepurchaseplan/', SalePurchasePlanView.as_view(), name='salepurchaseplan'),
    path('result/', ResultView.as_view(), name='result'),
    path('download/', DownloadView.as_view(), name='download'),
    path('refund/', RefundView.as_view(), name='refund'),
    path('whoisvygem/', WhoisvygemView.as_view(), name='whoisvygem'),

]