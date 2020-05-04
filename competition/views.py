from django.views.generic import DetailView, ListView

from competition.models import Competition, Semester, Series


#tento view by sa nemal pouzivat, namiesto neho je seriesProblemsView
class SemesterProblemsView(DetailView):
    template_name = 'competition/semester_problems.html'
    model = Semester
    context_object_name = 'semester'


class LatestSemesterView(SemesterProblemsView):
    def get_object(self, queryset=None):
        return Competition.get_seminar_by_current_site().semester_set.order_by('-end').first()


class SeriesProblemsView(DetailView):
    template_name = 'competition/series.html'
    model = Series
    context_object_name = 'series'

class LatestSeriesProblemsView(SeriesProblemsView):
    def get_object(self, queryset=None):
        #treba dorobit metodu co vrati aktualnu seriu a to tu capnut
        return Competition.get_seminar_by_current_site().semester_set.order_by('-end').first().series_set.first()


#iba placeholder aby to nieco zobrazovalo, ofc model nebude series
class ResultsView(DetailView):
    template_name = 'competition/results.html'
    model = Series
    context_object_name = 'series'



class ArchiveView(ListView):
    # toto prerobím keď pribudne model ročník
    template_name = 'competition/archive.html'
    model = Semester
    context_object_name = 'context'

    def get_queryset(self):
        site_competition = Competition.get_seminar_by_current_site()
        context = {}
        years = {}

        for sem in Semester.objects.filter(competition=site_competition).order_by('-year'):
            try:
                years[sem.year]
            except KeyError:
                years[sem.year] = []
            years[sem.year].append(sem)

        context["mostRecentYear"] = Semester.objects.filter(
            competition=site_competition).order_by('-year').first().year
        context["years"] = years
        return context


class SemesterDetailView(DetailView):
    template_name = 'competition/semester_detail.html'
    model = Semester
    context_object_name = 'semester'
