from django.db import models


# Create your models here.
class QuizQuestions(models.Model):
    question_text = models.TextField(default="Sample question text")
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_option=models.CharField(max_length=1)  


    def __str__(self):
        return self.question_text


class QuizAnswers(models.Model):
    user_id=models.CharField(max_length=100)
    questions=models.ForeignKey(QuizQuestions,on_delete=models.CASCADE,null=True, blank=True)
    selected_option=models.CharField(max_length=1)
    # submitted_at=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user_id} -Q{self.questions.id}:{self.selected_option}"


class UserInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    secondary_marks=models.FloatField()
    higher_Secondary_marks=models.FloatField()
    stream=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Career(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Skill(models.Model):
    skill=models.ForeignKey(Career,on_delete=models.CASCADE,null=True, blank=True)
    CAREER_CHOICES = [
        ('A', 'Software Engineer'),
        ('B', 'UI/UX Designer'),
        ('C', 'Data Analyst'),
        ('D', 'Fashion Designer'),
    ]
    
    title = models.CharField(max_length=200,default='Not Required')
    description=models.TextField(default="No description available")
    category=models.CharField(max_length=1,choices=CAREER_CHOICES,null=True,blank=True)
    key_skills = models.TextField(verbose_name="Key Skills & Competencies",default='Not Required')
    technology = models.TextField(default="No description available")  
    certification=models.TextField(default="ok")

    def __str__(self):
        # return f"{self.name} {{self.career.name}}"
        return f"{self.title} ({self.get_category_display()})"

