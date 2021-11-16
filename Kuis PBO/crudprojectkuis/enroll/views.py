from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#untuk fungsi tambah (create)
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['nama_barang']
            jm = fm.cleaned_data['jumlah_barang']
            hg = fm.cleaned_data['harga_barang']
            reg = User(nama_barang=nm, jumlah_barang=jm, harga_barang=hg)
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm,
        'stu':stud})

#untuk fungsi edit/hapus
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/update.html', {'form':fm})

#untuk fungsi hapus (delete)
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect ('/')