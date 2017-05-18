from django.db import models

# Create your models here.



class Project(models.Model):
    project_id = models.AutoField(primary_key = True)
    project_name = models.CharField(max_length=32)
    project_description = models.CharField(max_length=512)
    project_color = models.CharField(max_length=6)
    disabled = models.BooleanField(default = False)

    class Meta:
        db_table = 'project'







cprojectID	int(11)
teamID	integer(11)
projectName	varchar(128)
projectDescription	varchar(256)
projectColour	tinytext
	clientID	null(11)
disabled	tinyint