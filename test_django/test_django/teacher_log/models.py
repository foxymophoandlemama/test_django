from django.db import models

class Scholar(models.Model):
    
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField()
    grade = models.IntegerField()
    
    def __unicode__(self):
        return self.surname + '  ' + self.name
    
    def complete_name(self):
        return self.__unicode__()
    
class Subject(models.Model):
    
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
    
class Objective(models.Model):
    
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.name

class Vote(models.Model):
    
    test_date = models.DateField()
    scholar = models.ForeignKey(Scholar)
    subject = models.ForeignKey(Subject)
    objective = models.ForeignKey(Objective)
    value = models.FloatField()

    def __unicode__(self):
        return self.value

#class Absence(models.Model):
#    
#    scholar = models.ForeignKey(Scholar)
#    absence_date = models.DateField()
#    justified = models.BooleanField(default=True)    