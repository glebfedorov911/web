from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('price_per_carat/', CaratView.as_view(), name='price_per_carat'),
    path('color_of_gemstones/', ColorView.as_view(), name='color_of_gemstones'),
    path('transparency/', TransparencyView.as_view(), name='transparency'),
    path('cut-gemstones/', CutView.as_view(), name='cut-gemstones'),
    path('free-vygem/', FreeVygemView.as_view(), name='free-vygem'),
    path('clarity_of_gems/', ClarityView.as_view(), name='clarity_of_gems'),
    path('shape/', ShapeView.as_view(), name='shape'),
    path('brilliancy/', BrilliancyView.as_view(), name='brilliancy'),
    path('gemname/', GemnameView.as_view(), name='gemname'),
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