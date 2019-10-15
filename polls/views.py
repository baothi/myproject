from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    myname="baothi"
    taisan1 = ["dien thoai","may bay", "may tinh" ]
    context = {"name": myname, "taisan": taisan1}
    return render(request, "polls/index.html", context )

def viewlist(request):
	# get_object_or_404(Question, pk=1)
    lis_question = Question.objects.all()
    context = {"dsquest": lis_question}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request,"polls/detail_question.html", {"qs": q})

def vote(request, question_id):
	q = Question.objects.get(pk=question_id)
	try:
	    dulieu = request.POST["choice"]
	    c = q.choice_set.get(pk = dulieu)
	except:
		HttpResponse("loi khong co choice")
	c.vote = c.vote + 1
	c.save()
	return render(request, "polls/result.html", {"q":q})