from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse_lazy
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    model = Day
    paginate_by = 3
    # template_name = 'hogehoge'

# def index(request):
#     context = {
#         'day_list': Day.objects.all(),
#     }
#     return render(request, 'diary/day_list.html', context)


class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    # 上のと同じ意味 fiels = '__all__'
    success_url = reverse_lazy('diary:index')

# def add(request):
#     # 送信内容を基にフォームを作成 POSTじゃない場合は、空のフォーム
#     form = DayCreateForm(request.POST or None)

#     # method == POST （送信ボタン押下時、modelsにある入力チェックに問題がなければ
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('diary:index')
#     # 通常ページアクセス、入力内容に不備があればこちら
#     context = {
#         'form': form
#     }
#     return render(request, 'diary/day_form.html', context)


class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

# def update(request, pk):
#     # urlのpkを基に、Dayを取得
#     day = get_object_or_404(Day, pk=pk)
#     # フォームに取得したDayを紐付ける
#     form = DayCreateForm(request.POST or None, instance=day)

#     # method == POST （送信ボタン押下時、modelsにある入力チェックに問題がなければ
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('diary:index')
#     # 通常ページアクセス、入力内容に不備があればこちら
#     context = {
#         'form': form
#     }

#     return render(request, 'diary/day_form.html', context)


class DeleteView(generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')

# def delete(request, pk):
#     # urlのpkを基に、Dayを取得
#     day = get_object_or_404(Day, pk=pk)

#     # method == POST （送信ボタン押下時、modelsにある入力チェックに問題がなければ
#     if request.method == 'POST':
#         day.delete()
#         return redirect('diary:index')
#     # 通常ページアクセス、入力内容に不備があればこちら
#     context = {
#         'day': day
#     }

#     return render(request, 'diary/day_confirm_delete.html', context)


class DetailView(generic.DetailView):
    model = Day


# def detail(request, pk):
#     # urlのpkを基に、Dayを取得
#     day = get_object_or_404(Day, pk=pk)

#     # 通常ページアクセス、入力内容に不備があればこちら
#     context = {
#         'day': day
#     }

#     return render(request, 'diary/day_detail.html', context)
