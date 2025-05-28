# Imports.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    """
    The model for the projects you wish to add to you website via admin.

    Represents a project entry.

    Fields:
        title (str): Project title.
        description (str): Project description.
        date_created (date): Date the project was created.
        status (str): Project status.
        created_by (User): User who created the project.
        image (ImageField): Project image.

    Returns:
        None

    Return type:
        None
    """

    STATUS_CHOICES = [
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('SUSPENDED', 'Suspended'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ONGOING')
    # Optionally, track which user created the project (for example)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)

    def __str__(self):
        """
        Returns the project title.

        Parameters:
            None

        Returns:
            str: The project title.

        Return type:
            str
        """
        return self.title
