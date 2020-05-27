from django.shortcuts import render
from django.views import generic
from .models import Employee
from .froms import SeaarchForm

class IndexView(generic.ListView):
        model = Employee
        paginate_by = 1

        def get_context_data(self):
            context = super().get_context_data()
            context['form'] = SeaarchForm(self.request.GET)
            return context

        def get_queryset(self):
            form = SeaarchForm(self.request.GET)
            form.is_valid() #絶対やらないといけない

            #全社員取得
            queryset = super().get_queryset()

            #部署が選択されていれば絞る
            department = form.cleaned_data['department']
            if department:
                queryset = queryset.filter(department = department)

            #サークルの選択されていれば絞る
            club = form.cleaned_data['club']
            if club:
                queryset = queryset.filter(club = club)

            return queryset
