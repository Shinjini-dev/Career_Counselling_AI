from django.shortcuts import render,redirect
from .models import QuizQuestions,Skill
from .forms import UserInfoForm
from careerai.gemini import get_gemini_response

# Create your views here.
def quiz_view(request):
    questions=QuizQuestions.objects.all()
    return render(request,'quiz.html',{'questions':questions})

# for submit
def quiz_submit_view(request):
    if request.method=="POST":
        answers={}
        score={'A':0,'B':0,'C':0,'D':0}
    
        for key in request.POST:
            if key.startswith('q'):
                ans=request.POST[key]
                score[ans] += 1
                answers[key]=ans

    

    suggested=max(score,key=score.get)
    career_map={
        'A' :  'Software Engineer',
        'B' :  'UI/UX Designer',
        'C' :  'Data Scientist',
        'D' :   'Fashion Designer'
    }
    
    if score[suggested]>0:
        suggestion=career_map.get(suggested,'general Advice') 
    else:
        prompt="User answered the following quiz"
        for q,a in answers.items():
            prompt += f"{q}:{a}"
        prompt += "Based on their skill, Suggest a suitable path"
        suggestion=get_gemini_response(prompt)

    request.session['score'] = score
    request.session['suggestion'] = suggestion

    return redirect('result_view')

    

def user_view(request):
    if request.method=='POST':
        user_form = UserInfoForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            questions=QuizQuestions.objects.all()
            return render(request, 'quiz.html', {'questions': questions})
        else:
            return render(request, 'info.html', {'forms': user_form})
    else:
        user_form=UserInfoForm()
        return render(request,'info.html',{'forms': user_form})

def result_view(request):
    score = request.session.get('score', {})
    suggestion = request.session.get('suggestion', '')
    

    # Match suggestion to category
    career_code = {
        'Software Engineer': 'A',
        'UI/UX Designer': 'B',
        'Data Analyst': 'C',
        'Fashion Designer': 'D'
    }.get(suggestion, '')

    skill=Skill.objects.filter(category=career_code)
    return render(request,'recommended.html',{'score': score,'suggestion':suggestion,'skill':skill })
    

def score_view(request):
    score={
        "Logical Thinking":9,
        "Creative":7,
        "Communication":8
    }
    return render(request,'result.html',{'score':score})
