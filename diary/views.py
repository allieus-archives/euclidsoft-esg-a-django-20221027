from django.shortcuts import render, redirect

from diary.forms import MemoryForm
from diary.models import Memory


def memory_list(request):
    memory_qs = Memory.objects.all()  #.order_by("-id")
    return render(request, "diary/memory_list.html", {
        "memory_list": memory_qs,
    })


def memory_detail(request, pk):
    memory = Memory.objects.get(pk=pk)
    return render(request, "diary/memory_detail.html", {
        "memory": memory,
    })


def memory_new(request):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm()

    return render(request, "diary/memory_form.html", {
        "form": form,
    })
