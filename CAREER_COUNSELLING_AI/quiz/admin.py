from django.contrib import admin
from .models import QuizQuestions
from .models import QuizAnswers
from .models import Career,Skill

# Register your models here.
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text',)
    fields = ('question_text', 'option1', 'option2', 'option3', 'option4')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name','catagory')
    list_filter=('catagory')
    search_fields=('name','description')
    fields = ('question_text', 'option1', 'option2', 'option3', 'option4')
    


admin.site.register(QuizQuestions,QuizQuestionAdmin)
admin.site.register(QuizAnswers)
admin.site.register(Skill)
admin.site.register(Career)