from django.contrib import admin
from analysis.models import TextAnalysis, AnalysisSeo, AnalysisPhoto
# Register your models here.
admin.site.register(TextAnalysis)
admin.site.register(AnalysisSeo)
admin.site.register(AnalysisPhoto)