from django.shortcuts import render
from analysis.models import TextAnalysis,AnalysisPhoto, AnalysisSeo

# Create your views here.
def analysis(request):
    analyze_flag="current"
    seo=AnalysisSeo.objects.all()
    texts=TextAnalysis.objects.all()
    photos=AnalysisPhoto.objects.all()
    return render(request, 'analysis/dev/analysis.html', {'analyze_flag': analyze_flag, 'seo': seo, 'texts': texts, 'photos': photos})